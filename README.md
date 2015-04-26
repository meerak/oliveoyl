#CSE 6240 - Web search & Text Mining Project
### Research Project Implementation - Incorporating Implicit Feedback to Improve Recommender Systems

##### data
We have used the Yelp academic dataset to test the algorithms.
This dataset can be obtained by requesting access on the <a href="https://www.yelp.co.uk/academic_dataset">official site</a>   

#####helper code
jsonTocsv.py - Convert ratings file from json to csv format.
```bash
python jsonTocsv.py <data-file-location> > ratings.csv
```

train_test_split.py - This program splits a given data file into train and test set in the ratio 7:3.  
```bash
python train_test_split.py <data-file-location>
```

filter_items.py - This program prints businesses having more than x reviews and less than y reviews(optional). Default value of x is 20.
```bash
python filter_items.py <data-file-location> <optional-value-of-x> <optional-value-of-y> > filtered_items.txt 
```

filter_items.py - This program prints users who have given more than x reviews and less than y reviews(optional). Default value of x is 5.
```bash
python filter_users.py <ratings-file-location> <optional-value-of-x> <optional-value-of-y> > filtered_users.txt 
```

#####algorithms
**Previous approaches**

- ccf.py - This program uses the classical collaborative filtering approach to recommend an item to a user, based on items similar users have reviewed. It uses 10-fold cross validation and returns performance and accuracy metrics(RMSE, precision, recall, accuracy and f-measure) for the entire data as well as specialized user and item types.
```bash
python algorithms/ccf.py <ratings-file-location> > ccf_metrics.csv
```

- baselineparser.py - This program is based on the observation that ratings are usually dependent on users or items independently. It predicts values based  It uses 10-fold cross validation and returns performance and accuracy metrics(RMSE, precision, recall, accuracy and f-measure) for the entire data as well as specialized user and item types.
```bash
python algorithms/baselineparser.py <ratings-file-location> > baseline_metrics.csv
```
- ancf.py - This program builds on ccf and baseline predictors. It uses both baseline measures and similar users to recommend items to users. It uses 10-fold cross validation and returns performance and accuracy metrics(RMSE, precision, recall, accuracy and f-measure) for the entire data as well as specialized user and item types.
```bash
python algorithms/ancf.py <ratings-file-location> > ancf_metrics.csv
```

**New approach**
wancf.py - This program is an improvement over ancf. It incorporates the usefulness votes each reviews receives and uses it as a weighing factor while recommending items to users. It uses 10-fold cross validation and returns performance and accuracy metrics(RMSE, precision, recall, accuracy and f-measure) for the entire data as well as specialized user and item types.
```bash
python algorithms/wancf.py <ratings-file-location> > wancf_metrics.csv
```
