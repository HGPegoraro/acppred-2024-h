setup:
	mamba env create --file environment.yml || mamba env update --file environment.yml

dirs:
	mkdir -p data/models

preprocess:
	echo "Running Data Preprocessing"
	python acppred/preprocess.py

train: dirs
	echo "Running Model Training"
	python acppred/train.py 

all: preprocess train

test: 
	pytest