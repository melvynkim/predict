from setuptools import setup

setup(
    name='predict',
    version='0.1.0',
    description='Lightweight prediction model (AUC 0.77 from just 800 rows of data)',
    url='https://github.com/melvynkim/predict',
    author='Melvyn Kim',
    author_email='melvynkim@gmail.com',
    license='MIT',
    packages=['predict'],
    install_requires=[
        'scikit-learn',
        'pandas',
        'scipy'
        'matplotlib',
        'seaborn',
    ],
    zip_safe=False
)
