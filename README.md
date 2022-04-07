#### apicmdtool.py : `main file`

#### config.py :
            1. User token needs to be provided here
            2. object rid, object type and primary key is defined here
#### data.py : `create, delete, update data is defined under variables applyAction_createObject_var, applyAction_deleteObject_var, applyAction_updateObject_var respectively`

## execution :
`command1 : python3 apicmdtool.py -r  (To read data from defined object type eg: pricingitem, BeckettGradingItem)`

`command2 : python3 apicmdtool.py -g  (To fetch specified data object)`
`command3 : python3 apicmdtool.py -c  (To create new object data, need to provide relevant data for "applyAction_createObject_var" at data.py)`

`command4 : python3 apicmdtool.py -u  (To update existing object, needs to provide relevant data for "applyAction_updateObject_var" variable  at data.py )`

`command4 : python3 apicmdtool.py -d  (To delete existing object, needs to provide relevant data for "applyAction_deleteObject_var" variable  at data.py )`



reference link :
https://beckett.palantirfoundry.com/workspace/documentation/product/objects-gateway/apply-action
https://beckett.palantirfoundry.com/workspace/documentation/product/actions/action_types

