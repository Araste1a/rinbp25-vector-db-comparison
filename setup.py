from setuptools import setup, find_packages

setup(
    name='vector-db-comparison',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.20.0',
        'pandas>=1.3.0',
        'scikit-learn>=0.24.0',
        'torch>=1.9.0',
        'weaviate-client',
        'qdrant-client',
        'psycopg2-binary',
        'pyyaml',
        'matplotlib',
        'seaborn',
    ],
    python_requires='>=3.8',
)
