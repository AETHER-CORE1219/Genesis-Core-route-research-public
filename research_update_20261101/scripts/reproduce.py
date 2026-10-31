#!/usr/bin/env python3
"""Re-run finite candidate selection and training-only internal evaluation.

Python standard library only. Inputs are anonymous, opaque incidence projections.
This does not regenerate charts or adjudicate biographies from raw sources.
"""
import argparse, gzip, json, math, random, statistics
from collections import defaultdict, Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    with (gzip.open(path,'rt',encoding='utf8') if path.suffix=='.gz' else path.open(encoding='utf8')) as f:
        return json.load(f)

def mask(indices):
    return sum(1 << i for i in indices)

def prepare_historical(d):
    cores=[]
    for c in d['cores']:
        cores.append({'id':c['id'],'system':c['system'],'primary':set(c['primary_functions']),
                      'mask':int(c['people'],16),
                      'relations':{i:int(v,16) for i,v in enumerate(c['relations'])},
                      'composites':[{'mask':int(b['people'],16),'relation':b['relation'],'nonempty':b['nonempty_carrier']} for b in c['composites']]})
    return cores

def prepare_folds(d):
    descriptors={c['id']:c for c in d['cores']};rows=d['people'];folds=[];n=d['n']
    for fold in range(5):
        train=mask(i for i,p in enumerate(rows) if p['fold']!=fold);test=((1<<n)-1)^train
        available=defaultdict(set)
        for i,p in enumerate(rows):
            if (train>>i)&1:
                for cid,branches in p['features'].items():available[cid].update(branches)
        cores=[]
        for cid,allowed in available.items():
            desc=descriptors[cid];cm=0;bm={b:0 for b in allowed}
            for i,p in enumerate(rows):
                if cid not in p['features']:continue
                cm |= 1<<i
                for b in p['features'][cid]:
                    if b in bm:bm[b] |= 1<<i
            relations={b:v for b,v in bm.items() if desc['branches'][b]['kind']=='rel'}
            composites=[{'mask':v,'relation':desc['branches'][b]['relation'],'nonempty':desc['branches'][b]['nonempty_carrier']} for b,v in bm.items() if desc['branches'][b]['kind']=='comp']
            assert all(v&train for v in bm.values())
            assert all(b['relation'] in relations for b in composites)
            cores.append({'id':cid,'system':desc['system'],'primary':set(desc['primary_functions']),'mask':cm,'relations':relations,'composites':composites})
        folds.append({'cores':cores,'train':train,'test':test,'group_masks':[mask(d['source_groups'][k])&train for k in d['source_group_order']]})
    return folds

def select(cores,ys,functions,train,groups):
    n=train.bit_count();pred=[defaultdict(int) for _ in functions];nr=nl=0
    for c in cores:
        cm=c['mask']&train;nc=cm.bit_count()
        if nc<8:continue
        for fi,fn in enumerate(functions):
            y=ys[fi]&train;support=cm&y;nt=support.bit_count();nd=nc-nt
            if nt<5 or nd<3 or nt*n<=y.bit_count()*nc or not all(support&g for g in groups):continue
            directional=[]
            for b in c['composites']:
                bm=b['mask']&train;bt=(bm&y).bit_count();bd=bm.bit_count()-bt
                if bt>=3 and bt*nd>bd*nt:directional.append(b)
            if not directional:continue
            nl+=1
            selected=[b['mask'] for b in directional if b['nonempty']]
            if not selected:
                dr={}
                for rid,m in c['relations'].items():
                    bm=m&train;bt=(bm&y).bit_count();bd=bm.bit_count()-bt
                    if bt>=3 and bt*nd>bd*nt:dr[rid]=m
                if not any(b['relation'] in dr for b in directional):continue
                selected=list(dr.values())
            nr+=1;exposure=0
            for m in selected:exposure |= m
            pred[fi][c['system']+'_any'] |= exposure
            if fn in c['primary']:pred[fi][c['system']+'_primary'] |= exposure
    return pred,nr,nl

def statistics_for(pred,ys,functions,n):
    result={};max_rd=max_z=-1e9
    for fi,fn in enumerate(functions):
        p=pred[fi];surfaces={'primary_both':p['WESTERN_primary']&p['JYOTISH_primary'],'any_both':p['WESTERN_any']&p['JYOTISH_any'],'primary_western':p['WESTERN_primary'],'primary_jyotish':p['JYOTISH_primary'],'any_western':p['WESTERN_any'],'any_jyotish':p['JYOTISH_any']}
        total=ys[fi].bit_count();prev=total/n
        for name,m in surfaces.items():
            ne=m.bit_count();supported=(m&ys[fi]).bit_count()
            rd=supported/ne-(total-supported)/(n-ne) if 0<ne<n else None
            se=math.sqrt(prev*(1-prev)*(1/ne+1/(n-ne))) if rd is not None and 0<prev<1 else None
            z=rd/se if se else None
            result[fn+'|'+name]={'exposed':ne,'supported':supported,'recorded':total,'rd':rd,'z':z}
            if rd is not None:max_rd=max(max_rd,rd)
            if z is not None:max_z=max(max_z,z)
    return {'surfaces':result,'max_rd':max_rd,'max_z':max_z}

