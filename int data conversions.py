Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> int(10)
10
>>> int(5+9j)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    int(5+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(True)
1
>>> int(False)
0
>>> int("String")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("String")
ValueError: invalid literal for int() with base 10: 'String'
>>> int(5.6)
5
