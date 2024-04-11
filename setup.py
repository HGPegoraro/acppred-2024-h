from setuptools import setup, find_packages

setup(
    name="acppred",
    version="0.0.1",
    packages=find_packages(),
    author="Henrique Gonçalves Pegoraro",
    author_email="henrique.pegoraro2@gmail.com",
    description="Anticancer Peptide Prediction tool",
    entry_points = {
        'console_scripts': [
            'acppred-preprocess = acppred.preprocess:main',
            'acppred-train = acppred.train:main',
            'acppred-predict = acppred.predict:main'
        ]
    }
)

