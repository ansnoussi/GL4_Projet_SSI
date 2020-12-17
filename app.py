#!/usr/bin/env python
# encoding: utf-8

import npyscreen, curses

class MyApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", MainForm())

class MainForm(npyscreen.FormWithMenus):
    def create(self):
        self.add(npyscreen.TitleText, name = "Text:", value= "this is : PentCrate." )
        self.how_exited_handers[npyscreen.wgwidget.EXITED_ESCAPE]  = self.exit_application    
        
        # The menus are created here.
        self.mMain = self.add_menu(name="Menu", shortcut="m")
        
        self.mCodage = self.mMain.addNewSubmenu("Codage", "c")
        self.mCodage.addItemsFromList([
            ("Coder un message",   self.whenJustBeep),
            ("Decoder un message",   self.whenJustBeep),
        ])

        self.mMain.addItemsFromList([
            ("Hachage", self.whenJustBeep, "h"),
        ])  

        self.mMain.addItemsFromList([
            ("Craquage", self.whenJustBeep, "k"),
        ])  

        self.mChSym = self.mMain.addNewSubmenu("Chiffrement Symetrique", "s")
        self.mChSym.addItemsFromList([
            ("Saisir un message à chiffrer",   self.whenJustBeep),
            ("Saisir un message chiffré",   self.whenJustBeep),
        ])

        self.mChAsym = self.mMain.addNewSubmenu("Chiffrement Asymetrique", "a")
        self.mChAsym.addItemsFromList([
            ("Saisir un message à chiffrer",   self.whenJustBeep),
            ("Saisir un message chiffré",   self.whenJustBeep),
        ])

        self.mMain.addItemsFromList([
            ("Exit Application", self.exit_application, "e"),
        ])  

    def whenJustBeep(self):
        curses.beep()

    def exit_application(self):
        curses.beep()
        self.parentApp.setNextForm(None)
        self.editing = False
        self.parentApp.switchFormNow()

def main():
    TA = MyApp()
    TA.run()


if __name__ == '__main__':
    main()

