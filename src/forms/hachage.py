import npyscreen
from src.helpers.hachage import HachageHelper

class HachageForm(npyscreen.FormWithMenus, npyscreen.ActionFormMinimal):
    def create(self):


        self.add(npyscreen.FixedText,value= "OPTIONS:" )
        self.how_exited_handers[npyscreen.wgwidget.EXITED_ESCAPE]  = self.exit_application    
        
        self.Options = npyscreen.OptionList()
        # just for convenience so we don't have to keep writing Options.options
        options = self.Options.options
        
        options.append(npyscreen.OptionMultiFreeText('Votre Message', value=''))
        options.append(npyscreen.OptionSingleChoice('Fonction de hachage', choices=HachageHelper.getAvailable()))


        self.add(npyscreen.OptionListDisplay, name="Option List", 
                values = options, 
                scroll_exit=True,
                max_height=6)

        self.output = self.add(npyscreen.BoxTitle, name="Output:", max_height=4)
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
        self.output.values = [HachageHelper.hash(self.Options.get("Fonction de hachage").value[0], self.Options.get("Votre Message").value)]