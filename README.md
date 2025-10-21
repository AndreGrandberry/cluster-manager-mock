# Project 3 Cluster ETL Pipeline

## Overview

This project implements an ETL pipeline in Python to process JSON data from the `mock_data/input` directory and output a summary to `output.json`.

## Setup

1. Clone the repository.
   `git clone https://github.com/AndreGrandberry/cluster-manager-mock`
2. Create and activate a virtual environment
    `python3 -m venv venv source venv/bin/activate` (Mac: source venv/bin/activate. Windows: venv/Scripts/activate)
3. Install dependencies:
    `pip install -r requirements.txt`

## Usage

Run the main script:

`python backend/app/app.py`

The output will be saved to `output.json`.

## Code Quality: flake8-html

1. Install flake8 and flake8-html
    `pip install flake8 flake8-html`
2. Generatle HTML report
    `flake8 app --format=html --htmldir=flake8-report`
    The HTML report will be in the `flake8-report` directory.

## Project Structure

- `backend/app/app.py` — Main ETL pipeline script
- `mock_data/input/` — Input JSON files
- `output.json` — Output file
