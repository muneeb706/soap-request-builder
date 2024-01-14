import unittest
from unittest.mock import patch, mock_open
from soap_request_builder.main import get_sample_file_path, load_json, main


class TestMain(unittest.TestCase):
    def test_get_sample_file_path(self):
        # Call the function
        file_path = get_sample_file_path()

        # Assert that the file path ends with the expected path
        self.assertTrue(file_path.endswith("sample_requests/sample1.json"))

    def test_load_json(self):
        # Mock a file with some JSON content
        mock_file = mock_open(read_data='{"key": "value"}')

        # Replace the built-in open function with our mock file
        with patch("builtins.open", mock_file):
            # Call the function with a dummy file path
            data = load_json("dummy_path")

        # Assert that the function correctly loaded the JSON data
        self.assertEqual(data, {"key": "value"})

    @patch("soap_request_builder.main.StartTransactionRequestBuilder")
    def test_main(self, mock_builder):
        # Mock the StartTransactionRequestBuilder's build method
        mock_builder.return_value.build.return_value = "request"

        # Replace the built-in print function with a mock
        with patch("builtins.print") as mock_print:
            # Call the main function
            main()

        # Assert that the print function was called with the expected argument
        mock_print.assert_called_once_with("request")
