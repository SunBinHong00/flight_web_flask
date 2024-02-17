import os

path = "./ssl"

if not os.path.exists(path):
    os.makedirs(path)

key = os.environ["SSL_KEY"]
crt = os.environ["SSL_CRT"]

with open("./ssl/key.pem", "w") as pem_file:
    pem_file.write(key)
with open("./ssl/crt.pem", "w") as pem_file:
    pem_file.write(crt)
