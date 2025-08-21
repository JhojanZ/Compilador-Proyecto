from lexer import Lexer, tokenize

if __name__ == "__main__":
    text = """
    if (x <= 10) {
        print ("hello");
        x++;
    }
    """

    tokenize(text)