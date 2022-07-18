# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 16:33:32 2021

@author: Caroline
"""

#Email

import smtplib

from email.mime.text import MIMEText

msg= MIMEText("contenido")

msg['subject']='Asunto correo'
msg['From']='cpradave@gmail.com'
msg['To']= 'caroline.pradav@gmail.com'


#Config. Servidor
mailServer=smtplib.SMTP('smtp.gmail.com', 587)
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login('cpradave@gmail.com', "0101251356*")
mailServer.sendmail('cpradave@gmail.com', 'caroline.pradav@gmail.com', msg_as_string())
mailServer.close()