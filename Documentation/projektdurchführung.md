## Projektdurchführung

Mein Projekt "WebQuiz" besteht aus drei Komponenten: Website, Server und Datenbank.

Da ich meinen Fokus bei diesem Projekt auf die Kommunikation über Websockets legen wollte, begann ich zunächst damit: Eine kleine Demo-Website und ein Demo-Server, welche erste Nachrichten über Websockets übertragen konnte. Browser besitzen dafür eingebaute Websockets, während ich für Python das Package "Websockets" installieren musste.

Nachdem ich die Websocket-Verbindung aufgebaut hatte, begann ich mit der Datenbankanbindung. Die Datenbank wird die Fragen beinhalten, die das Quiz beinhaltet.
Zunächst hatte ich mich dazu entschieden, eine MSSQL Express Datenbank zu verwenden, da ich bereits Erfahrungen mit MSSQL sammeln konnte. Die Verbidung zu der Datenbank kann über Python durch das Package "pyodb" realsisiert werden, welches von Microsoft empfohlen wurde.

Ich habe mich jedoch dazu entschieden, auf eine SQLite-Datenbank umzusteigen, da eine SQLite-Datenbank portable ist und so keine Datenbank-Engine installiert werden muss, um diese anzusprechen. Das erleichtert die Projekt-Abgabe.
Durch Anwendung des Single Responsibility Principles war die Umstellung sehr einfach. MssqlDriver.py wurde einfach durch SqliteDriver.py ersetzt.

Anschließend erweiterte ich meine Demo-Website und meinen Demo-Server um Funktionalität. Der Python-Server konnte über eine Routing-Struktur leicht um Endpunkte (...Handler.py) erweitert werden. Die Website muss die UI-Elemente steuern, Nachrichten versenden und empfangene Nachrichten routen.

Hier kommt nun ein wichtiger Faktor ins Spiel: Zeit. Denn der Tag der Abgabe rückt näher. Jedoch stand erst das Grundgerüst. Ich legte meinen Fokus auf den Python Server, weil Python im Zentum unseres Unterrichts steht. Bei der Website folgte ich dagegen dem Ansatz "einfach so, dass es funktioniert".

Dann stieß ich auf ein Problem: die zeitliche Steuerung der Runden, dass zum Beispiel die Runde nach 1 Minute automatisch beendet wird, hatte zur Folge, dass manche Websockets keine Nachrichten mehr entgegennehmen. Ich prüfte meine asynchronen Abläufe, konnte das Problem jedoch nicht identifizieren. Gewartet wurde über asyncio.sleep(), der ausführende Thread wurde also nicht blockiert.
Es musste ein Workaround her: das Admin-Panel. Eine Webpage, welche sich um die Steuerung des Quizzes kümmert. Hier wurde die Rundensteuerung implementiert.

Insgesamt konnte ein Quiz realisiert werden. Es gibt jedoch stellen, die verbessert werden könnten:

Die Website:
- Aufteilung der Funktionsweise auf mehrere Klassen,
- Aufbau einer Routing-Struktur statt des einfachen switch/case
- Styling der Landing-Page und des Admin-Panels

Die Datenbank: 
- Spalten der Tabelle “Questions” in kleinere, verknüpfte Tabellen.

Der Python-Server:
- Anpassen des Message-Objekts, sodass Message.value kein String sein muss.
