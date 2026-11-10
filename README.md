# PADEL RUSH BERLIN — Schulprojekt

> **Status (10.11.2026):** Konzeptionelles Schul-Businessprojekt eines vierköpfigen Teams. **Keine echte Eröffnung, Buchbarkeit oder Standortzusage.**

PADEL RUSH ist die Idee für einen modernen Padel- und Freizeitclub in Berlin: Courts, Training, Turniere, offene Matches, Firmenevents und eine kleine Lounge. Das GitHub-Repository ist die **zentrale Arbeitsablage** für Konzept, Quellen, Standort, Finanzplanung, Marketing, Website-Demo und Präsentation.

## Schnellnavigation

| Thema | Dokument |
| --- | --- |
| Projektbrief, Entscheidungen, offene Fragen | [Projektbrief](docs/01-projektbrief.md) |
| Wunschstandort Betriebshof Niederschönhausen | [Standortanalyse](docs/02-standort.md) |
| **Standortrecherche vom 10.11.2026 mit Primärquellen** | [BVG-Prüfung + alternative Hallen](research/2026-11-10-standortpruefung-niederschoenhausen.md) |
| Vorlagen für sachliche Standortanfragen | [BVG/Makler](templates/standort-anfrage.md) |
| Checkliste zur Standortfreigabe | [Go/No-Go](templates/standort-pruefcheckliste.md) |
| **Hallenkonzept – 4 Indoor-Courts und 1.600 m² Modellfläche** | **[Hallenkonzept](docs/13-hallenkonzept.md)** |
| Geschäftsmodell, Zielgruppen und Angebote | [Geschäftsmodell](docs/03-geschaeftsmodell.md) |
| **Vollständige Angebots-, Kosten- und Erlöskalkulation** | **[14 — Preise und Deckungsbeiträge](docs/14-angebote-und-preiskalkulation.md)** |
| Angebote als CSV zum Nachrechnen | [Einzelkalkulation (CSV)](research/2026-11-10-angebote-einzelkalkulation.csv) |
| Automatischer Rechencheck ohne externe Bibliotheken | [Prüfskript (Python)](scripts/validate_financial_model.py) |
| **Marktanalyse Berlin – 8 recherchierte Wettbewerber** | **[Marktanalyse](docs/04-markt-und-konkurrenz.md)** |
| Vollständiger Quellen-/Konkurrenzbericht vom 10.11.2026 | [Research](research/2026-11-10-markt-konkurrenz-berlin.md) |
| Tabelle mit 8 Berliner Padelclubs (CSV) | [Wettbewerberdaten](research/2026-11-10-wettbewerber-berlin.csv) |
| Freiwillige Nachfrage-Umfrage (noch nicht durchgeführt) | [Fragebogen](templates/nachfrage-umfrage.md) |
| **Neuer Finanzplan: 340.000 € inkl. 50.000 € Reserve, Jahresanlauf** | **[Finanzplanung](docs/05-finanzen.md)** |
| Vollständige Finanzanlage, Szenarien und Break-even | [Rechenteil](docs/15-finanzanlage-fuer-praesentation.md) |
| **Vollständiges Vortragsskript 21 Folien (1:1 sprechen)** | **[Gesamtes Manuskript](presentation/PADEL-RUSH-PRAESENTATION-INHALT-KOMPLETT.md)** |
| **Vier einzelne Sprecher-Skripte und Folienübersicht** | [Vortragsordner](presentation/00-gesamtuebersicht.md) |
| **Quellen je Folie, Lehrerfragen, Medien und Faktencheck** | [Quellenregister](presentation/05-quellen-und-folienmaterial.md) · [Fragen](presentation/06-fragen-und-qualitaetssicherung.md) |
| Gliederung mit 21 Folien | [Präsentationsplanung](docs/06-praesentation.md) |
| Marke, Marketing und Kundenbindung | [Marketing](docs/07-marketing.md) |
| Vier Gründer, Zuständigkeiten und Werkzeuge | [Team und Tools](docs/08-team-und-tools.md) |
| Rechtliche Anforderungen und Risiken | [Recht und Risiken](docs/09-recht-und-risiken.md) |
| Roadmap, Aufgaben und Entscheidungen | [Arbeitsplan](docs/10-roadmap.md) |
| Quellen, Belegqualität, Nachprüfungen | [Quellen & Prüfstatus](docs/11-quellen-und-pruefstatus.md) |
| Website, Buchungsdemo und Verwaltungs-Demo | [Website-Demo](docs/12-website-und-demo.md) |
| Bisher im Chat bereitgestellte Bilder | [Asset-Verzeichnis](assets/README.md) |

