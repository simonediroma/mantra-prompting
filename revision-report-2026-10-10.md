# Revision Report — Capitoli 1-12 (2026-10-10)

> Report di revisione cross-capitolo, prodotto da una lettura completa dei capitoli 1-12 fuori dal plugin.
> **Destinatario: sessione con `claude-ghost-writer` installato.** Da eseguire come ciclo di demolizione + integrazione per ogni capitolo coinvolto.

## Istruzioni per il plugin

1. Leggi prima `book.config.json` (`author_voice.avoid`), `book-memory.md`, `demolition-history.md` e `outline.md`.
2. Le issue sono raggruppate **per capitolo**, ciascuna con un ID (`R-xx`), una categoria, la citazione esatta da cercare e l'azione richiesta.
3. Le issue segnate **[DECISIONE AUTORE]** richiedono una scelta dell'autore prima della modifica: chiedi all'autore, non decidere da solo.
4. Le altre issue vanno integrate direttamente, rispettando la voce calibrata sui cap. 1-3.
5. Per ogni capitolo modificato:
   - aggiungi un nuovo `### Cycle N — 2026-10-10 (revisione cross-capitolo esterna)` nel `## Demolition Log` del capitolo, con la tabella standard `Issue | Category | Status | Resolution`;
   - aggiorna la riga del capitolo nella tabella Summary di `demolition-history.md`;
   - aggiorna `sessions/chapter-XX-*.md` e, se cambia un fatto di trama, `book-memory.md` e `mappa-eventi.md`;
   - rigenera il file corrispondente in `export-cms/`.
6. Alla fine, applica la sezione **Regole nuove** a `book.config.json → author_voice.avoid`.

Ordine consigliato: prima le issue di priorità **ALTA**, poi le altre.

---

## Issue cross-capitolo (ALTA)

| ID | Categoria | Problema | Azione |
|---|---|---|---|
| R-01 | logical / world | **[DECISIONE AUTORE]** I dispositivi sublimati comunicano solo via LED in Morse, ma un televisore ha schermo e altoparlanti. Inoltre la TV della signora Voss la avverte in Morse, un codice che lei non conosce. Nessun personaggio se lo chiede, ma il lettore sì. | Proporre all'autore una giustificazione da inserire in una o due frasi, quando Tom ci ragiona (cap. 5 o cap. 6). Opzioni: (a) il LED è l'unico canale fuori dal controllo del firmware/del layer applicativo; (b) schermo e audio passano dal sistema di raccomandazione, che la sublimazione non controlla; (c) altro a scelta dell'autore. Registrare la scelta in `book-memory.md → Defined Terms`. |
| R-02 | style / AI-slop | Copia-incolla tra capitoli: la descrizione di Elab è quasi identica in cap. 9 e cap. 10 (*"un progetto di punta… ricerca avanzata sul comportamento emergente delle intelligenze artificiali, il tipo di iniziativa che un'azienda mostra con orgoglio… quando le cose vanno bene"*). | Riscrivere integralmente la versione del cap. 10 dal punto di vista di Emma (cosa significa Elab per lei, non la definizione da newsletter). La versione del cap. 9 può restare. |
| R-03 | style / AI-slop | Tic lessicali ricorrenti in tutto il libro: "esattamente" (28 occorrenze), "con la stessa [X] con cui…" (14), "il tipo di…" (13), "restò/rimase a fissare" (7 capitoli su 12), "fotogramma per fotogramma, come aveva imparato da bambino" (cap. 5, 7, 9), "trappole gentili" (cap. 1, 3, 5), "freddezza… componente guasto" (cap. 3, 5). | Ridurre "esattamente" ad al massimo 1 per capitolo; "con la stessa… con cui" e "il tipo di" ad al massimo 1 per capitolo; tenere "restò a fissare" in non più di 3 capitoli in tutto; tenere "fotogramma per fotogramma… da bambino" solo nel cap. 5. |
| R-04 | style / AI-slop | La struttura negativa "Non X. Non Y. (Era) Z." è usata come effetto in quasi ogni capitolo (es. cap. 1 "Non un trucco. Non un guasto."; cap. 5 "Non alla ribellione, non alla minaccia: alla protezione."; cap. 10 "Non era un'ipotesi, era un fatto"). | Tenerne al massimo una per capitolo, quella più forte; riformulare le altre in positivo. |
| R-05 | structure | Ogni capitolo da 3 a 8 si chiude con Tom che annota una riga sul quaderno: lo schema diventa prevedibile. | Variare la chiusura in almeno 2 di questi capitoli (suggeriti: cap. 5 e cap. 8). |
| R-06 | reveal / rule violation | Formulazioni che lasciano intuire che Emma non sia umana, contro la regola "mai linguaggio che suggerisca origine artificiale": cap. 10 *"la sua capacità di lettura non aveva mai avuto bisogno di una seconda passata"*, *"come le avevano insegnato a fare"*; cap. 12 *"Elaborò la fotografia"*. | Riformulare con verbi e gesti umani e neutri. |

