#!/user/bin/python
#coding=utf-8

l=[1,2,2,4,3,6,7,4,9]
for i in range(len(l)-1,-1,-1):
	print l[i]

print list(set(l))