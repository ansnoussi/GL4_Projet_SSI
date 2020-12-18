import npyscreen


class CodageForm(npyscreen.FormWithMenus):
    def create(self):
        self.add(npyscreen.FixedText,value= "CODAGE" )
        self.how_exited_handers[npyscreen.wgwidget.EXITED_ESCAPE]  = self.exit_application    
        
        # The menus are created here.
        self.mMain = self.add_menu(name="Menu")

        self.mMain.addItemsFromList([
            ("Retour", self.retour),
        ])  

    def exit_application(self):
        pass

    def retour(self, *args, **keywords):
        self.parentApp.change_form("MAIN")