Rispondimi in italiano, con risposte brevi.

## Compito

Asciugare i capitoli del romanzo "Mantra Prompting" secondo il piano in `analisi-ritmo-2026-11-28.md`. È un lavoro di **solo taglio**: togliere quello che rallenta senza cambiare fatti, voce o trama. **Non** fondere capitoli, **non** rinumerare, **non** toccare il podcast: quelle sono fasi successive.

## Prima di cominciare

1. Allinea il branch a `main`. Se `analisi-ritmo-2026-11-28.md` non c'è, fai merge di `origin/claude/fondatore-many-shot-prompting-gl2wkm`.
2. Leggi per intero, in quest'ordine:
   - `analisi-ritmo-2026-11-28.md`: per ogni capitolo, cosa tagliare e quanto;
   - `style-guide.md`, `voice-reference.md`, `style-rules.md` (regole R1-R16 e convenzioni di punteggiatura; R8-R16 coincidono con i tagli dell'analisi: similitudini, chiose, spiegazioni, presentazioni ripetute, parola ripetuta);
   - `book.config.json → author_voice` (tone, register, rhythm, avoid).
3. Come modello guarda i capitoli 20 e 21, già asciugati (v2.2 e v1.3), e la voce "Asciugatura — 2026-11-27" nel loro Demolition Log.

## Il libro

È un libro unico: la divisione in Libro 1 e Libro 2 è abbandonata. Le note che parlano di "Libro 1/2" vanno lette come prima e seconda metà del libro.

## Regole di taglio

- **Si taglia, non si riscrive.** È la regola R6: togli la coda, l'inciso, la frase che ripete. Riscrivi solo quanto serve a ricucire la sintassi dopo il taglio, mai per "migliorare" una frase che resta.
- **Cosa tagliare per primo:**
  - il ragionamento esposto passo per passo, quando l'azione o la conclusione bastano;
  - la regola aziendale rispiegata, quando è già stata spiegata in un capitolo precedente: basta un rimando di mezza riga;
  - le similitudini in serie del tipo "come si guarda un componente…" o "come un tecnico che…": tienine al massimo una o due per capitolo, le migliori;
  - i commenti del narratore su ciò che la scena ha appena mostrato;
  - gli elenchi da tre o quattro voci, quando ne basta una;
  - le ripetizioni di "dodici anni", del liceo di Pete e delle "ginocchia in bocca" oltre la prima per capitolo.
- **Cosa non toccare:**
  - i dialoghi, salvo ridondanze evidenti;
  - le battute comiche che reggono;
  - le onomatopee previste (una o due per capitolo);
  - le mail, i box e le schermate di sistema;
  - la riparazione vera del capitolo (regola dell'autore: almeno una per capitolo).
- **Elementi da conservare perché ripresi più avanti** (elenco completo nella sezione 4 di `analisi-ritmo-2026-11-28.md`): Sardegna e nonni (7 → 22); sifone a *Ciao Darwin* (10); rinforzo lombare, fiori immortali, cover su eDj (11 → 22); aspirapolvere, microonde, altoparlante portoghese (14 → 16); Forte Prenestino e Autistici (22 → 25); lavanderia (22 → 25); *Dalla Mela* e stampante (22 → 24); bagno e vellutata (23 → 24); furgone, terzo scaffale, tenda a fiori (21 → 23, 24). Prima di togliere un dettaglio concreto, cercalo con grep nei capitoli successivi.
- **Rispetta sempre** R1-R16, nessun trattino lungo in narrazione, numeri in lettere nella narrazione, "mail" e mai "email".
- **Obiettivo di lunghezza:** quello indicato per ogni capitolo nell'analisi, con una tolleranza del 10%. Se per arrivarci dovresti togliere un fatto, fermati prima e dimmelo.

## Procedura, un capitolo alla volta

1. Leggi il capitolo per intero e conta le parole del testo, escluso il Demolition Log.
2. Proponimi i tagli come elenco breve: paragrafo, cosa togli, quante parole. Aggiungi le due o tre frasi ricucite, mostrate prima e dopo.
3. **Aspetta la mia approvazione.** Applica solo quello che approvo.
4. Applica i tagli, porta la `version` alla minor successiva, aggiorna `revised` e aggiungi al Demolition Log una voce "Asciugatura — AAAA-MM-GG (vX.Y)" come nei capitoli 20 e 21.
5. Se il taglio cambia un fatto citato in `summary` o `claim` del frontmatter, aggiornali.
6. Commit, un capitolo per commit, e push.
7. Dimmi le parole prima e dopo e passa al capitolo successivo.

## Ordine

1. **Cap. 20:** togli solo "come si fa con un telecomando che non risponde", che è già nel cap. 19.
2. **Cap. 22, 23, 24:** i più carichi.
   - Nel 22, prima di tagliare, chiedimi se la cella *What if* (Chernobyl) va tenuta corta o tolta.
   - Nel 23, chiedimi se spostare una parte del honeypot di Pankow nella telefonata con Maurice del cap. 24.
3. **Cap. 1-19, a coppie** secondo la futura fusione: 1, 2-3, 4-5, 6-7, 8-9, 10-11, 12-13, poi 14-19 uno alla volta. Per le coppie, asciuga i due capitoli separatamente ma tenendo presente che verranno cuciti.
4. **Cap. 25:** taglio leggero. **Cap. 26:** non si tocca.

## Da non fare

- Non modificare file in `docs/episodes/`, `podcast/` o il feed.
- Non fondere né rinumerare capitoli.
- Non aprire pull request.
