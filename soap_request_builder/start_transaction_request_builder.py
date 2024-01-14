"""
Module for building Start Transaction SOAP requests.

This module handles converting a JSON request body into an XML 
SOAP request to initiate a transaction with the Equifax Start 
Transaction service.

It maps JSON keys to XML tag names and handles populating 
the XML elements based on the data in the JSON request.

The StartTransactionRequestBuilder class inherits from 
SoapRequestBuilder and customizes the mapping and XML 
generation specifically for Start Transaction requests.
"""

import xml.etree.ElementTree as ElementTree
from enum import Enum

from soap_request_builder.soap_request_builder_base import SoapRequestBuilder
from soap_request_builder.constants import CustomerInformationAttributes, ComplianceAttributes


class StartTransactionRequestBuilder(SoapRequestBuilder):
    # all XML tag names that can be used for sending start transaction request to Equifax
    class StartTransactionRequestXmlTagsNames(Enum):
        NAME = "Name"
        FIRST_NAME = "FirstName"
        LAST_NAME = "LastName"
        ADDRESS = "Address"
        HYBRID_ADDRESS = "HybridAddress"
        ADDRESS_TYPE = "addressType"
        ADDRESS_LINE = "AddressLine"
        CITY = "City"
        PROVINCE = "Province"
        POSTAL_CODE = "PostalCode"
        DATE_OF_BIRTH = "DateOfBirth"
        DAY = "Day"
        MONTH = "Month"
        YEAR = "Year"
        DRIVER_LICENSE = "DriversLicense"
        NUMBER = "Number"
        DRIVERS_LICENSE_ADDRESS_TYPE = "driversLicenseAddressType"
        SIN = "SIN"
        PHONE_NUMBER = "PhoneNumber"
        PHONE_TYPE = "phoneType"
        EMAIL = "Email"
        CUSTOMER_ID = "CustomerId"

    # JSON keys to XML tags mapping for XML attributes names
    START_TRANSACTION_REQUEST_ATTRIBUTES_MAPPINGS = {
        ComplianceAttributes.ADDRESS_TYPE.value: StartTransactionRequestXmlTagsNames.ADDRESS_TYPE.value,
        ComplianceAttributes.PHONE_TYPE.value: StartTransactionRequestXmlTagsNames.PHONE_TYPE.value,
        ComplianceAttributes.DRIVERS_LICENSE_ADDRESS_TYPE.value: StartTransactionRequestXmlTagsNames.DRIVERS_LICENSE_ADDRESS_TYPE.value,
    }

    # JSON keys to XML tags mapping for XML tags names
    START_TRANSACTION_REQUEST_TAGS_MAPPINGS = {
        ComplianceAttributes.NAME.value: StartTransactionRequestXmlTagsNames.NAME.value,
        CustomerInformationAttributes.FIRST_NAME.value: StartTransactionRequestXmlTagsNames.FIRST_NAME.value,
        CustomerInformationAttributes.LAST_NAME.value: StartTransactionRequestXmlTagsNames.LAST_NAME.value,
        CustomerInformationAttributes.ADDRESS.value: StartTransactionRequestXmlTagsNames.ADDRESS.value,
        ComplianceAttributes.HYBRID_ADDRESS.value: StartTransactionRequestXmlTagsNames.HYBRID_ADDRESS.value,
        CustomerInformationAttributes.ADDRESS_LINE_1.value: StartTransactionRequestXmlTagsNames.ADDRESS_LINE.value,
        CustomerInformationAttributes.ADDRESS_LINE_2.value: StartTransactionRequestXmlTagsNames.ADDRESS_LINE.value,
        CustomerInformationAttributes.CITY.value: StartTransactionRequestXmlTagsNames.CITY.value,
        CustomerInformationAttributes.STATE_REGION.value: StartTransactionRequestXmlTagsNames.PROVINCE.value,
        CustomerInformationAttributes.POSTAL_CODE.value: StartTransactionRequestXmlTagsNames.POSTAL_CODE.value,
        CustomerInformationAttributes.BIRTH_DATE.value: StartTransactionRequestXmlTagsNames.DATE_OF_BIRTH.value,
        ComplianceAttributes.DAY.value: StartTransactionRequestXmlTagsNames.DAY.value,
        ComplianceAttributes.MONTH.value: StartTransactionRequestXmlTagsNames.MONTH.value,
        ComplianceAttributes.YEAR.value: StartTransactionRequestXmlTagsNames.YEAR.value,
        CustomerInformationAttributes.DRIVER_LICENSE.value: StartTransactionRequestXmlTagsNames.DRIVER_LICENSE.value,
        CustomerInformationAttributes.NUMBER.value: StartTransactionRequestXmlTagsNames.NUMBER.value,
        CustomerInformationAttributes.TIN_SSN.value: StartTransactionRequestXmlTagsNames.SIN.value,
        CustomerInformationAttributes.PHONE.value: StartTransactionRequestXmlTagsNames.PHONE_NUMBER.value,
        CustomerInformationAttributes.EMAIL.value: StartTransactionRequestXmlTagsNames.EMAIL.value,
        CustomerInformationAttributes.ACCOUNT_ID.value: StartTransactionRequestXmlTagsNames.CUSTOMER_ID.value,
    }

    def __init__(self, json_request_body, input_language):
        super().__init__(
            json_request_body,
            input_language,
            __class__.START_TRANSACTION_REQUEST_ATTRIBUTES_MAPPINGS,
            __class__.START_TRANSACTION_REQUEST_TAGS_MAPPINGS,
        )

    def _create_body_element(self):
        soapenv_body = ElementTree.SubElement(self._soap_request, "soapenv:Body")
        initial_request = ElementTree.SubElement(soapenv_body, "v3:InitialRequest")
        identity = ElementTree.SubElement(initial_request, "v3:Identity")
        self._add_arguments_to_request_body(identity, self._json_request_body)
        processing_options = ElementTree.SubElement(
            initial_request, "v3:ProcessingOptions"
        )
        ElementTree.SubElement(
            processing_options, "v3:Language"
        ).text = self._processing_language
