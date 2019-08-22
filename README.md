# IntGen - A generator of a road intersection specification file. 



## Installation

```
$ pip install -r requirements.txt

$ pip install setup.py
```

## Development

This project includes a number of helpers in the `Makefile` to streamline common development tasks.

### Environment Setup

The following demonstrates setting up and working with a development environment (make sure that virtualenv is installed before starting. The pip command is given [here](https://pypi.org/project/virtualenv/)):

```
### create a virtualenv for development

$ make virtualenv

$ source env/bin/activate (for linux)

$ cd env/Scripts/
$ activate (for windows)


### run intgen cli application

$ intgen --help
