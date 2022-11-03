import re
class Token:
    def __init__(self) -> None:
        cp = ''
        vp = ''
        ln = None

class Tokenizer:
    def __init__(self,words):
        self.words = words

    def tokenizer(self):
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
                            'INTEGER','FLOAT','IMAGINARY','OPERATORS','STRING','Paren','IDENTIFIER','OTHERS']}
        i = 0
        while i<len(self.words):
            token = Token()
            if re.findall(Re_Keywords_Dt,self.words[i]):  
                tokens['Dt'].append(self.words[i])
                # i += 1

            elif re.findall(Re_Keywords_Conditions,self.words[i]):
                tokens['Conditions'].append(self.words[i])
                
                # tokens.append(['Re_Keywords_Dt',self.words[i]])
                # i += 1

            elif re.findall(Re_Keywords_Class,self.words[i]):
                tokens['Class'].append(self.words[i])

                # tokens.append(['Re_Keywords_Class',self.words[i]])
                # i += 1

            elif re.findall(Re_Keywords_Lor,self.words[i]):
                tokens['Lor'].append(self.words[i])

                # tokens.append(['Re_Keywords_Lor',self.words[i]])
                # i += 1

            elif re.findall(Re_Keywords_Land,self.words[i]):
                tokens['Land'].append(self.words[i])

                # tokens.append(['Re_Keywords_Land',self.words[i]])
                # i += 1
                
            elif re.findall(Re_Keywords_Lnot,self.words[i]):
                tokens['Lnot'].append(self.words[i])

                # tokens.append(['Re_Keywords_Lnot',self.words[i]])
                # i += 1
                
            elif re.findall(Re_Keywords_Co,self.words[i]):
                tokens['Co'].append(self.words[i])

                # tokens.append(['Re_Keywords_Co',self.words[i]])
                # i += 1
        
            elif re.findall(Re_Keywords_WoConditions,self.words[i]):
                tokens['WoConditons'].append(self.words[i])

                # tokens.append(['Re_Keywords_WoCondition',self.words[i]])
                # i += 1

            elif re.findall(Re_Keywords_Am,self.words[i]):
                tokens['Am'].append(self.words[i])

                # tokens.append(['Re_Keywords_Am',self.words[i]])
                # i += 1

            elif re.findall(Re_Keywords_Cs,self.words[i]):
                tokens['Cs'].append(self.words[i])

                # tokens.append(['Re_Keywords_Cs',self.words[i]])
                # i += 1
                
            # elif re.findall(Re_Keywords_MDM,self.words[i]):
            #     tokens.append(['Re_Keywords_MDM',self.words[i]])
            #     i += 1

            elif re.findall(Re_Keywords_Operators,self.words[i]):
                tokens['Operators'].append(self.words[i])

                # tokens.append(['Re_Keywords_Operators',self.words[i]])
                # i += 1

            elif re.findall(Re_Keywords_For,self.words[i]):
                tokens['For'].append(self.words[i])

                # tokens.append(['Re_Keywords_For',self.words[i]])
                # i += 1

            elif re.findall(Re_Keywords_Catch,self.words[i]):
                tokens['Catch'].append(self.words[i])

                # tokens.append(['Re_Keywords_Catch',self.words[i]])
                # i += 1
                
            elif re.findall(Re_Keywords_Is,self.words[i]):
                tokens['Is'].append(self.words[i])

                # tokens.append(['Re_Keywords_Is',self.words[i]])
                # i += 1
            
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
            elif re.match('^[-+]?[0-9]+$',self.words[i]):
                tokens['INTEGER'].append(self.words[i])

                # tokens.append(['INTEGER',self.words[i]])
                # i+=1

            elif re.match('^[-+]?\d*\.\d+$',self.words[i]):
                tokens['FLOAT'].append(self.words[i])

                # tokens.append(['INTEGER',self.words[i]])
                # i+=1

            # imaginary            
            elif re.match('^\d*\+?\d*(.\d)?im$',self.words[i]):
                tokens['IMAGINARY'].append(self.words[i])

                # tokens.append(['INTEGER',self.words[i]])
                # i+=1

            elif re.match('\-|\+|\^|\%|\/|\*',self.words[i]):
                tokens['OPERATORS'].append(self.words[i])

                # tokens.append(['OPERATORS',self.words[i]])
                # i+=1

                # identifier 
            elif re.match('^[a-zA-Z|_]\w*$',self.words[i]):
                tokens['IDENTIFIER'].append(self.words[i])
                
                # tokens.append(['IDENTIFIER', self.words[i]])
                # i+=1


            elif re.search(Re_Keywords_Paren,self.words[i]):
                tokens['Paren'].append(self.words[i])

                # tokens.append(['Re_Keywords_Paren',self.words[i]])
                # i += 1

            # This will recognize an string and create an STRING token for it
            elif re.match(r'^".+"$',self.words[i]):
                tokens['STRING'].append(self.words[i])

                # tokens.append(['STRING',self.words[i]])
            else:
                tokens['OTHERS'].append(self.words[i])
                
            i+=1


            
        
        
        return tokens
