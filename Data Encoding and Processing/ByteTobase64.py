"""Encoding and Decoding Binary Data"""
import base64

binary = b'binary text'
encoded = base64.b64encode(binary)
print(f'Encoded String: {encoded}')

decoded = base64.b64decode(encoded)
print(f'Decoded String: {decoded}')
