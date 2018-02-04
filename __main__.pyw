while True:
    try:
        import os
        import clipboard
        import time
        break
        
    except:
        if(os.name == "nt"):
            os.system("pip install clipboard")
        else:
            os.system("pip3 install clipboard")

class Elabora():
    def setAffiliate(self, stringa):
        self.affiliate = stringa

    def setText(self, ext):
        self.ext = ext

    def copiaClipboard(self):
        self.link = clipboard.paste()

    def incollaClipboard(self):
        clipboard.copy(self.link)
        #print("Eseguito: " + self.link)

    def identificaLink(self):
        for ext in self.ext:
            if(ext[1] == True):
                if(self.link.startswith("https://www.amazon." + ext[0]) or self.link.startswith("www.amazon." + ext[0])):
                    if(not "&tag=" in self.link):
                        return True
        
        return False

    def elaboraLink(self):
        self.link += self.affiliate

    def start(self):
        while True:
            self.copiaClipboard()
            if(self.identificaLink()):
                self.elaboraLink()
                self.incollaClipboard()
            time.sleep(5)

if(__name__ == "__main__"):
    stringa = "&tag=acuf59280d-21"

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

    A = Elabora()
    A.setAffiliate(stringa)
    A.setText(ext)
    A.start()