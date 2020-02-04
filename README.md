# Unit Test Examples Using Pytest
This project assumes the following:
- **Python 3.5 or above** is installed in the system
- **git** is inatalled in the system
- **virtualenv** package is installed in the system. If not installed, then install using `pip3 install virtualenv` or `pip install virtualenv`


## Clone the project
- Clone the project: `git clone https://github.com/MhmdRyhn/unittest_using_pytest.git`
- Enter project root directory: `cd unittest_using_pytest`


## Create Virtual Environment
Run following command:
If Python 2.x is the default python version, then 
```
virtualenv -p python3 venv
```
If Python 3.x is the default python version, then 
```
virtualenv -p python3 venv
```


## Activate Virtual Environment
- Command: `source venv/bin/activate`


## Install Required Packages
- Install requirements: `pip3 install -r requirements.txt` or `pip install -r requirements.txt`


## Add Project Root to the Path
- Command: `export PATH="$(pwd):$PATH"`


## Run the Test Cases
- Command: `pytest` <br>

It will output in console that -> *====== X passed in X.XXs =======*
