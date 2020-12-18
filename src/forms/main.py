import npyscreen, curses


class MainForm(npyscreen.FormWithMenus):
    def create(self):
        self.add(npyscreen.FixedText,value= "OUTIL SSI_INSAT POUR LA CRYPTOGRAPHIE" )
        self.how_exited_handers[npyscreen.wgwidget.EXITED_ESCAPE]  = self.exit_application    
        
        # The menus are created here.
        self.mMain = self.add_menu(name="Menu")
        
        self.mCodage = self.mMain.addNewSubmenu("Codage")
        self.mCodage.addItemsFromList([
            ("Coder un message",   self.goToCodage),
            ("Decoder un message",   self.goToDecodage),
        ])

        self.mMain.addItemsFromList([
            ("Hachage", self.goToHachage),
        ])  

        self.mMain.addItemsFromList([
            ("Craquage", self.goToCraquage),
        ])  

        self.mChSym = self.mMain.addNewSubmenu("Chiffrement Symetrique")
        self.mChSym.addItemsFromList([
            ("Saisir un message à chiffrer",   self.goToChiffSym),
            ("Saisir un message chiffré",   self.goToDechiffSym),
        ])

        self.mChAsym = self.mMain.addNewSubmenu("Chiffrement Asymetrique")
        self.mChAsym.addItemsFromList([
            ("Saisir un message à chiffrer",   self.goToChiffAsym),
            ("Saisir un message chiffré",   self.goToDechiffAsym),
        ])

        self.mMain.addItemsFromList([
            ("Quitter", self.exit_application),
        ])  

    def whenJustBeep(self):
        curses.beep()

    def exit_application(self):
        curses.beep()
        self.parentApp.setNextForm(None)
        self.editing = False
        self.parentApp.switchFormNow()

    def goToCodage(self, *args, **keywords):
        self.parentApp.change_form("CODAGE")
    def goToDecodage(self, *args, **keywords):
        self.parentApp.change_form("DECODAGE")
    def goToHachage(self, *args, **keywords):
        self.parentApp.change_form("HACHAGE")
    def goToCraquage(self, *args, **keywords):
        self.parentApp.change_form("CRAQUAGE")
    def goToChiffSym(self, *args, **keywords):
        self.parentApp.change_form("CHIFF_SYM")
    def goToDechiffSym(self, *args, **keywords):
        self.parentApp.change_form("DECHIFF_SYM")
    def goToChiffAsym(self, *args, **keywords):
        self.parentApp.change_form("CHIFF_ASYM")
    def goToDechiffAsym(self, *args, **keywords):
        self.parentApp.change_form("DECHIFF_ASYM")