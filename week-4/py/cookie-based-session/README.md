Table of Contents
1. [Live Demo](#live-demo)
1. [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
2. [Usage](#usage)
    - [Run the program](#run-the-program)
    - [Run unit tests](#run-unit-tests)

## Live Demo

Url: http://rto55210.pythonanywhere.com/  
Email: rto55210@nezid.com  

## Getting Started

### Prerequisites

Python virtual enviroment is recommended
1. Create virtual environment
   ```sh
   python -m venv venv
   ```
2. Activate virtual environment
   ```sh
   venv\Scripts\activate.bat
   ```
3. Set PYTHONPATH enviroment variable
   ```sh
   SET PYTHONPATH=%CD%
   ```

### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/vkmouse/web-dev-assignment.git
   ```
2. Change the directory to `web-dev-assignment\week-4\py\cookie-based-session`
   ```sh
   cd web-dev-assignment\week-4\py\cookie-based-session
   ```
3. Install the requirement packages
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Run the program

1. Change the directory to `web-dev-assignment\week-4\py\cookie-based-session`
   ```sh
   cd web-dev-assignment\week-4\py\cookie-based-session
   ```
2. Run the program
   ```sh
   python app.py
   ```

### Run unit tests

1. Change the directory to `web-dev-assignment\week-4\py\cookie-based-session`
   ```sh
   cd web-dev-assignment\week-4\py\cookie-based-session
   ```
2. Run unit tests
   ```sh
   pytest -s
   ```
