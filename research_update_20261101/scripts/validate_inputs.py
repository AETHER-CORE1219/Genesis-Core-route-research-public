#!/usr/bin/env python3
"""Validate the public projection schema and train/test separation invariants."""
import json,re,copy
from pathlib import Path
from reproduce import ROOT,read,mask,prepare_folds,select

def integer(v):return type(v) is int
def keys(obj,allowed):assert type(obj) is dict and set(obj)==set(allowed),(set(obj),allowed)
def bitset(s,n):
    assert type(s) is str and re.fullmatch(r'0x[0-9a-f]+',s)
    value=int(s,16);assert 0<=value<(1<<n);return value

def common(d):
    n=d['n'];assert n==420 and len(d['functions'])==len(set(d['functions']))==11
    assert all(re.fullmatch('[A-Z_]+',f) for f in d['functions'])
    assert set(d['source_group_order'])==set(d['source_groups'])=={'SOURCE_REVIEWED311','RECOVERED109'}
    all_ids=[i for k in d['source_group_order'] for i in d['source_groups'][k]]
    assert all(integer(i) for i in all_ids) and sorted(all_ids)==list(range(n))
    assert len(d['source_groups']['SOURCE_REVIEWED311'])==311 and len(d['source_groups']['RECOVERED109'])==109

def validate_historical(d):
    keys(d,['schema','n','functions','source_groups','source_group_order','activity_profiles','cores','permutations','seed','person_order','meaning_boundary']);common(d)
    assert d['schema']=='OPAQUE_FINITE_SELECTION_INPUT_V1' and d['permutations']==999 and d['seed']==20261031
    assert len(d['activity_profiles'])==420 and all(integer(x) and 0<=x<2048 for x in d['activity_profiles'])
    assert len({c['id'] for c in d['cores']})==len(d['cores'])
    for c in d['cores']:
        keys(c,['id','system','primary_functions','people','relations','composites']);assert re.fullmatch(r'H\d{5}',c['id']) and c['system'] in ['WESTERN','JYOTISH'];assert set(c['primary_functions'])<=set(d['functions'])
        cm=bitset(c['people'],420);rm=[bitset(m,420) for m in c['relations']];assert all(m&~cm==0 for m in rm)
        for b in c['composites']:
            keys(b,['people','relation','nonempty_carrier']);assert type(b['nonempty_carrier']) is bool and integer(b['relation']) and 0<=b['relation']<len(rm)
            bm=bitset(b['people'],420);assert bm&~rm[b['relation']]==0

def validate_internal(d):
    keys(d,['schema','n','functions','source_groups','source_group_order','cores','people','permutations','seed','endpoints','endpoint_boundary']);common(d)
    assert d['schema']=='OPAQUE_REPAIRED_CHAIN_INPUT_V1' and d['permutations']==199 and d['seed']==20261101
    assert d['endpoints']==['recorded_any','recorded_supported'];cores={c['id']:c for c in d['cores']};assert len(cores)==len(d['cores'])
    for c in d['cores']:
        keys(c,['id','system','primary_functions','branches']);assert re.fullmatch(r'C\d{5}',c['id']) and c['system'] in ['WESTERN','JYOTISH'];assert set(c['primary_functions'])<=set(d['functions'])
        for b in c['branches']:
            keys(b,['kind','relation','nonempty_carrier']);assert b['kind'] in ['rel','comp'] and type(b['nonempty_carrier']) is bool
            assert integer(b['relation']) and 0<=b['relation']<len(c['branches']) and c['branches'][b['relation']]['kind']=='rel'
    assert len(d['people'])==420
    for i,p in enumerate(d['people']):
        keys(p,['id','fold','profiles','features']);assert p['id']==f'A{i+1:04d}' and integer(p['fold']) and 0<=p['fold']<5
        assert len(p['profiles'])==2 and all(integer(x) and 0<=x<2048 for x in p['profiles']);assert p['profiles'][1]&~p['profiles'][0]==0
        for cid,bs in p['features'].items():
            assert cid in cores and len(bs)==len(set(bs)) and all(integer(b) and 0<=b<len(cores[cid]['branches']) for b in bs)
            assert all(cores[cid]['branches'][b]['relation'] in bs for b in bs)

def isolation_test(d):
    profiles=[p['profiles'] for p in d['people']];functions=d['functions'];folds=prepare_folds(d)
    for fold in folds:
        assert not (fold['train']&fold['test']) and (fold['train']|fold['test']).bit_count()==420
        for ep in range(2):
            ys=[mask(i for i,p in enumerate(profiles) if p[ep]&(1<<f)) for f in range(11)]
            a=select(fold['cores'],ys,functions,fold['train'],fold['group_masks']);b=select(fold['cores'],[y^fold['test'] for y in ys],functions,fold['train'],fold['group_masks']);assert a==b

def main():
    h=read(ROOT/'data/historical_selection_input.json.gz');c=read(ROOT/'data/repaired_chain_input.json.gz');validate_historical(h);validate_internal(c);isolation_test(c)
    bad=copy.deepcopy(c);bad['people'][0]['birth_time']='private field must be rejected'
    try:validate_internal(bad)
    except AssertionError:pass
    else:raise AssertionError('Unexpected field not rejected')
    bad=copy.deepcopy(c);bad['source_groups']['RECOVERED109'][0]=bad['source_groups']['SOURCE_REVIEWED311'][0]
    try:validate_internal(bad)
    except AssertionError:pass
    else:raise AssertionError('Duplicate membership not rejected')
    print(json.dumps({'status':'PASS','n':420,'schema_whitelist':True,'identity_birth_location_fields_allowed':False,'fold_label_isolation':True,'negative_controls':2,'boundary':'Schema/projection checks do not prove impossibility of statistical reidentification or empirical validity.'}))
if __name__=='__main__':main()
