import socket
import pandas as pd
from io import StringIO
import threading


c = socket.socket()

#server will bind the port number and client will simply
#connect the port number together

c.connect(('localhost', 9998))

name = input("Enter your name")

query = input('what do you want to know?')
filename = input("What is the name of your company")
OTP = input("Enter the OTP")

client_side_info = filename + " " + OTP


c.send(bytes(client_side_info, 'utf-8'))
#c.close()
c.send(bytes(query, 'utf-8'))
#c.send(bytes(query,'utf-8'))
df = c.recv(2048).decode()
print(df)

df_new = pd.read_csv(StringIO(df), sep='\s+')
df_new.to_csv(filename + '.csv', mode='a', index=False, header=False)


