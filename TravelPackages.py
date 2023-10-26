from ClientList import ClientList
from RouteList import RouteList
class Packages: # Ïóò¸âêà
    def __init__(self, date='', quantity=0, discount=0):
        self.__clientList = ClientList()
        self.__routeList = RouteList()
        self.setDate(date)
        self.setQuantity(quantity)
        self.setDiscount(discount)

    def setDate(self, value):
        self.__date = value
    def setQuantity(self, value):
        self.__quantity = int(value)
    def setDiscount(self, value):
        self.__discount = int(value)
    def getRoute(self):
        return self.__routeList
    def getClient(self):
        return self.__clientList
    def getDate(self):
        return self.__date
    def getQuantity(self):
        return self.__quantity
    def getDiscount(self):
        return self.__discount

    def appendClient(self, value):
        self.__clientList.appendItem(value)
    def removeClient(self, value):
        self.__clientList.removeItem(value)
    def appendRoute(self, value):
        self.__routeList.appendItem(value)
    def removeRoute(self, value):
        self.__routeList.removeItem(value)

    def getPackageInf(self):
        s = 'Information about travel package:\n'
        s += f'Clients => {self.__clientList.getStr()}\n'
        s += f'Route => {self.__routeList.getStr()}\n'
        s += f'Data => {self.__date}\n'
        s += f'Discount => {self.__discount}\n'
        return s

