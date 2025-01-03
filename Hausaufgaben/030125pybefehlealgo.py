# Aufgabe: Erstelle ein Algo aus Git-Befehlen

git_befehle = {
"clone" : "Kopiert die Ursprungs-URL",
"pull" : "Der git pull -Befehl wird verwendet, um Inhalte aus einem Remote-Repository herunterzuladen und unverzüglich das lokale Repository zu aktualisieren, damit die Inhalte übereinstimmen.",
"push" : "Du kannst mit diesem Befehl einen lokalen Branch in ein anderes Repository verschieben, was eine bequeme Methode zur Veröffentlichung von Beiträgen ist.",
"pull Request" : "Vorschlag zum Zusammenführen einer Reihe von Änderungen von einem Branch in einen anderen. In einem Pull Request können Projektmitarbeiter die vorgeschlagenen Änderungen überprüfen und besprechen, bevor sie die Änderungen in die Standard-Codebasis integrieren.", 
"merge" : "In Git kannst du einen geforkten Verlauf per Merging wieder zusammensetzen.",
"branch" : "Du kannst Branches verwenden, um sicher mit Änderungen an deinem Projekt zu experimentieren. Branches isolieren deine Entwicklungsarbeit von anderen Branches im Repository. Du könntest beispielsweise einen Branch verwenden, um ein neues Feature zu entwickeln oder einen Fehler zu beheben.",
"repo" : "Ein Git-Repository ist der Ordner .git/ innerhalb eines Projekts . Dieses Repository verfolgt alle an Dateien in Ihrem Projekt vorgenommenen Änderungen und erstellt im Laufe der Zeit einen Verlauf. Das heißt, wenn Sie den Ordner .git/ löschen, löschen Sie den Verlauf Ihres Projekts.",
"github" : "GitHub ist eine cloud-basierte Plattform, auf der Sie Code speichern, teilen und mit anderen zusammenarbeiten können. Indem Sie Code in einem „Repository“ auf GitHub speichern, können Sie: Ihre Arbeit präsentieren oder teilen. Änderungen an Ihrem Code im Laufe der Zeit nachverfolgen und verwalten.",
"commit": "Speichert die Änderungen im Repository.",
}

def git_befehl_info(befehl):
   
    return git_befehle.get(befehl, "Befehl nicht gefunden. Bitte einen gültigen Git-Befehl eingeben.")


befehl = input("Gib einen Git-Befehl ein: ").lower()
beschreibung = git_befehl_info(befehl)
print(beschreibung)