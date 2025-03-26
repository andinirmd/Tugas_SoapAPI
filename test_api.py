import requests

# Endpoint API SOAP
contact_url = "http://localhost:8000/contact"
address_url = "http://localhost:8000/address"

# Header untuk request SOAP
headers = {
    "Content-Type": "text/xml; charset=utf-8"
}

# Request SOAP untuk Contact
contact_request = """<?xml version="1.0"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                  xmlns:con="http://example.com/contact">
   <soapenv:Header/>
   <soapenv:Body>
      <con:get_contact>
         <id>1</id>
      </con:get_contact>
   </soapenv:Body>
</soapenv:Envelope>"""

# Request SOAP untuk Address
address_request = """<?xml version="1.0"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                  xmlns:addr="http://example.com/address">
   <soapenv:Header/>
   <soapenv:Body>
      <addr:get_address>
         <id>1</id>
      </addr:get_address>
   </soapenv:Body>
</soapenv:Envelope>"""

# Kirim Request ke API SOAP
contact_response = requests.post(contact_url, data=contact_request, headers=headers)
address_response = requests.post(address_url, data=address_request, headers=headers)

# Cetak Hasil Respons
print("Response Contact:")
print(contact_response.text)

print("\nResponse Address:")
print(address_response.text)
