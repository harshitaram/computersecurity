import ssl
import csv
import socket
import OpenSSL
#from OpenSSL._util import (
#    lib as _lib,
#)
from datetime import datetime
import socket

socket.setdefaulttimeout(10)
sock = socket.socket()
sock.timeout
10.0

def get_cert_ob(website):
    #website = 'google.com'
    ctx = ssl.create_default_context()
    try:
        connection = socket.socket()
        connection.timeout
        connection = socket.create_connection((website, 443))
        s = ctx.wrap_socket(connection, server_hostname=website)
        cert = s.getpeercert(True)
        s.close()
        cert = ssl.DER_cert_to_PEM_cert(cert)
        x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert) 
        return x509
    except:
        return "fail"


def Q12(cert):
    name_ob = cert.get_issuer()
    org_name = name_ob.organizationName
    return org_name 

def Q13_start(cert):
    start_time = cert.get_notBefore()
    return start_time

def Q13_end(cert):   
    end_time = cert.get_notAfter()
    return end_time

def turn_ASN1_time_to_datetime(asn_time: bytes): #Ed #238
    """
    function to convert ASN times as given by the certs
    to a date time
    YYYYMMDDhhmmssZ
    """


    #print(len(asn_time))
    assert len(asn_time) == 15
    asn_date = datetime.strptime(asn_time.decode('ascii'),"%Y%m%d%H%M%SZ")

    return asn_date

def find_second_difference_for_asn_times(asn_time_1: bytes, asn_time_2: bytes) -> float:
    end_date = turn_ASN1_time_to_datetime(asn_time_1)
    start_date = turn_ASN1_time_to_datetime(asn_time_2)

    #date_1_timestamp = date_1.timestamp()
    #date_2_timestamp = date_2.timestamp()



    difference = end_date - start_date

    return difference.days

def Q14(cert):
    get_key = cert.get_pubkey()
    get_int = get_key.type()

    rsa_comp = OpenSSL.crypto.TYPE_RSA #https://github.com/pyca/pyopenssl/blob/main/src/OpenSSL/crypto.py#L106
    dsa_comp = OpenSSL.crypto.TYPE_DSA
    dh_comp = OpenSSL.crypto.TYPE_DH
    ec_comp = OpenSSL.crypto.TYPE_EC

    if get_int == rsa_comp:
        return "RSA"
    elif get_int == dsa_comp:
        return "DSA"
    elif get_int == dh_comp:
        return "DH"
    elif get_int == ec_comp:
        return "EC"
    else:
        return "Not found"
 
def Q15(cert):
    get_key = cert.get_pubkey()
    get_int = get_key.bits()
    return get_int

def Q16(cert):
    #if RSA type 
    get_pkey = cert.get_pubkey()
    get_key = get_pkey.to_cryptography_key()
    get_pub = get_key.public_numbers()
    get_exponent = get_pub.e #https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/#cryptography.hazmat.primitives.asymmetric.rsa.RSAPublicNumbers.e
    return(get_exponent)

def Q17(cert):
    sig_alg = cert.get_signature_algorithm()
    return sig_alg #in bytes 

if __name__ == "__main__":
   
   """ cert_try = get_cert_ob('google.com')
   print(cert_try)
   q12 = Q12(cert_try)
   print(q12)
   q13_start = Q13_start(cert_try)
   q13_end = Q13_end(cert_try)
   q13 = find_second_difference_for_asn_times(q13_end, q13_start)
   print(q13)
   q14 = Q14(cert_try)
   print(q14)
   q15 = Q15(cert_try)
   print(q15)
   #q16 = Q16(cert_try)
   #print(q16)
   q17 = Q17(cert_try)
   print(q17) """
   with open("step0-othersites.csv", "r") as input_file:
        # Open result CSV file for writing
        with open("step4-othersites-selenium.csv", "w", newline='') as output_file:
            # Create a CSV writer
            csv_writer = csv.writer(output_file)
            
            # Iterate through each row in the input CSV file
            for i, line in enumerate(input_file):

                #if i < 390:
                #    continue
                # Extract the URL and index from the line
                index, destination = line.split(",", 1)
                index = index.strip()
                destination = destination.strip() 
                cert_try = get_cert_ob(destination)
                if cert_try == "fail":
                    continue 
                q12 = Q12(cert_try)
   
                q13_start = Q13_start(cert_try)
                q13_end = Q13_end(cert_try)
                q13 = find_second_difference_for_asn_times(q13_end, q13_start)
                
                q14 = Q14(cert_try)
                q15 = Q15(cert_try)
                if q14 == "RSA":
                    q16 = Q16(cert_try)
                else:
                    q16 = "none"
   
                q17 = Q17(cert_try)

                row = [index, destination, q12, q13, q14, q15, q16, q17]
                csv_writer.writerow(row)
                print(i)
    
input_file.close()   
output_file.close()
exit()