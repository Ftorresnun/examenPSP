import smtplib

client=smtplib.SMTP('192.168.1.45:1025')
message_template = 'From: %s\r\nTo: %s\r\n\r\n%s'
sender = 'torres.nufed21@zaragoza.salesianos.edu'
dest = 'gorka.sanz@zaragoza.salesianos.edu'
message = 'contenido del formulario'

client.set_debuglevel(1)

client.sendmail(sender,dest,message_template%(sender,dest,message))
client.ehlo()

