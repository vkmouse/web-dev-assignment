class Member:
    def __init__(self, id: int, name: str, username: str, password: str):
        self.__id = id
        self.__name = name
        self.__username = username
        self.__password = password
    
    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

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
