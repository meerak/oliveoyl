import json
import pdb

users = {}
with open('users50.txt') as business_data:
    for line in business_data.readlines():
        users[line.split(" ")[0]] = 1

with open('data/yelp_academic_dataset_review.json') as json_data:
    for line in json_data.readlines():
        review = json.loads(line)
        if review["user_id"] in users:
            print str(review["business_id"]) + ","+ str(review["user_id"]) + ","+ str(review["stars"]) + ","+ str(review["votes"]["useful"])
