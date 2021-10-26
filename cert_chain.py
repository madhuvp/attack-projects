#!/usr/bin/python3

from OpenSSL import SSL,crypto
from OpenSSL.crypto import X509,X509Store,X509StoreContext
import socket
import certifi
import pem
import fnmatch
import urllib.request

# Cert Paths
TRUSTED_CERTS_PEM = certifi.where()

def get_cert_chain(target_domain):
    '''
    This function gets the certificate chain from the provided
    target domain. This will be a list of x509 certificate objects.
    '''
    # Set up a TLS Connection
    dst = (target_domain.encode('utf-8'), 443)
    ctx = SSL.Context(SSL.SSLv23_METHOD)
    s = socket.create_connection(dst)
    s = SSL.Connection(ctx, s)
    s.set_connect_state()
    s.set_tlsext_host_name(dst[0])

    # Send HTTP Req (initiates TLS Connection)
    s.sendall('HEAD / HTTP/1.0\n\n'.encode('utf-8'))
    s.recv(16)
    
    # Get Cert Meta Data from TLS connection
    test_site_certs = s.get_peer_cert_chain()
    #print(vars(test_site_certs))
    s.close()
    return test_site_certs

############### Add Any Helper Functions Below

##############################################



def x509_cert_chain_check(target_domain: str) -> bool:
    '''
    This function returns true if the target_domain provides a valid 
    x509cert and false in case it doesn't or if there's an error.
    '''
    
    
    store = crypto.X509Store()
    #store_ctx = crypto.X509Store()
    
    root = pem.parse_file(TRUSTED_CERTS_PEM)
    for i in root:
      parsed_root = crypto.load_certificate(crypto.FILETYPE_PEM,str(i))
      store.add_cert(parsed_root)
    
   
    
    
    chain = get_cert_chain(target_domain)
    leng = len(chain)
    chain.reverse()
    
    for k in chain:
     print(type(k))
     store_ctx = crypto.X509StoreContext(store,k)
     print(store_ctx)
     try:
       store_ctx.verify_certificate()
       return True
     except:
       return False
     store.add_cert(k) 
     
     
   
    
    
    
    #test_site_certs = get_cert_chain(target_domain)
    #parsed_chain = crypto.load_certificate(crypto.FILETYPE_ASN1, test_site_certs)
    #print("hee")
    
    #test_site_certs = get_cert_chain(target_domain)
    #leng = len(test_site_certs)
    #print(leng)
    
    
    #for k in range(leng-1,-1,-1):
     #print(test_site_certs[k])
     #parsed_chain = crypto.load_certificate(crypto.FILETYPE_ASN1, test_site_certs)
     #print(parsed_chain)
    
    #parsed_chain = crypto.load_certificate(crypto.FILETYPE_ASN1, test_site_certs)
    #
    #for i in parsed_root:
    #	print(parsed_root)
   
    #store = X509Store()
    #store.add_cert(parsed_root) 
    
    #store_ctx = X509StoreContext(store,parsed_chain)
    #store_ctx.verify_certificate()
    #store.add_cert(parsed_chain)
    

    # TODO: Complete Me!
    pass
    


if __name__ == "__main__":
    
    # Standalone running to help you test your program
    print("Certificate Validator...")
    target_domain = input("Enter TLS site to validate: ")
    print("".format(target_domain, get_cert_chain(target_domain)))
    print("Certificate for {} verifed: {}".format(target_domain, x509_cert_chain_check(target_domain)))
