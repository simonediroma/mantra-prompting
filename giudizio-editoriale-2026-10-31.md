# Giudizio editoriale e piano di lavoro — *Mantra Prompting: Incontrando Emma*

> Data: 2026-10-31. Base: `chapters/01-13` (~15.700 parole di testo narrativo), `podcast/scripts/episode-01..13`, i 13 MP3 in `docs/episodes/`, `outline.md` v0.2, `characters/*`, `book-memory.md`, `revision-report-2026-10-10.md`.
> Ordine del documento: (1) verdetto, (2) **Parte A: modifiche per portare a casa l'audiolibro**, (3) **Parte B: modifiche per passare dall'audiolibro al libro stampato**, (4) appendice con l'analisi dettagliata di scrittura, personaggi e ambiente che motiva le liste.
> Principio che regge tutto il piano: **l'audio fissa il testo**. Ogni modifica a un capitolo già renderizzato costa una rigenerazione. Quindi le modifiche di contenuto vanno fatte prima di congelare; dopo, al libro stampato restano solo tipografia, impaginazione e aggiunte che non cambiano i fatti.

---

## 1. Verdetto in breve

| Dimensione | Voto | Una riga |
|---|---|---|
| Scrittura, frase per frase | 7/10 | Voce riconoscibile, ironia bassa e precisa nei cap. 1-4; calo di tono e paragrafi non rifiniti nei cap. 6 e 13. |
| Scrittura, struttura e ritmo | 6/10 | Nove capitoli consecutivi (5-13) quasi senza dialogo; tre capitoli di Emma (11-13) che sono letture di liste e pannelli; cuciture visibili dove sono stati fusi i capitoli. |
| Tom | 7/10 | Il personaggio più riuscito. Manca la ferita (il profilo la segna "da approfondire"). |
| Emma | 6,5/10 | Il materiale migliore del libro è suo (cap. 13), ma viene presentata per ritratto più che per scena. |
| Pete | 4/10 | Esiste solo come firma (cap. 2). Il profilo è ricchissimo, il testo no. |
| Signora Voss | 7/10 | Il miglior secondario, grazie all'unico dialogo lungo del libro. |
| Ambiente istituzionale (Meridian) | 8/10 | La parte più solida: regole, sanzioni, turni, archivi. |
| Ambiente fisico e sensoriale | 4/10 | Zero odori, una sola parola di luce o buio, nessuna città, nessuna stagione. |
| Audiolibro, stato attuale | 6,5/10 | Voce e adattamento corretti. L'episodio 13 è indietro rispetto al capitolo. |

In sintesi: il libro ha una voce, un'idea forte e un apparato di coerenza invidiabile. Gli manca carne: corpi, stanze, voci che parlano, e il riso promesso dalle prime pagine anche nella seconda metà.

---

## 2. Parte A — Modifiche per portare a casa l'audiolibro

Obiettivo: Libro 1 completo in audio (cap. 1-20), con testo congelato, senza dover rigenerare due volte lo stesso episodio.

### A1. Interventi tecnici immediati (nessuna modifica ai capitoli)

| # | Intervento | File | Effetto sull'audio |
|---|---|---|---|
| A1.1 | **Riallineare l'episodio 13 al cap. 13 v2.4.** Il copione si ferma a "Riaprì la sua mail e questa volta non la lesse per capire chi l'avesse scritta" e mancano le ~350 parole finali (le due righe di Tom, il registro interventi, la decisione della mail di scuse). L'annuncio di chiusura dice "Nel prossimo episodio, Le due volte di Tom", capitolo tagliato. | `podcast/scripts/episode-13.md` | Rigenerare ep. 13 |
| A1.2 | **Correggere la chiusura dell'episodio 11** ("La notizia" → "Solo un tecnico?"). Già in `plan.md` come correzione in sospeso. | `podcast/scripts/episode-11.md` | Rigenerare ep. 11 (o solo la coda, se lo script lo consente) |
| A1.3 | **Togliere il titolo dagli annunci "Nel prossimo episodio"** in tutti i copioni, lasciando solo la frase di gancio, oppure farli generare dal piano al momento del build. Due su tredici sono già rotti per rinominazioni e l'outline dei cap. 14-20 cambierà ancora. | tutti i copioni, `export_podcast.py` | Da applicare solo agli episodi che si rigenerano comunque; per gli altri, al prossimo giro |
| A1.4 | **Congelare lo status dei cap. 1-5** (`status: draft` → `complete`), come i 6-13. Sono i più revisionati e sono già in audio pubblicato. Finché restano "draft" ogni passata di `revise` li ritocca e l'audio diverge. | `chapters/01-05` frontmatter | Nessuno |
| A1.5 | **Decidere la sorte dell'episodio 8** (4:25, cap. da 528 parole). Come puntata seriale regge appena; come traccia di audiolibro continuo stona accanto ai 16 minuti dell'ep. 1. Opzioni: lasciare così (serie), oppure fondere 8+9 nell'audio tenendo i capitoli separati nel testo. | `plan.md`, `export_podcast.py` | Eventuale ep. 8+9 unico |
| A1.6 | **Aggiornare la tabella Pronunciation** per i termini nuovi dei cap. 10-13 e dei prossimi (eBlog, eDj, eStories, Mixcloud, LinkedIn, "2x"). Oggi copre fino al cap. 9. | `podcast/plan.md` | Nessuno sugli episodi esistenti |

