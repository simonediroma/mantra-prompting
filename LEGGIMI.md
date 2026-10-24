# Kit podcast — Mantra Prompting

Trasforma i capitoli del libro in episodi podcast narrati, con la base grime già pronta come intro.
Gratis e open source: Piper (voce, offline) + ffmpeg. Non serve aggiornare il plugin ghost-writer.

## Come si usa

1. **Estrai lo zip nella cartella del libro**, quella che contiene `book.config.json` e `chapters/`.
   Ti ritrovi:
   ```
   export_podcast.py                    ← script audio
   .claude/skills/podcast/SKILL.md      ← la skill per Claude Code
   podcast/music/mantra-prompting-loop.wav  ← base grime 150 BPM, strumenti 0.25
   ISTRUZIONI-CLAUDE.md                 ← cosa deve fare Claude
   ```
2. **Apri Claude Code in quella cartella** e incolla questo messaggio:

   > Leggi ISTRUZIONI-CLAUDE.md e seguile per creare il podcast del libro.

3. Claude ti guida: installa le dipendenze, ti fa ascoltare le voci, propone gli episodi, ti mostra ogni copione da approvare e poi genera gli MP3 in `podcast/episodes/`.

## Requisiti

- Python 3.9+ e ffmpeg (`brew install ffmpeg` su Mac · `winget install ffmpeg` su Windows · `apt install ffmpeg` su Linux)
- Internet solo la prima volta, per scaricare la voce (~60 MB da huggingface.co). Poi funziona offline.
- Se usi Claude Code **sul web** (sessione cloud) e huggingface.co è bloccato dalla rete dell'ambiente,
  i copioni si possono fare lì ma l'audio va generato sul tuo computer: `python3 export_podcast.py build`.

## I capitoli originali non vengono mai modificati

I copioni adattati per l'ascolto stanno in `podcast/scripts/`.
