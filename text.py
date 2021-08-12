
b2 = b
res = 1
while e:
if e & 1:
res = (res * b2) % m
b2 = (b2*b2) % m
e >>= 1
return res
efile = open('efile.pem', 'r')
e = int(efile.read())
efile.close()
dfile = open('dfile.pem', 'r')
d = int(dfile.read())
dfile.close()

nfile = open('nfile.pem', 'r')
n = int(nfile.read())
nfile.close()
def encrypt():
try:
char_list = [ch for ch in open(askopenfilename(filetypes = [("TXT
files","*.txt")])).read()]
print(char_list)
num = [ord(char) for char in char_list]
print(num)
for i in range(len(num)):
x = num[i]
x = powmod(x, e, n)
num[i] = x
print(num)
with open('enfile.txt', 'w') as filehandle:
for items in num:
filehandle.write('%s; ' %items)
enfinish()
except TypeError:
filenameerror()
except AttributeError:
filenameerror()
def decrypt():
try:
char_list = [ch for ch in (open(askopenfilename(filetypes = [("TXT
files","*.txt")])).read()).split(';')]
length = (len(char_list))
print(length)
char_list.pop(length-1)
length = (len(char_list))
print(length)
for iamgettingmad in range(0, length):
k = char_list[iamgettingmad]
k = int(k)
char_list[iamgettingmad] = k
print(char_list)
#num1 = [(char) for char in char_list]
#print(num1)
for i1 in range(len(char_list)):
x1 = char_list[i1]
x1 = powmod(x1, d, n)
char_list[i1] = x1
num1 = [chr(char) for char in char_list]
print(num1)
with open('defile.txt', 'w') as filehandle: #make it .pem file than .txt for good
for items1 in num1:
filehandle.write('%s' %items1)
definish()
except TypeError:
filenameerror()
except AttributeError:
filenameerror()
def goback():
exit()
