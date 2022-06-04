# File Client

## Description
Simple CLI application which retrieves and prints data from server

    Usage: file-client [options] stat UUID
           file-client [options] read UUID
           file-client --help

    UUID - id of the file

    Subcommands:
      stat                  Prints the file metadata in a human-readable manner.
      read                  Outputs the file content.

    Options:
      --help                Show this help message and exit.
      --backend             Set a backend to be used, choices are django and flask. Default is django.
      --django-server       Set a host and port of the Django server. Default is localhost:8000 .
      --flask-server        Set a host and port of the Flask server. Default is 127.0.0.1:5000.
      --output              Set the file where to store the output. Default is -, i.e. the stdout.

## Installation (For Linux/Mac)
### Virtual environment
First of all in the folder with setup.py open the terminal and create virtual environment
```sh
python3 -m venv .venv
```
and activate it
```sh
source .venv/bin/activate
```

##### *All the following commands are run from a virtual environment*


### Installation
From root folder(where is the setup.py) execute following command
```sh
pip3 install -e .
```

## Launch
After that launch server.py and in another terminal window(from virtual environment) use *file-client* command. For example:
```sh
file-client --backend=rest --base-url=localhost:5000 stat 2
```
