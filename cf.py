import json
import pdb


reviews = {}
with open('yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_review.json') as json_data:
    for line in json_data.readlines():
        review = json.loads(line)
        if review["user_id"] in reviews:
            reviews[review["user_id"]] +=1
        else:
            reviews[review["user_id"]] =1

for user_id, count in reviews.items():
    print user_id, count