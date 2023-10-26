class GeneralList:
    def __init__(self):
        self.__list = []
    def clear(self):
        self.__list = []
    def getItems(self):
        return [i for i in self.__list]
    def appendItem(self, value):
        self.__list.append(value)
    def removeItem(self, value):
        self.__list.remove(value)
    def getStr(self):
        pass

