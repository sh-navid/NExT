class ChatBot:
    pass

class ChatInterface:
    pass

class DesktopChatInterface(ChatInterface):
    @staticmethod
    def on(callback):
        while True:
            callback(input("?"))
        
