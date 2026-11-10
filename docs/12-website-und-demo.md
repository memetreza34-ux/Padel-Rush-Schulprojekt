# 12 — Website, Buchungsdemo und interne Verwaltungs-Demo
**Ziel:** Präsentationsfähige, professionelle Demo der geplanten Padelhalle. **Kein echter Betrieb.**

## MVP-Website
1. Startseite mit Logo, Hero-Foto/Visualisierung und Unternehmensvision.
2. Unsere Courts: **vier Indoor-Courts als beschlossenes Schulmodell**, null Outdoor zur Eröffnung; Außen-Court nur spätere Vision. [Hallenkonzept](13-hallenkonzept.md).
3. Preise: 28 €/h Nebenzeit, 40 €/h Hauptzeit (**Planpreise**).
4. Angebote: Rush Social, Rush League, Rush Academy, Rush Business, Lounge.
5. Über uns: Vier Gründer ohne erfundene Namen und ohne unnötige persönliche Daten.
6. Standortvision: Niederschönhausen, **Vorbehalt der Freigabe** sichtbar.
7. Demo-Kalender mit **fiktiven** Zeiten, Testbuchungen nur im Demozustand.
8. Kontaktbereich als **Simulation**, falls noch kein rechtskonformer realer Kontaktkanal eingerichtet wurde.

## Demo-Buchung
- Besucher wählt Court, fiktives Datum, Zeit und Dauer.
- System zeigt rechnerisch passenden **Beispielpreis**.
- Bestätigung lautet „Demobuchung — keine reale Reservierung“.
- Keine echten Zahlungen, keine Kreditkarten, kein Adresszwang.
- Buchungslogik verhindert doppelte **Demobelegung** in derselben Sitzung.

## Demo-Backoffice (nur wenn Zeit bleibt)
- Übersicht belegter Beispielstunden / simulierte Auslastung.
- Beispielkassenbelege für Getränke/Schläger, **ohne echte Kassenfunktion**.
- Aufgabenboard: Reinigung, Wartung, Events.
- Export eines **Beispielberichts**, der als fiktiv markiert ist.

## Technik
- Website-Bau: Lovable als Startpunkt.
- Für Zusatzcode alternativ **ein** Coding-Agent (Claude Code oder Codex), kein Pflicht-Doppelwerkzeug.
- Supabase nur bei echtem Backend-/Datenbedarf; für Demo möglichst Beispieldaten.
- Produktivbetrieb später mit professionellem Courtbuchungsanbieter und rechtskonformer Kassenlösung prüfen, nicht durch ungetestete KI-Programmierung ersetzen.

## Abnahmekriterien
- Mobil- und Desktopansicht funktionieren.
- Brandfarben/Logo sind einheitlich.
- Preise stimmen mit dem Finanzmodell und der Preistabelle überein.
- Kein „Jetzt buchen“ vermittelt eine echte reservierbare Halle.
- Angaben über Standort, Eröffnung und Bildmaterial sind transparent.
