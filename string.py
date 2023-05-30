
## TYPE-1:--

#% Input---"santosh is proposing a girl tomorrow"
## Output---"tomorrow girl a proposing is santosh"

s="santosh is proposing a girl tomorrow"
s1=s.split()
x=[]
for i in range(-1,-len(s1)-1,-1):
    x.append(s1[i])
print(' '.join(x))





## TYPE-2:--
#% Input---"santosh is proposing a girl tomorrow"
## Output---"hsotnas si gnisoporp a lrig worromot"

s="santosh is proposing a girl tomorrow"
s1=s.split()
x=[] 
for i in s1:
    x.append(i[::-1])
print(' '.join(x))





## TYPE-3:--
#% Input---"santosh is proposing a girl tomorrow"
## Output---"hsotnas si gnisoporp a lrig worromot"
s="santosh is proposing a girl tomorrow"
s1=s.split()
print(len(s1))
x=[] 
for i in range(len(s1)):
    x.append(s1[i[::-1]])
print(' '.join(x))