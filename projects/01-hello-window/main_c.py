# =============================================================================
# PROJEKT 1: DAS SCHWARZE FENSTER - LERNDOKUMENTATION
# =============================================================================
"""
LERNZIELE ERREICHT:
✅ Game Loop Konzept verstehen und implementieren
✅ Pygame Grundlagen (Initialisierung, Display, Event Handling)
✅ FPS-Management und Performance-Grundlagen
✅ Event-System für saubere Programmbeendigung
✅ Match-Case für modernen, sauberen Code
✅ Rendering Pipeline Basics verstehen

WICHTIGE ERKENNTNISSE:
- Jedes Spiel ist eine Endlosschleife (Game Loop)
- Input → Update → Render ist der Kern JEDES Spiels
- Events vs. kontinuierliche Checks unterscheiden
- Clock-System für konsistente Performance
- Double Buffering (flip) verhindert Flackern
"""

import pygame

# =============================================================================
# 1. GRUNDSTRUKTUR EINES PYGAME-PROGRAMMS
# =============================================================================

"""
JEDES Pygame-Programm folgt diesem Schema:
1. Import und Initialisierung
2. Hauptfenster erstellen
3. Game Loop starten
4. Sauber aufräumen
"""

# 1.1 IMPORTS UND KONSTANTEN
# -----------------------------------------------------------------------------
# Warum Konstanten? Zentrale Konfiguration, bessere Lesbarkeit
FPS = 60  # Ziel-Framerate - Standard für flüssige Spiele

# 1.2 PYGAME INITIALISIERUNG
# -----------------------------------------------------------------------------
pygame.init()  # Startet ALLE Pygame-Module (Grafik, Sound, Input, etc.)
# Warum nötig? Pygame muss Hardware-Zugriff einrichten

# 1.3 DISPLAY SETUP
# -----------------------------------------------------------------------------
screen = pygame.display.set_mode((800, 600))  # Erstellt Hauptfenster
# Returns: Surface-Objekt (Zeichenfläche)
# (800, 600) = Breite x Höhe in Pixeln

pygame.display.set_caption("Schwarzes Fenster 1 - The Beginning Of The Void!")
# Setzt Fenster-Titel (wird in Taskleiste angezeigt)

# =============================================================================
# 2. CLOCK-SYSTEM FÜR FPS-MANAGEMENT
# =============================================================================

"""
CLOCK KONZEPT:
- Clock misst Zeit zwischen Frames
- tick(fps) wartet maximal bis Ziel-FPS erreicht
- get_fps() gibt tatsächliche FPS zurück (basiert auf gemessenen Zeiten)

WICHTIG: Clock braucht tick() Aufrufe zum Messen!
Ohne tick() → get_fps() returns 0
"""

clock = pygame.time.Clock()  # Erstellt Clock-Objekt für FPS-Management
frame_count = 0  # Counter für Debug-Output

# =============================================================================
# 3. DER GAME LOOP - HERZSTÜCK JEDES SPIELS
# =============================================================================

"""
GAME LOOP PHILOSOPHIE:
1. Events verarbeiten (Input)
2. Spiellogik updaten (Update) 
3. Bildschirm neu zeichnen (Render)
4. FPS begrenzen (Performance)

Läuft 60x pro Sekunde = 60 FPS
"""

running = True  # Game Loop Kontrollvariable

