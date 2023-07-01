# Optimizing git actions by adjusting job sequence
made by @sanzhik22

This project used to show that parallel git actions to parse data less time consuming than sequence.

## Installation
Clone the repo
```
$ git clone https://github.com/sanzhik22/My_first_API_with_dbconnection/blob/main/README.md
```
Requires Python 3.11.3 # adjust it

Create a virtual environment and activate it:
```commandline
python -m venv /path/to/repo
// in venv directory:
Scripts/activate
```

Install dependencies in venv using pip

```
pip install -r requirements.txt
```
python main.py

## How to create paralel or sequence actions:

### Paralel:
```yaml
name: Processes Sequenced

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  Process1:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run Process1
        run: python3 Py_scr/Process1.py

  Process2:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run Process1
        run: python3 Py_scr/Process2.py
```
To create paralel jobs just put JOBS on in jobs section in your *yml*

### Sequence jobs
```yaml
name: Processes Sequenced

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  Process1:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run Process1
        run: python3 Py_scr/Process1.py

  Process2:
    runs-on: ubuntu-latest
    needs: [Process1]

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run Process1
        run: python3 Py_scr/Process2.py
```
To create sequence jobs under each job write **needs: [ jobs that needs to run ]**

## Report 

To create data action we create file action.ymd, as you can see in directory *.github/workflows* i have two *.ymd* files:

1) *action.yml* - which uses paralel actions to load data
![img.png](img.png)
2) *sequence.yml* - which uses sequence actions to load data
![img_1.png](img_1.png)

As we can see *Action.yml* which is paralel takes 102 seconds and *Sequence.yml* takes 232 seconds

As conclusion we can see:
```math
1-(102/232) * 100% = 56,03%
```
We reduced time consumption on 53%

## References
[Arciticle on Medium about paralel jobs](https://medium.com/tradeling/how-to-achieve-parallel-execution-using-github-actions-d534404702fb)