import npyscreen
from src.forms.main import MainForm

class MyApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", MainForm())