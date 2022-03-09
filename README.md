# Projekt 4.1: Persistente Todo-Liste

Diese Übung basiert auf der Übung https://github.com/Oberschule-an-der-Egge/python-04. Es wird empfohlen letztere Übung zunächst (inklusive der Bonusaufgabe) abzuschließen, bevor die hier vorliegende Übung angegangen wird.




## Problemstellung: Unterschieldiche Betriebssysteme



**Dateien bearbeiten**

Betriebssysteme (Windows, MacOS, Linux) benutzen unterschiedliche Pfadangaben. Mit der Standard-Bibliothek `os` können diese Pfade unabhängig vom Betriebssystem erstellt werden.

```python
import os
    
dateipfad = os.path.abspath('Neue_Textdatei.txt')
# -> /home/tim/desktop/Neue_Textdatei.txt (Linux) oder 
# -> C:\Users\Tim\Desktop\Neue_Textdatei.txt (Windows)
```


## Dateien mit Inhalt erstellen



Um Dateien zu schreiben nehmen wir `open()` und den Kontextmanager `with .. as ..:`

```python
with open(dateipfad, "w") as datei_out:
    datei_out.write("Beliebiger String")
    
    # text -> ['Zeile eins\n', 'Zeile zwei\n', ...]
```

Beachten Sie, dass die Methode `open` zwei Argumente fordert: Zum einen den Dateipfad als string; zum anderen das Argument `"w"`.


## Probieren Sie es aus!

Versuchen Sie zunächst eine Textdatei mit beliebiegen Inhalt zu erstellen. Welchen Unterschied macht es, wenn Sie bei `open` statt des Arguments `"w"` das Argument `a` verwenden?


## Wenden Sie das erlernte an!

Versuchen Sie nun die in https://github.com/Oberschule-an-der-Egge/python-04 erstellte ToDo-Liste wie folgt zu erweitern:

![image](Todo_Liste_Persistenz.png)

Nach dem beenden des Beispielprogramms sollte eine Textdatei entstanden sein, die wie folgenden Inhalt hat.:

![image](Todo-Datei.png)

**Achtung:** `datei_out.write` fordert als Argument einen String. Sollten Sie eine Liste Speichen wollen, müssen Sie diese erst umwandeln.


## Bonusaufgabe: Praktischer Anwendungsfall

Will man die gespeicherte Datei praktisch verwenden, indem man etwa die ToDo-Liste druckt, ist es sinnvoll die Listeneinträge einzeln untereinander in der Ausgabedatei zu speichern. Dies gelingt am einfachsten mittels einer Schleife.

**Aufgabe** -> Wandeln Sie Ihren Quellcode so ab, dass ihre `Todo.txt` nicht dies:

`['Milch', 'Eier', 'Käse']`

sondern dies enthält:

```
Milch
Eier
Käse
```

