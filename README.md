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
