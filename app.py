from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

# Definisi layanan Contact
class ContactService(ServiceBase):
    @rpc(Integer, _returns=Unicode)
    def get_contact(ctx, id):
        contacts = {1: "Andini Rahmadina", 2: "Dila Ayumaulana"}
        return contacts.get(id, "Not Found")

# Definisi layanan Address
class AddressService(ServiceBase):
    @rpc(Integer, _returns=Unicode)
    def get_address(ctx, id):
        addresses = {1: "Jl. Merdeka No. 1, Jakarta", 2: "Jl. Pahlawan No. 13, Kediri"}
        return addresses.get(id, "Not Found")

# Konfigurasi aplikasi SOAP
application = Application(
    [ContactService, AddressService], 
    tns='http://example.com/',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

# Menjalankan server SOAP
from wsgiref.simple_server import make_server
server = make_server('0.0.0.0', 8000, WsgiApplication(application))
print("SOAP API berjalan di http://localhost:8000")
server.serve_forever()
