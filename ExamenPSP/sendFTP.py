from ftplib import FTP
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

url ="192.168.1.45:23"
with FTP(url) as conn:
    conn.login("username", "password")
    conn.cwd('/')
    conn.pwd()
    conn.getwelcome()
    #descargar archivo
    conn.retrbinary('RETR ' + 'archivo.txt', open('archivo.txt', 'wb').write)
    #guardar archivo en carpeta descarga
    conn.retrbinary('RETR ' + 'archivo.txt', open('descarga/archivo.txt', 'wb').write)

file_in = open("nombreArchivo", "rb")

private_key = RSA.import_key(open("private.pem").read())

enc_session_key = file_in.read(private_key.size_in_bytes())
file_in.close()

cipher_rsa = PKCS1_OAEP.new(private_key)
session_key = cipher_rsa.decrypt(enc_session_key)
print(session_key)