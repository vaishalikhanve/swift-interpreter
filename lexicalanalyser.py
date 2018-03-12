#code of the function to divide the given program to tokens

                
                

def divide_into_tokens(string,tokens):
    keywords=["associatedtype","class","deinit","enum","extension","fileprivate","func","import","init","inout","internal","let","open","operator","private","protocol","public","static","struct","subscript","typealias","var","break","case","continue","default","defer","do","else","fallthrough","for","guard","if","in","repeat","return","switch","where"," while","as","Any","catch","false","is","nil","rethrows","super","self","Self","throw","throws","true","try","_","#available","#colorLiteral","#column","#else","#elseif","#endif","#file","#fileLiteral","#function","#if","#imageLiteral","#line","#selector"," #sourceLocation","associativity","convenience","dynamic","didSet","final","get","infix","indirect","lazy","left","mutating","none","nonmutating","optional","override","postfix","precedence","prefix","Protocol","required","right","set","Type","unowned","weak","willSet"]
    operators=["+","-","/","%","<",">","*",".","!",":","&","(",")","{","}","[","]","-","?","#","=",'"',"'"]
    op=["(",")","{","}","[","]","'",'"']
    separators=[",",";"]
    comments=["#"]
    
    keywords_list=[]
    operators_list=[]
    separators_list=[]

    for i in string:
        if i in comments:
            break
        elif i in keywords:
            tokens.append(i)
            keywords_list.append(i)
            print(i,"->keyword")
        elif i in operators:
            tokens.append(i)
            operators_list.append(i)
            print(i,"->operator")
        elif i in separators:
            tokens.append(i)
            separators_list.append(i)
            print(i,"->separator")
        else:
            num=len(i)
            swift=i
            j=0
            while j<num:
                variable=''
                if swift[j].isdigit() or swift[j].isalpha() or swift[j]=="_" or swift[j]=='"' or swift[j]=="'":
                    while swift[j].isdigit() or swift[j].isalpha() or swift[j]=="_" or swift[j]=='"' or swift[j]=="'":
                        variable+=swift[j]
                        j+=1
                        if j==num:
                            break
                    if variable in keywords:
                        tokens.append(variable)
                        keywords_list.append(variable)
                        print(variable,"->keyword")
                        continue
                    else:
                        tokens.append(variable)
                        keywords_list.append(variable)
                        print(variable,"->identifier")
                        continue
                elif swift[j] in separators:
                    tokens.append(swift[j])
                    separators_list.append(swift[j])
                    print(swift[j],"->separator")
                    j+=1
                    continue
                elif swift[j] in operators:
                    operator=''
                    if swift[j] in op:
                        tokens.append(swift[j])
                        operators_list.append(swift[j])
                        print(swift[j],"->operator")
                        j+=1
                        continue
                    while swift[j] in operators:
                        operator+=swift[j]
                        j+=1
                        if j==num:
                            break
                    tokens.append(operator)
                    operators_list.append(operator)
                    print(operator,"->operator")
                    continue
                else:
                    #break
                    j+=1
                    continue
    #print(tokens)
    #print(keywords_list)
    #print(operators_list)
    #print(separators_list)
   # return tokens
#code for reading the input from the given file(I gave the same program as input)


