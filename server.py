import socket
import pandas as pd
import csv
from Login_Register import check_OTP


client_side_OTP = []
company_names = []
pointer = 0

s = socket.socket()

print('socket created')

#this is the server socket that accepts the port numbers


s.bind(('localhost', 9998))

#start listening to the client
#listneing for 3 clients
s.listen(3)

print('waiting for connection')



while True:
    c, addr = s.accept()
    data = c.recv(1024).decode()
    #print(data)
    data_split = data.split(' ')
    print(data_split)
    name_of_company = data_split[0]
    OTP = data_split[1]
    client_side_OTP.append(OTP)
    company_names.append(name_of_company)
    print("This is the entered OTP provided by client " + OTP)
    #check_OTP(OTP)
    #c.close()

    #query = c.recv((1024).decode())
    #print("Query received about: Potatoes")
    print('client connected with', addr,data)
    df = pd.read_csv("Employee_Satisfaction.csv")
    c.send(bytes(str(df),'utf-8'))
    #c.send(bytes('Hello ' + str(name) + ' welcome to Shaikat Server', 'utf-8'))
    #c.send(bytes("Thank you for making a query about " + str(query)))

    print("This is the client side OTPlist: " + str(client_side_OTP))
    check_OTP(client_side_OTP[pointer])
    pointer = pointer + 1

    c.close()



