class RequestToEquifaxTimedOutError(Exception):
    def __init__(self):
        default_message = "Request to equifax has timed out!"
        super().__init__(default_message)


class EquifaxServerError(Exception):
    def __init__(self, equifax_response):
        default_message = f"Server error occurred at Equifax or Equifax has returned unexpected response. " \
            f"Response from Equifax: {equifax_response}"
        self.__error_response_from_equifax = equifax_response
        super().__init__(default_message)

    def get_error_response_from_equifax(self):
        return self.__error_response_from_equifax


# class VendorUnavailableError(Exception):
#     def __init__(self):
#         default_message = "Vendor is in maintenance mode"
#         super().__init__(default_message)


class InvalidCustomerIdentityInformationError(Exception):

    def __init__(self, invalid_fields, message):
        default_message = "Submitted Customer identity is invalid."
        self.__message = message is not None and message or default_message
        self.__invalid_fields = invalid_fields
        super().__init__(self.__message)

    def get_invalid_fields_list(self):
        return self.__invalid_fields

    def get_message(self):
        return self.__message


class SOAPRequestBuildFailedError(Exception):
    pass
