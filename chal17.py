from Crypto.Cipher import AES
import random
import base64
import os

def pad(msg):
    return msg + bytes([16 - (len(msg)%16) for _ in range(16 - (len(msg)%16))])

def unpad(msg):
    if len(msg) % 16 != 0:
        return False
    tmp = msg[-1]
    for _ in range(1,tmp+1):
        if msg[-_] != tmp:
            return False
    return True

def function_to_encrypt():
    strings_ = ["MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=",
    "MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=",
    "MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==",
    "MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==",
    "MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl",
    "MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==",
    "MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==",
    "MDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=",
    "MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=",
    "MDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93"]
    msg = base64.b64decode(random.choice(strings_).encode())

    key = os.urandom(16)
    IV = os.urandom(16)
    aes = AES.new(key = key,mode = AES.MODE_CBC,iv = IV)
    cipher = (IV + aes.encrypt(pad(msg)))
    return key,cipher

def function_to_check():
    key,cipher = function_to_encrypt()
    IV = cipher[:16]
    ciphertext = cipher[16:]
    aes = AES.new(key = key,mode = AES.MODE_CBC,iv = IV)
    msg = aes.decrypt(ciphertext)
    return unpad(msg)

print(function_to_check())