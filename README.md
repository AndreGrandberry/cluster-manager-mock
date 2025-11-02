# Project 3 Cluster ETL Pipeline

## Overview

This project implements an ETL pipeline in Python to process JSON data from the `mock_data/input` directory and output a summary to `output.json`.

## Setup (Mac)

1. Clone the repository.
   `git clone https://github.com/AndreGrandberry/cluster-manager-mock`
2. Create and activate a virtual environment
    `python3 -m venv venv source venv/bin/activate` (Mac: source venv/bin/activate. Windows: venv/Scripts/activate)
3. Install dependencies:
    `pip install -r requirements.txt`

## Setup (Windows & VS Code)

### 1. Install Docker

- Download and install Docker Desktop from [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop).
- Follow the installation instructions for your operating system (Windows, macOS, or Linux).

### 2. Ensure Docker is Running

- Start Docker Desktop and verify it is running before opening the project in your devcontainer.
- You can check Docker status by running:
  ```bash
  docker info

### 3. Configure Project

- Open the project with preferred IDE. If using VS Code, the IDE will read the devcontainer.json file and prompt you to reopen the project in the devcontainer. Do so.
- Once the project is open, refer to the 'Create and activate a virutal environment' instructions and create a venv file.

## Usage

Run the main script:

Navigate to the app directory and run the command:
`python app.py`

The output will be saved to `output.json` in the app directory. 

## Code Quality: flake8-html

1. Install flake8 and flake8-html
    Flake8 should already be installed when you run the requirement.txt
    install script. If not, run this script
    `pip install flake8 flake8-html`
2. Generatle HTML report
    `flake8 app --format=html --htmldir=flake8-report`
    The HTML report will be in the `flake8-report` directory.

## Project Structure

- `backend/app/app.py` — Main ETL pipeline script
- `mock_data/input/` — Input JSON files
- `output.json` — Output file


