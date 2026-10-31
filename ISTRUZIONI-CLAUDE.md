# Istruzioni per Claude Code — podcast di "Mantra Prompting"

Obiettivo: trasformare i capitoli di questo libro in episodi podcast **narrati** (una voce), un episodio per capitolo, con la base musicale già pronta come intro. Rispondi all'autore in italiano.

La procedura completa è nella skill `.claude/skills/podcast/SKILL.md` (comando `/podcast`): **leggila tutta e seguila**. Qui sotto le decisioni già prese e i passi specifici di questo kit.

## Decisioni già prese (non richiederle)

- Formato: narrato, una sola voce. Niente voci per personaggi salvo richiesta esplicita.
- Intro: `podcast/music/mantra-prompting-loop.wav`, già generata (grime-loop, seed 1, 150 BPM, strumenti a 0.25). **Non rigenerarla.** Nessuna outro.
- Solo strumenti gratuiti e open source: Piper TTS + ffmpeg. Nessun servizio a pagamento, nessuna API key.

## Passi

1. **Verifica il progetto**: `book.config.json` e i capitoli (`chapters/`, o `manuscript/*-final.md` se esiste). Se il manoscritto finale esiste, usa quello. Se non trovi i capitoli, chiedi all'autore dove sono.

2. **Dipendenze**:
   ```bash
   python3 -m pip install piper-tts numpy
   ffmpeg -version
   ```
   Se ffmpeg manca, dai all'autore il comando per il suo sistema e aspetta.

3. **Config**: aggiungi a `book.config.json` la sezione `podcast` **senza toccare le altre chiavi** (se esiste già, aggiorna solo questi campi):
   ```json
   "podcast": {
     "voice": "it_IT-paola-medium",
     "speaker": null,
     "speed": 1.0,
     "sentence_pause": 0.35,
     "paragraph_pause": 0.9,
     "voices": {},
     "intro_music": "podcast/music/mantra-prompting-loop.wav",
     "outro_music": null,
     "intro_overlap": 1.5,
     "bitrate": "96k",
     "base_url": ""
   }
   ```

4. **Voce** (skill, step 1a): prendi 2-3 frasi dal primo capitolo e genera i campioni:
   ```bash
   python3 export_podcast.py sample it_IT-paola-medium it_IT-riccardo-x_low --text "…frasi del libro…"
   ```
   Fai ascoltare `podcast/samples/*.mp3`, fai scegliere voce e velocità (`speed` 0.9–1.1), salva in config.
   Se il download della voce fallisce per la rete (huggingface.co bloccato), dillo subito all'autore: puoi comunque preparare piano e copioni, l'audio lo genererà sul suo computer con `python3 export_podcast.py build`.

5. **Piano episodi** (skill, step 2) → `podcast/plan.md`, conferma dell'autore.

6. **Copioni** (skill, step 3), uno alla volta, in `podcast/scripts/episode-NN.md`. Il libro parla di prompting: attenzione a sigle e termini tecnici (es. "LLM" → "elle elle emme", "ChatGPT" → "Ciat Gi Pi Ti", "prompt" resta "prompt", codice e prompt di esempio vanno letti in modo naturale o descritti). Annota le scelte di pronuncia in `podcast/plan.md → ## Pronunciation` e applicale a tutti i copioni. Mostra all'autore apertura, chiusura e lista delle modifiche; procedi solo dopo l'approvazione.

7. **Audio** (skill, step 4):
   ```bash
   python3 export_podcast.py build episode-01.md
   ```
   Genera **prima solo l'episodio 1** e chiedi all'autore di ascoltarlo (voce, pronunce, volume della base sotto la voce). Poi tutti gli altri: `python3 export_podcast.py build`.

8. **Feed** (facoltativo, skill step 5): `python3 export_podcast.py feed` dopo aver chiesto `base_url`.

## Copioni dai capitoli (aggiunto il 2026-10-31)

- `python3 export_podcast.py scripts [NN...]` rigenera i copioni dai capitoli con le regole di adattamento del progetto, conservando `description`, `recap`, `teaser` e `status` del frontmatter di ogni copione.
- `python3 export_podcast.py check` fallisce se un copione non è allineato al suo capitolo: lanciarlo prima di ogni `build` e prima di assemblare il libro.
- Gli annunci di chiusura non citano il titolo del capitolo successivo.

## Regole

- Non modificare mai i file in `chapters/` o `manuscript/`.
- Nessun audio prima dell'approvazione del copione.
- Non scaricare musica o campioni da altre fonti.
