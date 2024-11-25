
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
    
    def save_to_file (self, chat_database): # menyimpan chat & reply ke dalam file
                     with open('./app/cli/data/chat_database.txt', 'a') as file:
                           file.write(f"{self.sender} : {self.message}\n")
                           for reply in self.replies:
                                 reply.save_to_file(chat_database)
    


def load_from_file(): # mengambil data dari file
    chats = []
    with open ('app/cli/data/chat_database.txt', 'r') as file:
        lines = file.readlines()
        current_chat = None
        for line in lines:
            if line:
                if line.startswith("[") and line.endswith("]"):
                    if current_chat:
                        chats.append(current_chat)
                    sender_message = line [1:-2].split("]: ")
                    current_chat = Chat(sender_message[0], sender_message[1])
                else:
                    if current_chat:
                        current_chat.add_reply("ReplySender", line)
        if current_chat:
            chats.append(current_chat)
    return chats