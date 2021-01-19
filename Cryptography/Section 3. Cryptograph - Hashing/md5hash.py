# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 10:17:13 2021

@author: Wen
"""

import hashlib
import os

md5hasher = hashlib.md5(b'hello')
md5hasher.hexdigest()


hashlib.md5(b'bob'*2).hexdigest()
hashlib.md5(b'bobbob').hexdigest()

hashlib.md5(b'password').hexdigest()

md5example = hashlib.md5()
md5example.update(0b1100001)


path = 'D:\\OneDrive - University of Toledo\\Desktop'
os.chdir(path)


hasher = hashlib.md5()
with open('IJPE - National Culture.zip', 'rb') as afile:
    buf = afile.read()
    hasher.update(buf)
    
print(hasher.hexdigest())

#Print as bin string
    
binstring = bin(int(hasher.hexdigest(), 16))

print(binstring)

#https://www.pythoncentral.io/hashing-files-with-python/

import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend

salt = os.urandom(16)

kdf = Scrypt(salt = salt, length = 32, n = 2**14, r = 8, p = 1, backend = default_backend())

key = kdf.derive(b"my great password")

kdf = Scrypt(salt = salt, length = 32, n = 2**14, r = 8, p = 1, backend = default_backend())
kdf.verify(b"my great password", key)
print("success! (Exception if mismatch)")



