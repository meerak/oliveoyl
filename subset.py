import pdb 
import random

with open('data/academic/ratings_5.csv') as f:
    data = f.read().split("\n")

random.shuffle(data)

total = len(data)
test = open('data/test50_5.txt', 'w')
train = open('data/train50_5.txt', 'w')
t1 = int(0.7*total)
for row in data[:t1]:
    train.write(row + '\n')
for row in data[t1+1:]:
    test.write(row + '\n')
