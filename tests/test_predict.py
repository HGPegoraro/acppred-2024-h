from acppred.predict import predict_anticancer_peptide

def test_predict_anticancer_peptide():
    predict_anticancer_peptide('MWSGRT')

def test_predict_anticancer_peptide_variable_type():
    prediction = predict_anticancer_peptide('AAAA')
    assert isinstance(prediction, float)