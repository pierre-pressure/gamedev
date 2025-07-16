# =============================================================================
# PROJEKT 2: BEWEGLICHE RECHTECKE - LERNDOKUMENTATION
# =============================================================================
"""
LERNZIELE ERREICHT:
✅ Position + Velocity Mathematik verstehen und implementieren
✅ pygame.Rect System für Sprites und Kollisionen beherrschen
✅ Boundary Collision Detection mit perfekter Response
✅ Physics-basierte Bewegung in der Update-Phase
✅ Code-Struktur mit Konstanten und professioneller Organisation
✅ Transfer-Learning: Pattern-Erkennung für verschiedene Achsen

WICHTIGE ERKENNTNISSE:
- position = position + velocity ist das Herz aller Bewegung
- pygame.Rect macht Kollisionen und Positionierung trivial
- 3-Schritt Kollisions-Pattern: Detect → Respond → Correct
- Clean Code mit Konstanten ist Industry-Standard
- Update-Phase ist der richtige Ort für Bewegungslogik
"""

import pygame

# =============================================================================
# 1. KONSTANTEN UND SETUP - PROFESSIONAL CODE ORGANIZATION
# =============================================================================

"""
WARUM KONSTANTEN AM ANFANG?
- Zentrale Konfiguration (keine "Magic Numbers")
- Einfache Anpassungen (Fenstergröße, Geschwindigkeiten)
- Bessere Lesbarkeit und Wartbarkeit
- Industry-Standard Practice
"""

pygame.init()

# WINDOW CONFIGURATION
FPS = 60              # Standard für smooth Gaming
WIDTH = 800           # Fensterbreite
HEIGHT = 600          # Fensterhöhe

# COLOR DEFINITIONS
WHITE = (255, 255, 255)  # RGB: Maximale Helligkeit alle Kanäle
BLACK = (0, 0, 0)        # RGB: Keine Helligkeit = schwarz

# PLAYER CONFIGURATION  
PLAYER_W = 50         # Player Breite
PLAYER_H = 50         # Player Höhe

# PHYSICS CONFIGURATION
PLAYER_VELX = 5       # Horizontale Geschwindigkeit (Pixel pro Frame)
PLAYER_VELY = 5       # Vertikale Geschwindigkeit (für spätere Nutzung)

# =============================================================================
# 2. PYGAME.RECT - DAS SPRITE-SYSTEM VERSTEHEN
# =============================================================================

"""
RECT KONZEPT:
- Rect = Rectangle = Rechteck mit Position UND Größe
- Ersetzt x,y,width,height Variablen durch EIN Objekt
- Eingebaute Collision Detection und Helper-Properties
- Standard für ALLE Sprites in Pygame

RECT CREATION PATTERNS:
pygame.Rect(x, y, width, height)  # Direkte Koordinaten
pygame.Rect(pos, size)            # Tuple-basiert
"""

# DISPLAY SETUP
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bewegliche Rechtecke 2 - Jetzt erst recht-eck")

# PLAYER RECT CREATION - Zentrierte Startposition
player = pygame.Rect(
    WIDTH / 2 - PLAYER_W / 2,   # X: Bildschirmmitte minus halbe Breite
    HEIGHT / 2 - PLAYER_H / 2,  # Y: Bildschirmmitte minus halbe Höhe  
    PLAYER_W,                   # Breite
    PLAYER_H                    # Höhe
)

# VELOCITY VARIABLES - Das Herzstück der Bewegung
player_velx = PLAYER_VELX  # Horizontale Geschwindigkeit
player_vely = PLAYER_VELY  # Vertikale Geschwindigkeit (unused in diesem Projekt)

# PERFORMANCE MONITORING
clock = pygame.time.Clock()
frame_count = 0

# =============================================================================
# 3. RECT PROPERTIES - DER GAME-CHANGER
# =============================================================================

"""
WICHTIGE RECT PROPERTIES:
.x, .y          # Obere linke Ecke (Standard-Koordinaten)
.centerx, .centery  # Mittelpunkt-Koordinaten
.center         # Mittelpunkt als (x,y) Tuple

BOUNDARY PROPERTIES (sehr wichtig für Kollisionen):
.left           # X-Koordinate der linken Kante (= .x)
.right          # X-Koordinate der rechten Kante (= .x + .width)
.top            # Y-Koordinate der oberen Kante (= .y)  
.bottom         # Y-Koordinate der unteren Kante (= .y + .height)

WARUM BOUNDARY PROPERTIES NUTZEN?
- .right >= WIDTH ist intuitiver als .x + .width >= WIDTH
- Collision Detection wird lesbarer
- Position-Korrekturen werden einfacher
- Code wird self-documenting

BEISPIEL RECT MIT WIDTH=50, HEIGHT=50 bei Position (100, 200):
.x = 100, .y = 200          # Obere linke Ecke
.right = 150, .bottom = 250 # Untere rechte Ecke
.centerx = 125, .centery = 225  # Mittelpunkt
"""

