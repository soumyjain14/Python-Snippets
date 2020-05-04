fname=input('enter the file name')
fhandle=open(fname)
counts=dict()
for line in fhandle:
    if line.startswith('From:'):
        continue
    if line.startswith('From'):
        line=line.rstrip()
        words=line.split()
        for word in words[1:2]:
            if word not in counts:
                counts[word]=1
            else:
                counts[word]=counts[word]+1
bigword=None
bigcount=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count
print(bigword,bigcount)
