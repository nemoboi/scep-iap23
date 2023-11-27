## Scheduling conscious of energy production overhead

This project seeks to implement a schedling tool which delays the execution of a program until a sufficient overhead of local energy production is given.

*Scientific Software Center, Heidelberg University, 12/2020*

The code can compute side lengths of two geometric objects - of a square and a pentagon. You have to select either one, output of both objects is currently not implemented. For usage see [input](doc/input.md). The methods are described in [method](doc/method.md). Details on the input parameters are given in [parameters](doc/parameters.md). A detailed source code description is given through the sphinx documentation (here will be the link to the doc).

The program requires a working python environment.

## github actions

This repository contains a github action in `./github/workflows/`. This will run linting, unit tests and update the documentation upon push to the master branch and upon pull request. The action can also be run manually in the "Actions" tab on the github website.

### Linting
The linter (in this case, `flake8` will point out potential bugs, errors, styling issues, and suspicious code.

### Testing
You should always test your code against a reference. In this template, we use `pytest` which is a popular option that is very versatile.

So far, only *unit tests* are included in the code template (that is, tests of a specific component of the software), but as you develop your software, you should also add `integration tests` that check the overall behaviour of your code.

In the github action, the tests are performed under ubuntu, windows and mac operating systems to ensure that the code runs in different environments. Also, two different python versions are tested right now, 3.8 and 3.9.

### Source Code Documentation: Functions, modules, classes, ...
The documentation should be updated as you update your code. Include appropriate method descriptions in your code and `sphinx` will update the documentation html for your functions, classes, etc. The documentation is build using `make html` in the `doc` folder. On your local machine, you can navigate to `doc/build/index.html` and check the styling.
If your code is in a public repository, you can push your sphinx documentation to [Read the docs](https://ssc-hd-python-project-template.readthedocs.io/en/latest/?).