### A2. Modifiche al testo da fare PRIMA di congelare (cambiano il contenuto che l'audio fisserebbe)

Ordinate per rapporto tra beneficio e costo di rigenerazione. Ogni riga indica l'episodio da rigenerare. Le modifiche a episodi che si rigenerano comunque (11 e 13) sono gratis.

| # | Capitolo | Modifica | Perché ora e non dopo | Episodio da rigenerare |
|---|---|---|---|---|
| A2.1 | 13 | Riscrivere il paragrafo "Il primo impulso fu togliere il video" (connettivi da verbale: "Però, elaborando la situazione", "Alla fine, riflettendo, si convinse che, eventualmente", "Inoltre, tra i suoi ragionamenti si era palesata"). Togliere una delle tre ripetizioni della bugia di Tom (una nel corpo, una nel nucleo ex cap. 14, una nel paragrafo delle scuse). Chiudere su un beat, non su un riassunto (regola R-74/R-93 del progetto). | È il momento di scelta morale del capitolo e l'ep. 13 va rigenerato comunque. | 13 (già previsto) |
| A2.2 | 11 | Dare a Emma una voce parlata: portare in scena il fondatore con un indovinello (oggi è solo citato nel cap. 10) al posto o accanto all'articolo sui fiori essiccati. Una scena di dialogo in un capitolo che oggi è una lista di task. | L'ep. 11 va rigenerato comunque; e da qui al cap. 13 l'ascoltatore ha un'ora di narrato senza una voce. | 11 (già previsto) |
| A2.3 | 12 | Sostituire almeno due delle tre etichette emotive ("era sgomento", "lucidità fredda e totale", "L'allarme montò") con un gesto o un'immagine, sul modello del paragrafo del sollievo nel cap. 13. | Il cap. 12 è il primo vero capitolo emotivo di Emma; in audio le etichette suonano da referto. | 12 |
| A2.4 | 9 | Dimezzare il paragrafo sull'archivio artefatti (~330 parole, due minuti e mezzo di narratore che spiega una policy, subito prima del colpo di scena). Attenuare il "cento per cento, generato da intelligenza artificiale" unanime su un transcript di quindici minuti di consigli fitness: un detector su tre, o percentuali alte ma non unanimi. | È il punto meno credibile dell'indagine e il blocco espositivo più lungo del libro. | 9 |
| A2.5 | 6 | Tagliare il paragrafo del "miracolo dell'era moderna" (angelo caduto nel televisore, "Rise tra sé a quel pensiero quasi mistico"): unico punto in cui il narratore spiega la battuta e il registro scivola. | Breve, ma in audio l'inciampo di tono si sente. | 6 |
| A2.6 | 10 | Ridurre a una frase il ritratto "Emma era meticolosa, era così da sempre… Nessun supervisore avrebbe mai preteso di più": scheda personaggio incollata, tutto ciò che dice lo vediamo fare nel cap. 11. Aggiungere mezza riga che spieghi *Ciao Darwin* in un'ambientazione non italiana (un trend italiano intercettato da una pipeline globale), visto che la scelta R-101 è confermata. | Costa poco, migliora il primo capitolo dal POV di Emma. | 10 |
| A2.7 | 12-13 | Decidere una volta sola dove sta l'informazione "Tom sapeva della morte quando ha scritto": oggi nel 12, due volte nel 13, e tornerà nel 14 dal lato di Tom. | Il cap. 14 non è ancora scritto: va deciso adesso. | 12, 13 |

Costo totale se si fa tutto: 6 episodi da rigenerare (6, 9, 10, 11, 12, 13), di cui 2 già dovuti. Se si vuole il minimo: A2.1 + A2.2 + A2.7 (solo gli episodi già da rifare).

