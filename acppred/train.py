from acppred.models import Model
from sklearn.metrics import classification_report
from sklearn.base import BaseEstimator
import pandas as pd
import pickle

def train_model(csv_file:str, output_file:str) -> BaseEstimator:
    """
    Trains a classification model for anticancer peptide
    predicition from a amino acid composition CSV file 
    and saves the model on a .piclke file. The trained 
    model is returned by the function. 
    
    Args:

    - csv_file (str): input file containing aa composition of anticancer
                      and non-anticancer peptides.
    - output_file (str): output .pickle file with trained model.

    Returns:

    - model (BaseEstimator): trained model.
    """
    
    df = pd.read_csv(csv_file)
    X_train = df.drop(['activity'], axis=1)
    y_train = df['activity']

    model = Model(estimator='random_forest')
    model.fit(X_train, y_train)
    model.save(output_file)
    
    return model

def evaluate_model(model:BaseEstimator, csv_file:str) -> str:
    """

    Evaluates a classification model using a test dataset and
    returns a classification report.

    Args: 

    - model (BaseEstimator): a scikit-learn classifier
    - csv_file (str): a CSV file containing the test dataset

    Returns:

    - report (str): a classification report for the model
    """

    df = pd.read_csv(csv_file)
    X_test = df.drop(['activity'], axis=1)
    y_test = df['activity']
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred)
    return report

if __name__ == '__main__':
    model = train_model('data/processed/train.csv', 'data/models/model.pickle')
    report = evaluate_model(model, 'data/processed/test.csv')
    print(report)