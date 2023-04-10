a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
sln=a
if b>sln:
    sln=b
if c>sln:
    sln=c 
snn=a
if b<snn:
    snn=b
if c<snn:
    snn=c
print('SLN=',sln,sep='')
print('SBN=',snn,sep='')