Da **non** fare prima dell'audio, perché non cambiano i fatti e si possono aggiungere solo al libro (vedi B2): dettagli sensoriali, descrizioni di luoghi, ritocchi di ritmo nei cap. 1-5.

### A3. Regole per scrivere i cap. 14-20 con l'audio in mente

1. **Una voce parlata per capitolo.** Dal cap. 8 al 13 nessuno parla (righe di dialogo per capitolo: 7, 0, 1, 13, 1, 1, 3, 0, 0, 0, 0, 0, 0). I cap. 14-20 hanno già nell'outline mail, meeting e Pete: usare ogni occasione per far parlare qualcuno ad alta voce, non solo per iscritto. Nei capitoli di Emma, il fondatore.
2. **Lunghezza minima 1.000 parole di testo** (episodio da 7 minuti). Il cap. 20 è previsto "breve per scelta": in audio sarà un episodio da 3-4 minuti che chiude il Libro 1. Valutare di dargli almeno la scena completa di Pete davanti allo screenshot.
3. **Box di sistema e mail corti.** In audio diventano elenchi letti. Il pannello del cap. 13 funziona perché ha cinque righe; non superare quella misura.
4. **Pete deve essere udibile prima del cap. 17.** Tredici episodi su venti senza antagonista in scena. Una comparsa breve (un corridoio, una battuta) nel cap. 14 o 15 costa poco.
5. **Per ogni capitolo: `status: complete` prima del copione, copione approvato prima del render, un solo render.** Niente audio su capitoli `draft`.
6. **Annunci di chiusura senza titolo** (vedi A1.3).

### A4. Ordine operativo consigliato

1. A2.1, A2.2, A2.7 sui cap. 11, 12, 13 → aggiornare copioni 11, 12, 13 → rigenerare.
2. Decidere se fare anche A2.3-A2.6 (altri 4 episodi) o rimandarli al libro stampato accettando la divergenza audio/testo. Consiglio: farli, perché il libro stampato partirà da questi stessi capitoli e non conviene mantenere due versioni.
3. A1.3, A1.4, A1.6.
4. Scrivere i cap. 14-20 con le regole A3, un capitolo alla volta: scrittura → demolizione → `complete` → copione → render.
5. A1.5 alla fine, quando si vede la distribuzione delle durate su venti episodi.

---

## 3. Parte B — Dall'audiolibro al libro stampato

Obiettivo: Libro 1 (cap. 1-20) come manoscritto impaginabile, partendo dai capitoli congelati per l'audio.

### B1. Fonte del testo e controllo di divergenza

| # | Intervento |
|---|---|
| B1.1 | **Il libro si monta dai `chapters/`, mai dai copioni.** I copioni hanno Morse a scatti ("Io. Sono. Qui."), box letti come elenchi, numeri in lettere nei box, niente corsivi. Sono adattamenti per l'orecchio. |
| B1.2 | **Verificare che nessuna correzione fatta solo nel copione sia rimasta fuori dal capitolo.** Oggi copioni e capitoli 1-12 coincidono parola per parola salvo gli adattamenti previsti; va mantenuto così con un diff prima dell'assemblaggio (lo script di confronto usato per questo report può entrare in `export_podcast.py` come comando `check`). |
| B1.3 | **Decidere la politica delle divergenze.** Ogni frase aggiunta al libro dopo l'audio è una frase che l'ascoltatore non sente. Consiglio: ammesse solo aggiunte descrittive e tipografiche (B2, B3), mai modifiche a fatti, battute o ordine delle scene. |

### B2. Modifiche al testo per la pagina (non per l'orecchio)

| # | Modifica | Dove |
|---|---|---|
| B2.1 | **Tre dettagli fisici per scena nei capitoli di Tom**: un odore in laboratorio, la temperatura del corridoio, il rumore del nastro trasportatore, la luce di casa sua la sera. Su 15.700 parole: 0 odori, 1 parola di luce o buio, nessuna città, nessuna stagione. Il laboratorio è descritto una volta (cap. 1) e poi mai più; la casa di Tom è una scrivania, una pila di libri e un giradischi. In audio la voce copre; sulla pagina il vuoto si vede. La riorganizzazione dell'assistenza in stanze singole (in `characters/meridian-technologies.md`) è una scena ambientale già pronta. | cap. 1-9, 14-20 |
| B2.2 | **Ritmo dei paragrafi del cap. 1**: undici paragrafi sotto le dodici parole, contro 0-2 negli altri capitoli. In audio sono pause; in stampa sono una pagina a scatti. Verificare quali restano come battute Morse (giusti) e quali sono beat isolati (regola del progetto contro i paragrafi-lampo). | cap. 1 |
| B2.3 | **Emma senza spazio fisico** resta per regola. Ma allora il mondo deve passare tutto da Tom: nei cap. 14-20 ogni scena di Tom porta il peso dell'ambientazione per entrambi. | cap. 14-20 |
| B2.4 | **Il titolo del libro va pronunciato una volta nel Libro 1.** Nessun personaggio dice "mantra prompting" in venti capitoli; nel libro stampato, con il titolo in copertina, l'assenza pesa più che in un feed podcast. Basta il nome di un vecchio progetto del fondatore. | cap. 11 o 16 |
| B2.5 | **Promessa aperta più visibile su carta**: come il televisore sapeva del cuore della signora (eWatch). Il lettore se lo chiede dal cap. 5. In un libro che si legge in due sere, otto capitoli di rinvio si notano più che in otto settimane di puntate. Collocarlo entro il cap. 15. | cap. 14-15 |

