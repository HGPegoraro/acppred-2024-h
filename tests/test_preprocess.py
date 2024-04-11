from acppred.preprocess import compute_aa_composition
from acppred.preprocess import preprocess_datasets
import os 

def test_compute_aa_composition_homopolymer():
    aa_composition = compute_aa_composition ('AAAAA')
    assert aa_composition['A'] == 1

def test_compute_aa_composition_complex_peptide():
    aa_composition = compute_aa_composition('MWRL')
    assert aa_composition ['M'] == 0.25
    assert aa_composition ['W'] == 0.25
    assert aa_composition ['R'] == 0.25
    assert aa_composition ['L'] == 0.25

def test_preprocess_dataset():
    preprocess_datasets(
        'data/test/positive_peptides.txt',
        'data/test/negative_peptides.txt',
        output_file='data/test/train.txt'
    )
    assert os.path.isfile('data/test/train.txt')