# =============================================================================
# 4. POSITION + VELOCITY MATHEMATIK
# =============================================================================

"""
DAS FUNDAMENT ALLER BEWEGUNG:
position = position + velocity

JEDEN FRAME ausgeführt ergibt smooth movement:
Frame 1: x = 100, velx = 5  →  x = 105
Frame 2: x = 105, velx = 5  →  x = 110  
Frame 3: x = 110, velx = 5  →  x = 115
...

WARUM VELOCITY STATT DIREKTE POSITION-ÄNDERUNG?
1. PHYSICS: Geschwindigkeit kann verändert werden (Beschleunigung)
2. DIRECTION: velocity *= -1 kehrt Richtung um (Bounce!)
3. LOGIC: Bewegungslogik getrennt von Positions-Updates
4. FLEXIBILITY: Einfache Implementierung von Reibung, Gravitation, etc.

VELOCITY PATTERNS:
velx = 5   # Bewegung nach rechts
velx = -5  # Bewegung nach links  
velx = 0   # Stillstand
velx *= -1 # Richtung umkehren (bounce effect)
"""

# =============================================================================
# 5. DER GAME LOOP MIT MOVEMENT
# =============================================================================

running = True

while running:
    
    # =========================================================================
    # 5.1 EVENT HANDLING (INPUT PHASE)
    # =========================================================================
    """
    Gleich wie Projekt 1 - Event System bleibt konsistent
    """
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                running = False
            case pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        running = False

    # =========================================================================
    # 5.2 UPDATE PHASE - MOVEMENT UND COLLISION LOGIC
    # =========================================================================
    """
    HIER PASSIERT DIE MAGIE:
    1. Position basierend auf Velocity updaten
    2. Kollisionen checken
    3. Physics Response anwenden
    4. Position korrigieren
    
    WICHTIG: Update-Phase kommt VOR Render-Phase!
    """
    
    # MOVEMENT UPDATE - Das Herz der Physics
    player.x += player_velx  # Position = Position + Velocity
    
    # COLLISION DETECTION UND RESPONSE
    """
    COLLISION DETECTION PATTERN:
    1. DETECT: Kollision erkennen (Boundary Check)
    2. RESPOND: Physics anwenden (Bounce, Stop, etc.)
    3. CORRECT: Position fixen (Anti-Clipping)
    
    WARUM POSITION CORRECTION?
    Ohne Korrektur kann der Player "in" die Wand eindringen:
    player.x = 790, WIDTH = 800, player.width = 50
    player.right = 840 (außerhalb des Bildschirms!)
    """
    
    # RECHTE WAND KOLLISION
    if player.right >= WIDTH:
        player_velx *= -1        # RESPOND: Geschwindigkeit umkehren
        player.right = WIDTH     # CORRECT: Position an Wand setzen
        
    # LINKE WAND KOLLISION  
    elif player.left <= 0:
        player_velx *= -1        # RESPOND: Geschwindigkeit umkehren
        player.left = 0          # CORRECT: Position an Wand setzen

    # =========================================================================
    # 5.3 RENDER PHASE - VISUELLES UPDATE
    # =========================================================================
    """
    RENDERING BLEIBT EINFACH:
    1. Background clearen
    2. Alle Objekte zeichnen
    3. Frame anzeigen
    """
    
    screen.fill(WHITE)                              # Background
    pygame.draw.rect(screen, BLACK, player)        # Player zeichnen
    pygame.display.flip()                          # Frame anzeigen

    # =========================================================================
    # 5.4 PERFORMANCE MONITORING
    # =========================================================================
    frame_count += 1
    if frame_count % 60 == 0:
        fps = clock.get_fps()
        print(f"Gameloop läuft mit {fps:.0f} FPS")

    clock.tick(FPS)

# =============================================================================
# 6. COLLISION PATTERNS IM DETAIL
# =============================================================================

"""
BOUNDARY COLLISION COMPONENTS:

1. DETECTION (Wann passiert Kollision?):
   - player.right >= WIDTH   # Rechte Wand berührt
   - player.left <= 0        # Linke Wand berührt
   - player.bottom >= HEIGHT # Boden berührt
   - player.top <= 0         # Decke berührt

2. RESPONSE (Was passiert bei Kollision?):
   - velocity *= -1          # Bounce (Richtung umkehren)
   - velocity = 0            # Stop (Bewegung stoppen)
   - velocity += gravity     # Physics (z.B. Gravitation)

3. POSITION CORRECTION (Clipping verhindern):
   - player.right = WIDTH    # An rechte Wand setzen
   - player.left = 0         # An linke Wand setzen
   - player.bottom = HEIGHT  # Auf Boden setzen
   - player.top = 0          # An Decke setzen

WARUM ELIF STATT IF?
elif verhindert "corner cases" wo beide Kollisionen gleichzeitig auftreten
"""