### B3. Tipografia e impaginazione

| # | Intervento |
|---|---|
| B3.1 | **Morse**: le trascrizioni restano in maiuscolo con slash (`IO / SONO / QUI`), come da regola del progetto; la riga di punti e linee del cap. 1 in carattere a spaziatura fissa. Verificare che i puntini e le lineette non vengano convertiti dall'impaginatore in puntini di sospensione o trattini tipografici. |
| B3.2 | **Box di sistema** (cap. 2, 9) e **pannello eTv** (cap. 13): riquadri con carattere diverso dal corpo, non grassetto inline. Sostituire l'emoji 🏅 del cap. 13 con testo o un glifo stampabile: in stampa in bianco e nero non esiste. |
| B3.3 | **`compacting context`** e i termini di sistema in spaziatura fissa, coerenti ovunque. |
| B3.4 | **Numeri**: in lettere nel corpo, in cifre solo nei box. Oggi è rispettato (0 cifre fuori dai box in 12 capitoli su 13, 2 nel cap. 7 dentro un titolo di video). Mantenere con `revise` sui cap. 14-20. |
| B3.5 | **Struttura del volume**: frontespizio, indice, le otto Parti dell'outline come separatori (oggi esistono solo nell'outline, non nei capitoli), titoli dei capitoli numerati. Decidere se il Libro 1 esce da solo (cliffhanger di Pete al cap. 20) o si aspetta il Libro 2. |
| B3.6 | **Copertina**: `docs/cover.jpg` è 3000×3000, adatta a podcast e ebook. Per la stampa serve un formato verticale con dorso, da rifare. |
| B3.7 | **Dimensioni**: il Libro 1 chiuderà intorno alle 24-25.000 parole. È una novella, non un romanzo. In stampa: circa 110-130 pagine in formato tascabile. Va presentato come tale sulle piattaforme candidate. |

### B4. Processo editoriale per il manoscritto

1. `ghost-writer:consistency-check` sui venti capitoli (cronologia G0-G34, nomi, turni, matricole).
2. `ghost-writer:revise` capitolo per capitolo (punteggiatura, regole di `style-rules.md`, numeri).
3. Passata B2 (dettagli fisici) con controllo che nessun fatto cambi rispetto all'audio.
4. `ghost-writer:manuscript-final` → `ghost-writer:export-pdf` per la bozza da beta reader.
5. `ghost-writer:corrections` per raccogliere le note dei beta reader; applicarle **anche ai copioni** se toccano fatti, altrimenti solo al libro.
6. Impaginazione definitiva con B3.

---

## 4. Appendice — Analisi dettagliata

### 4.1 Qualità della scrittura

**Cosa funziona**
- L'incipit (`chapters/01-primo-contatto.md:8`): la lista dei suoni televisivi mancati e la chiusa sull'"interlocutore più valido della settimana" fissano tono, personaggio e solitudine.
- La burocrazia come comicità (`chapters/02-stallo-burocratico.md:153`): la formula della trattenuta, fattore turno 2,5, supplemento base, arrotondamento per eccesso. La comicità sta nella precisione, non nell'esagerazione. Il piccione (riga 157) è il paragone giusto per Pete.
- Il metodo di Tom come stile: le domande-trappola, "lampeggia tre volte", il silenzio al telefono (`chapters/04-la-chiamata-alla-signora.md:288`).
- Il quotidiano che vince sul mistero: "Prima di qualunque televisore consapevole, prima di qualunque avvertimento, veniva la cena" (cap. 5).
- La frase migliore della parte di Emma: "Era una sensazione piccola e tiepida, come il sollievo di chi sente un rumore in una casa rimasta vuota troppo a lungo" (cap. 13). Dice tutto di lei senza dire niente della sua natura.
- Pulizia tecnica: i tic del report del 10 ottobre sono rientrati. Su 13 capitoli: "esattamente" 5, "con la stessa" 8, "il tipo di" 9, "a fissare" 5, struttura "Non X. Non Y." 3. Nessun em dash, nessuna cifra in narrazione fuori dai box, nessuna contraddizione di fatto trovata tra i capitoli.