## Arbeitsumfang: ausschließlich Schulprojekt

Die Gründung und die Umnutzung des Betriebshofs sind **hypothetisch**. Wir erstellen einen Businessplan und Präsentationsmaterial, ohne Eigentümer, Behörden oder Vermieter zu kontaktieren. Externe Risiken werden erwähnt, aber nicht praktisch bearbeitet.

## Sofort wichtigste offene Punkte

1. **Standort-Alarm ROT:** Die BVG prüft/plant die Rückkehr der Straßenbahnnutzung; 2026 wurde die Planung eines Gleichrichterwerks veröffentlicht. Für das denkmalgeschützte Depot **keine Sportflächenfreigabe und kein Mietangebot**. Als Alternative ist eine 1.400-m²-Kalthalle in Niederschönhausen mit Inseratskosten dokumentiert; auch deren Sportnutzung ist **nicht geklärt**. Details: [Standortprüfung](research/2026-11-10-standortpruefung-niederschoenhausen.md).
2. **Hallenkonzept für die Schulplanung festgelegt:** **4 Indoor-Courts, 0 Outdoor zum Start, ca. 1.600 m² angenommene Gesamtfläche**. Outdoor auf der Visualisierung = mögliche spätere Erweiterung. [Detailplan](docs/13-hallenkonzept.md).
3. **Marktanalyse durchgeführt:** **8 reale Vergleichsclubs, Q3/2026-Berlinzahlen, Anbieterpreise und Schulumfragevorlage dokumentiert**. Echte lokale Nachfrage und Zahlungsbereitschaft sind **nicht gemessen**. [Auswertung](docs/04-markt-und-konkurrenz.md).
4. **Finanzmodell und Vortragsinhalt ausgearbeitet:** Produktkalkulation, 12-Monats-Anlauf, Kreditanalyse und Szenarien. **340.000 €** fiktiver Kapitalbedarf einschließlich **50.000 € Reserve**; bei 45 % Auslastung ergibt sich eine **ca. +1.374 € vereinfachte Monatsbudgetdeckung**, aber ein **ca. −28.932 €** rechnerisches Startjahresergebnis nach Budget-Auszahlungen. **Das ist kein tatsächlicher Gewinn.** [Finanzanlage](docs/15-finanzanlage-fuer-praesentation.md).
5. **Branding:** Logo und Visualisierungen liegen im Gespräch vor; Original-Bilddateien sind noch **nicht in diesem Repository**. Vor öffentlicher Nutzung Bildrechte und Namens-/Markenkonflikte prüfen.

## Inhaltliche Fertigstellung der Präsentation

**Alle 21 Folien und sämtliche Sprechertexte sind ausgearbeitet** und als [zusammenhängendes Vortragsmanuskript](presentation/PADEL-RUSH-PRAESENTATION-INHALT-KOMPLETT.md) gespeichert. **Noch nicht erstellt:** PowerPoint-Datei, endgültige Bildintegration, tatsächliche 20–25-Minuten-Sprechprobe. Nach nächster Rückmeldung folgt die PowerPoint-Gestaltung im vorhandenen PR-BERLIN-Branding.

## Arbeitsregeln

- **Fakten, Planannahmen, Ideen und offene Fragen konsequent trennen.**
- Quellen mit URL, Abrufdatum und Geltungsbereich dokumentieren.
- Keine erfundenen Genehmigungen, Hallenangebote, Kunden, Auslastungen oder Buchungen.
- Änderungen in passenden Dokumenten nachführen und den [Arbeitsplan](docs/10-roadmap.md) aktualisieren.
- Für Schul-Demos keine echten Zahlungen, personenbezogenen Kundendaten oder vermeintlich live buchbaren Courts anbieten.

**Status der Organisation:** Ein gemeinsamer Arbeitsordner für das gesamte Schulprojekt, nicht der Nachweis eines bereits existierenden Unternehmens.
