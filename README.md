# File Client

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
