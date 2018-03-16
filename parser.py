from lexicalanalyser import *

# S->iECT
# T->eC
# E->(b)
# C->{c}
def isTerminal(a,list1):
    if a<97 and a>122:
        return False
    else:
        return True
def parser(Token):
    d1={'if':'i','else':'e','(b)':'E','{c}':'C'}
    table={'S':'iECT','T':'eC'}
    list1=[]
    matched=[]              
    matched2=[]
    prod=['S->iECT','T->eC' ]
    nonterm=['S','T']
    terminals=['i','e','E','C']
    x=len(Token)
    i=0
    error=0
    list1.append('~')       #stack of production keys
    list1.append('S')
    while(i<x):
    	#print(Token[i])
    	#print(i)
        if Token[i]=='(':
            if Token[i-1]!="if":
                error=1
                print("parsing error")
                break
         
            i=i+1
            str=""
            while Token[i]!=')':
                str=str+Token[i]
                i=i+1
           # i=i+1       
            if i<(x-1):
                a="(b)"
                a=d1.get(a)
            else:
                error=1
                print("parsing error")
                break
        elif Token[i]=='{':
            if Token[i-1]==')' or Token[i-1]=="else":
                i=i+1
                str=""
                while Token[i]!='}':
					str=str+Token[i]
					i=i+1 
                if i<x:
                    a="{c}"
                    a=d1.get(a)
                else:
                    error=1
                    print("parsing error")
                    break
            else:
                error=1
                print("parsing error")
       
        else:
            a=d1.get(Token[i])

        #print(a)
        top=list1[len(list1)-1]
        #print(top)
        if a==top:
            matched.append(a)
            list1.pop()
            i=i+1
        
        elif top in nonterm:
            list1.pop()
            str1=table.get(top)
            y=(len(str1)-1)
            while(y>=0):
                list1.append(str1[y])
                y=y-1
        elif isTerminal(a,list1):
        	print(a)
        	print("Parsing Error")   # If yes, then it is an error

        	error=1
        	break
        else:
        	print("parsing error")
        	break
    if error!=1:
       print("semantics is correct")

with open('input2.txt') as fp:
	s=fp.read().strip().split(' ')
#print(s)
Token=[]
divide_into_tokens(s,Token)
print(Token)
parser(Token)
