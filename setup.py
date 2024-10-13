from setuptools import setup, find_packages

setup(
    name='read_dataframe',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'pandas'
    ],
    entry_points={
        'console_scripts': [
            'rdf = read_dataframe.rdf:cliread',
        ],
    },
)
