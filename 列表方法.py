Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list1=[2,3,4,1,32,4]
>>> list1
[2, 3, 4, 1, 32, 4]
>>> list1.append(19)
>>> list1
[2, 3, 4, 1, 32, 4, 19]
>>> list1.count(4)
2
>>> list2 = [33,43]
>>> list1.extend(list2)
>>> list1
[2, 3, 4, 1, 32, 4, 19, 33, 43]
>>> list1.index(4)
2
>>> list1.insert(1,25)
>>> list1
[2, 25, 3, 4, 1, 32, 4, 19, 33, 43]
>>> 
