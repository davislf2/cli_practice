# qmatch-cli 

A command-line-interface (CLI) tool for finding the top 2 matched questions from user's input. It use [Multinomial Naive Bayes from Scikit-learn](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html) to classify the most correlated questions.

Author: [Davis Hong (davislf2)](https://github.com/davislf2) | davislf2.net@gmail.com



## Install

Environment: Python 3.5, pip 18.0

```sh
pip install -e .[test]
```



## Run

There are four different commands in this cli.

```sh
qmatch m <question>		# Find the top 2 matched questions
qmatch hello			# Hello World
qmatch -h | --help		# Help function
qmatch --version		# Version of this app
```

For example, if you command

```sh
qmatch m "I understand clearly what I need to do to be successful in my current role"
```

The result will look like

![alt text](https://raw.githubusercontent.com/davislf2/qmatch-cli/master/resource/screenshot%202018-10-02%20at%207.30.23%20PM.png)



## Reference Questions

| Question                                                     | Code  |
| ------------------------------------------------------------ | ----- |
| I know what I need to do to be successful in my role         | ALI.5 |
| The information I need to do my job effectively is readily available | ENA.3 |
| We are encouraged to be innovative even though some of our initiatives may not succeed | INN.2 |
| We hold ourselves and our team members accountable for results | TEA.2 |



## Structure

```sh
qmatch
├── README.md
├── LICENCE
├── MANIFEST.in
├── requirement.txt
├── setup.cfg
├── setup.py
└── qmatch
    ├── __init__.py
    ├── __main__.py
    ├── cli.py
    ├── test
    ├── nlp
    |	├── __init__.py
    |	└── best_match.py
    └── commands
        ├── __init__.py
        ├── base.py
        ├── hello.py
        └── m.py
```



## Testing

You can run testing through the command

```sh
python setup.py test
```



This project has passed 97% coverage by unittest.

```sh
---------- coverage: platform darwin, python 3.5.2-final-0 -----------
Name                          Stmts   Miss  Cover   Missing
-----------------------------------------------------------
qmatch/__init__.py                1      0   100%
qmatch/__main__.py                2      2     0%   1-2
qmatch/cli.py                    13      0   100%
qmatch/commands/__init__.py       2      0   100%
qmatch/commands/base.py           7      1    86%   13
qmatch/commands/hello.py          6      0   100%
qmatch/commands/m.py             15      0   100%
qmatch/nlp/__init__.py            1      0   100%
qmatch/nlp/best_match.py         56      0   100%
-----------------------------------------------------------
TOTAL                           103      3    97%
```

