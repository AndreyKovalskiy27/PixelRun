class BaseNotifier:
    messages_list: dict

    def draw(self, screen):
        for message in self.messages_list.values():
            message.draw(screen)

    def show(self, message_to_show):
        for message, message_object in self.messages_list.items():
            if message != message_to_show:
                message_object.hide()

            elif message == message_to_show:
                message_object.show()
