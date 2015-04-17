import numpy as np
import pdb

users = {}
business = {}
user_idx = 0
business_idx = 0

sum_useful = 0
row_count = 0 
mu = 0

def rmse(predictions,targets):
    return np.sqrt(((predictions - targets)** 2).mean())

def pearson_coefficient(u, v):
    nonzero_u = np.nonzero(u)[0]
    nonzero_v = np.nonzero(v)[0]
    index_common = np.intersect1d(nonzero_u, nonzero_v)

    u_mean = np.mean(u[index_common])
    v_mean = np.mean(v[index_common])

    #u_mean = np.mean(u[nonzero_u])
    #v_mean = np.mean(v[nonzero_v])
    x = u[index_common] - u_mean
    y = v[index_common] - v_mean
    den = float(np.sqrt(np.sum(np.square(x), axis=0))
                * np.sqrt(np.sum(np.square(y), axis=0)))
    if den == 0:
        return 0
    else:
        return np.dot(x, y) / den

def cosine_similarity(user1, user2):
    den = float(np.sqrt(np.sum(np.square(user1), axis=0))
                * np.sqrt(np.sum(np.square(user2), axis=0)))
    if den == 0:
        return 0
    else:
        return np.dot(user1, user2) / den

# count number of users and businesses
with open('samples/ratings_15.csv') as f:
    for line in f.readlines():
        #business_id, user_id, stars, useful
        tokens = line.split(",")
        if not tokens[1] in users:
            users[tokens[1]] = user_idx
            user_idx += 1
        if not tokens[0] in business:
            business[tokens[0]] = business_idx
            business_idx+=1
        
#similarity = np.zeros((len(users), len(users)))
#similarity = lil_matrix((len(users), len(users)))

with open('samples/train50_15.txt') as f:
    for line in f.readlines():
        tokens = line.split(",")
        sum_useful += int(tokens[3])
        row_count += 1
        mu += int(tokens[2])

    #print len(users), len(business)

    ratings_star = np.zeros((len(users), len(business)))
    ratings_useful = np.zeros((len(users), len(business)))
    
    mu = mu/ float(row_count)

    mean_useful = sum_useful/ float(row_count)
    weighted_total = 0
    den = 0

    baseline_user = np.zeros(len(users))
    baseline_business = np.zeros(len(business))

    count_user = np.zeros(len(users))
    count_business = np.zeros(len(business))

    lambda2 = 25
    lambda3 = 10

    f.seek(0)
    user_id = 0;
    for line in f.readlines():
        tokens = line.split(",")
        
        user_id = users[tokens[1]]
        business_id = business[tokens[0]]
        rating_star = int(tokens[2])
        
        ratings_star[user_id, business_id] = rating_star
        if float(tokens[3]) >= mean_useful:
            x = float(tokens[3])
        else:
            x = 1.0
        ratings_useful[user_id, business_id] = x
        
        weighted_total += x* rating_star
        den += x

        baseline_business[business_id] += rating_star  - mu
        count_business[business_id] +=1.0

    baseline_business = baseline_business / (lambda2+ count_business)

    weighted_mean = weighted_total/ float(den)
    print "Weighted mean" , weighted_mean

    f.seek(0)
    for line in f.readlines(): 
        tokens = line.split(",")
        
        user_id = users[tokens[1]]
        business_id = business[tokens[0]]
        rating_star = int(tokens[2])
        
        baseline_user[user_id] += (rating_star - mu - baseline_business[business_id])
        count_user[user_id] +=1.0
    
    baseline_user = baseline_user / (lambda3+ count_user)
    print "baseline user calculated"
    '''for i in range(len(users)):
        for j in range(i+1,len(users)):
            val = pearson_coefficient(ratings_star[i,:], ratings_star[j,:])
            if val < 0.7:
                val  = 0.0
            similarity[i,j] = val
            similarity[j,i] = val'''

baseline_ui = np.zeros((len(users), len(business)))
for i in range(len(users)):
    for j in range(len(business)):
        baseline_ui[i, j] =  baseline_user[i] + baseline_business[j] + weighted_mean

with open('samples/test50_15.txt') as f:
    actual = []
    predicted_new = []
    for line in f.readlines():
        tokens = line.split(",")
        user_id = users[tokens[1]]
        business_id = business[tokens[0]]
        
        similarity = np.zeros(len(users))
        for i in range(len(users)):
            val = pearson_coefficient(ratings_star[user_id,:], ratings_star[i,:])
            if val < 0.7:
                val  = 0.0
            similarity[i] = val
    
        nonzero =  np.where(ratings_star[:,business_id]>0)[0]
        predicted = np.sum(np.dot(similarity[nonzero], ratings_star[nonzero,business_id] - baseline_ui[nonzero,business_id]))
        
        den  = np.sum(similarity[nonzero]) + 15.0
        
        predicted = baseline_ui[user_id, business_id] + predicted / float(den)
        print predicted, tokens[2]
        predicted_new.append(predicted)
        actual.append(float(tokens[2]))

print "RMSE: ", rmse(np.array(predicted_new), np.array(actual))
