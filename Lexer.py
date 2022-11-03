class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
    
    def __EOF(self,index):
        return index == len(self.source_code)
            
    def word_splitter(self) -> list:
        
        #print('test')
        # where all the tokens created by lexer will be stored

        lexem = ""
        words = []
        i = 0
        code = self.source_code # Our text file in string datatype
        curLine = 1
        while i<len(code):           

            if code[i] in ["|","!","&","(",")","[","]","{","}","-","+","^","%","/","*",","]: # Separators + (mathematical + logical)operators
                words.append(lexem)
                lexem = ""
                words.append(code[i])
                
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
            
            elif code[i] in ["~"]:# skipping the comment sigle-line
                words.append(lexem)
                lexem = ""
                while not self.__EOF(i) or code[i] != "\n" : i+=1
                curLine += 1
            elif code[i] in ['`']: # skipping the comment mul-line
                words.append(lexem)
                lexem = ""
                i+=1
                tempLineCounts = 0
                try:
                    while code[i] != '`':
                        if(code[i]=='\n'):
                            tempLineCounts += 1
                        i+=1
                except:
                    errMsg = f"Comment Error on line {curLine}."
                    raise Exception(errMsg)
                curLine += tempLineCounts
            
            elif code[i] in [" ",";"]:
                words.append(lexem)
                lexem = ""

            elif(code[i]=='\n'):
                    curLine += 1
                    words.append(lexem)
                    lexem = ""
                    words.append(code[i])

            else:
                lexem += code[i]
            i+=1
        words.append(lexem) if lexem else None
        words = [i for i in words if i]

        return words
        
        
                