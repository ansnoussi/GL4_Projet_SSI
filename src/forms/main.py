import npyscreen, curses


class MainForm(npyscreen.FormWithMenus):
    def create(self):
        self.add(npyscreen.FixedText,value= "OUTIL SSI_INSAT POUR LA CRYPTOGRAPHIE" )
        self.how_exited_handers[npyscreen.wgwidget.EXITED_ESCAPE]  = self.exit_application    
        
        # The menus are created here.
        self.mMain = self.add_menu(name="Menu")
        
        self.mCodage = self.mMain.addNewSubmenu("Codage")
        self.mCodage.addItemsFromList([
            ("Coder un message",   self.whenJustBeep),
            ("Decoder un message",   self.whenJustBeep),
        ])

        self.mMain.addItemsFromList([
            ("Hachage", self.whenJustBeep),
        ])  

        self.mMain.addItemsFromList([
            ("Craquage", self.whenJustBeep),
        ])  

        self.mChSym = self.mMain.addNewSubmenu("Chiffrement Symetrique")
        self.mChSym.addItemsFromList([
            ("Saisir un message à chiffrer",   self.whenJustBeep),
            ("Saisir un message chiffré",   self.whenJustBeep),
        ])

        self.mChAsym = self.mMain.addNewSubmenu("Chiffrement Asymetrique")
        self.mChAsym.addItemsFromList([
            ("Saisir un message à chiffrer",   self.whenJustBeep),
            ("Saisir un message chiffré",   self.whenJustBeep),
        ])

        self.mMain.addItemsFromList([
            ("Exit Application", self.exit_application),
        ])  

    def whenJustBeep(self):
        curses.beep()

    def exit_application(self):
        curses.beep()
        self.parentApp.setNextForm(None)
        self.editing = False
        self.parentApp.switchFormNow()