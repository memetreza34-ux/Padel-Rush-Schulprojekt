# 12 — Website, Buchungsdemo und interne Verwaltungs-Demo
**Ziel:** Präsentationsfähige, professionelle Demo der geplanten Padelhalle. **Kein echter Betrieb.**

## MVP-Website
1. Startseite mit Logo, Hero-Foto/Visualisierung und Unternehmensvision.
2. Unsere Courts: **vier Indoor-Courts als beschlossenes Schulmodell**, null Outdoor zur Eröffnung; Außen-Court nur spätere Vision. [Hallenkonzept](13-hallenkonzept.md).
3. Preise: **28 €/h Nebenzeit (08–17 Uhr Mo–Fr), 40 €/h Hauptzeit (Mo–Fr 17–22 Uhr und Sa/So), 42/60 € für 90 Minuten**. Alle als Schulmodell gekennzeichnet. [Vollständige Preisliste](14-angebote-und-preiskalkulation.md).
4. Angebote und Demo-Preise: **Rush Starter 29 €/Person, Rush Academy 45 €/Person, Rush Social 18 €/Person, Rush League 129 €/Person/Saison, Rush Tournament 35 €/Person, Rush Business 599 €/Gruppe, Rush Member 9,90 €/Monat** sowie Lounge. Alles fiktiv, nicht real buchbar.
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
- Preise, zeitabhängige 60/90-Minuten-Preise, Paketumfang und erlaubte Courtzeit stimmen mit [Angebotskalkulation](14-angebote-und-preiskalkulation.md) und Finanzmodell überein.
- Kein „Jetzt buchen“ vermittelt eine echte reservierbare Halle.
- Angaben über Standort, Eröffnung und Bildmaterial sind transparent.
