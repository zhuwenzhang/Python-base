Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a ={"111":"朱文章","222":"朱文章二号"}
>>> a["111"]
'朱文章'
>>> a["222"] = "zhuwen"
>>> a["222"]
'zhuwen'
>>> a["333"]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a["333"]
KeyError: '333'
>>> 
