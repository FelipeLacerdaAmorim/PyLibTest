from setuptools import setup, find_packages

setup(
    name='my_keycloak_test_lib_fel',
    version='0.1',
    packages=find_packages(),
    description='Uma biblioteca de exemplo',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Felipe Lacerda',
    author_email='joaofelipe.amorim@aluno.uece.br',
    url='https://github.com/FelipeLacerdaAmorim/PyLibTest',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)