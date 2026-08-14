# Mortality Risk Estimator
A command-line tool demonstrating linear algebra concepts through healthcare risk assessment.
## Overview
This tool calculates mortality risk scores using vector operations (dot product).
It demonstrates fundamental NumPy operations modular structure and unit testing.
## Requirements
- Python 3.8+
- NumPy
## Setup
1. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate # On Windows: .venv\Scripts\activate
```
2. Install dependencies:
```bash
pip install numpy
```
## Usage
```bash
python src/cli.py --vector "75,120,80,1" --weights "0.02,0.5,0.1,5"
```
## Project Structure
- `src/cli.py` - Command-line interface
- `src/math_ops.py` - Core mathematical operations
- `src/io_parser.py` - Input parsing utilities
## Author
Created as part of AI Engineering Bootcamp - Week 1, Tuesday Code Session
