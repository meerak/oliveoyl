import json
import pdb

users = []
with open('users20.txt') as business_data:
    for line in business_data.readlines():
        users.append(line.split(" ")[0])

with open('data/yelp_academic_dataset_review.json') as json_data:
    for line in json_data.readlines():
        review = json.loads(line)
        if review["user_id"] in users:
            print str(review["business_id"]) + ","+ str(review["user_id"]) + ","+ str(review["stars"]) + ","+ str(review["votes"]["useful"])
