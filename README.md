# Projekt 4.0: Unterfunktionen und Refactoring

Diese Übung basiert auf der Übung https://github.com/Oberschule-an-der-Egge/python-04. Es wird empfohlen letztere Übung zunächst (inklusive der Bonusaufgabe) abzuschließen, bevor die hier vorliegende Übung angegangen wird.




## Problemstellung: Übersichtlichkeit im Quellcode

Eine Mögliche Lösung von https://github.com/Oberschule-an-der-Egge/python-04 könnte lauten:


```python
print("----------------------------------------------------------------------------\n"
      "                                     TODO-Liste\n"
      "----------------------------------------------------------------------------\n")

print("Wilkommen in deiner Todo-list was möchtest tu tun?")


userinput = ""
todo = []

while userinput != "B":
    item_on_list = 0
    items = len(todo)
    userinput = input("Einträge [A]nzeigen [H]inzufügen [B]eenden [L]öschen? ")
    if userinput == "A":
        print(f"du hast {items} auf deiner liste:")
        while items > item_on_list:
            element = todo[item_on_list]
            print(f"{item_on_list + 1}. {element}")
            item_on_list = item_on_list + 1
    elif userinput == "H":
        hinzufuegen = input("Was möchtest du hinzufügen? ")
        todo.append(hinzufuegen)
    elif userinput == "L":
        print(f"du hast {items} auf deiner liste:")
        while items > item_on_list:
            element = todo[item_on_list]
            print(f"{item_on_list + 1}. {element}")
            item_on_list = item_on_list + 1
        delete = int(input("Was möchtest du entfernen? "))
        delete = delete - 1
        todo.pop(delete)
    elif userinput == "B":
        print("tschüss")
    else:
        print("Eingabe nicht erkannt")


```

**Was fällt Ihnen auf, wenn Sie ie Kommandos unter elif `userinput == "A"` und `elif userinput == "L"` vergleichen?


## Unterfunktionen

Um Quellcode übersichtlicher zu gestalten, ist es sinnvoll Codeblöcke zu unterteilen, je nachdem welche Funktion mit den jeweiligen Kommandos ausgeführt werden soll. Hierdurch wird der Quellcode übersichtlicher und Redundanzen können vermieden werden.


```python

def Say_Hello():
    print("----------------------------------------------------------------------------\n"
          "                                     TODO-Liste\n"
          "----------------------------------------------------------------------------\n")
    
    print("Wilkommen in deiner Todo-list was möchtest tu tun?")


def Main_loop():
    userinput = ""
    todo = []
    
    while userinput != "B":
        item_on_list = 0
        items = len(todo)
        userinput = Get_Input()
        if userinput == "A":
            Show_List(todo, items)
        elif userinput == "H":
            hinzufuegen = input("Was möchtest du hinzufügen? ")
            todo.append(hinzufuegen)
        elif userinput == "L":
            Show_List(todo, items)
            delete = int(input("Was möchtest du entfernen? "))
            delete = delete - 1
            todo.pop(delete)
        elif userinput == "B":
            print("tschüss")
        else:
            print("Eingabe nicht erkannt")
            
def Show_List(todo, items):
    print(f"du hast {items} auf deiner liste:")
    while items > item_on_list:
        element = todo[item_on_list]
        print(f"{item_on_list + 1}. {element}")
        item_on_list = item_on_list + 1

def Get_Input():
    x = input("Einträge [A]nzeigen [H]inzufügen [B]eenden [L]öschen? ")
    return x   

if __name__ == '__main__':
    Say_Hello()
    Main_loop()

```

*** #TODO: Return erklären, Argumente Erklären, Weiterführende Aufgabe stellen
