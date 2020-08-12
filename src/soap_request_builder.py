import logging
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod

from constants import LANGUAGE_MAPPINGS, NAMESPACES
from exceptions import SOAPRequestBuildFailedError

log = logging.getLogger(__name__)


class SoapRequestBuilder(ABC):

    def __init__(self, json_request_body, input_language, attributes_mappings, tags_mappings):
        self._processing_language = LANGUAGE_MAPPINGS[input_language]
        self._json_request_body = json_request_body
        self._attributes_mappings = attributes_mappings
        self._tags_mappings = tags_mappings
        self._soap_request = None
        super().__init__()

    def build(self):
        self._soap_request = __class__.__create_root_element()
        self.__create_header_element()
        self._create_body_element()
        return ElementTree.tostring(self._soap_request)

    @staticmethod
    def __create_root_element():
        soapenv = ElementTree.Element('soapenv:Envelope', {
            'xmlns:soapenv': NAMESPACES['soapenv'],
            'xmlns:v3': NAMESPACES['v3']
        })
        return soapenv

    def __create_header_element(self):
        soap_request_header = ElementTree.SubElement(self._soap_request, 'soapenv:Header')
        security = ElementTree.SubElement(soap_request_header, 'wsse:Security',
                                          {'soapenv:mustUnderstand': "1",
                                           'xmlns:wsse': NAMESPACES['wsse']})
        username_token = ElementTree.SubElement(security, 'wsse:UsernameToken')
        username = ElementTree.SubElement(username_token, 'wsse:Username')
        password = ElementTree.SubElement(username_token, 'wsse:Password')
        username.text = "username"
        password.text = "password"

    @abstractmethod
    def _create_body_element(self):
        pass

    def _add_arguments_to_request_body(self, parent_element, child_elements_json):
        """
        converts JSON object into XML and adds that XML (arguments) inside SOAP request body
        :param parent_element: xml element which will encapsulate arguments in the form of XML
        :param child_elements_json: JSON object which will be converted into XML (arguments)
        """
        try:
            for key, value in child_elements_json.items():
                # if item is an attribute of parent element
                if key in self._attributes_mappings:
                    parent_element.set(self._attributes_mappings[key], value)
                # if item is a child element of parent element
                else:
                    # if item is a simple dictionary object
                    if isinstance(value, dict) and key in self._tags_mappings:
                        self.__create_object_element(key, parent_element, value)
                    # if item is an array object
                    elif isinstance(value, list) and key in self._tags_mappings:
                        self.__create_array_elements(key, parent_element, value)
                    # if an item is not an object of any type
                    elif key in self._tags_mappings:
                        current_element = ElementTree.SubElement(parent_element,
                                                                 'v3:' + self._tags_mappings[key])
                        current_element.text = value
        except KeyError as error:
            log.error(str(error))
            raise SOAPRequestBuildFailedError(error)

    def __create_array_elements(self, key, parent_element, value):
        for val in value:
            self.__create_object_element(key, parent_element, val)

    def __create_object_element(self, key, parent_element, value):
        current_element = ElementTree.SubElement(parent_element,
                                                 'v3:' + self._tags_mappings[key])
        self._add_arguments_to_request_body(current_element, value)
        return current_element