def historical(d,cores,profiles):
    ys=[mask(i for i,p in enumerate(profiles) if p&(1<<f)) for f in range(len(d['functions']))]
    pred,nr,nl=select(cores,ys,d['functions'],(1<<d['n'])-1,[mask(d['source_groups'][k]) for k in d['source_group_order']])
    return {**statistics_for(pred,ys,d['functions'],d['n']),'selected_rules':nr,'training_leads':nl}

def internal(d,folds,profiles):
    endpoints={};max_z=-1e9
    for ei,ep in enumerate(d['endpoints']):
        ys=[mask(i for i,p in enumerate(profiles) if p[ei]&(1<<f)) for f in range(len(d['functions']))]
        oof=[defaultdict(int) for _ in d['functions']];counts=[]
        for fd in folds:
            pred,nr,nl=select(fd['cores'],ys,d['functions'],fd['train'],fd['group_masks']);counts.append(nr)
            for fi,p in enumerate(pred):
                for k,m in p.items():oof[fi][k] |= m&fd['test']
        stats=statistics_for(oof,ys,d['functions'],d['n']);stats['fold_rule_counts']=counts;endpoints[ep]=stats;max_z=max(max_z,stats['max_z'])
    return {'endpoints':endpoints,'max_z':max_z}

def shuffled(profiles,d,rng):
    out=profiles.copy()
    for k in d['source_group_order']:
        ids=d['source_groups'][k];vals=[profiles[i] for i in ids];rng.shuffle(vals)
        for i,v in zip(ids,vals):out[i]=v
    return out

def pvalue(values,observed):
    return None if observed is None else (1+sum(x>=observed for x in values))/(len(values)+1)

def run_historical(d,quick=False):
    cores=prepare_historical(d);profiles=d['activity_profiles'];obs=historical(d,cores,profiles)
    assert obs['selected_rules']==741 and obs['training_leads']==786
    if quick:return {'observed':obs}
    rng=random.Random(d['seed']);draws=[historical(d,cores,shuffled(profiles,d,rng)) for _ in range(d['permutations'])]
    tests={k:{'same_surface_p':pvalue([x['surfaces'][k]['z'] if x['surfaces'][k]['z'] is not None else -1e9 for x in draws],r['z']),'max_z_p':pvalue([x['max_z'] for x in draws],r['z']),'max_rd_p':pvalue([x['max_rd'] for x in draws],r['rd'])} for k,r in obs['surfaces'].items()}
    return {'observed':obs,'draws':len(draws),'seed':d['seed'],'max_rd_p':pvalue([x['max_rd'] for x in draws],obs['max_rd']),'max_z_p':pvalue([x['max_z'] for x in draws],obs['max_z']),'selected_rules_median':statistics.median(x['selected_rules'] for x in draws),'selected_rules_range':[min(x['selected_rules'] for x in draws),max(x['selected_rules'] for x in draws)],'tests':tests}

def run_internal(d,quick=False):
    folds=prepare_folds(d);profiles=[p['profiles'] for p in d['people']];obs=internal(d,folds,profiles)
    if quick:return {'observed':obs}
    rng=random.Random(d['seed']);draws=[internal(d,folds,shuffled(profiles,d,rng)) for _ in range(d['permutations'])]
    tests={}
    for ep,e in obs['endpoints'].items():
        for k,r in e['surfaces'].items():
            tests[ep+'|'+k]={'same_surface_p':pvalue([x['endpoints'][ep]['surfaces'][k]['z'] if x['endpoints'][ep]['surfaces'][k]['z'] is not None else -1e9 for x in draws],r['z']),'max_z_p':pvalue([x['max_z'] for x in draws],r['z'])}
    return {'observed':obs,'draws':len(draws),'seed':d['seed'],'max_z_p':pvalue([x['max_z'] for x in draws],obs['max_z']),'tests':tests}

def close(a,b,path='root'):
    if isinstance(a,dict):
        assert set(a)==set(b),(path,'keys')
        for k in a:close(a[k],b[k],path+'.'+k)
    elif isinstance(a,list):
        assert len(a)==len(b),(path,'length')
        for i,(x,y) in enumerate(zip(a,b)):close(x,y,path+f'[{i}]')
    elif isinstance(a,(int,float)) and not isinstance(a,bool):assert math.isclose(a,b,rel_tol=1e-10,abs_tol=1e-12),(path,a,b)
    else:assert a==b,(path,a,b)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--quick',action='store_true');ap.add_argument('--output',type=Path);args=ap.parse_args()
    result={'historical_selection':run_historical(read(ROOT/'data/historical_selection_input.json.gz'),args.quick),'repaired_internal':run_internal(read(ROOT/'data/repaired_chain_input.json.gz'),args.quick)}
    if not args.quick:close(result,read(ROOT/'EXPECTED_REPLAY_RESULTS.json'))
    if args.output:args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
    print(json.dumps({'status':'OBSERVED_ONLY' if args.quick else 'PASS','historical_selected_rules':result['historical_selection']['observed']['selected_rules'],'historical_draws':result['historical_selection'].get('draws',0),'internal_draws':result['repaired_internal'].get('draws',0),'repaired_max_p':result['repaired_internal'].get('max_z_p'),'boundary':'Exact replay from released opaque projections; not raw-source regeneration or independent empirical confirmation.'}))

if __name__=='__main__':main()
