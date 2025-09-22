from setuptools import setup, find_packages

setup(
    name='myproj',
    version='1.2.3',
    description="An example project...",
    packages=find_packages(exclude=['tests']),
    python_requires=">=3.6",
    extras_require=dict(
        test=[
            'pytest',
            'pytest-cov',
            'sybil',
            ],
        docs=[
            'furo',
            'sphinx'
        ]
    ),
)
