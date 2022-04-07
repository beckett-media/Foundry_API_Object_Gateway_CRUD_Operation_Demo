# DEMO PLEASE USE THIS FILE AS A REFERENCE ONLY

ontologyRid = "ri.ontology.main.ontology.b034a691-27e9-4959-9bcc-bc99b1552c97"
objectType = "Ontology_Object_Name_Here"
primaryKey = "dates"  # primary key of Pricing_items which is Item_id value for example
actionType_update = "modify-grading-object-action"  # actiontype name
actionType_create = "create-grading-object-action"
actionType_delete = "delete-grading-object-action"

listObjects_api_url = "https://beckett.palantirfoundry.com/objects-gateway/api/v1/ontologies/{}/objects/{}".format(
    ontologyRid, objectType)

getObject_api_url = "https://beckett.palantirfoundry.com/objects-gateway/api/v1/ontologies/{}/objects/{}/{}".format(
    ontologyRid, objectType, primaryKey)

applyAction_update_api_url = "https://beckett.palantirfoundry.com/objects-gateway/api/v1/ontologies/{}/actions/{}/apply".format(
    ontologyRid, actionType_update)

applyAction_create_api_url = "https://beckett.palantirfoundry.com/objects-gateway/api/v1/ontologies/{}/actions/{}/apply".format(
    ontologyRid, actionType_create)

applyAction_delete_api_url = "https://beckett.palantirfoundry.com/objects-gateway/api/v1/ontologies/{}/actions/{}/apply".format(
    ontologyRid, actionType_delete)

api_bearer_token = "TOKEN HERE"
