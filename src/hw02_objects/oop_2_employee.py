"""
Exercise 2: (4 points)

a) Write the complete code for the Employee class
    (including constructor, __str__,...) (2 points)

b) Create a few employee objects and show how you can
    manipulate them using the methods. (1 points)

c) Draw a UML class diagram for your Employee class. (1 point)
"""

class Employee:
    
    """ Diese Klasse enthält Attribute wie Name, Geburtzdatung, Geschlecht und Methoden
    wie __init__, change_name, set_addresse, set_famillienstand, set_gehalt, raise_gehalt und  __str__.
    Mit der Methode change_name  wird der Name geändert und mit 
    Methode set_addresse wird die Adresse geändert. 
    Die Methode set_famillienstand setzt den Famillienstand und bestimmt die Steuerklasse (vereinfacht: 1 vs. 3) 
    Mit set_gehalt wird das Gehalt gesetzt. 
    Mit raise_gehalt wird das Gehalt um eine Prozentzahl erhöht.
    Alle Informationen werden bei Aufruf als string zurückgegben
    """
    # constructor
    def __init__ (self, nam, geb, ges):
        # werden Name, Geburtzdatung, Geschlecht gesetzt.
        self.Name = nam
        self.Geburtzdatung = geb
        self.Geschlecht = ges
    # Methods
    def change_name(self, nam):
        # Mit der Methode change_name  wird der Name geändert
        self.Name = nam
    def set_addresse(self, add):
        # mit Methode set_addresse wird die Adresse geändert. 
        self.Addresse = add
    def set_familienstand(self, fam):
        # Die Methode set_famillienstand setzt den Famillienstand und bestimmt die Steuerklasse (vereinfacht: 1 vs. 3) 
        self.Fam = fam
        if(self.Fam == "ledig"):
            self.Steuer = "Klassen 1"
        elif (self.Fam == "verheiratet"):
            self.Steuer = "Klassen 3"
        else:
            raise ValueError
    def set_gehalt(self, geh, pos):
        # Mit set_gehalt wird das Gehalt gesetzt. 
        self.Gehalt = geh
        self.Position = pos
    def raise_gehalt(self, pozent):
        # Mit raise_gehalt wird das Gehalt um eine Prozentzahl erhöht.
        self.Gehalt = self.Gehalt + self.Gehalt * pozent/100
    def __str__ (self):
        # Alle Informationen werden bei Aufruf als string zurückgegben
        res = "*** Employee Information ***\n"
        res += "Name: " + str(self.Name) + "\n"
        res += "Geschlecht: " + str(self.Geschlecht) + "\n"
        res += "Address: " + str(self.Addresse) + "\n"
        res += "Geburtzdatung: " + str(self.Geburtzdatung) + "\n"
        res += "Familienstand: " + str(self.Fam) + "\n"
        res += "Steuerklassen: " + str(self.Steuer) + "\n"
        res += "Gehalt: " + str(self.Gehalt) + "\n"
        res += "Position: " + str(self.Position) + "\n"
        return res

if __name__ == "__main__":
    print("Employee application" )
    
    empAnne = Employee("Anne", "01.06.1997", "Frau")
    empAnne.change_name("Hanna")
    empAnne.set_addresse("Werner-Heisenberg-Allee 25, 80939 München")
    empAnne.set_familienstand("ledig")
    empAnne.set_gehalt(5000, "Tutor")
    empAnne.raise_gehalt(3)
    print(empAnne)
    
    
    
