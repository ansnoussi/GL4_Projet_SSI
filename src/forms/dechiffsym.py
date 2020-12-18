import npyscreen


class DechiffSymForm(npyscreen.FormWithMenus):
    def create(self):
        self.add(npyscreen.FixedText,value= "DECHIFFREMENT SYMETRIQUE" )
        self.how_exited_handers[npyscreen.wgwidget.EXITED_ESCAPE]  = self.exit_application    
        
        # The menus are created here.
        self.mMain = self.add_menu(name="Menu")

        self.mMain.addItemsFromList([
            ("Retour", self.retour),
        ])  

    def exit_application(self):
        curses.beep()
        self.parentApp.setNextForm(None)
        self.editing = False
        self.parentApp.switchFormNow()

    def retour(self, *args, **keywords):
        self.parentApp.change_form("MAIN")