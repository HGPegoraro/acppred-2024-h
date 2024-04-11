setup:
	mamba env create --file environment.yml || mamba env update --file environment.yml

dirs:
	mkdir -p data/models

preprocess:
	echo "Running Data Preprocessing"
	acppred-preprocess data/raw data/processed

train: dirs
	echo "Running Model Training"
	acppred-train data/processed/ data/models/model.pickle

all: preprocess train

test: 
	pytest