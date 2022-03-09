### Import der Bibliothek os und Festlegen des Zieldateipfads als globale Variable
import os
dateipfad = os.path.abspath('Todo.txt')





def Say_Hello():
    ###### Begrüßungstext
    
    print("----------------------------------------------------------------------------\n"
          "                                     TODO-Liste\n"
          "----------------------------------------------------------------------------\n")

    print("Wilkommen in deiner Todo-list was möchtest tu tun?")


def Main_loop():
    
    
    #####Hauptschleife
    
    userinput = ""
    todo = []

    while userinput != "B":
        item_on_list = 0
        items = len(todo)
        userinput = input("Einträge [A]nzeigen [H]inzufügen [B]eenden [L]öschen, [S]peichern: ")
        if userinput == "A":
            Show_list(todo, items, item_on_list)
        elif userinput == "H":
            todo = Hinzufuegen_Funktion(todo)
        elif userinput == "S":
            #TODO: Hier muss die Funktion zum Speichern aufgerufen werden
        elif userinput == "L":
            Show_list(todo, items, item_on_list)
            todo = Entfernen(todo)
        elif userinput == "B":
            Goodbye()
        else:
            Error()


def Show_list(todo, items, item_on_list):
    
    #### Funktion, um die Liste anzuzeigen
    
    print(f"du hast {items} auf deiner liste:")
    while items > item_on_list:
        element = todo[item_on_list]
        print(f"{item_on_list + 1}. {element}")
        item_on_list = item_on_list + 1

def Hinzufuegen_Funktion(todo):
    
    #### Funktion zum Hinzufügen
    
    hinzufuegen = input("Was möchtest du hinzufügen? ")
    todo.append(hinzufuegen)
    return todo

def Entfernen(todo):
    
    #### Funktion zum Entfernen
    
    delete = int(input("Was möchtest du entfernen? "))
    delete = delete - 1
    todo.pop(delete)
    return todo

def Goodbye():
    
    #### Abschiedstext
    
    print("tschüss")

def Save(###TODO:Welche Variablen müssen übegeben werden?):
   #TODO: An dieser Stelle muss die Funktion zum Speichern eingebaut werden

def Error():
    
    #### Ausnahmebehandlung/Error Exception
    
    print("Eingabe nicht erkannt")

if __name__ == '__main__':
    #### Notwendige Hauptmethode zum Aufrufen aller Unterfunktionen
    Say_Hello()
    Main_loop()
