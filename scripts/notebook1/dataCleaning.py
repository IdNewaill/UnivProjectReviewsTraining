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
    cleaned_data = raw_data[raw_data.isna()]

    # Delete duplicates
    cleaned_data = cleaned_data.drop_duplicates()

    return cleaned_data

def getOnlyDataWithCorrectValues(cleaned_data):

    ## TODO : Vérifier les données en s'assurant que tous les chiffres sont corrects

    # Verify that stars_review are correct

    return raw_data

def devideData(correct_data):
    x_train, y_train, x_test, y_test = train_test_split(test_size=0.30)
    

### Main
cleanCsv()