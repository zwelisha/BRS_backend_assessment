## Getting Started

### Requirements

1. Python3
2. pytest
3. Text editor (Recommended: Atom, VSCode or SublimeText)

### Installation

#### 1. Python3

The installation differ from one operating system to the other, but the documentation which can be found [here](https://www.python.org/downloads/) have clear instructions for each operating system you use.

#### 2. Pytest
1. First check if pip is installed by running `pip --version`
2. If it is not installed, Pytest can be installed using pip. First download and install pip, [here](https://pip.pypa.io/en/stable/installation/)
3. Run `pip install pytest`


#### 3. Text Editor

Any text editor of your choice can be used. However Visual Studio Code is highly recommended.

#### Folder Structure
For simplicity I put all the files in one folder
```
BRS_Backend_Assessment
    assessment.py
    hello.txt
    .gitignore
    README.md
    test_assessment.py

```

### Formatting The Code

I use Black for consistency, here is the link to detailed steps of installing and using Black [link](https://www.freecodecamp.org/news/auto-format-your-python-code-with-black/)


### Running The Project

#### 1. Clone the project

```
git clone https://github.com/zwelisha/BRS_backend_assessment.git
```

#### 2. Change Directory (To the root folder of the project)

Change directory to the project `cd BRS_backend_assessment`. There you will see the folder structure detailed above.


To run the project you can simple run the tests or the assessment.py file.

```
python3 assessment.py
```

Now you should be able to see the following on your terminal:

```
None
[0, 1, 2, 3, 5, 6, 10, 40]
```

To run tests `pytest` and ENTER.

Feel free to add your own tests on `test_assessment.py`, I did not test all the functions in the assessment module. I only tested the first one for demonstration purposes.

#### Authors

[Zweli Mthethwa](https://www.linkedin.com/in/zweli-mthethwa-244b45a8/)