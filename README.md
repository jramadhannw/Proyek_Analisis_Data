# Proyek Analisis Data Dashboard

## Setup Environment - Anaconda
### 1. Create a new environment
```
conda create --name main-ds python=3.12
```
### 2. Activate the environment
```
conda activate main-ds
```
### 3. Install the required packages
```
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
### 1. Create a new directory for the project
```
mkdir "Proyek Analisis Data"
```
### 2. Change into the project directory
```
cd "Proyek Analisis Data"
```
### 3. Install Pipenv (if not installed)
```
pip install pipenv
```
### 4. Install the required packages
```
pipenv install
```
### 5. Activate the Pipenv shell
```
pipenv shell
```
### 6. Install packages from `requirements.txt`
```
pip install -r requirements.txt
```

## Run steamlit app
```
streamlit run dashboard.py
```