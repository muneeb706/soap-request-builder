"""
Main module to build a SOAP request from a JSON sample file.
"""

from os import path
import json
from soap_request_builder import StartTransactionRequestBuilder


def get_sample_file_path():
    dirname = path.dirname(__file__)
    return path.join(dirname, "sample_requests", "sample1.json")


def load_json(file_path):
    with open(file_path) as json_file:
        return json.load(json_file)


def main():
    json_path = get_sample_file_path()
    if path.exists(json_path):
        json_content = load_json(json_path)
        request_builder = StartTransactionRequestBuilder(json_content, "en")
        print(request_builder.build())

    else:
        print(f"File {json_path} does not exist.")


if __name__ == "__main__":
    main()
