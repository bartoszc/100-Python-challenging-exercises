"""Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!"."""
from gzip import zlib as z


strr = '"hello world!hello world!hello world!hello world!"'
strr = strr.encode('utf-8')
t = z.compress(strr, 1)
print(t)
t = z.decompress(t)
print(t)