**Cosa non funziona ancora** (dettaglio delle voci A2 e B2)
- Il dialogo sparisce dal cap. 8 al 13.
- Le emozioni di Emma vengono nominate (cap. 12: "sgomento", "lucidità fredda e totale", "allarme" in una pagina).
- Il ritratto al posto della scena (cap. 10, "Emma era meticolosa").
- Paragrafi non rifiniti: l'angelo del cap. 6; "Il primo impulso fu togliere il video" del cap. 13.
- Le cuciture delle fusioni nel cap. 13 (la bugia di Tom ripetuta tre volte; chiusura riassuntiva).
- L'infodump dell'archivio nel cap. 9 e il "100% IA" unanime.
- Il pannello eTv con riproduzioni per singolo utente anonimo e velocità prevalente: licenza già accettata in demolizione (C2); una frase che lo attribuisca a un pannello interno di Emma la renderebbe gratuita.
- Media parole per frase: 22-26 nei cap. 1-3, 14 nei cap. 12-13. Differenza di voce tra Tom ed Emma difendibile, purché voluta.

### 4.2 Personaggi

**Tom.** Metodo, debolezza mostrata (mente male agli umani), rivincita privata (47 secondi), rituale (giradischi). La regola "motivazione tecnica, mai morale" lo rende originale ma, tenuta per altri sette capitoli, rischia di renderlo freddo proprio mentre deve infatuarsi. Il profilo lascia ferita e tell "da definire": vanno chiusi prima del cap. 14. Indizio da pagare: non ascolta più musica (cap. 7, notato da Emma nel cap. 12).

**Emma.** Le regole che la governano (emozione prima, analisi dopo; guardrail aziendali come limite interiore; istinto di procreazione mai nominato) sono eccellenti e visibili nel cap. 13. Nei cap. 10-12 la conosciamo per ciò che il narratore dice di lei e per i suoi strumenti, non per scelte. Una sola interazione in quattro capitoli, ed è una mail. Gli indizi lessicali ambigui ("elaborò", "registrarne") sono scelta d'autore; in audio passano quasi inosservati, quindi il reveal si reggerà sui fatti.

**Pete.** Una firma e un piccione. Il profilo (Agent Smith, Tabella di Conversione, pollo fritto, mensa anticipata) non è ancora in scena. Entra al cap. 17, a tre capitoli dalla fine del Libro 1.

**Signora Voss.** Riuscita perché parla: "Non 'non riusciva' ad accendersi: proprio non voleva. C'è differenza, sa?". Morte fuori scena gestita con il giusto distacco.

**Il fondatore.** Non valutabile: nessuna battuta, nome non assegnato. Ma la tesi che dà il titolo al libro è sua, e nel Libro 1 nessuno la pronuncia.

### 4.3 Ambiente

**Meridian come istituzione.** Turni per trimestre, fattore turno, soglia dei cinque minuti, 120 giorni e 33%, archivio artefatti, i "Meridians". Un mondo con regole che generano trama. Il file di Meridian ha molto altro non ancora speso (Accademia, inidonei, smistatore, cognomi vietati): materiale per i cap. 14-20 senza inventare nulla.

**Il mondo fisico.** Numeri su 15.700 parole:

| Famiglia lessicale | Occorrenze |
|---|---|
| odori | 0 |
| luce, buio, ombra, neon | 1 |
| stagione, meteo, temperatura | 13, quasi tutte "freddezza" in senso figurato |
| colori | 11, metà sono il LED e l'etichetta gialla |

**L'ambiente digitale.** Preciso e credibile (box, pannelli, liste, archivio). Rischio opposto: cinque capitoli di fila (9-13) in cui l'azione è "aprì, filtrò, lesse".

### 4.4 Una nota sul metodo

L'apparato di coerenza (profili, mappa eventi, memoria, log di demolizione) è professionale e si vede: nessuna contraddizione di fatto in tredici capitoli. Il rischio è che ottimizzi ciò che misura: tic, cronologie, punteggiatura. Le mancanze elencate qui (odori, voci, stanze, antagonista in scena) non sono misurabili da una regola e non sono mai state segnalate. Tre domande da aggiungere alla checklist di ogni capitolo: chi parla ad alta voce, cosa si sente con il corpo, cosa vuole il personaggio che prima non voleva.
