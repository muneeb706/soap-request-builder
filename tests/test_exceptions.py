import unittest
from soap_request_builder.exceptions import (
    RequestToEquifaxTimedOutError,
    EquifaxServerError,
)


class TestExceptions(unittest.TestCase):
    def test_request_to_equifax_timed_out_error(self):
        try:
            raise RequestToEquifaxTimedOutError()
        except RequestToEquifaxTimedOutError as e:
            self.assertEqual(str(e), "Request to equifax has timed out!")

    def test_equifax_server_error(self):
        try:
            raise EquifaxServerError("Server Error")
        except EquifaxServerError as e:
            self.assertEqual(
                str(e),
                "Server error occurred at Equifax or Equifax has returned unexpected response. Response from Equifax: Server Error",
            )
            self.assertEqual(e.get_error_response_from_equifax(), "Server Error")
