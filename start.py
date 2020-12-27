#!/bin/python3
#edited for GIT
alph = 'abcdefghijklmnopqrstuvwxyz'
a = []
char = input('Please enter a character: ')
key = int(input('Enter a key(1-26): '))
for i in char:
  if(i==' '):
    newC = ' '
    a.append(newC)
  else:
    pos = alph.find(i)
    NewPos = (pos + key) % 26
    newC = alph[NewPos]
    a.append(newC)
msg = ''.join(a)
print(msg)
print("New Commit")
