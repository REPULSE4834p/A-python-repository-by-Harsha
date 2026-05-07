Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> float(10)
10.0
>>> float(5+6j)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    float(5+6j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> float(True)
1.0
>>> float(False)
0.0
>>> float("string")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    float("string")
ValueError: could not convert string to float: 'string'
>>> float(5.6)
5.6
