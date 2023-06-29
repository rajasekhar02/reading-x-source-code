from collections import *

def specialString(s, n, p):
    stringList = [s[i]-ord('a') for i in range(0,n)]
    
    for changeLen in range(1, n+1):
        
        for char in range(0,p):
            