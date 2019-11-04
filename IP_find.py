import socket

print("Enter Website\n")

SITE = input(">>> ")
print(" ")

ip = socket.gethostbyname(SITE)
print("========================================")
print(SITE + "'s IP is: " + ip)
print("========================================")
