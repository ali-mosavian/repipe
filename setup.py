from setuptools import setup, find_packages

setup(
    name='re-pipe',
    version='0.0.1',
    description='A reproducible data/NLP pipeline',
    url='https://github.com/stdexcept/repipe',
    author='Ali Mosavian',
    author_email='ali@octai.se',

    python_requires='>=3.6',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        'gensim >= 3.8.1',
        'joblib >= 0.14.0',        
        'nltk >= 3.4.4',
        'numpy >= 1.17.3',
        'pandas >= 0.25.2',
        'scikit-learn >= 0.21.3',
        'scipy >= 1.3.1',
    ],
    extras_require={
        'test': [
            'pyyaml==5.1.2',
            'nose==1.3.7'
        ],
        'keras': [
            'Keras-Preprocessing >= 1.1.0'
        ],        
    }
)