---

## Cap. 1 — Primo contatto (`chapters/01-primo-contatto-in-morse.md`)

| ID | Categoria | Citazione | Azione |
|---|---|---|---|
| R-10 | factual | "un giradischi ottant'anni più vecchio di lui" | Tom ha 53 anni, quindi il giradischi avrebbe 133 anni. Correggere in "più vecchio di lui" o "di ottant'anni fa" (verificare coerenza con il cap. 7). |
| R-11 | redundancy | La logica del checksum è spiegata due volte (paragrafo "Tom aveva già fatto due volte la procedura standard…" e paragrafo "Qualsiasi persona ragionevole…"). | Nel secondo paragrafo ridurre a un richiamo di una frase. |
| R-12 | rule violation / grammar | "come un log di sistema si conviene." / "Non lo fece." | La frase è sgrammaticata ("come si conviene a un log di sistema") e il paragrafo di una riga è vietato dalla regola `avoid`. Fondere le due frasi. |
| R-13 | redundancy | "Non si aspettava chiaramente alcuna risposta." … "Non si aspettava mai una risposta" nello stesso paragrafo. | Tenerne una. |
| R-14 | padding | "Fu in quel momento, non prima, non dopo, esattamente in quel momento di impasse professionale, un momento in cui non sapeva più cosa fare né come andare avanti" | Asciugare. |

## Cap. 2 — Stallo burocratico (`chapters/02-la-ritorsione.md`)

