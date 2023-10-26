from GeneralList import GeneralList
class ClientList(GeneralList):
    def getStr(self):
        s = ''
        for i in self.getItems():
            s += i.getClientInf() #+ ' ||| '
        return s


     