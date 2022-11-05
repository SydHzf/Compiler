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

    def validateIndentifierForKeyword(self, i):
        if re.findall(RE_KEYWORDS_DT,self.words[i]):
            curClassPart = "DT"
            
        elif re.findall(RE_KEYWORDS_CO,self.words[i]):
            curClassPart = "Co"

        elif re.findall(RE_KEYWORDS_WO_CONDITIONS,self.words[i]):
            curClassPart = "WoConditons"

        elif re.findall(RE_KEYWORDS_CONDITIONS,self.words[i]):
            curClassPart = "Conditions"

        elif re.findall(RE_KEYWORDS_CS,self.words[i]):
            curClassPart = "Cs"

        elif re.findall(RE_KEYWORDS_OPERATORS,self.words[i]):
            curClassPart = "Operators"
    
        elif re.findall(RE_LOR,self.words[i]):
            curClassPart = "Lor"

        elif re.findall(RE_LAND,self.words[i]):
            curClassPart = "Land"
            
        elif re.findall(RE_LNOT,self.words[i]):
            curClassPart = "Lnot"

        elif re.findall(RE_KEYWORDS_AM,self.words[i]):
            curClassPart = "Am"
            
        else:
            curClassPart = self.words[i]

        # This will recognize an integer and create an INTEGER token for it
        return curClassPart
    
    
    def tokensIterator(self, tokens):
        for token in tokens:
            print(f"LineNo: '{token.lineNumber}', ClassPart: '{token.classPart}', ValuePart: '{token.valuePart}' \n")


    def tokenizer(self):
        tokensList = []
        curLine = 1
        i = 0
        while i<len(self.words):
            token = Token()
            curClassPart = ''

            if(self.words[i] == '\n'):
                curLine += 1

            elif re.match(RE_INTEGER,self.words[i]):
                curClassPart = "INTEGER"

            elif re.match(RE_FLOAT,self.words[i]):
                curClassPart = "FLOAT"

            # imaginary            
            elif re.match(RE_IMAGINARY,self.words[i]):
                curClassPart = "IMAGINARY"

            elif re.match(RE_OPERATORS,self.words[i]):
                if re.match(RE_INTEGER,self.words[i]+self.words[i+1]):
                    curClassPart = "INTEGER"
                    token.valuePart += self.words[i]
                    i += 1
                elif re.match(RE_FLOAT,self.words[i]+self.words[i+1]):
                    curClassPart = "FLOAT"
                    token.valuePart += self.words[i]
                    i += 1
                elif re.match(RE_IMAGINARY,self.words[i]+self.words[i+1]):
                    curClassPart = "IMAGINARY"
                    token.valuePart += self.words[i]
                    i += 1
                else:
                    curClassPart = "OPERATORS"

                # identifier 
            elif re.match(RE_IDENTIFIER,self.words[i]):
                if re.match(RE_ALL_KEYWORDS,self.words[i]):
                    res = self.validateIndentifierForKeyword(i)
                    curClassPart = res
                else:
                    curClassPart = "IDENTIFIER"

            elif re.search(RE_PAREN,self.words[i]):
                curClassPart = "Paren"

            # This will recognize an string and create an STRING token for it
            elif re.match(RE_STRING,self.words[i]):
                curClassPart = "STRING"

            else:
                curClassPart = "Invalid"

            token.classPart = curClassPart
            token.valuePart += self.words[i]
            token.lineNumber = curLine
            tokensList.append(token) if(curClassPart) else None

            i+=1

        return tokensList
