# Practice programming problems

![test suite](https://github.com/rehmanis/practice/actions/workflows/tests.yml/badge.svg) [![codecov](https://codecov.io/gh/rehmanis/practice/branch/main/graph/badge.svg?token=ClJ7h7BfIl)](https://codecov.io/gh/rehmanis/practice) [![pre-commit.ci status](https://results.pre-commit.ci/badge/github/rehmanis/practice/main.svg)](https://results.pre-commit.ci/latest/github/rehmanis/practice/main)

This repository is just to practice data structures and algorithms based on leetcode questions. In addition to writing
solutions for problems, it also includes small test cases for each problem and tries to follow best practices of programming

## Setup
* create a python virtual env and activate it (using python3.9 for the venv)
```
python3 -m venv env && source env/bin/activate
```


* install the python dependencies in the requirements folder
```

pip install -rrequirements/tests.txt && pip install -rrequirements/dev.txt
```

* to just run the all the test suite

```
tox -e py39
```
