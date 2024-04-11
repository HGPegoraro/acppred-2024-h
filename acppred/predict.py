from acppred.preprocess import compute_aa_composition
from acppred.models import Model
from argparse import ArgumentParser
import pandas as pd

def predict_anticancer_peptide(peptide:str, model:str='data/models/model.pickle') -> float:
    """

    Predicts the probability of anticancer activity for an input peptide 

    Args: 

    - peptide (str): peptide sequence (one letter code).

    Kwargs:

    - model (str): file containing pre-trainde model.

    Returns:

    - probability (float): probability of anticancer activity.
    """

    model = Model.load(model)
    
    df_input = pd.DataFrame([compute_aa_composition(peptide)])
    probability = model.predict_proba(df_input)[0][1]
    return probability

def main():
    argument_parser = ArgumentParser()
    argument_parser.add_argument('model', help='Pre-trained classification model')
    argument_parser.add_argument('peptide', help='Sequence of the peptide to be analyzed')
    arguments = argument_parser.parse_args()

    probability = predict_anticancer_peptide(arguments.peptide, arguments.model)
    print(arguments.peptide, probability, sep='\t')

if __name__ == '__main__':
    main()
    

