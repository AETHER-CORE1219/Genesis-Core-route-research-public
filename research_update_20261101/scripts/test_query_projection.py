#!/usr/bin/env python3
"""Synthetic semantic regressions, not empirical people or route evidence."""
import json,copy
from query_projection import neutral_features

def main():
    caps={'Venus':'FORM','Mercury':'MEDIATION','Mars':'EXECUTION'}
    context={'original_context':{'system':'WESTERN','functional_role':'MC_RULER','actor_planet':'Venus','actor_capability_family':'FORM'},'relations':[],'carriers':[{'carrier_chain_class':'W_POSITION','carrier_derivation_group':'W.house_position_methods','house_or_varga_classes':['KENDRA_OR_ANGULAR']}],'dispositor_paths':{'outgoing':{'kind':'OUTGOING_DISPOSITOR_PATH','ordered_path':['Venus','Mercury'],'terminal':'Mercury','cycle':None},'incoming':[{'kind':'INCOMING_DISPOSITOR_PATH','ordered_path':['Mars','Venus']}],'self_terminal_state':False,'cycle_state':False}}
    person={'contexts':[context]};features=neutral_features(person,caps);kinds={v['core']['relation_type'] for v in features.values()};assert kinds=={'INCOMING_DISPOSITOR_PATH','OUTGOING_DISPOSITOR_PATH'}
    order={v['core']['relation_type']:v['core']['ordered_capabilities'] for v in features.values()};assert order['INCOMING_DISPOSITOR_PATH']==('EXECUTION','FORM');assert order['OUTGOING_DISPOSITOR_PATH']==('FORM','MEDIATION')
    self_person=copy.deepcopy(person);p=self_person['contexts'][0]['dispositor_paths'];p['outgoing']['ordered_path']=['Venus'];p['incoming']=[];p['self_terminal_state']=True
    sf=neutral_features(self_person,caps);assert {v['core']['relation_type'] for v in sf.values()}=={'SELF_TERMINAL_STATE'}
    bad=copy.deepcopy(person);bad['contexts'][0]['dispositor_paths']['outgoing']['cycle']='__MISSING__'
    try:neutral_features(bad,caps)
    except ValueError:pass
    else:raise AssertionError('Missing placeholder was accepted')
    print(json.dumps({'status':'PASS','synthetic_only':True,'incoming_outgoing_distinct':True,'self_terminal_is_state':True,'missing_placeholder_rejected':True}))
if __name__=='__main__':main()
