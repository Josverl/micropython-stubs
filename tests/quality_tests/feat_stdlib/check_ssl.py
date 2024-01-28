import ssl

from typing_extensions import assert_type, get_type_hints

a = ssl.CERT_NONE
b = ssl.CERT_OPTIONAL
c = ssl.CERT_REQUIRED

# valid
ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_SERVER) 

# below should NOT be available in stubs
# FIXME = ssl.create_default_context() 
