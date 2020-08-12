from enum import Enum

# Mappings for language code to language
LANGUAGE_MAPPINGS = {
    "en": "English",
    "fr": "French"
}

# Namespaces that are used in SOAP request
NAMESPACES = {
    'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
    'v3': 'http://eid.equifax.com/soap/schema/canada/v3',
    'wsse': 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd'
}

# JSON keys related to customer/consumer details that can be received in requests
class CustomerInformationAttributes(Enum):
    PHONE = 'phone'
    FIRST_NAME = 'first-name'
    LAST_NAME = 'last-name'
    BIRTH_DATE = 'birth-date'
    ADDRESS = 'address'
    ADDRESS_LINE_1 = 'address-line-1'
    ADDRESS_LINE_2 = 'address-line-2'
    CITY = 'city'
    STATE_REGION = 'state-region'
    POSTAL_CODE = 'postal-code'
    COUNTRY_CODE = 'country-code'
    TIN_SSN = 'tin-ssn'
    ACCOUNT_ID = 'account-id'
    APPLICATION_CREATED_AT = 'application-created-at'
    APPLICATION_ID = 'application-id'
    CORRELATION_ID = 'correlation-id'
    EMAIL = 'email'
    IP_ADDRESS = 'ip-address'
    CBI_CONTEXT = 'cbi-context'
    DRIVER_LICENSE = 'driver-license'
    NUMBER = 'number'
    ORDER_ID = 'order-id'
    LOAN_ID = 'loan-id'

    @staticmethod
    def values():
        return list(map(lambda c: c.value,
                        CustomerInformationAttributes))

# Keys that are not received in request, but are used for compliance during transformation of request
# So that the JSON request can easily be converted into XML
class ComplianceAttributes(Enum):
    PHONE_TYPE = 'phone-type'
    NAME = 'name'
    HYBRID_ADDRESS = 'hybrid-address'
    ADDRESS_TYPE = 'address-type'
    DAY = 'day'
    MONTH = 'month'
    YEAR = 'year'
    IQ_ANSWER_REQUEST = 'iq-answer-request'
    DRIVERS_LICENSE_ADDRESS_TYPE = 'drivers-license-address-type'
