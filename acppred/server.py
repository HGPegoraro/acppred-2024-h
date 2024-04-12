from acppred.models import Model 
from acppred.preprocess import compute_aa_composition
from flask import Flask, render_template, request
from argparse import ArgumentParser
import pandas as pd

app = Flask(__name__)
models = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    peptide = request.form['sequence']
    df_input = pd.DataFrame([compute_aa_composition(peptide)])
    probability = models['model'].predict_proba(df_input)[0][1]
    return render_template("index.html", peptide=peptide, probability=probability, show_results=True)

def main():
    argument_parser = ArgumentParser()
    argument_parser.add_argument('model', help="Pre-trained ACPPred model.")
    arguments = argument_parser.parse_args()
    models['model'] = Model.load(arguments.model)
    app.run()

if __name__ == "__main__":
    main()