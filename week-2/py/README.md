Table of Contents
1. [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
2. [Usage](#usage)
3. [Unit Test](#unit-test)

## Getting Started

### Prerequisites

Python virtual enviroment is recommended
- Create virtual environment
  ```sh
  python -m venv venv
  ```
- Activate virtual environment
  ```sh
  venv\Scripts\activate.bat
  ```

### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/vkmouse/web-dev-assignment.git
   ```

2. Change the directory to `web-dev-assignment\week-2\py`
   ```sh
   cd web-dev-assignment\week-2\py
   ```

3. Install the requirement packages
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Change the directory to `web-dev-assignment\week-2\py`
   ```sh
   cd web-dev-assignment\week-2\py
   ```

2. Run the program
   ```sh
   python main.py
   ```

## Unit Test

1. Change the directory to `web-dev-assignment\week-2\py`
   ```sh
   cd web-dev-assignment\week-2\py
   ```

2. Run unit tests
   ```sh
   python -m unittest discover -s functions -p *_test.py
   ```
