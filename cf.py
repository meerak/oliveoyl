import json
import pdb


reviews = {}
with open('data/yelp_academic_dataset_review.json') as json_data:
    for line in json_data.readlines():
        review = json.loads(line)
        if review["business_id"] in reviews:
            reviews[review["business_id"]] +=1
        else:
            reviews[review["business_id"]] =1

for user_id, count in reviews.items():
    print user_id, count