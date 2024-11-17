
class Chat:
    def __init__(self, pengirim, pesan, balasan=None):
        self.sender = pengirim
        self.message = pesan
        self.replies = balasan if balasan else []

    def add_reply(self, pengirim, pesan):
        self.replies.append(Chat(pengirim, pesan))

    def display_pesan(self, indent=0):
        print(" " * indent + f"[{self.sender}]: {self.message}")
        for reply in self.replies:
            reply.display_pesan(indent + 4)

