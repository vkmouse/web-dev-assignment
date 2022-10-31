class Member:
    def __init__(self, id: int, name: str, username: str, password: str):
        self.id = id
        self.name = name
        self.username = username
        self.password = password

class Message:
    def __init__(self, __name: str, __content: str):
        self.__name = __name
        self.__content = __content

    @property
    def name(self):
        return self.__name

    @property
    def content(self):
        return self.__content
