import json
import pdb

reviews = {}
# with open('data/filteredDataset_Restuarants.json') as json_data:
#     for line in json_data.readlines():
#         review = json.loads(line)
#         if review["user_id"] in reviews:
#             reviews[review["user_id"]] +=1
#         else:
#             reviews[review["user_id"]] =1
with open('data/filteredDataset_Restuarants.json') as json_data:
    for line in json_data.readlines():
        review = json.loads(line)
        if review["business_id"] in reviews:
            reviews[review["business_id"]] +=1
        else:
            reviews[review
for user_id, count in reviews.items():
    if count>=20:
        print user_id, count


# with open('data/filteredDataset.json') as json_data:
#     for line in json_data.readlines():
#         # print line
#         review = json.loads(line)
#         if review["user_id"] in reviews:
#             reviews[review["user_id"]] +=1
#         else:
#             reviews[review["user_id"]] =1

# for business_id, count in reviews.items():
#     if count>20:
#         print business_id, count
