import Lexer
#import my_parser

def main():
    # Read the current flow source code test.lang and store it in variable
    content = ""
    with open('t.lang','r') as file:
        content = file.read()

    print("\n____________________________" +  "   Input   " + "____________________________\n")
    print(content)
    
    print("\n____________________________" +  "   Output   " + "____________________________\n")
    #
    #Lexer
    #

    # we call the lexer class and initailize the it with the source code
    lex = Lexer.Lexer(content)
    tokens = lex.tokenized()
    return tokens

main()