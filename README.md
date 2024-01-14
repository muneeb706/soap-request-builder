# SOAP Request Builder

This project demonstrates how to convert a JSON request into an XML SOAP request. It uses sample data to build a Start Transaction request for the [Equifax](https://www.equifax.com/personal/) Start Transaction Service.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The project is written in Python (tested with python 3.9.1). You need to have Python installed on your machine. You can download Python [here](https://www.python.org/downloads/).

### Installation

1. Clone the repository:
    ```
    git clone https://github.com/muneeb706/soap-request-builder.git
    ```
2. Navigate to the project directory:
    ```
    cd soap-request-builder
    ```
3. Install the dev dependencies:
    ```
    pip install -r requirements-dev.txt
    ```

### How to run

Run the `main.py` script:
    ```
    python main.py
    ```

This will execute the `main.py` script, which uses the `StartTransactionRequestBuilder` class to convert a JSON request into a SOAP request. The SOAP request will be printed in the terminal.

### Running the Tests

After installing the dev dependencies, you can run the unit tests and generate a coverage report.

1. Navigate to the project directory:
    ```
    cd soap-request-builder
    ```
2. Run the tests with coverage:
    ```
    coverage run -m unittest discover tests
    ```
3. Generate the coverage report:
    ```
    coverage report -m
    ```

This will execute the unit tests and print a coverage report in the terminal. The coverage report shows the percentage of your code that is covered by the tests.