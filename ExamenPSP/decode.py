# import cryptography
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

file_in = open("nombreArchivo", "rb")

private_key = RSA.import_key(open("private.pem").read())

enc_session_key = file_in.read(private_key.size_in_bytes())
file_in.close()

cipher_rsa = PKCS1_OAEP.new(private_key)
session_key = cipher_rsa.decrypt(enc_session_key)
print(session_key)