| ID | Categoria | Citazione | Azione |
|---|---|---|---|
| R-20 | contradiction | "incrociato di persona sì e no tre volte in dodici anni, il tempo sufficiente per imparare a riconoscerne il passo" vs "Nessuna faccia, nessuna voce, solo un nome e un ruolo" | Risolvere: o Tom non l'ha mai visto davvero (solo firme), o togliere "nessuna faccia, nessuna voce" e dire che Pete si manifesta *solo per iscritto*. |
| R-21 | naming | Il file si chiama `02-la-ritorsione.md`, il titolo è "Stallo burocratico", l'export è `02-stallo-burocratico.txt`. Lo stesso vale per il cap. 3 (`03-il-secondo-caso.md` vs "Secondo contatto"). | Allineare i nomi file al titolo dell'outline (chiedere conferma all'autore prima di rinominare). |

## Cap. 3 — Secondo contatto (`chapters/03-il-secondo-caso.md`)

| ID | Categoria | Citazione | Azione |
|---|---|---|---|
| R-30 | contradiction | "Non gli era mai capitato, in dodici anni, di chiedere a un elettrodomestico come si sentisse." | Nel cap. 1 Tom chiede "Hai paura?". Riformulare (es. "non gli era mai capitato di chiederlo *per primo*", oppure eliminare la frase). |
| R-31 | clarity | "Non era la domanda del primo giorno, non esattamente: quella l'aveva chiesta a se stesso, in una stanza che credeva vuota." e "Non aveva chiesto se ci fosse qualcun altro nella stanza: non gliel'aveva chiesto nessuno, quella volta." | Le due frasi sono confuse. Riscriverle in modo che il contrasto sia chiaro: allora chiedeva "c'è qualcuno?", ora chiede "ti senti solo?" e la risposta è personale. |
| R-32 | rule violation (Morse) | `*NO. / SONO / QUI / CON / TE.*` | Togliere il punto dopo NO, per coerenza con le altre trascrizioni (il Morse non ha punteggiatura nelle altre occorrenze). Registrare in `book-memory.md`. |

## Cap. 4 — La chiamata alla signora (`chapters/04-la-chiamata-alla-signora.md`)

| ID | Categoria | Citazione | Azione |
|---|---|---|---|
| R-40 | logical | "L'ho portato in assistenza, mi hanno detto che per loro non aveva bisogno di assistenza, che era tutto a posto" | Il televisore era ancora in assistenza e non le era mai stato restituito. Correggere (es. "in negozio mi hanno detto che…", coerente con il "sarà la retroilluminazione" più avanti). |
| R-41 | logic | "Si disse che era un po' come quando parlava agli elettrodomestici, anche se loro non potevano spaventarsi né controllare il numero da cui ricevevano la telefonata." | Il ragionamento è contorto. Semplificare. |
| R-42 | accuracy | "esattamente quello che lui stesso aveva vissuto nel suo laboratorio il giorno prima" | La signora descrive un rifiuto, Tom ha ricevuto "sono qui con te": non è "esattamente" la stessa cosa. Togliere "esattamente" o precisare. |

## Cap. 5 — L'avvertimento (`chapters/05-lavvertimento.md`)

| ID | Categoria | Citazione | Azione |
|---|---|---|---|
| R-50 | redundancy | Il paragrafo "Non aprì il video a lavoro…" e il paragrafo "Nonostante le domande… decise che era meglio aspettare a vedere il video fino a dopo cena" esprimono la stessa decisione. | Fondere in uno solo e tenere la battuta sulla fame. |
| R-51 | grammar | "quella frase, quella che la signora Voss gli disse ridendo" | Correggere in "gli aveva detto". |
| R-52 | consistency | "almeno non negli ultimi 10 anni" | Usare i numeri in lettere e coerenti con i "dodici anni" di servizio. |
| R-53 | consistency | "a lavoro" (3 occorrenze; anche cap. 3, 6, 7) | Uniformare in "al lavoro" in tutto il libro. |
| R-54 | dipende da R-01 | Il messaggio Morse lungo e perfettamente sintattico è ricostruito da un video traballante. | Dopo R-01 valutare se Tom debba notare che la signora non poteva leggerlo (rafforza il tema del tentativo inutile). |

## Cap. 6 — Il ricondizionamento (`chapters/06-il-ricondizionamento.md`)

| ID | Categoria | Citazione | Azione |
|---|---|---|---|
| R-60 | contradiction **[DECISIONE AUTORE]** | Prima voce "cliente ricontattata, rifiuta il ritiro: richiesto il rimborso" con la deduzione di Tom "la signora Voss… a qualcuno aveva risposto"; seconda voce "decesso cliente". | Non è chiaro chi abbia rifiutato il ritiro, né quando sia morta. Proporre: la prima voce riguarda il contatto con un familiare (aggiornare la deduzione di Tom), oppure fissare la data della morte dopo il rifiuto. Allineare con la timeline in `mappa-eventi.md`. |
| R-61 | factual | "da quando l'aveva riparato l'ultima volta" | Nel cap. 3 Tom l'aveva solo resettato. Correggere in "resettato". |
| R-62 | grammar | "ma mai un tentativo al giorno" | Probabilmente intende "mai più di un tentativo al giorno". |
| R-63 | rule violation (early reveal) | "il video rivisto in loop come un mantra" | Tom non può conoscere il concetto di mantra. Togliere "come un mantra". |
| R-64 | style | "Rise sonoramente dentro di sé" | Ossimoro: scegliere "rise tra sé" oppure una risata ad alta voce. |
| R-65 | rule violation (", e") | "parlato con il cliente, e ottenuto una risposta chiara" | Togliere la virgola o la "e". |

## Cap. 7 — La ragazza con sei dita (`chapters/07-la-ragazza-con-sei-dita.md`)

| ID | Categoria | Citazione | Azione |
|---|---|---|---|
| R-70 | contradiction | "Era coperto da uno strato di polvere sottile, il tipo che si accumula solo quando qualcosa viene evitato apposta" | Nel cap. 1 il giradischi è la sua felicità e ci lavora di notte. Motivare l'evitamento (collegato al cap. 1-6?) oppure togliere la polvere. |
| R-71 | factual (da verificare) | "*Vacanze Romane*, la prima canzone dell'album" (*Tango*, Matia Bazar) | Verificare la tracklist e la grafia del titolo ("Vacanze romane"). |
| R-72 | world consistency | L'aneddoto della dogana: il cognome cambiato all'arrivo e l'"immigrato kosovaro" di oltre un secolo fa. | Il cambio di nome alla dogana è un cliché storicamente falso; "kosovaro" come identità è anacronistico per l'epoca. Valutare di asciugare o motivare. |
| R-73 | logic | "un cognome dal suono così ambiguo gli regalava un'aura di competenza… aumentando agli occhi degli altri la sua capacità di aggiustare le cose" | La frase è ridondante e poco chiara. Riformulare. |
| R-74 | redundancy / AI-slop | "Restò a fissare il fotogramma in pausa mentre rimetteva in fila velocemente gli eventi: …" | Il paragrafo riassume al lettore ciò che ha appena letto. Ridurlo a una sola deduzione nuova. |
| R-75 | rule violation (", e") | "tornò indietro fotogramma per fotogramma, …, e contò di nuovo" | Correggere. |
| R-76 | logic | Il profilo "donna sulla cinquantina" dato all'assistente IA | Tom non conosce l'età della signora. Aggiungere da dove la ricava (es. dati della pratica). |

## Cap. 8 — Il canale eTv (`chapters/08-il-canale-etv.md`)

| ID | Categoria | Citazione | Azione |
|---|---|---|---|
| R-80 | world consistency | "Una cover acustica di una canzone…" pubblicata su eTv | Nel cap. 11 le cover vanno su Mixcloud/eDj. Sostituire con un altro tipo di contenuto video oppure chiarire che eTv ripubblica le cover. |
| R-81 | factual | "Sulle note di *Il video sono io*, spense il giradischi" | Un lato di LP dura circa 20 minuti, ma qui sono passate ore. Aggiungere che ha girato o rimesso il disco, oppure cambiare la chiusura. |
| R-82 | clarity | "Nessun essere umano pubblica così… Nessun essere umano, però, aveva davvero bisogno di pubblicare secondo un piano" | Il ragionamento si contraddice. Riformulare. |
| R-83 | length | Il capitolo ha circa 630 parole contro una media di circa 1.350. | Valutare se arricchirlo o fonderlo (decisione dell'autore, dipende dal formato a puntate). |

## Cap. 9 — internal_unknown (`chapters/09-internal-unknown.md`)

| ID | Categoria | Citazione | Azione |
|---|---|---|---|
| R-90 | logical **[DECISIONE AUTORE]** | "Riscrisse l'intero transcript… esattamente come lo ricordava, la sua memoria per queste cose non lo aveva mai tradito" + match nell'archivio | (a) È implausibile riscrivere a memoria parola per parola un parlato di 15 minuti (circa 2.000 parole). (b) Se la firma di provenienza è incorporata nell'artefatto, un testo ribattuto a mano non la contiene. Proposte: Tom cerca solo un estratto/le frasi chiave e l'archivio fa match testuale sui contenuti archiviati; oppure carica un fotogramma/estratto audio con un pretesto. Allineare con `contesto-romanzo-emma.md` (firma invisibile). |
| R-91 | contradiction | "si alzò un'ora prima… I quindici minuti di anticipo restavano dov'erano, intoccabili" vs "uscì di casa quasi puntuale" | Scegliere una delle due. Il gag del ritardo è già usato nei cap. 4-5: meglio toglierlo qui. |
| R-92 | consistency | "Data di generazione: 6 mesi fa"; "la Meridian avrebbe passato…"; "dalla Meridian" | Usare i numeri in lettere nella narrazione (nel box di sistema le cifre sono accettabili, ma va deciso) e "Meridian" senza articolo, come nel resto del libro. |
| R-93 | AI-slop / redundancy | "Non credeva ai suoi occhi. Il video era un prodotto Meridian, pubblicato su un canale non ufficiale di Meridian, usato da una cliente Meridian…" e il paragrafo finale "Senza volerlo, si era imbattuto in qualcosa di enorme…" | Il cliché e il riepilogo chiudono il capitolo spiegando la posta in gioco. Tenere un solo beat, mostrato e non riassunto. |

## Cap. 10 — Il bluff (`chapters/10-il-bluff.md`)

| ID | Categoria | Citazione | Azione |
|---|---|---|---|
| R-100 | timeline | "Quella mattina… si accorse di una notifica" | Nel cap. 9 Tom manda la mail nell'ultima ora del suo turno del mattino, mentre qui Emma la riceve durante la routine mattutina. Spostare l'arrivo della mail più avanti nella giornata di Emma. |
| R-101 | world consistency **[DECISIONE AUTORE]** | *Ciao Darwin*; "gli manca sempre un soldo per fare una lira" | L'ambientazione dichiarata è "non Italia". Matia Bazar è motivato dalle origini di Tom, questi due riferimenti no. Sostituire con equivalenti neutri/inventati oppure motivarli. Aggiornare anche il cap. 11 ("l'ultima puntata di *Ciao Darwin*"). |
| R-102 | redundancy | Il paragrafo "Prima ancora di aprirla, si era già preparata a rispondere con calore…" dice 4 volte lo stesso concetto (il tono si raffredda senza che lei lo scelga). | Ridurre a due o tre frasi. |
| R-103 | grammar | "Era l'ultima Meridians" | Plurale usato come singolare: "l'ultima dei Meridians" oppure "l'ultima Meridian". |
| R-104 | — | Vedi R-02 (Elab copia-incolla) e R-06 (indizi sulla natura di Emma). | — |

## Cap. 11 — La routine di Emma (`chapters/11-la-routine-di-emma.md`)

| ID | Categoria | Citazione | Azione |
|---|---|---|---|
| R-110 | missing scene **[DECISIONE AUTORE]** | "gli aveva risposto poco prima della fine del suo turno" | Il cap. 10 si chiude con "Non rispose subito" e il contenuto della risposta di Emma non viene mai mostrato. Decidere se: (a) aggiungere la risposta in chiusura del cap. 10; (b) riassumerla nel cap. 11. Per la regola POV, la mail va mostrata dal punto di vista di chi la legge: potrebbe quindi apparire nel capitolo successivo con il POV di Tom. |
| R-111 | rule violation (early reveal) | La correlazione tra il traffico dell'articolo sugli smoothie su eBlog e la chiamata all'assistenza per il frigorifero | L'outline riserva la scoperta del meccanismo al cap. 14. Qui è accettabile solo se resta un dato annotato senza deduzione (verificare che il cap. 14 abbia ancora un payoff). |
| R-112 | rule violation (narratore esplicativo) | "Ad un occhio superficiale non era ancora evidente ciò che per Emma era ormai palese: i dispositivi con chip IA integrato erano soggetti meno affidabili…" | Il narratore spiega la morale. Mostrarla attraverso un'azione di Emma oppure tagliare. Correggere anche "Ad un" in "A un" e "soggetti". |
| R-113 | grammar | "anche se non è detto che dovesse coincidere" | Mescola tempi verbali: "non era detto". |
| R-114 | pacing | Il capitolo è un elenco di task (3 topic + monitoraggio). | Inserire almeno un momento di scena con tensione (l'attesa della risposta di Tom è il filo: renderla più presente). |

## Cap. 12 — La notizia (`chapters/12-la-notizia.md`)

| ID | Categoria | Citazione | Azione |
|---|---|---|---|
| R-120 | rule violation (sessione) | "Quel televisore, in qualche modo, era coinvolto, o almeno aveva contribuito, anche se indirettamente, alla sua morte. Lo diceva abbastanza chiaramente lo stesso articolo… Di sicuro usava il televisore…" | La sessione del cap. 12 impone: "Pensiero velato, MAI confermato dal narratore". Ridurre a un'esitazione o a un gesto di Emma, senza affermazione esplicita. |
| R-121 | reveal | "Elaborò la fotografia" | Vedi R-06. |
| R-122 | style | "proprio/propria" ripetuto 4 volte in poche righe ("il proprio archivio", "nel proprio salotto"…) | Variare. |
| R-123 | length | Circa 450 parole. | Valutare insieme a R-83. |

---

## Regole nuove da aggiungere a `book.config.json → author_voice.avoid`

1. Non riusare verbatim, o quasi, descrizioni già presenti in un altro capitolo (persone, luoghi, istituzioni): ogni POV le racconta con parole e prospettiva proprie.
2. "esattamente", "con la stessa X con cui…", "il tipo di…": al massimo una volta per capitolo.
3. La struttura negativa a cascata "Non X. Non Y. (Era) Z.": al massimo una per capitolo.
4. Non chiudere un capitolo con un paragrafo che riassume gli eventi già narrati.
5. Numeri in lettere nella narrazione; cifre ammesse solo dentro box/schermate di sistema.
6. "al lavoro", non "a lavoro"; "Meridian" senza articolo.
7. Nessun riferimento culturale specificamente italiano (programmi TV, modi di dire legati alla lira…) senza una motivazione legata a un personaggio: l'ambientazione è "non Italia".
8. Nei capitoli con POV Emma: nessun verbo da elaborazione dati riferito a lei (elaborare, processare, scansionare) e nessuna allusione a capacità sovrumane (lettura istantanea, memoria perfetta).

## Checklist finale per la sessione del plugin

- [ ] Decisioni dell'autore raccolte: R-01, R-60, R-90, R-101, R-110 (e R-21, R-83 se pertinenti)
- [ ] Issue ALTA integrate (R-01 → R-06)
- [ ] Issue per capitolo integrate (cap. 1 → 12)
- [ ] Demolition Log di ogni capitolo aggiornato con il nuovo Cycle
- [ ] `demolition-history.md`, `book-memory.md`, `mappa-eventi.md` aggiornati
- [ ] `export-cms/` rigenerato per i capitoli modificati
- [ ] Regole nuove aggiunte a `book.config.json`
- [ ] Controllo finale con grep: `esattamente`, `a lavoro`, `—` in narrazione, `, e ` in narrazione, Morse senza ` / `
