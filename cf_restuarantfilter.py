import json
import pdb

reviews = {}
with open('data/filteredDataset_Restuarants.json') as json_data:
    for line in json_data.readlines():
        review = json.loads(line)
        if review["business_id"] in reviews:
            reviews[review["business_id"]] +=1
        else:
            reviews[review["business_id"]] =1

for user_id, count in reviews.items():
    if count>=20:
        print user_id, count


# with open('data/yelp_academic_dataset_business.json') as json_data:
#     for line in json_data.readlines():
#         review = json.loads(line)
#         if "Restaurants" in review["categories"]:
#             print review["business_id"]


#             reviews[review["business_id"]] +=1
#         else:
#             reviews[review["business_id"]] =1

# for business_id, count in reviews.items():
#     print business_id, count
