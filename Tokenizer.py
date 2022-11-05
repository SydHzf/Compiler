from Constants import *
import re


class Token:
    def __init__(self):
        self.classPart = ''
        self.valuePart = ''
        self.lineNumber = None

class Tokenizer:
    def __init__(self,words):
        self.words = words

    def validateIndentifierForKeyword(self, tokens, i):

        if re.findall(RE_KEYWORDS_DT,self.words[i]):
            curClassPart = "DT"
            tokens['Dt'].append(self.words[i])
            
        elif re.findall(RE_KEYWORDS_CO,self.words[i]):
            curClassPart = "Co"
            tokens['Co'].append(self.words[i])

        elif re.findall(RE_KEYWORDS_WO_CONDITIONS,self.words[i]):
            curClassPart = "WoConditons"
            tokens['WoConditons'].append(self.words[i])

        elif re.findall(RE_KEYWORDS_CONDITIONS,self.words[i]):
            curClassPart = "Conditions"
            tokens['Conditions'].append(self.words[i])
        

        elif re.findall(RE_KEYWORDS_CS,self.words[i]):
            curClassPart = "Cs"
            tokens['Cs'].append(self.words[i])

            # tokens.append(['Re_Keywords_Cs',self.words[i]])
            
            
        # elif re.findall(Re_Keywords_MDM,self.words[i]):
        #     tokens.append(['Re_Keywords_MDM',self.words[i]])
        #     i += 1

        elif re.findall(RE_KEYWORDS_OPERATORS,self.words[i]):
            curClassPart = "Operators"
            tokens['Operators'].append(self.words[i])

            # tokens.append(['Re_Keywords_Operators',self.words[i]])
        
            
    
        elif re.findall(RE_LOR,self.words[i]):
            curClassPart = "Lor"
            tokens['Lor'].append(self.words[i])


            # tokens.append(['Re_Keywords_Lor',self.words[i]])
            

        elif re.findall(RE_LAND,self.words[i]):
            curClassPart = "Land"
            tokens['Land'].append(self.words[i])

            # tokens.append(['Re_Keywords_Land',self.words[i]])
            
            
        elif re.findall(RE_LNOT,self.words[i]):
            curClassPart = "Lnot"
            tokens['Lnot'].append(self.words[i])

        elif re.findall(RE_KEYWORDS_AM,self.words[i]):
            curClassPart = "Am"
            tokens['Am'].append(self.words[i])

            # tokens.append(['Re_Keywords_Am',self.words[i]])
            
        else:
            curClassPart = self.words[i]
            tokens[self.words[i]]
        
        # elif re.findall(Re_Keywords_SA,self.words[i]):
        #     tokens.append(['Re_Keywords_SA',self.words[i]])
        #     i += 1

        # elif re.findall(Re_Keywords_Expo,self.words[i]):
        #     tokens.append(['Re_Keywords_Expo',self.words[i]])
        #     i += 1
            
        # elif re.findall(Re_Keywords_Paren,self.words[i]):
        #     tokens.append(['Re_Keywords_Paren',self.words[i]])
        #     i += 1

        # This will recognize a word and create and identifier token for it
        # elif re.match('[a-zA-Z|_]',self.words[i]):
            
        #     tokens.append(['IDENTIFIER', self.words[i]])
        #     i+=1

        # This will recognize an integer and create an INTEGER token for it
        return curClassPart,tokens
    
    
    def tokensIterator(self, tokens):
        for token in tokens:
            print(f"LineNo: '{token.lineNumber}', ClassPart: '{token.classPart}', ValuePart: '{token.valuePart}' \n")


    def tokenizer(self):
        # Re_Keywords_Dt = "str|int|flt|img|bool|null|Vect|Dict|Set"
        # Re_Keywords_Conditions = "if|orif|until"
        # Re_Keywords_Class = "class"
        # Re_Keywords_Lor = "\|"
        # Re_Keywords_Lnot = "!"
        # Re_Keywords_Land = "&"
        # Re_Keywords_Co = "Gt|Lt|Eq|Neq|Gte|Lte"
        # Re_Keywords_WoConditions = "else|try|atlast"
        # Re_Keywords_Am = "priv|pub|prot"
        # Re_Keywords_Cs = "this"
        # # Re_Keywords_MDM = "*|/|%"
        # Re_Keywords_Operators = "Incas|Decas|Inc|Dec"
        # Re_Keywords_For = "for"
        # Re_Keywords_Catch = "catch"
        # Re_Keywords_Is = "Is"
        # # Re_Keywords_SA = "-|+"
        # # Re_Keywords_For = "for"
        # # Re_Keywords_Expo = "^"
        # Re_Keywords_Paren = r'\(|\)|\[|\]|\{|\}'

        tokens =  {k:[] for k in ['Dt', 'Conditions', 'Class','Lor', 'Land', 'Lnot'
                            ,'Co', 'WoConditions', 'Am','Cs', 'Operators', 'For','Catch','Is',
                            'INTEGER','FLOAT','IMAGINARY','OPERATORS','STRING','Paren','IDENTIFIER','OTHERS']}

        tokensList = []
        curLine = 1
        i = 0
        while i<len(self.words):
            token = Token()
            curClassPart = ''

            if(self.words[i] == '\n'):
                curLine += 1

            # elif re.findall(RE_KEYWORDS_DT,self.words[i]):
            #     pass

            elif re.match(RE_INTEGER,self.words[i]):
                curClassPart = "INTEGER"
                tokens['INTEGER'].append(self.words[i])

                # tokens.append(['INTEGER',self.words[i]])
                # i+=1

            elif re.match(RE_FLOAT,self.words[i]):
                curClassPart = "FLOAT"
                tokens['FLOAT'].append(self.words[i])

                # tokens.append(['INTEGER',self.words[i]])
                # i+=1

            # imaginary            
            elif re.match(RE_IMAGINARY,self.words[i]):
                curClassPart = "IMAGINARY"
                tokens['IMAGINARY'].append(self.words[i])

                # tokens.append(['INTEGER',self.words[i]])
                # i+=1

            elif re.match(RE_OPERATORS,self.words[i]):
                # curClassPart = "OPERATORS"
                # tokens['OPERATORS'].append(self.words[i])
                if re.match(RE_INTEGER,self.words[i]+self.words[i+1]):
                    curClassPart = "INTEGER"
                    tokens['INTEGER'].append(self.words[i]+self.words[i+1])
                    token.valuePart += self.words[i]
                    i += 1
                elif re.match(RE_FLOAT,self.words[i]+self.words[i+1]):
                    curClassPart = "FLOAT"
                    tokens['FLOAT'].append(self.words[i]+self.words[i+1])
                    token.valuePart += self.words[i]
                    i += 1
                elif re.match(RE_IMAGINARY,self.words[i]+self.words[i+1]):
                    curClassPart = "IMAGINARY"
                    tokens['IMAGINARY'].append(self.words[i]+self.words[i+1])
                    token.valuePart += self.words[i]
                    i += 1
                else:
                    curClassPart = "OPERATORS"
                    tokens['OPERATORS'].append(self.words[i])

                # tokens.append(['OPERATORS',self.words[i]])
                # i+=1

                # identifier 
            elif re.match(RE_IDENTIFIER,self.words[i]):
                # curClassPart = "IDENTIFIER"
                # tokens['IDENTIFIER'].append(self.words[i])
                if re.match(RE_ALL_KEYWORDS,self.words[i]):
                    res = self.validateIndentifierForKeyword(tokens, i)
                    curClassPart = res[0]
                    tokens = res[1]
                else:
                    curClassPart = "IDENTIFIER"
                    tokens['IDENTIFIER'].append(self.words[i])
                
                # tokens.append(['IDENTIFIER', self.words[i]])
                # i+=1


            elif re.search(RE_PAREN,self.words[i]):
                curClassPart = "Paren"
                tokens['Paren'].append(self.words[i])

                # tokens.append(['Re_Keywords_Paren',self.words[i]])
                # i += 1

            # This will recognize an string and create an STRING token for it
            elif re.match(RE_STRING,self.words[i]):
                curClassPart = "STRING"
                tokens['STRING'].append(self.words[i])

                # tokens.append(['STRING',self.words[i]])
            else:
                curClassPart = "Invalid"
                tokens['Invalid'].append(self.words[i])

            token.classPart = curClassPart
            token.valuePart += self.words[i]
            token.lineNumber = curLine
            tokensList.append(token) if(curClassPart) else None

            i+=1

        return tokensList