while running:  # Die Endlosschleife - jeden frame

    # =========================================================================
    # 3.1 EVENT HANDLING (INPUT PHASE)
    # =========================================================================
    """
    EVENT SYSTEM:
    - pygame.event.get() holt ALLE Events seit letztem Frame
    - Events sind einmalige Aktionen (Tastendruck, Mausklick, Fenster schließen)
    - WICHTIG: Event-Queue MUSS geleert werden, sonst "hängt" das Programm
    """

    for event in pygame.event.get():  # Alle Events durchgehen
        match event.type:  # Modern Python 3.10+ Syntax (statt if-elif)

            # QUIT EVENT - Fenster schließen (X-Button)
            case pygame.QUIT:
                running = False  # Beendet Game Loop

            # KEYBOARD EVENTS - Tasten-Eingaben
            case pygame.KEYDOWN:  # Taste wurde gedrückt (einmalig!)
                match event.key:  # Nested match-case für spezifische Tasten
                    case pygame.K_ESCAPE:  # ESC-Taste
                        running = False
                    # Weitere Tasten können hier hinzugefügt werden:
                    # case pygame.K_SPACE:
                    #     print("Leertaste gedrückt!")

    # =========================================================================
    # 3.2 UPDATE PHASE (SPIELLOGIK)
    # =========================================================================
    """
    Hier würde normalerweise die Spiellogik laufen:
    - Charaktere bewegen
    - Physik berechnen
    - Kollisionen prüfen
    - KI updaten
    
    In Projekt 1: Keine Logik nötig (nur schwarzer Bildschirm)
    """
    # (Momentan leer - kommt in späteren Projekten)

    # =========================================================================
    # 3.3 RENDER PHASE (ZEICHNEN)
    # =========================================================================
    """
    RENDERING KONZEPT:
    - Alles wird auf "Surfaces" gezeichnet
    - screen.fill() füllt gesamte Surface mit Farbe
    - pygame.display.flip() zeigt gezeichneten Frame an (Double Buffering)
    
    WARUM JEDER FRAME NEU ZEICHNEN?
    - Spiele sind dynamisch - ständige Veränderungen
    - Konsistente Performance besser als on-demand rendering
    """

    screen.fill((0, 0, 0))  # RGB: (Rot, Grün, Blau) - (0,0,0) = Schwarz
    # Füllt GESAMTE Surface mit der Farbe

    pygame.display.flip()  # Zeigt den Frame an (Double Buffering)
    # Warum flip()? Verhindert Flackern durch Doppelpufferung

    # =========================================================================
    # 3.4 DEBUG OUTPUT & PERFORMANCE MONITORING
    # =========================================================================
    """
    PERFORMANCE DEBUGGING:
    - frame_count % 60 = alle 60 Frames (einmal pro Sekunde bei 60 FPS)
    - clock.get_fps() gibt tatsächliche FPS zurück
    - Hilft bei Performance-Problemen
    """

    frame_count += 1
    if frame_count % 60 == 0:  # Alle 60 Frames (≈ 1 Sekunde)
        fps = clock.get_fps()  # Tatsächliche FPS messen
        print(f"Game Loop läuft... FPS: {fps:.0f}")

    # =========================================================================
    # 3.5 FPS LIMITING (PERFORMANCE CONTROL)
    # =========================================================================
    """
    CLOCK.TICK() FUNKTIONSWEISE:
    - Misst Zeit seit letztem tick()
    - Wartet falls nötig bis Ziel-Zeit erreicht
    - Beispiel: Frame dauerte 10ms, Ziel 16.67ms → wartet 6.67ms
    - Wenn Frame länger dauert → wartet nicht (kann keine Zeit zurückdrehen)
    
    WARUM FPS BEGRENZEN?
    - Stromsparend (verhindert 3000+ FPS)
    - Konsistente Geschwindigkeit auf verschiedener Hardware
    - Vorhersagbare Performance
    """

    clock.tick(FPS)  # Begrenzt auf 60 FPS (wartet max. 16.67ms)

# =============================================================================
# 4. CLEANUP - SAUBERES BEENDEN
# =============================================================================
"""
WICHTIG: Ressourcen freigeben!
- pygame.quit() schließt alle SDL-Subsysteme
- Ohne cleanup können Ressourcen "hängen" bleiben
"""

print("Spiel beendet!")  # User-Feedback
pygame.quit()  # Pygame ordnungsgemäß beenden

# =============================================================================
# 5. WICHTIGE PYGAME KONZEPTE VERSTANDEN
# =============================================================================

"""
SURFACE KONZEPT:
- Alles in Pygame ist eine Surface (Zeichenfläche)
- screen = Haupt-Surface (das Fenster)
- Sprites, Text, etc. sind auch Surfaces
- Surfaces können auf andere Surfaces gezeichnet werden

EVENT SYSTEM:
- Events = einmalige Aktionen (Tastendruck, Mausklick)
- Kontinuierliche Checks = pygame.key.get_pressed() (kommt später)
- Event-Queue MUSS geleert werden (pygame.event.get())

KOORDINATENSYSTEM:
- (0,0) = oben links
- X = nach rechts
- Y = nach UNTEN (nicht wie in Mathe!)

DOUBLE BUFFERING:
- Zwei "Leinwände": eine wird gezeichnet, andere angezeigt
- display.flip() tauscht die beiden
- Verhindert Flackern und zerrissene Frames
"""

# =============================================================================
# 6. HÄUFIGE FEHLER UND LÖSUNGEN
# =============================================================================

"""
PROBLEM: Fenster öffnet sich nicht
LÖSUNG: pygame.init() vergessen oder display.set_mode() fehlt

PROBLEM: Spiel lässt sich nicht schließen
LÖSUNG: Event-Loop fehlt oder pygame.QUIT nicht behandelt

PROBLEM: Hohe CPU-Last
LÖSUNG: clock.tick() vergessen

PROBLEM: get_fps() gibt 0 zurück
LÖSUNG: clock.tick() wird nicht aufgerufen (Clock braucht tick() zum Messen)

PROBLEM: Programm "hängt"
LÖSUNG: pygame.event.get() fehlt (Event-Queue verstopft)
"""

# =============================================================================
# 7. NÄCHSTE SCHRITTE
# =============================================================================

"""
PROJEKT 2 VORBEREITUNG:
- Sprites und Bewegung
- Pygame Rect-System
- Grundlegende Physik (Gravity)
- Boundary Collision Detection

NEUE KONZEPTE:
- pygame.Surface für Sprites
- pygame.Rect für Positionierung
- Bewegungslogik in Update-Phase
- Asset Loading (Bilder/Grafiken)
"""

# =============================================================================
# ENDE PROJEKT 1 DOKUMENTATION
# =============================================================================
