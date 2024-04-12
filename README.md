# acppred

By Henrique Pegoraro

Anticancer Peptide Prediction Software

## Setup

To install the acppred program, run the following command:
(Mamba is required)

```
$ make setup
```

- `Makefile`: centralize the commands for the program `make`.

- `environment.yml`: contains all packages that are installed, and their dependencies. This environment contains `Python 3.8`, `pip` and `jupyter`.

- `requirements.txt`: registers a list with all current packages being used in the `appred` program.

- `models.py`: used to create a classification model based on `Logistic Regression` or `Random Forest`.

- `predict.py`: used to predict the probability of anticancer activity for an input peptide using a pre-trained model.

- `preprocess.py`: compute the amino acid composition for a peptide sequence and returns a dictionary containing the percentage of each amino acid.

- `train.py`: Trains a classification model for anticancer peptide predicition from a amino acid composition CSV file and saves the model on a .pickle file. The trained model is returned by the function.

- `server.py`: codes the server where the prediction model and custom sequence are used by the user.

