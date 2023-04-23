## How to start?

Die folgenden Konsolenbefehle sind ausgehend aus dem Projektverzeichnis.

Das WebQuiz verwendet die Ports 8000 (Web-Server) und 8123 (Quiz-Server)

#### Game-Server starten:

`python main.py`

#### Web-Server starten:

`cd www`<br>
`python -m http.server 8000`


#### Quiz im Browser aufrufen:

url: `http://localhost:8000/`

Das Admin-Panel muss offen sein, damit die Runden des Quiz gesteuert werden können.<br>
Das Quiz selbst wird aufgerufen, indem ein Username eingegeben wird und dann "connect" gedrückt wird.