# =============================================================================
# 7. ERWEITERTE PHYSICS KONZEPTE
# =============================================================================

"""
BOUNCE PHYSICS VERSTEHEN:

ELASTISCHER BOUNCE (Perfect Bounce):
velocity *= -1  # Vollständige Energieerhaltung

GEDÄMPFTER BOUNCE (Realistic Bounce):  
velocity *= -0.8  # 20% Energieverlust pro Bounce

GRAVITATION HINZUFÜGEN:
velocity_y += gravity  # Konstante Beschleunigung nach unten

REIBUNG IMPLEMENTIEREN:
velocity_x *= friction  # Geschwindigkeit nimmt ab (friction < 1.0)

MAXIMALGESCHWINDIGKEIT:
if abs(velocity_x) > max_speed:
    velocity_x = max_speed * (1 if velocity_x > 0 else -1)
"""

# =============================================================================
# 8. CODE ARCHITECTURE LESSONS
# =============================================================================

"""
SAUBERE CODE-ORGANISATION:

1. KONSTANTEN ZUERST:
   - Konfiguration zentral
   - Keine Magic Numbers
   - Einfache Anpassungen

2. SETUP-BEREICH:
   - Pygame Initialisierung
   - Object Creation
   - Variable Initialization

3. GAME LOOP STRUKTUR:
   - Events → Update → Render → Performance
   - Jede Phase hat klaren Zweck
   - Keine Vermischung der Phasen

4. VARIABLE NAMING:
   - player_velx (descriptive)
   - nicht: vx (cryptic)
   - Konsistente Naming Convention

5. COMMENTS UND STRUKTUR:
   - CodeBullet Trennung mit # ----
   - Sektionen klar abgegrenzt
   - Kommentare erklären WARUM, nicht WAS
"""

# =============================================================================
# 9. TRANSFER LEARNING - PATTERN RECOGNITION
# =============================================================================

"""
ERKANNTE PATTERNS:

1. ACHSEN-UNABHÄNGIGKEIT:
   X-Achse: left/right boundaries mit WIDTH
   Y-Achse: top/bottom boundaries mit HEIGHT
   → Gleiche Logik, andere Properties

2. COLLISION TEMPLATE:
   if object.boundary >= limit:
       object.velocity *= -1
       object.boundary = limit

3. MOVEMENT TEMPLATE:
   object.position += object.velocity

4. DIESE PATTERNS FUNKTIONIEREN FÜR:
   - Pong Bälle
   - Breakout Spiele
   - Platform Game Physics
   - Particle Systems
   - ALLE bewegten Objekte!
"""

# =============================================================================
# 10. DEBUGGING UND HÄUFIGE FEHLER
# =============================================================================

"""
HÄUFIGE PROBLEME UND LÖSUNGEN:

PROBLEM: Player "hängt" in der Wand
LÖSUNG: Position correction vergessen (player.right = WIDTH)

PROBLEM: Player verschwindet aus Bildschirm
LÖSUNG: Falsche Boundary Check (.x statt .right verwendet)

PROBLEM: Doppel-Bounce an Ecken
LÖSUNG: elif statt if verwenden für Kollisions-Checks

PROBLEM: Inkonsistente Bewegung
LÖSUNG: Velocity in Update-Phase, nicht in Event-Phase ändern

PROBLEM: Performance Issues
LÖSUNG: Movement Logic zu komplex, Grundlagen vereinfachen

DEBUG TIPPS:
- print(player.x, player.y) für Position-Debugging
- print(player_velx) für Velocity-Debugging  
- Temporäre Geschwindigkeit reduzieren für bessere Sichtbarkeit
"""

# =============================================================================
# 11. NÄCHSTE SCHRITTE UND ERWEITERUNGEN
# =============================================================================

"""
MÖGLICHE ERWEITERUNGEN:

1. Y-ACHSE MOVEMENT:
   player.y += player_vely
   if player.bottom >= HEIGHT: player_vely *= -1; player.bottom = HEIGHT
   if player.top <= 0: player_vely *= -1; player.top = 0

2. DIAGONAL MOVEMENT:
   Beide Achsen gleichzeitig aktivieren für DVD-Screensaver Effect

3. MULTIPLE OBJECTS:
   Liste von Rects mit eigenen Velocities

4. REALISTIC PHYSICS:
   Gravity, Friction, Energy Loss implementieren

5. INPUT CONTROL:
   User kann Geschwindigkeit/Richtung beeinflussen

SKILL FOUNDATIONS GELEGT:
✅ Object-based Movement
✅ Collision Detection
✅ Physics Response
✅ Clean Code Architecture
✅ Pattern Recognition

READY FÜR:
- Player Input Systems
- Multiple Object Management  
- Object-to-Object Collisions
- Advanced Physics
- Game Mechanics Implementation
"""

print("Spiel wurde beendet")
pygame.quit()

# =============================================================================
# ENDE PROJEKT 2 DOKUMENTATION
# =============================================================================