class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
    
    def __EOF(self,index): # End Of File
        return index == len(self.source_code)
            
    def word_splitter(self):
        
        #print('test')
        # where all the tokens created by lexer will be stored

        lexem = ""
        words = []
        i = 0
        code = self.source_code # Our text file in string datatype
        curLine = 1
        while i<len(code):           
            # saare wo jo akely apna mtlb rkhty hain
            if code[i] in ["|","!","&","(",")","[","]","{","}","-","+","^","%","/","*",","]: # Separators + (mathematical + logical)operators
                words.append(lexem)
                lexem = ""
                words.append(code[i])
            # String ka scene
            elif code[i] in ['"']:
                words.append(lexem)
                lexem = ""
                lexem +=code[i]
                i+=1
                
                try:
                    while code[i] != '"':
                        if code[i] == '\\' and code[i+1] == '"':
                            lexem  += code[i+1]
                            i+=2
                        else:
                            lexem  += code[i]
                            i+=1
                except:
                    errMsg= f"String Error on line {curLine}."
                    raise Exception(errMsg)
                
                lexem += code[i]
                words.append(lexem)
                lexem = ""
            
            # Single line cmnt ka scene
            elif code[i] in ["~"]:
                words.append(lexem)
                lexem = ""
                while True:
                    if self.__EOF(i):
                        break
                    elif code[i] == "\n" :
                        words.append(code[i])
                        break
                    else:
                        i+=1
                curLine += 1
            #multi line ka scene
            elif code[i] in ['`']: # skipping the comment mul-line
                words.append(lexem)
                lexem = ""
                i+=1
                tempLineCounts = 0
                try:
                    # while (code[i] != '`':
                    while True:
                        if(code[i] == '\\'):
                            if(code[i+1] == '`'):
                                i+=2
                        elif(code[i] == '`'):
                            break
                        
                        if(code[i]=='\n'):
                            words.append(code[i])
                            tempLineCounts += 1
                        i+=1
                except:
                    errMsg = f"Comment Error on line {curLine}."
                    raise Exception(errMsg)
                curLine += tempLineCounts
            # jin pr cheezyn break ho rhi hain
            elif code[i] in [" ",";"]:
                words.append(lexem)
                lexem = ""
            # jb line khtm horhi hai
            elif(code[i]=='\n'):
                    curLine += 1
                    words.append(lexem)
                    lexem = ""
                    words.append(code[i])
                    
            # "." wala scene 
            elif code[i] == ".":
                
                if code[i-1].isdigit() or code[i+1].isdigit():
                    lexem+=code[i]
                else:
                    words.append(lexem)
                    lexem = ''
                    words.append(code[i])
                    
            else:
                lexem += code[i]
            i+=1

        #Agr lexem mai kuch howa aur breaker nhi aya koi   
        words.append(lexem) if lexem else None
        words = [i for i in words if i]

        return words
        
        
                
