#!/usr/bin/env python
import hashlib
def GenerateMD5 (x):
      m=hashlib.md5()
      m.update(x)
      a=m.hexdigest()
      print a
def GenerateSHA (x):
      s=hashlib.sha()
      s.update(x)
      a=s.hexdigest()
      print a
b=raw_input("Inserire il tipo:MD5 o SHA:")
if b=="MD5":
      pwn=raw_input("Inserire la password da criptare:")
      GenerateMD5(pwn)
elif b=="SHA":
      pwn=raw_input("Inserire la password da criptare:")
      GenerateSHA(pwn)
else:
      print 'Inserire MD5 o SHA'
