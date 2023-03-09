#!/usr/bin/python3

# Creati o clasa de nume “FamiliaMea”, iar obiectele asociate acesteia corespund membrilor familiei voastre. Clasa va contine variabilele “nume”, “prenume”, “vara”, o lista de pasiuni, denumire “pasiuni” si o functie denumita “motto”, care afiseaza motto-ul familiei voastre.
# Creati un constructor fara parametrii care initializeaza variabilele cu date default
# Creati un constructor cu parametrii care initializeaza variabilele cu cele setate crearea instantei (obiectului)
# Creati metode de tipul “Get” si “Set” pentru modificarea apelarea/modificarea campurilor din clase
# Afisati variabilele pe ecran folosind “Getters” si modificati valorile campurilor prin apelarea “Setters

class FamiliaMea:

    def afisare_motto(self):
        """Functie pentru afisarea motto-ului familiei."""
        return "Acest text este motto-ul familiei."

    # def __init__(self):
    #   """Constructor pt initializare cu valori implicite"""
    #     self.nume = "n/a"
    #     self.prenume = "n/a"
    #     self.varsta = 0
    #     self.pasiuni = []
    #     self.motto = "n/a"

    def __init__(self, nume, prenume, varsta, pasiuni : list, motto):
        """Constructor pt initializare cu valori date ca parametru"""
        self.nume = nume
        self.prenume = prenume
        self.varsta = varsta
        self.pasiuni = pasiuni
        self.motto = self.afisare_motto()

    def getNume(self):
        return self.nume
    def getPrenume(self):
        return self.prenume
    def getVarsta(self):
        return self.varsta
    def getPasiuni(self):
        return self.pasiuni
    def getMotto(self):
        return self.motto
    def info(self):
        """Metoda pentru afisarea tuturor informatiilor stocate despre o persoana"""
        print("\nAfisarea tuturor informatiilor despre persoana:")
        print("Nume: " +self.nume , "\nPrenume: " +self.prenume, "\nVarsta: " + str(self.varsta), "\nPasiuni: " + str(self.pasiuni), "\nMotto-ul familiei: " + self.motto)

    def setNume(self, nume):
        self.nume = nume
    def setPrenume(self, prenume):
        self.prenume = prenume
    def setData(self, nume, prenume, varsta, pasiuni):
        """Metoda pentru modificarea tuturor informatiilor stocate despre o persoana"""
        self.nume = nume
        self.prenume = prenume
        self.varsta = varsta
        self.pasiuni = pasiuni

# p1 = FamiliaMea()
# print(p1.__dict__)
p2 = FamiliaMea('Jack', 'George', 28, ["s","b","c"], "")
print(p2.getNume())
print(p2.getPrenume())
print(p2.getVarsta())
print(p2.getPasiuni())
print(p2.getMotto())
p2.info()
print(FamiliaMea.afisare_motto(""))
p2.setPrenume("Gigi")
p2.info()
p2.setNume("Popescu")
p2.info()
p2.setData("Ion","Gigel",40,['t','x','b'])
p2.info()