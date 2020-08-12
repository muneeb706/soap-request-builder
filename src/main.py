import os.path
from os import path
import json
import copy
from constants import CustomerInformationAttributes, ComplianceAttributes
from start_transaction_request_builder import StartTransactionRequestBuilder
import datetime

if __name__ == "__main__":
    
    dirname = os.path.dirname(__file__)
    json_path = os.path.join(dirname, '..\sample_requests\sample1.json')
    
    if (path.exists(json_path)):
        with open(json_path) as json_file:
            try:
                json_content = json.load(json_file)
                language_code = "en"
                start_transaction_request = StartTransactionRequestBuilder(json_content, language_code).build()
                print(start_transaction_request)
            except ValueError:
                print("Given JSON file is invalid. Content of the file should be a valid JSON object.")
    else:
        print(f"File {json_path} does not exist.")