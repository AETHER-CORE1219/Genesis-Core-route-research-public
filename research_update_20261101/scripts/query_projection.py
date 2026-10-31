#!/usr/bin/env python3
"""Construct finite query descriptors from an already typed, source-independent graph.

This is the query projection used by the internal evaluation. It does not compute
astronomical charts from birth inputs. Opaque incidence IDs in the released data
are not publicly joined to these rich semantic descriptors or private people.
"""
import json

def token(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"))

def neutral_features(p, capabilities):
    """Feature extraction has no activity, identity name, or other-person input."""
    if '__MISSING__' in json.dumps(p):
        raise ValueError('Missing-value placeholders are not relational evidence')
    cores={}
    for cx in p['contexts']:
        c=cx['original_context'];role=c['functional_role'];actor=c['actor_planet'];sys=c['system']
        entries=[]
        for r in cx['relations']:
            e=r['endpoints'];other=tuple(sorted({capabilities[x] for x in r['connected_planets']}));direction=r['direction'];source=e.get('from_planet',e.get('disposed_planet'));target=e.get('to_planet',e.get('actual_dispositor_planet'))
            if source is not None:direction+='|'+('ACTOR_EMITS' if source==actor else 'ACTOR_RECEIVES' if target==actor else 'DOWNSTREAM_IN_ACTOR_PATH')
            named=e.get('yoga_name',e.get('configuration_type'))
            semantic=r['semantic_relation_family']
            if named and not other:semantic='SINGLE_ACTOR_CONFIGURATION_STATE'
            entries.append(({'system':sys,'functional_role':role,'actor_capability_family':c['actor_capability_family'],'connected_capability_families':other,'semantic_relation_family':semantic,'relation_type':r['relation_type'],'actor_direction':direction,'named_configuration':named,'ordered_capabilities':None},r['relation_mode_family']))
        path=cx['dispositor_paths']
        if path:
            for pp in [{'kind':'OUTGOING_DISPOSITOR_PATH',**path['outgoing']},*path['incoming']]:
                chain=pp['ordered_path']
                if len(chain)<2:continue
                entries.append(({'system':sys,'functional_role':role,'actor_capability_family':c['actor_capability_family'],'connected_capability_families':tuple(sorted({capabilities[x] for x in chain if x!=actor})),'semantic_relation_family':'DEPENDENCY_GOVERNANCE_OR_MEDIATED_DELIVERY','relation_type':pp['kind'],'actor_direction':pp['kind'],'named_configuration':None,'ordered_capabilities':tuple(capabilities[x] for x in chain)},pp['kind']))
            if path['self_terminal_state']:
                entries.append(({'system':sys,'functional_role':role,'actor_capability_family':c['actor_capability_family'],'connected_capability_families':(),'semantic_relation_family':'SELF_GOVERNANCE_STATE','relation_type':'SELF_TERMINAL_STATE','actor_direction':'SELF','named_configuration':None,'ordered_capabilities':None},'SELF_TERMINAL_STATE'))
        for core,mode in entries:
            key=token(core);item=cores.setdefault(key,{'core':core,'branches':{}})
            rel=token({'mode':mode,'kind':'RELATION_MODE'});item['branches'][rel]={'nonempty':False,'kind':'rel','relation':rel}
            for carrier in cx['carriers']:
                b=token({'mode':mode,'kind':'RELATION_CARRIER_COMPOSITE','carrier':carrier['carrier_chain_class'],'derivation':carrier['carrier_derivation_group'],'classes':carrier['house_or_varga_classes']})
                item['branches'][b]={'nonempty':bool(carrier['house_or_varga_classes']),'kind':'comp','relation':rel}
    return cores
