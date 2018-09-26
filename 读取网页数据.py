import urllib.request
infile = urllib.request.urlopen("http://www.baidu.com/index.html")
print(infile.read().decode())