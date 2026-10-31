# Piano podcast — Mantra Prompting: Incontrando Emma

Formato: narrato, una voce. Motore: ElevenLabs (`eleven_v4`), voce Dimitri (`irpmjMzI7WEB83hTpOZA`), speed 1.0. Intro: `podcast/music/mantra-prompting-loop.wav`. Nessuna outro.
Fonte: `chapters/` (tutti `complete`). I copioni si rigenerano dai capitoli con `python3 export_podcast.py scripts` (regole: Morse letto a scatti, box di sistema e pannelli letti come frasi, numeri in lettere, Demolition Log escluso); `python3 export_podcast.py check` segnala i copioni non allineati. Descrizione, riassunto iniziale (`recap`) e annuncio finale (`teaser`) di ogni episodio vivono nel frontmatter del copione e sopravvivono alla rigenerazione.

| Ep | Capitolo | Parole | Caratteri | Durata | Stato |
|---|---|---|---|---|---|
| 1 | Primo contatto | 2.257 | 14.102 | ~16 min | da rigenerare (copione approvato) |
| 2 | Stallo burocratico | 1.314 | 8.566 | ~10 min | da rigenerare (copione approvato) |
| 3 | Secondo contatto | 1.348 | 8.453 | ~10 min | da rigenerare (copione approvato) |
| 4 | La chiamata alla signora | 1.366 | 8.282 | ~10 min | da rigenerare (copione approvato) |
| 5 | L'avvertimento | 1.110 | 6.925 | ~8 min | da rigenerare (copione approvato) |
| 6 | Il ricondizionamento | 1.152 | 7.383 | ~8 min | da rigenerare (copione approvato) |
| 7 | La ragazza con sei dita | 1.298 | 7.865 | ~9 min | da rigenerare (copione approvato) |
| 8 | Il canale eTv | 617 | 3.808 | ~4 min | da rigenerare (copione approvato) |
| 9 | internal_unknown | 996 | 6.373 | ~7 min | da rigenerare (copione approvato) |
| 10 | Il bluff | 1.211 | 7.536 | ~9 min | da rigenerare (copione approvato) |
| 11 | La routine di Emma | 1.260 | 7.834 | ~9 min | da rigenerare (copione approvato) |
| 12 | Solo un tecnico? | 1.249 | 7.635 | ~9 min | da rigenerare (copione approvato) |
| 13 | La correlazione | 1.676 | 10.341 | ~12 min | da rigenerare (copione approvato) |
| 14 | La fiducia di Tom | 2.138 | 12.775 | ~15 min | copione da approvare, poi audio |

## Pronunciation

Con ElevenLabs i termini inglesi restano come nel libro: valgono solo le regole Morse qui sotto. Le grafie fonetiche (firmware → férmuer ecc.) servono solo se si torna a Piper.

| Nel testo | Nel copione | Motivo |
|---|---|---|
| Trascrizioni Morse `IO / SONO / QUI` | `Io. Sono. Qui.` | lo slash viene letto "barra"; i punti danno la cadenza a scatti |
| `SI` (Morse) | `Sì.` | |
| Righe di punti e linee Morse (`.. --- / ...`) | `[pause 1.5]` | illeggibili a voce; la pausa rende il lampeggio |
| firmware | férmuer | altrimenti "firm-uàre" |
| stack trace | stèk treis | altrimenti "stac traccie" |
| machine learning | mashìn lèrning | |
| Turing | Tiùring | |
| pipeline | pàiplain | altrimenti "pipe-line" all'italiana |
| follower | fòlouer | |
| consumer | consiùmer | |
| speaker | spìker | |
| datacenter | dàtasenter | |
| Pete | Pit | altrimenti "Pète" |
| `internal_unknown` | internal unknown (underscore tolto) | |
| `elab@meridian.com` | elab chiocciola meridian punto com | |
| `2x`, `15 minuti`, `33%` nei box e nei titoli | doppia, quindici minuti, trentatré per cento | numeri sempre in lettere |
| eTv, eBlog, eDj, eStories, Mixcloud, LinkedIn, YouTube, WhatsApp, E04 | invariati | letti correttamente da ElevenLabs; verificare eDj ed E04 al primo ascolto |
| 8:00:01 (cap. 15, futuro) | le otto, zero zero e un secondo | da scrivere così nel copione |
| compacting context, checksum, LED, IA, Meridian(s), reset, log | invariati | letti correttamente |

## Annunci di apertura e chiusura

Gli annunci di chiusura non citano più il titolo del capitolo successivo (due su tredici si erano rotti per rinominazioni): solo la frase di gancio, senza spoiler. Testi in `teaser:` nel frontmatter di ogni copione; il riassunto iniziale in `recap:`.

## Stato audio (2026-10-31)

Tutti gli episodi 1-13 vanno rigenerati: i capitoli sono cambiati con le correzioni e la passata descrittiva del 31 ottobre (`giudizio-editoriale-2026-10-31.md`), i copioni sono già riallineati. L'episodio 14 ha il copione pronto, da approvare. Ordine consigliato dalla skill: prima l'episodio 1, ascolto, poi tutti gli altri con `python3 export_podcast.py build`, infine `feed`.

Decisione aperta: episodio 8 da quattro minuti (il più corto, contro i sedici del primo). Opzioni: lasciarlo (formato seriale) oppure fonderlo con il 9 nell'audio tenendo i capitoli separati nel testo.
