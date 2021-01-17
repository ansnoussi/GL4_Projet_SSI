import npyscreen
from src.helpers.ChiffSym import ChiffSymHelper

class ChiffSymForm(npyscreen.FormWithMenus, npyscreen.ActionFormMinimal):
    def create(self):


        self.add(npyscreen.FixedText,value= "OPTIONS:" )
        self.how_exited_handers[npyscreen.wgwidget.EXITED_ESCAPE]  = self.exit_application    
        
        self.Options = npyscreen.OptionList()
        # just for convenience so we don't have to keep writing Options.options
        options = self.Options.options
        
        options.append(npyscreen.OptionMultiFreeText('Votre Message', value=''))
        options.append(npyscreen.OptionSingleChoice('Type de chiffrement', choices=ChiffSymHelper.getAvailable()))
        # options.append(npyscreen.TitlePassword('Votre Mot de passe', value=''))        


        self.add(npyscreen.OptionListDisplay, name="Liste d'options", 
                values = options, 
                scroll_exit=True,
                max_height=2)
        self.pwd = self.add(npyscreen.TitlePassword, name = "Mot de passe:")
        

        self.output = self.add(npyscreen.BoxTitle, name="Sortie de texte:", max_height=4)
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
        self.output.values = [ChiffSymHelper.encrypt(self.Options.get("Type de chiffrement").value[0], self.Options.get("Votre Message").value, self.pwd.value)]