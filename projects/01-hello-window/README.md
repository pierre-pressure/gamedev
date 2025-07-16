# Projekt 1: Das schwarze Fenster

## 🎯 Lernziele
- **Game Loop Konzept** verstehen und implementieren
- **Pygame Grundlagen** (Initialisierung, Display, Event Handling)
- **FPS-Management** und Performance-Grundlagen
- **Event-System** für saubere Programmbeendigung
- **Rendering Pipeline** Basics verstehen

## 📚 Was du in diesem Projekt lernst

### Der Game Loop - Das Herz jedes Spiels
Ein Spiel ist im Grunde eine endlose Schleife, die ca. 60x pro Sekunde läuft. In jedem "Frame" passiert folgendes:
1. **Events verarbeiten** (Tastatureingaben, Mausklicks, Fenster schließen)
2. **Spiellogik updaten** (Bewegungen berechnen, Kollisionen prüfen)
3. **Bildschirm neu zeichnen** (alles sichtbar machen)

### Warum brauchen wir überhaupt einen Game Loop?
- **Kontinuierliche Updates**: Spiele sind dynamisch - Charaktere bewegen sich, Animationen laufen
- **Responsivität**: Nutzereingaben müssen sofort verarbeitet werden
- **Smooth Performance**: 60 FPS sorgen für flüssige Darstellung
- **Vorhersagbarkeit**: Gleiche Zeitabstände zwischen Updates = berechenbare Physik

### Event-System verstehen
- **pygame.QUIT**: Wird ausgelöst wenn der User das Fenster schließt (X-Button)
- **Warum Event-Loop?**: Ohne sie würde das Programm "hängen" und das Fenster nicht reagieren
- **OS-Integration**: Das Betriebssystem kommuniziert über Events mit unserem Spiel

### Rendering Pipeline Basics
- **Surface-Konzept**: Alles in Pygame ist eine "Surface" (Zeichenfläche)
- **display.flip()**: Macht den gezeichneten Frame sichtbar (Double Buffering)
- **Clock**: Steuert die Geschwindigkeit des Game Loops

## 🛠️ Aufgabe

Ein **800x600 Pixel** schwarzes Fenster mit dem Titel **"Mein erstes Spiel"** erstellen.

### Technische Anforderungen:
- ✅ Fenster öffnet sich in der Bildschirmmitte
- ✅ Saubere Beendigung über X-Button oder ESC-Taste
- ✅ 60 FPS Game Loop
- ✅ Schwarzer Hintergrund (RGB: 0, 0, 0)
- ✅ Konsolen-Output: "Game Loop läuft..." alle 60 Frames
- ✅ Konsolen-Output beim Beenden: "Spiel beendet!"

### Bausteine zum Erarbeiten:
- Pygame importieren und initialisieren
- Display-Modus setzen
- Event-Loop programmieren
- FPS-Management implementieren
- Saubere Ressourcen-Freigabe

## 🧠 Verständnisfragen:
1. **Warum braucht es `pygame.init()`?**
2. **Was passiert ohne `clock.tick(60)`?**
3. **Warum ist `pygame.quit()` wichtig?**
4. **Was ist Double Buffering und warum `display.flip()`?**
5. **Warum Event-Loop statt normale while-Schleife?**

## 📁 Dateistruktur
```
projects/01-hello-window/
├── main.py
├── main_c.py
└── README.md
```