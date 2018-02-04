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

    def setext(self, ext):
        self.ext = ext

    def copiaclipboard(self):
        self.link = clipboard.paste()

    def incollaclipboard(self):
        clipboard.copy(self.link)
        #print("Eseguito: " + self.link)

    def identificalink(self):
        for ext in self.ext:
            if(ext[1] == True):
                if(self.link.startswith("https://www.amazon." + ext[0]) or self.link.startswith("www.amazon." + ext[0])):
                    if(not "&tag=" in self.link):
                        return True
        
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

    ext = [("it", True), 
            ("ca", False), 
            ("es", False), 
            ("co.jp", False), 
            ("co.uk", False), 
            ("in", False), 
            ("com", False), 
            ("de", False), 
            ("fr", False), 
            ("cn", False),] 

    A = elabora()
    A.setaffiliate(stringa)
    A.setext(ext)
    A.start()