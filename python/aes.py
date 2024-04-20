# AES Encrypt / Decrypt - Simple script to encrypt or decrypt text using the AES algorithm in CBC mode. WIP.

import argparse
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
    return ciphertext


def decrypt(key, ciphertext):
    cipher = AES.new(key, AES.MODE_CBC)
    plaintext = cipher.decrypt(unpad(ciphertext, AES.block_size))
    return plaintext.decode('utf-8')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Encrypt or decrypt text using the AES algorithm in CBC mode.')
    parser.add_argument('key', type=str, help='the encryption key')
    parser.add_argument('-iv', type=str, help='the initialization vector')
    parser.add_argument(
        'text', type=str, help='the text to encrypt or decrypt')
    parser.add_argument('-d', '--decrypt', action='store_true',
                        help='decrypt the input text')
    args = parser.parse_args()

    key = args.key.encode('utf-8')

    iv = args.iv.encode('utf-8')

    text = args.text

    if args.decrypt:
        ciphertext = bytes.fromhex(text)
        plaintext = decrypt(key, ciphertext)
        print(plaintext)
    else:
        ciphertext = encrypt(key, text)
        print(ciphertext.hex())
