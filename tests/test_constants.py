import unittest
from soap_request_builder.constants import (
    LANGUAGE_MAPPINGS,
    NAMESPACES,
    CustomerInformationAttributes,
    ComplianceAttributes,
)


class TestConstants(unittest.TestCase):
    def test_language_mappings(self):
        self.assertEqual(LANGUAGE_MAPPINGS["en"], "English")
        self.assertEqual(LANGUAGE_MAPPINGS["fr"], "French")

    def test_namespaces(self):
        self.assertEqual(
            NAMESPACES["soapenv"], "http://schemas.xmlsoap.org/soap/envelope/"
        )
        self.assertEqual(
            NAMESPACES["v3"], "http://eid.equifax.com/soap/schema/canada/v3"
        )
        self.assertEqual(
            NAMESPACES["wsse"],
            "http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd",
        )

    def test_customer_information_attributes(self):
        self.assertEqual(CustomerInformationAttributes.PHONE.value, "phone")
        self.assertEqual(CustomerInformationAttributes.FIRST_NAME.value, "first-name")
        self.assertEqual(CustomerInformationAttributes.LAST_NAME.value, "last-name")
        # Add more assertions for other attributes as needed

        # Test the values() method
        values = CustomerInformationAttributes.values()
        self.assertIn("phone", values)
        self.assertIn("first-name", values)
        self.assertIn("last-name", values)
        # Add more assertions for other values as needed

    def test_compliance_attributes(self):
        self.assertEqual(ComplianceAttributes.PHONE_TYPE.value, "phone-type")
        self.assertEqual(ComplianceAttributes.NAME.value, "name")
        self.assertEqual(ComplianceAttributes.HYBRID_ADDRESS.value, "hybrid-address")
        # Add more assertions for other attributes as needed