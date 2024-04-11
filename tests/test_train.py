from acppred.train import train_model
from acppred.train import evaluate_model
from acppred.models import Model


def test_train_model_output_variable_type():
    model = train_model(
        'data/test/train.txt',
        output_file='data/test/model.pickle'
    )
    assert isinstance(model, Model)

def test_evaluate_model_output_variable_type():
    model = train_model(
        'data/test/train.txt',
        output_file='data/test/model.pickle'
    )
    report = evaluate_model(model, 'data/test/train.txt')
    assert isinstance(report, str)