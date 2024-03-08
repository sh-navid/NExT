from engines.tokenizer import FaTokenizer
from engines.chatbot import ChatBot,DesktopChatInterface


if __name__ == "__main__":
    def listen(data):
        print(data)

    DesktopChatInterface.on(listen)