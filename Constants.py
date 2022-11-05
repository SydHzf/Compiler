# from enum import Enum
 
# class TokenNames(Enum):
#     Dt = 'Dt'
#     Conditions = 'Conditions'
#     Class'Class','Lor', 'Land', 'Lnot'
#                             ,'Co', 'WoConditions', 'Am','Cs', 'Operators', 'For','Catch','Is',
#                             'INTEGER','FLOAT','IMAGINARY','OPERATORS','STRING','Paren','IDENTIFIER','OTHERS'
#     AUTUMN = 3
#     WINTER = 4


# Regular Expressions

#KEYWORDS
RE_KEYWORDS_DT = "^str$|^int$|^flt$|^img$|^bool$|^null$|^Vect$|^Dict$|^Set$"
RE_KEYWORDS_AM = "^priv$|^pub$|^prot$"
RE_KEYWORDS_CS = "^this$"
RE_KEYWORDS_CONDITIONS = "^if$|^orif$|^until$"
RE_KEYWORDS_FOR = "^for$"
RE_KEYWORDS_IS = "^Is$"
RE_KEYWORDS_CATCH = "^catch$"
RE_KEYWORDS_OPERATORS = "^Incas$|^Decas$|^Inc$|^Dec$"
RE_KEYWORDS_WO_CONDITIONS = "^else$|^try$|^atlast$"
RE_KEYWORDS_CO = "^Gt$|^Lt$|^Eq$|^Neq$|^Gte$|^Lte$"
RE_KEYWORDS_CLASS = "^class$"

RE_ALL_KEYWORDS = RE_KEYWORDS_DT \
    +'|'+RE_KEYWORDS_AM+'|'+RE_KEYWORDS_CS \
    +'|'+RE_KEYWORDS_CONDITIONS \
    +'|'+RE_KEYWORDS_WO_CONDITIONS+'|'+RE_KEYWORDS_FOR+'|'+RE_KEYWORDS_IS \
    +'|'+RE_KEYWORDS_CATCH \
    +'|'+RE_KEYWORDS_OPERATORS \
    +'|'+RE_KEYWORDS_CO \
    +'|'+RE_KEYWORDS_CLASS \

RE_LOR = "^\|$"
RE_LNOT = "^!$"
RE_LAND = "^&$"
# RE_MDM = "^*|/|%$"
# RE_SA = "^-|+$"
# RE_FOR = "^for$"
# RE_EXPO = "^^$"
RE_PAREN = r'\(|\)|\[|\]|\{|\}'

#CONSTANT
RE_INTEGER = '^[-+]?[0-9]+$'
RE_FLOAT = '^[-+]?\d*\.\d+$'
RE_IMAGINARY = '^\d*\+?\d*(.\d)?im$'
RE_OPERATORS = '\-|\+|\^|\%|\/|\*'
RE_IDENTIFIER = '^[a-zA-Z|_]\w*$'
# RE_IDENTIFIER = '^[a-zA-Z|_][a-zA-Z0-9|_]*$'
RE_STRING = r'^".*"$'
