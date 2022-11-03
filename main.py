from Lexer import Lexer
from Tokenizer  import Tokenizer
#import my_parser

def main():
    # Read the current flow source code test.lang and store it in variable
    content = ""
    with open('testing.txt','r') as file:
        content = file.read()

    print("\n____________________________" +  "   Input   " + "____________________________\n")
    print(content)
  
    print("\n             ______________" +  "   LEXICAL ANALYZER   " + "_______________\n")
    
    print("\n____________________________" +  "   Word_Splitter   " + "____________________________\n")
    wor = Lexer(content)
    words = wor.word_splitter()
    print(words)

    print("\n____________________________" +  "   Tokenized   " + "____________________________\n")
    tok = Tokenizer(words)
    tokens = tok.tokenizer()
    print(tokens)

main()