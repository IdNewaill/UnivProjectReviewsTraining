import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

### Open the raw csv
raw_data = pd.read_csv("data/yelp_sentiment_master_dataset.csv")

### Functions
def cleanCsv(raw_data):
    # Remove empty data
    cleaned_data = raw_data.dropna()

    # Delete duplicates
    cleaned_data = cleaned_data.drop_duplicates()

    return cleaned_data

def getOnlyDataWithCorrectValues(cleaned_data):
    # Verify that stars_review are correct
    
    correct_review_stars = [1,2,3,4,5]
    res = cleaned_data[cleaned_data["stars_review"].isin(correct_review_stars)]

    return res

def devideData(correct_data):
    # TODO : not sure it's the division needed
    x_train, y_train, x_test, y_test = train_test_split(test_size=0.30)

def main():
    #clean data
    cleaned_data = cleanCsv(raw_data)

    #verify value
    correct_data = getOnlyDataWithCorrectValues(cleaned_data)
    print(correct_data)

    #devideData(correct_data)

### Main
main()