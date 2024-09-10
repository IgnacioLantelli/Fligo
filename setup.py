from setuptools import setup, find_packages

setup(
    name='your_project_name',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'lightgbm',
        'matplotlib',
        'seaborn',
        'shap',
        'scipy',
    ],
    # Optional: if you want to include additional metadata
    # author='Your Name',
    # description='Description of your project',
    # url='https://github.com/yourusername/yourrepository',
)
