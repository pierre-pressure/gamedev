# Python Game Development Lernpfad: Isometric Hack & Slash Mastery

Ein strukturierter 20‑Wochen‑Roadmap für Python‑Entwickler mit mittlerem Erfahrungsschatz, die professionelle isometrische Hack‑&‑Slash‑Spiele (z. B. Diablo 3) bauen möchten. Die Lernreise führt von den Grundlagen bis hin zu KI‑Integration, Deployment und dem Übergang zu Profi‑Engines.

---

## 📚 1. Lernphasen (ca. 20 Wochen)

| Phase       | Wochen  | Ziele                                                         |
| ----------- | ------- | ------------------------------------------------------------- |
| **Phase 1** | 1 – 8   | Game‑Loop, Core‑Mechaniken, Pygame‑Basics                     |
| **Phase 2** | 9 – 16  | KI‑Integration, fortgeschrittene Systeme (Arcade, TensorFlow) |
| **Phase 3** | 17 – 20 | Optimierung, Deployment & Distribution (PyInstaller, Steam)   |

**Übergang der Bibliotheken:**

1. **Pygame** (Fundament)
2. **Arcade** (Hardware‑Beschleunigung, saubere API)
3. Optional **Pyglet** (Low‑Level‑Grafik‑Kontrolle)

---

## 🎮 2. Fundamentals & Projektmeilensteine

1. **Erstes Projekt: Game Window & Sprite‑Bewegung**

   * Game‑Loop: Event‑Handling, State‑Update, Rendering
   * Koordinatensystem & Tastatur‑Input
   * Kollisionserkennung am Fenster‑Rand

2. **Pong‑Klon**

   * Ball‑Rückstoß, Paddle‑Kollision
   * Spielstatus‑Management

3. **Snake‑Spiel**

   * Gitterbasiertes Movement
   * Wachsender Snake‑Körper, Wachstumspunkte

4. **Isometrischer Renderer** (ab Woche 13)

   * Intuitive Transformation nach 2D‑Basics
   * Motivation durch sichtbaren Fortschritt

---

## 🧩 3. Isometrische Entwicklung

* **2:1 Pixel‑Ratio (Dimetrisch)**

  ```python
  screen_x = (map_x - map_y) * TILE_WIDTH_HALF
  screen_y = (map_x + map_y) * TILE_HEIGHT_HALF
  # übliche Tile-Größe: 64×32 px
  ```

* **Trennung von Logik & Rendering**

  * Spiel‑Logik in kartesischen `map_x`/`map_y`
  * Isometrische Transformation nur beim Zeichnen

* **Rendering‑Reihenfolge (Painter’s Algorithm)**

  1. Zeilen von hinten nach vorne
  2. In jeder Zeile: links → rechts
  3. Objekte nach `map_y + map_x` sortieren

* **Kamerasystem & Viewport‑Culling**

  * Kamera folgt Ziel in Weltkoordinaten
  * Nur sichtbare Tiles zeichnen, um Performance zu sparen

---

## 🤖 4. KI‑ & Neural‑Network‑Strategie

* **Start:** ab Woche 10 mit TensorFlow + Keras

* **Echtzeit‑Performance:**

  * AI in separaten Threads
  * Kommunikation über Queues
  * Ziel: < 10 ms Entscheidungslatenz (60 FPS), < 200 MB Speicher

* **Anwendungen:**

  * Adaptive Gegner‑Taktiken (Nah‑/Fernkampf‑Präferenzen)
  * Prozedurale Inhaltserzeugung (Loot, Challenges)

* **Bibliotheken:**

  * Scikit‑learn (Clustering, Verhaltenserkennung)
  * TensorFlow Agents (Reinforcement Learning)

---

## ⚔️ 5. Kampfmechaniken & Item‑System

1. **Item‑Qualität (Diablo 3‑Modell):**

   | Typ       | Eigenschaften                            |
   | --------- | ---------------------------------------- |
   | Normal    | Basis‑Stats                              |
   | Magic     | 1–3 zufällige Eigenschaften              |
   | Rare      | 4–6 Eigenschaften                        |
   | Legendary | 6–8 Eigenschaften + einzigartige Effekte |

2. **Datenbank‑Struktur:**

   * `base_items` (Vorlagen)
   * `item_modifiers` (Pools)
   * `player_items` (Instanzen)

3. **Schadensformeln:**

   ```python
   defense_reduction = defender.defense / (defender.defense + 100)
   crit_chance       = min(100, max(0, attacker.luck - defender.luck))
   ```

4. **Enhancement (Metin2‑Stil):**

   * Levels 0–2: 100 % Erfolg
   * bis Level 15: 4 % Erfolg
   * Fehlschläge zerstören Item (Bannrolle schützt)

---

## 🚀 6. Deployment & Distribution

* **PyInstaller:** Single‑File Executables, plattformübergreifend

* **Nuitka:** Python → C++ → Binary für maximale Performance

* **Steam‑Integration:**

  1. Partner‑Fee: 100 \$
  2. SDK‑Integration (Achievements, Networking)
  3. App‑Konfiguration & Review (2–3 Wochen)
  4. Umsatzteilung: 30 % (Steam), 70 % (Dev)

* **Performance‑Optimierung:**

  * Früh‑Profiling (cProfile)
  * Objekt‑Pooling
  * Frame‑Rate‑Limiting (30–60 FPS)

* **Asset‑Schutz:**

  * PyInstaller‑Verschlüsselung
  * Custom‑Formate, XOR‑Encryption
  * Server‑Validierung wichtiger Logik

---

## 🗂️ 7. Repo‑Organisation & Tracking

* **Phase‑basierte Ordner** mit nummerierten Projekten
* Jede Phase hat eigene **README.md** (Ziele, Konzepte, Code‑Walkthrough)
* **Meilensteine** über GitHub Milestones & Portfolio
* **Dokumentation:** „Why?“ statt nur „How?“
* **Assessment‑Kriterien:**

  * Funktionalität: 40 %
  * Code‑Qualität: 25 %
  * Lernziele: 20 %
  * Kreativität: 15 %

---

## 🔄 8. Übergang zu Profi‑Engines

* **Godot (GDScript):** Python‑ähnlich, Node‑Architektur

* **Unity (C#):** Statisches Typing, große Industrie‑Adoption

* **Fokus:**

  * Game‑Loop, Component‑Pattern, OOP
  * Architektur‑Muster & Problemlösungsansatz

* **Timeline:**

  | Abschnitt                  | Dauer    |
  | -------------------------- | -------- |
  | Python‑Journey             | 5 Monate |
  | Engine‑Fundamentals        | 1 Monat  |
  | Portierung Python → Engine | 3 Monate |
  | Eigene Engine‑Projekte     | 3 Monate |

---

## 🎓 Fazit: Dein Weg zur Isometric Mastery

Durch konsequente Praxis, saubere Dokumentation und stetigen Kompetenz‑Aufbau wirst du zum **isometrischen Hack‑&‑Slash‑Entwickler**. Dieser 20‑Wochen‑Pfad kombiniert Grundlagen, KI‑Techniken, Deployment und professionelle Engine‑Übergänge – von Sprite‑Bewegung bis Steam‑Release. Viel Erfolg!
