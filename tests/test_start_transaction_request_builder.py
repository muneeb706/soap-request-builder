import unittest
from unittest.mock import patch
import json
from soap_request_builder.start_transaction_request_builder import (
    StartTransactionRequestBuilder,
)


class TestStartTransactionRequestBuilder(unittest.TestCase):
    def setUp(self):
        with open("sample_requests/sample1.json", "r") as file:
            self.json_request_body = json.load(file)
        self.input_language = "en"
        self.builder = StartTransactionRequestBuilder(
            self.json_request_body, self.input_language
        )

    @patch("soap_request_builder.soap_request_builder.SoapRequestBuilder.build")
    def test_build(self, mock_super_build):
        # Mock the build method of the superclass
        mock_super_build.return_value = "mocked SOAP request"

        # Call the build method
        soap_request = self.builder.build()

        # Assert that the build method of the superclass was called
        mock_super_build.assert_called_once()

        # Assert that the build method returns the expected SOAP request
        self.assertEqual(soap_request, "mocked SOAP request")
