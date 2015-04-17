import json

# users = {}
# with open('users50.txt') as business_data:
#     for line in business_data.readlines():
#         users[line[:-1]] = 1

businesses = {}
with open('restuarantList.txt') as business_data:
    for line in business_data.readlines():
        businesses[line[:-1]] = 1

f = open("data/filteredDataset_Restuarants.json","w")
with open('data/yelp_academic_dataset_review.json') as json_data:
    for line in json_data.readlines():
    	review = json.loads(line)
    	if review["business_id"] in businesses:
    		f.write(line)