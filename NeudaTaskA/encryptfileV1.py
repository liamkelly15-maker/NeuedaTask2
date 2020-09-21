# Neueda Task Python script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Press Shift+F10 to execute it.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json as j
from cryptography.fernet import Fernet

with open("../json_file.json") as json_format_file:
  d = j.load(json_format_file)
import xml.etree.cElementTree as e
r = e.Element("Employee")
e.SubElement(r,"Name").text = d["Name"]
e.SubElement(r,"Designation").text = d["Designation"]
e.SubElement(r,"Salary").text = str(d["Salary"])
e.SubElement(r,"Age").text = str(d["Age"])
project = e.SubElement(r,"Projects")
for z in d["Projects"]:
  e.SubElement(project,"Topic").text = z["Topic"]
  e.SubElement(project,"Category").text = z["Category"]
  e.SubElement(project,"Months").text = str(z["Months"])
a = e.ElementTree(r)
a.write("../json_to_xml.xml")

def write_key():
    """Generates a key and save it into a file"""
    key = Fernet.generate_key()
    with open("../key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """Loads the key from the current directory named `key.key`"""
    return open("../key.key", "rb").read()

def encrypt(filename, key):
    """Given a filename (str or xml) and key (bytes), it encrypts the file and write it"""
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
        # encrypt data
        encrypted_data = f.encrypt(file_data)
        # write the encrypted file
        with open(filename, "wb") as file:
            file.write(encrypted_data)


def decrypt(filename, key):
    """Given a filename (str or xml) and key (bytes), it decrypts the file and write it"""
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)

#generate the key
write_key()
#load the key
key = load_key()
#check the key
#print(key)
# file name
file = "../json_to_xml.xml"
# encrypt it
encrypt(file, key)
# decrypt it
#decrypt(file, key)




