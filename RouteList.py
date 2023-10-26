from GeneralList import GeneralList
class RouteList(GeneralList): 
    def getStr(self):
        s = ''
        for i in self.getItems():
            s += i.getRouteInf() #+ ' ||| '
        return s

