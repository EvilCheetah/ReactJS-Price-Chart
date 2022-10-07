# Price Chart Data Generator

This is a Python Script that generates data for [ReactJS Price Chart](https://github.com/EvilCheetah/ReactJS-Price-Chart).

## How to Run

### Virtual Environment
In order to run a program in isolation mode, make sure you create a Virtual Environment.  
More about it on Python Documentation Page [venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html).

### Installation
Preferrably, after creating and entering virtual environment, we have to make sure all dependencies are installed.  
In order to do that, run `pip install -r requirements.txt`.

### Preparation
Copy `.env.example` into `.env`, inspect it and fill out all necessary data.

### All Necessary Environment Variables For This Project
- `OUTPUT_DIRECTORY` - must be a directory
- `OUTPUT_FILENAME` - must be a filename
- `MIN_NUMBER_OF_ENTRIES_PER_PLATFORM` - must an integer above 0

### Execution 
To generate data, run `python main.py`.