# Introduction

This project was design to scrape information from Aneel's Open Data webstite

## Instalation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages listed on requirements.txt file.

```bash
pip install -r requirements.txt
```

## Usage

```python
python ./pipeline/main.py
```

## DISCLAMER

Due to the limited time I was able to dispense to focus on this project, I chose to maintain all processing locally and did not connect on AWS cloud.

Going forward with the development of this project, I would connect to Glue to execute the main function on a schedule to make sure our datawarehouse is up to date as frequently as possible.

Another option would be using Airflow to schedule Glue jobs and account for different (more complex) extractions/ingestions data sources.
