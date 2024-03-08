import re

class Tokenizer:
    def break_down():
        pass

class FaTokenizer(Tokenizer):
    def break_down(content):
        # remove multiple spaces
        content=re.sub(' +', ' ', content)