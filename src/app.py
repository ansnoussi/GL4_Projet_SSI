import npyscreen
from src.forms.main import MainForm

from src.forms.codage import CodageForm
from src.forms.decodage import DecodageForm
from src.forms.hachage import HachageForm
from src.forms.craquage import CraquageForm
from src.forms.chiffsym import ChiffSymForm
from src.forms.dechiffsym import DechiffSymForm
from src.forms.chiffasym import ChiffAsymForm
from src.forms.dechiffasym import DechiffAsymForm

class MyApp(npyscreen.NPSAppManaged):
    def onStart(self):
        # When Application starts, set up the Forms that will be used.
        # These two forms are persistent between each edit.
        self.addForm("MAIN",       MainForm, name="OUTIL SSI_INSAT POUR LA CRYPTOGRAPHIE", color="IMPORTANT",)
        # This one will be re-created each time it is edited.
        self.addFormClass("CODAGE", CodageForm, name="Codage", color="WARNING")
        self.addFormClass("DECODAGE", DecodageForm, name="Deodage", color="WARNING")
        self.addFormClass("HACHAGE", HachageForm, name="Hachage", color="WARNING")
        self.addFormClass("CRAQUAGE", CraquageForm, name="Craquage", color="WARNING")
        self.addFormClass("CHIFF_SYM", ChiffSymForm, name="Chiffrement Symetrique", color="WARNING")
        self.addFormClass("DECHIFF_SYM", DechiffSymForm, name="Dechiffrement Synetrique", color="WARNING")
        self.addFormClass("CHIFF_ASYM", ChiffAsymForm, name="Chiffrement Asymetrique", color="WARNING")
        self.addFormClass("DECHIFF_ASYM", CodageForm, name="Dechiffrement Asynetrique", color="WARNING")
        
    def onCleanExit(self):
        npyscreen.notify_wait("Au revoir!")
    
    def change_form(self, name):
        # Switch forms.  NB. Do *not* call the .edit() method directly (which 
        # would lead to a memory leak and ultimately a recursion error).
        # Instead, use the method .switchForm to change forms.
        self.switchForm(name)
        
        # By default the application keeps track of every form visited.
        # There's no harm in this, but we don't need it so:        
        self.resetHistory()