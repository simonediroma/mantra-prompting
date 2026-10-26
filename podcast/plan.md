# Piano podcast — Mantra Prompting: Incontrando Emma

Formato: narrato, una voce. Motore: ElevenLabs (`eleven_v4`), voce Dimitri (`irpmjMzI7WEB83hTpOZA`), speed 1.0. Intro: `podcast/music/mantra-prompting-loop.wav`. Nessuna outro.
Fonte: `chapters/` (cap. 1-5 ancora in `draft`). Sezioni `## Demolition Log` escluse dai copioni.

| Ep | Capitolo | Parole | Caratteri | Durata | Stato |
|---|---|---|---|---|---|
| 1 | Primo contatto | 2.381 | 14.888 | ~16 min | rendered |
| 2 | Stallo burocratico | 1.274 | 8.330 | ~8 min | rendered |
| 3 | Secondo contatto | 1.216 | 7.697 | ~8 min | rendered |
| 4 | La chiamata alla signora | 1.316 | 8.025 | ~9 min | rendered |
| 5 | L'avvertimento | 1.047 | 6.602 | ~7 min | rendered |
| 6 | Il ricondizionamento | 1.135 | 7.311 | ~8 min | rendered |
| 7 | La ragazza con sei dita | 1.252 | 7.605 | ~8 min | rendered |
| 8 | Il canale eTv | 588 | 3.653 | ~4 min | rendered |
| 9 | internal_unknown | 1.085 | 7.123 | ~7 min | rendered |
| 10 | Il bluff | 1.124 | 6.960 | ~7 min | rendered |
| 11 | La routine di Emma | 1.001 | 6.310 | ~7 min | rendered |
| 12 | Solo un tecnico? (fusione ex 12 + ex 13) | 1.190 | 7.296 | ~9 min | rendered |

## Sound effects

Onomatopee inserite nella prosa e riprese come effetti nell'episodio. Valutazione un punto alla volta (proposta iniziale: 20 punti). Gli effetti si applicano ai copioni quando `export_podcast.py` supporterà il tag `[sfx …]`.

| # | Cap | Punto | Prosa | Podcast | Stato |
|---|---|---|---|---|---|
| 1 | 1 | Ronzio dell'alimentatore | *mmmmm* continuo | ronzio elettrico basso dopo la sigla, sotto i primi tre paragrafi, poi sfuma | approvato |
| 2 | 1 | Messaggi Morse del LED | Tom segue il ritmo con l'indice, *tic tic, tac tac tac* (= IO) | bip Morse reali e lenti, codificati sul messaggio, prima di ogni trascrizione letta: IO SONO QUI ×2, SI, NON LO SO ×2 (sostituiscono `[pause 1.5]`); tre bip uguali per «lampeggia tre volte» | approvato |
| 3 | 1 | Spegnimento del LED (*tic* del relè) | — | — | scartato |
| 4 | 2 | Accordo del terminale | *din-don-dan* | tre note ascendenti, allegre da jingle aziendale (sintetizzate), subito dopo il titolo, prima della voce | approvato |
| 5 | 3 | Cronometro dell'eWatch | Tom lo ferma, *bip* | bip singolo corto e acuto da orologio digitale (sintetizzato); riusabile quando Tom si cronometra | approvato |
| 6 | 3 | Morse NO SONO QUI CON TE ×2 | invariata | bip Morse come al cap. 1, prima di entrambe le trascrizioni | approvato |

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
| `internal_unknown` | internal anknoun (da verificare al cap. 9) | |
| compacting context, checksum, LED, IA, Meridian(s), reset, log | invariati | letti correttamente |
