#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os

def encrypt_char(msg_char, key_char):
    return chr(ord(msg_char) ^ ord(key_char))

def decrypt_char(ciphertext_char, key_char):
    """Takes two characters and decrypt the first using
    the second as a key."""
    return encrypt_char(ciphertext_char, key_char)

def encrypt(msg, key):
    """Encrypts msg string with key."""
    cipher = [encrypt_char(m, k) for (m, k) in zip(msg, key)]
    return ''.join(cipher)

def decrypt(ciphertext, key):
    """Decrypts ciphertext string with key."""
    return encrypt(ciphertext, key)

def get_key():
    return os.urandom(20)

msg = "Attack at dawn"
key = get_key()

# Encrypting msg 'u' with key 'o'
# print encrypt('u', 'o')
# print decrypt_char(encrypt_char('u', 'o'), 'o')

# E_k(m) = c
# D_k = E_k
# D_k(E_k(m)) = m
# E_k(E_k(m)) = m
