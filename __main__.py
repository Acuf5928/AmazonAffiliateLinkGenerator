Cont = True

while(Cont == True):
    try:
        import os
        import clipboard
        import time
        Cont = False
    except:
        os.system("pip install clipboard")

class elabora():
    def setaffiliate(self, stringa):
        self.affiliate = stringa

    def copiaclipboard(self):
        self.link = clipboard.paste()

    def incollaclipboard(self):
        clipboard.copy(self.link)
        #print("Eseguito: " + self.link)

    def identificalink(self):
        if(self.link.startswith("https://www.amazon.it") or self.link.startswith("www.amazon.it")):
            if(not "&tag=" in self.link):
                return True
        else:
            return False

    def elaboralink(self):
        self.link += self.affiliate

    def start(self):
        while True:
            self.copiaclipboard()
            if(self.identificalink()):
                self.elaboralink()
                self.incollaclipboard()
            time.sleep(5)

if(__name__ == "__main__"):
    stringa = "&tag=acuf5928-21" 

    A = elabora()
    A.setaffiliate(stringa)
    A.start()