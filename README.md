# Hilfe zur Installation
Eine Schritt für Schritt Anleitung für die Installation von Python und aller benötigter Pakete. Wir gehen hier von einer Windows10-Installation und dem Nutzen der Powershell aus.

## Python
1. Lade dir `Python 3.7.7` herunter, damit wurde gecodet und getestet (aber eigentlich müsste auch `3.8.3` funktionieren).
2. Führe das heruntergeladene Installationsprogramm aus. Wähle beim Durchgehen des Installers die Punkte **pip** und  **Add Python 3.7 to PATH (Python 3.7 zu PATH hinzufügen)** aus. Das Installationsprogramm installiert Python in deinen Benutzerordner und fügt seine ausführbaren Verzeichnisse deinem Benutzerpfad hinzu.
3. Da die `PATH` Variable aktualisiert wurde, können wir in der Kommandozeile nun die Befehle `pip` und `python` verwenden. Öffne deine Kommandozeile (im Startmenü zu finden als Eingabeaufforderung) und führe die Befehle `python --version` und `pip --version` aus. Beide müssen bei erfolgreicher Installation eine Versionsnummer ausgeben.

## Die virtuelle Pythonumgebung `venv`
Es empfiehlt sich eine virtuelle Pythonumgebung zu nutzen, in die nur die benötigten Pakete für das auszuführende Programm geladen werden. 

Zunächst installieren wir mit dem Kommandozeilenbefehl `pip install virtualenv` das Paket für das Erzeugen einer virtuellen Umbegung.

Leg dir zum Programmtest einen 'Projektordner' auf dem Desktop an und lege alle Dateien aus dieser ZIP dort hinein. Wechsle in der Kommandozeile in den Projektordner (`cd c:\Pfad\zu\deinem\Projektordner\auf\dem\Desktop\`) und führe den Befehl `python -m venv .\venv` aus. Er erzeugt dir im Projektordner einen neuen Order namens `venv`, der deine virtuelle Pythonumgebung beinhaltet.

Starte nun mit `.\venv\Scripts\Activate.ps1` dein virtualenv. Es kann sein, dass ein Fehler der etwas von ***Execution_Policies*** schreibt auftritt. Um ihn zu beheben muss als Administrator in der Powershell der Befehl `Set-Executionpolicy Unrestricted -Force` ausgeführt werden. Danach das Aktivierungsskript nochmal als normaler Nutzer ausführen. In der Kommandozeile sollte nun `(venv)` vor dem aktuellen Pfad stehen.

## Installation der benötigten Pakete
Du befindest dich immernoch im Pfad deines Projektordners. Teste ob du mit dem Befehl `ls` eine Datei namens `requirements.txt` findest. In dieser stehen alle Pakete die mittels des `pip` Befehls installiert werden müssen. Um nicht alle Pakete händisch installieren zu müssen, kannst du mit `pip install -r requirements.txt` alle gelisteten Pakete auf einmal in deine virtuelle Python Umgebung installieren. Sie sind dann nur dort nutzbar und die Dependency-Hölle sollte auf deinen Rechner nicht losbrechen.