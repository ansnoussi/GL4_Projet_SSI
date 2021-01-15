import npyscreen
from src.helpers.ChiffAsym import ChiffAsymHelper

class DechiffAsymForm(npyscreen.FormWithMenus, npyscreen.ActionFormMinimal):
    def create(self):


        self.add(npyscreen.FixedText,value= "OPTIONS:" )
        self.how_exited_handers[npyscreen.wgwidget.EXITED_ESCAPE]  = self.exit_application    
        
        self.Options = npyscreen.OptionList()
        # just for convenience so we don't have to keep writing Options.options
        options = self.Options.options
        
        options.append(npyscreen.OptionMultiFreeText('Votre Message', value=''))
        options.append(npyscreen.OptionSingleChoice('Type de chiffrement', choices=ChiffAsymHelper.getAvailable()))

        self.add(npyscreen.OptionListDisplay, name="Option List", 
                values = options, 
                scroll_exit=True,
                max_height=2)
        self.keyFile = self.add(npyscreen.TitleFilenameCombo,name="Choisir votre clef prive", label=True)
        self.pwd = self.add(npyscreen.TitlePassword, name = "Mot de passe (pour clef prive)")
        self.mode = self.add(npyscreen.TitleSelectOne, max_height=4, value = [1,], name="Pick Mode",values = ["Decrypt","Verify-Sign"], scroll_exit=True)
        

        self.output = self.add(npyscreen.BoxTitle, name="Output:", max_height=6)
        self.output.values = []


        # The menus are created here.
        self.mMain = self.add_menu(name="Menu")
        self.mMain.addItemsFromList([
            ("Retour", self.retour),
        ])  

    def exit_application(self):
        pass

    def retour(self, *args, **keywords):
        self.parentApp.change_form("MAIN")

    def afterEditing(self):
        pass
    def on_ok(self):
        self.output.values = [ChiffAsymHelper.encrypt(
            self.Options.get("Type de chiffrement").value[0], 
            self.mode.value[0] , 
            self.Options.get("Votre Message").value, 
            self.keyFile.value,
            self.pwd.value)]