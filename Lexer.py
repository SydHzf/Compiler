import re

class Lexer(object):
    def __init__(self, source_code):
        self.source_code = source_code

    def tokenized(self):
        #print('test')
        # where all the tokens created by lexer will be stored

        lexem = ""
        words = []
        i = 0
        code = self.source_code # Our text file in string datatype
        while i<len(code): 
           
            if code[i] in ["(",")","[","]","{","}","-","+","^","%","/","*"]:
                words.append(lexem)
                lexem = ""
                words.append(code[i])
                
            elif code[i] in ['"']:
                lexem +=code[i]
                i+=1
                
                while code[i] != '"':
                    lexem  += code[i]
                    i+=1
                lexem += code[i]
                words.append(lexem)
                lexem = ""
            
            elif code[i] in ["~"]:# skipping the comment line
                while code[i] != "\n": i+=1
            
            elif code[i] in [" ","\n",";",","]:
                words.append(lexem)
                lexem = ""
            
            else:
                lexem += code[i]
            i+=1
            
        words = [i for i in words if i]

        
        
        Re_Keywords_Dt = "str|int|flt|img|bool|null|Vect|Dict|Set"
        Re_Keywords_Conditions = "if|orif|until"
        Re_Keywords_Class = "class"
        Re_Keywords_Lor = "\|"
        Re_Keywords_Lnot = "!"
        Re_Keywords_Land = "&"
        Re_Keywords_Co = "Gt|Lt|Eq|Neq|Gte|Lte"
        Re_Keywords_WoConditions = "else|try|atlast"
        Re_Keywords_Am = "priv|pub|prot"
        Re_Keywords_Cs = "this"
        # Re_Keywords_MDM = "*|/|%"
        Re_Keywords_Operators = "Incas|Decas|Inc|Dec"
        Re_Keywords_For = "for"
        Re_Keywords_Catch = "catch"
        Re_Keywords_Is = "Is"
        # Re_Keywords_SA = "-|+"
        # Re_Keywords_For = "for"
        # Re_Keywords_Expo = "^"
        Re_Keywords_Paren = r'\(|\)|\[|\]|\{|\}'

        tokens =  {k:[] for k in ['Dt', 'Conditions', 'Class','Lor', 'Land', 'Lnot'
                            ,'Co', 'WoConditions', 'Am','Cs', 'Operators', 'For','Catch','Is',
                            'INTEGER','FLOAT','IMAGINARY','OPERATORS','STRING','Paren','IDENTIFIER']}
        i = 0
        while i<len(words):
            if re.findall(Re_Keywords_Dt,words[i]):  
                tokens['Dt'].append(words[i])
                i += 1

            elif re.findall(Re_Keywords_Conditions,words[i]):
                tokens['Conditions'].append(words[i])
                
                # tokens.append(['Re_Keywords_Dt',words[i]])
                i += 1

            elif re.findall(Re_Keywords_Class,words[i]):
                tokens['Class'].append(words[i])

                # tokens.append(['Re_Keywords_Class',words[i]])
                i += 1

            elif re.findall(Re_Keywords_Lor,words[i]):
                tokens['Lor'].append(words[i])

                # tokens.append(['Re_Keywords_Lor',words[i]])
                i += 1

            elif re.findall(Re_Keywords_Land,words[i]):
                tokens['Land'].append(words[i])

                # tokens.append(['Re_Keywords_Land',words[i]])
                i += 1
                
            elif re.findall(Re_Keywords_Lnot,words[i]):
                tokens['Lnot'].append(words[i])

                # tokens.append(['Re_Keywords_Lnot',words[i]])
                i += 1
                
            elif re.findall(Re_Keywords_Co,words[i]):
                tokens['Co'].append(words[i])

                # tokens.append(['Re_Keywords_Co',words[i]])
                i += 1
        
            elif re.findall(Re_Keywords_WoConditions,words[i]):
                tokens['WoConditons'].append(words[i])

                # tokens.append(['Re_Keywords_WoCondition',words[i]])
                i += 1

            elif re.findall(Re_Keywords_Am,words[i]):
                tokens['Am'].append(words[i])

                # tokens.append(['Re_Keywords_Am',words[i]])
                i += 1

            elif re.findall(Re_Keywords_Cs,words[i]):
                tokens['Cs'].append(words[i])

                # tokens.append(['Re_Keywords_Cs',words[i]])
                i += 1
                
            # elif re.findall(Re_Keywords_MDM,words[i]):
            #     tokens.append(['Re_Keywords_MDM',words[i]])
            #     i += 1

            elif re.findall(Re_Keywords_Operators,words[i]):
                tokens['Operators'].append(words[i])

                # tokens.append(['Re_Keywords_Operators',words[i]])
                i += 1

            elif re.findall(Re_Keywords_For,words[i]):
                tokens['For'].append(words[i])

                # tokens.append(['Re_Keywords_For',words[i]])
                i += 1

            elif re.findall(Re_Keywords_Catch,words[i]):
                tokens['Catch'].append(words[i])

                # tokens.append(['Re_Keywords_Catch',words[i]])
                i += 1
                
            elif re.findall(Re_Keywords_Is,words[i]):
                tokens['Is'].append(words[i])

                # tokens.append(['Re_Keywords_Is',words[i]])
                i += 1
            
            # elif re.findall(Re_Keywords_SA,words[i]):
            #     tokens.append(['Re_Keywords_SA',words[i]])
            #     i += 1

            # elif re.findall(Re_Keywords_Expo,words[i]):
            #     tokens.append(['Re_Keywords_Expo',words[i]])
            #     i += 1
                
            # elif re.findall(Re_Keywords_Paren,words[i]):
            #     tokens.append(['Re_Keywords_Paren',words[i]])
            #     i += 1

            # This will recognize a word and create and identifier token for it
            # elif re.match('[a-zA-Z|_]',words[i]):
                
            #     tokens.append(['IDENTIFIER', words[i]])
            #     i+=1

             # This will recognize an integer and create an INTEGER token for it
            elif re.match('^[-+]?[0-9]+$',words[i]):
                tokens['INTEGER'].append(words[i])

                # tokens.append(['INTEGER',words[i]])
                i+=1

            elif re.match('^[-+]?\d*\.\d+$',words[i]):
                tokens['FLOAT'].append(words[i])

                # tokens.append(['INTEGER',words[i]])
                i+=1

            # imaginary            
            elif re.match('^\d*\+?\d*(.\d)?im$',words[i]):
                tokens['IMAGINARY'].append(words[i])

                # tokens.append(['INTEGER',words[i]])
                i+=1

            elif re.match('\-|\+|\^|\%|\/|\*',words[i]):
                tokens['OPERATORS'].append(words[i])

                # tokens.append(['OPERATORS',words[i]])
                i+=1

                # identifier 
            elif re.match('^[a-zA-Z|_]\w*$',words[i]):
                tokens['IDENTIFIER'].append(words[i])
                
                # tokens.append(['IDENTIFIER', words[i]])
                i+=1


            elif re.search(Re_Keywords_Paren,words[i]):
                tokens['Paren'].append(words[i])

                # tokens.append(['Re_Keywords_Paren',words[i]])
                i += 1

            # This will recognize an string and create an STRING token for it
            elif re.match(r'^".+"$',words[i]):
                tokens['STRING'].append(words[i])

                # tokens.append(['STRING',words[i]])
                i+=1


            
        print(words)
        print("\n____________________________" +  "   Tokenized   " + "____________________________\n")
        print(tokens)
        #return tokens
1.