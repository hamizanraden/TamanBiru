class Chat:
    def __init__(self, sender, message, replies=None):
        self.sender = sender
        self.message = message
        self.replies = replies if replies else []

    def add_reply(self, sender, reply):
        self.replies.append(Chat(sender, reply))

    def display_pesan(self, spasi=0):
        print(' ' * spasi + f"[{self.sender}]: {self.message}")
        for reply in self.replies:
            reply.display_pesan(spasi + 4)