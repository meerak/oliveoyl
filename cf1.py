import json
import pdb

business = []
with open('top_business.txt') as business_data:
    for line in business_data.readlines():
        business.append(line[:-1])

with open('data/yelp_academic_dataset_review.json') as json_data:
    for line in json_data.readlines():
        review = json.loads(line)
        if review["business_id"] in business:
            print str(review["business_id"]) + ","+ str(review["user_id"]) + ","+ str(review["stars"]) + ","+ str(review["votes"]["useful"])