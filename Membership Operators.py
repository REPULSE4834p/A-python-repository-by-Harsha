Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> ("Membership Operator")
'Membership Operator'
>>> a=1,2,3,4,5,6,7,8,9,10
>>> if 10 in a:
...     print("Yes")
... 
...     
Yes
>>> if 11 not in a:
...     print("No")
... 
...     
No
>>> if 11 not in a or 10 in a:
...     print("Yes")
... 
...     
Yes
