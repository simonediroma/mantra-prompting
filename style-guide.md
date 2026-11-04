# Guida di stile — Mantra Prompting

> Guida unica per tutto il libro. Va letta prima di scrivere, integrare o rivedere qualunque capitolo, insieme a `style-rules.md` (regole meccaniche R1-R5), `voice-reference.md` (campione fisso) e il cap. 1.
> Ordine di precedenza: le parole dell'autore in sessione > questa guida > `book.config.json → author_voice` > le abitudini di chi scrive.
> Fonti: i campioni di voce salvati capitolo per capitolo (cap. 12-16, cronologia git di `voice-sample.md`), il cap. 1, i testi liberi dell'autore nel cap. 16, la calibrazione in `book-memory.md`, il giudizio editoriale del 2026-10-31. Creata il 2026-11-04.

---

## 1. Il punto di partenza

Il testo che l'autore ha indicato come il più vicino al suo stile è il cap. 16 nella versione 4.9 (campione in `voice-reference.md`). Il cap. 1 è il modello per l'ironia. Tutti e due hanno le stesse sei qualità, che sono il cuore di questa guida.

1. **Il fatto prima dell'immagine.** Si dice cosa succede. Un'immagine entra solo se fa ridere o stringe, mai per decorare.
2. **Le idee si tengono per mano.** Due cose in relazione stanno nella stessa frase, collegate. Il lettore non deve ricucire da solo.
3. **Il flusso è legato.** Periodi con subordinate e connettivi, frasi brevi solo quando danno un colpo.
4. **Il comico viene dalla situazione.** Un equivoco, una regola aziendale presa sul serio, un apparecchio con una volontà. Il narratore lo constata e passa oltre.
5. **Si nomina la cosa per intero.** Niente pronomi da sciogliere, niente "quello che…" spiegato tre frasi dopo.
6. **Ogni fatto una volta.** Nel punto in cui pesa di più.

L'autore lo ha detto con due frasi: "non deve essere mai un esercizio di stile sterile" e "questo è un esempio di come connettere le cose".

---

## 2. Il narratore

È asciutto, osservatore e un po' sarcastico. Guarda il mondo di Meridian come la *Guida galattica* guarda l'universo: con falsa serietà, nomi aziendali trattati da enciclopedia, regole assurde descritte con precisione.

**Commenta un fatto con un altro fatto, in poche parole.**
- ✅ "Non era possibile, naturalmente. Era il modo in cui la vendevano." (cap. 1)
- ✅ "Tom aveva ricopiato le sue note, il che per un tecnico era il massimo della sincerità con il minimo della fatica." (cap. 16)
- ✅ "«Il benessere comincia dallo schermo», diceva, senza specificare di chi." (cap. 16)

**Non spiega mai il significato di una scena**, il parallelismo tra due personaggi o la morale. Mostra e lascia al lettore il collegamento.

**Non anticipa la tensione.** Ogni frase sa solo quello che il personaggio sa in quel momento. Per esempio, è stato scartato "esisteva *ancora* un mondo" nel cap. 1.

**Satira di Meridian, sempre nello stesso ordine causale**: la facciata del benessere, il vero scopo di controllo, lo strumento (supervisori, avvisi), il limite preciso di chi può vedere cosa.
- ✅ "…a tutela del riposo dei dipendenti, che l'azienda proteggeva con un avviso automatico al supervisore per chiunque riposasse nel modo sbagliato."

L'indifferenza di Meridian è cieca e burocratica, mai complice. Niente frasi che facciano pensare a un insabbiamento consapevole.

---

## 3. La frase e il flusso

### 3.1 Periodi legati

Il difetto più grave emerso nel cap. 16 è il testo scattoso: frasi spezzate per chiarezza che, una dietro l'altra, fanno singhiozzare la lettura. La cura è legare con connettivi veri: perché, mentre, ma, finché, eppure, senza, come invece, così, tranne che.

| ❌ Scattoso | ✅ Legato |
|---|---|
| Alle diciassette chiuse la casella. La domanda poteva aspettare le otto. Non ancora. | Alle diciassette chiuse la casella, perché la domanda poteva aspettare le otto. |
| Il sabato Tom non rispose. La domenica in Meridian non si scriveva. | Il sabato Tom non rispose e la domenica non avrebbe potuto, perché in Meridian la domenica non si scriveva… |
| Una volta ci si andava per i ravioli. Poi si era cominciato ad andarci per l'ambiente. | …i più buoni del mondo, anche se ormai lo sapevano soltanto i ravioli, perché da tempo ci si andava per l'ambiente… |

Vincolo che resta: in narrazione, mai virgola seguita da "e" (vedi `book.config.json → avoid`). Si lega con un altro connettivo o con una subordinata.

### 3.2 Le frasi brevi

Una frase breve isolata è ammessa solo se ha un motivo: un'azione, un fatto che scandisce, un rifiuto, un colpo emotivo.
- ✅ "Emma non scrisse." (paga il divieto della domenica)
- ✅ "Non la diede." (il non gesto prima del gesto)
- ✅ "Di Tom, niente."
- ❌ "C'era tutto." / "In entrambi i casi la forma era la stessa." / "Aveva deciso così." (sentenze rafforzative, tutte tolte dal cap. 16)

Mai paragrafi di una riga come chiusura filosofica ("Non era irripetibile.", scartato due volte). La struttura negativa a cascata "Non X. Non Y. Z." al massimo una volta per capitolo.

### 3.3 Due idee in relazione, una frase (R2)

Il modello è la frase dell'autore sui proprietari della Mela Morsicata:

> Quel nome i proprietari l'avevano scelto perché un peccato originale appeso sopra una strada piena di insegne si faceva notare, senza nessuna allusione al santo laico dell'informatica, come invece si dice del logo che Jobs scelse per la sua Apple.

Contrapposizione, causa e confronto stanno insieme. La versione sbagliata le divideva in tre frasi: il nome provocante, poi la leggenda Apple, poi la smentita del designer.

### 3.4 Aprire una scena

Si apre da un'abitudine o da un gesto concreto, poi si mette un'idea dopo l'altra nello stesso respiro: posto, nome, insegna, perché del nome. Non si intercala il passato o il carattere del personaggio prima di aver dato il luogo.
- ✅ "Si ritrovò lì, seduta al suo noodle bar preferito, come più o meno ogni venerdì sera."
- ✅ "L'aspirapolvere era arrivato sul banco con la dignità di un mulo a fine carriera." (cap. 14)
- ❌ "Si ritrovò seduta al solito ristorante cinese. [subito dopo] Di giorno prendeva alla lettera ogni regola di Meridian…"

La prima frase di un capitolo deve reggere da sola, senza l'intro del podcast. Evitare di aprire con un verbo di schermo (aprì, riaprì, controllò).

### 3.5 Incisi

Gli incisi lunghi tra parentesi fanno perdere il filo, soprattutto in audio. Si sciolgono in frasi autonome (C-27). Un inciso breve tra virgole va bene.

---

## 4. Chiarezza

### 4.1 Nominare la cosa (R4)

| ❌ Rimando da sciogliere | ✅ La cosa per intero |
|---|---|
| aspettando che a toglierle la sete fosse quella. | aspettando che a toglierle la sete fosse proprio ciò che la stava provocando. |
| Qualcosa si era allentato. […] Quello che si era allentato tornò al suo posto. | Mentre leggeva si era sentita sollevata, almeno fino in fondo, dove cercò la morte della cliente e non la trovò. |

### 4.2 L'effetto sul personaggio, non il meccanismo

- ❌ "Il sofisma di Tommy le disse in quale punto della catena stava l'errore." (il lettore deve risolvere il sillogismo)
- ✅ "Il sofisma di Tommy le aveva dato la chiave per leggere il suo momento di impasse." (si capisce senza risolverlo)

### 4.3 Ogni fatto una volta

Nel cap. 16 l'omissione di Tom era spiegata quattro volte, nei cap. 12-13 la bugia di Tom quattro volte. Si decide dove l'informazione pesa di più e la si dice lì. In audio la ripetizione non si può saltare. Sulla pagina il lettore la salta e perde fiducia.

### 4.4 Niente verbale

Connettivi da pratica d'ufficio nei momenti di scelta: ❌ "Però, elaborando la situazione… Alla fine, riflettendo, si convinse che, eventualmente… Inoltre, tra i suoi ragionamenti si era palesata un'altra ragione" (cap. 13, prima stesura). ✅ "Il primo impulso fu togliere il video. Era la cosa più semplice da fare, il che bastava a renderla sospetta."

### 4.5 Chiusure

Si chiude su un beat mostrato, mai su un paragrafo che riassume o spiega la posta.
- ✅ "Restò un po' con la penna sopra la pagina, poi lo richiuse senza aver scritto niente." (cap. 14)
- ✅ "«Ciao, stranger» disse il cameriere, da qualche parte, a qualcun altro." (cap. 16)

---

## 5. Il comico

### 5.1 Da dove nasce

In ordine di resa:

1. **Equivoco di situazione.** I proprietari scelgono il nome per il peccato originale, i clienti ci vanno per Turing.
2. **Precisione burocratica presa sul serio.** La formula della trattenuta con fattore turno e arrotondamento (cap. 2), la decurtazione per i loghi obsoleti, l'avviso per chi riposa nel modo sbagliato.
3. **Gli apparecchi con una volontà.** L'altoparlante che ha deciso di parlare solo portoghese in una casa dove nessuno lo parla, il bidet scritto in terza persona, gli apparecchi che "si offendevano, proprio come prometteva la pubblicità".
4. **Il personaggio che si coglie in flagrante**, soprattutto Emma.
   - ✅ "Si accorse di stare progettando un furto in tre tappe ai danni di un'azienda che le pagava lo stipendio, per un oggetto che non avrebbe saputo dove mettere." (vecchio cap. 14, POV Emma)
5. **La chiusa che sgonfia.** "Un hobby che, spiegato a una festa, svuotava la stanza in una media di novanta secondi." (cap. 1)

### 5.2 Metafore e paragoni (R3)

Poche, basse, fisiche, quasi scatologiche quando serve. Devono far ridere davvero, oppure stringere. Mai una per paragrafo, ma nemmeno zero. Mai auliche, epiche o mitologiche per chi deve restare piccolo, come Pete o Meridian.

**Tenute, il registro giusto:**
- "Un piccione non avverte mai chi si trova sotto di lui prima di lasciarsi andare." (Pete, cap. 2)
- "…con l'espressione di chi ha appena scoperto che il proprio gatto sa contare fino a dieci" (cap. 1)
- "…con la dignità di un mulo a fine carriera" / "…con l'entusiasmo di una ruota di criceto in una casa senza criceti" (cap. 14)
- "…come se ogni aggettivo costasse una decurtazione" / "…anche se ormai lo sapevano soltanto i ravioli" / "…come certi zii ai matrimoni dopo il secondo bicchiere" (cap. 16)

**Scartate, da non rifare:**
- Da tradurre prima di capire: "lo spazio di un punto", "una scheda da compilare al contrario", "come si registra un cambio di temperatura", "avrebbe scoperto le carte, non la fonte", "lunga quanto una scheda", "il codice a barre e il nome".
- Mitologiche per un personaggio piccolo: "un temporale, una forza della natura" per Pete.
- Il narratore che spiega la battuta: "Rise tra sé a quel pensiero quasi mistico" (cap. 6).

### 5.3 Quanto

Almeno un'immagine bassa e fisica per capitolo. Il registro comico non si spegne nella seconda metà del libro, né nei capitoli di Emma. Il riso è quello che il libro ha promesso.

---

## 6. Corpo e luogo

Ogni scena, nelle prime righe, ha quattro cose: dove sta il corpo, che ora è e che luce c'è, cosa fa il luogo mentre il personaggio pensa (il nastro, il corridoio, il disco che gira) e un oggetto in mano. Non servono descrizioni, servono dettagli.

- **Capitoli di Tom**: almeno tre dettagli fisici per scena, cioè odore, luce, temperatura o suono dell'edificio. I verbi fisici (svitò, girò, posò) devono pesare più dei verbi di schermo (aprì, lesse, filtrò).
- **Capitoli di Emma**: una sola stanza, mai descritta. Ci sono la striscia di luce sotto la porta, le porte che si chiudono alle cinque, il carrello del caffè delle dieci, la poltrona e la stampante del fondatore. Fa eccezione la Mela Morsicata, resa come luogo fisico con gli spiragli per il lettore attento (vedi §9).
- **Onomatopee**: una o due per capitolo, in corsivo, solo per macchine ed edificio, con suono fisso per macchina (*dlin*, *clac*, *bzz bzz*, *frrr*, *cri-cri*, *krrr*…, elenco in `book-memory.md`).

---

## 7. I personaggi sulla pagina

**Tom.** È curioso, tecnico, parla agli apparecchi ("gli chiese, per abitudine, se avesse qualcosa da dirgli"). La motivazione è sempre tecnica, mai morale: non giudica l'etica di niente. La sua curiosità non è mai un rimpianto. Mente male agli umani. Frase più lunga, piena di gesti.

**Emma.**
- L'emozione arriva prima del ragionamento, poi viene analizzata. Va mostrata, mai nominata come etichetta ("era sgomento").
- Prende le regole di Meridian come qualunque regola, senza che le piacciano o le pesino, finché non trova un motivo per infrangerle. Non è "l'unica" a seguirle.
- La sua frase è più breve di quella di Tom, ma non scattosa.
- Il lessico ambiguo è ammesso e voluto ("elaborò", "registrarne", "le costò"), sempre leggibile in chiave umana.
- Vietato il linguaggio di progettazione o attivazione ("da quando aveva iniziato a esistere").

**Pete.** Patetico e grottesco, comico nella sua fame. Paragoni bassi, mai grandiosi.

**La signora Voss.** Viva perché parla. "Non 'non riusciva' ad accendersi: proprio non voleva. C'è differenza, sa?"

**Il fondatore.** Gentile, gli indovinelli ripetuti come un mantra con parole sempre nuove.

---

## 8. Dialogo

- **Una voce parlata in ogni capitolo**, anche in quelli di Emma: il fondatore, il cameriere, Tommy.
- **Nel dialogo i personaggi possono essere prolissi, teatrali, ridondanti**: è caratterizzazione. Lì la ", e" è libera.
- **Caporali** «» per il dialogo, virgolette alte "" per pensieri e citazioni.

---

## 9. Il mistero e i tre livelli di lettura

- **Il reveal arriva nel Libro 2.** Fino ad allora nessuna scena dal POV di Emma lo scioglie. Mai nominare sublimazione, Artefatto Generatore o percentuali del fenomeno: solo l'effetto osservabile.
- **Ogni scena con un indizio ha tre letture** (decise con l'autore sulla Mela Morsicata):
  - Il lettore distratto vede la superficie: un ristorante, una donna sola.
  - Il lettore attento sospetta: è una chat? Emma non è umana?
  - Il lettore nerd sorride ai riferimenti (Blade Runner, Turing, il gioco dell'imitazione, «stranger», ping, quit, la cipolla di Tor) e resta nel dubbio.
- **Contro la lettura sbagliata**, per esempio androidi tra gli umani, si mette un'àncora leggera: "ognuno era quello che diceva di essere".
- **Regola per le scene alla Mela Morsicata**: niente affermazioni definitive (non "nessuno mangia", ma "il cibo era passato in secondo piano"). Nessuno ci sta controvoglia.

---

## 10. Regole di mondo che toccano lo stile

- **Mail.** Si racconta sempre dal POV di chi la legge, mai di chi la scrive o la invia.
- **Morse.** Trascrizioni con lo slash tra le parole (IO / SONO / QUI). Codici verificati.
- **Numeri** in lettere nella narrazione, cifre solo in box e schermate.
- **Grafie fisse.** "Mail", mai "email". "Meridian" senza articolo. "Al lavoro", mai "a lavoro". "Hard reset", mai sinonimi.
- **Fatti verificati.** Una leggenda si scrive come leggenda: "come invece si dice del logo che Jobs scelse per la sua Apple", non come fatto. Lo stesso vale per guasti, componenti e cronologie, che vanno controllati come li controllerebbe chi ripara.
- **Il quaderno di Tom** non va mai al lavoro.

---

## 11. Come si è arrivati qui (dai campioni)

| Campione | Cosa insegna |
|---|---|
| Cap. 12 | Emma ragiona per ipotesi in frasi brevi e pulite. Rischio: le emozioni nominate ("l'allarme allentò la presa"). |
| Cap. 13, prima stesura | Il verbale nei momenti di scelta ("elaborando la situazione… eventualmente"). Corretto nella versione finale. |
| Vecchio cap. 14 (tagliato) | Il miglior comico dal POV di Emma: il furto in tre tappe per un oggetto che non saprebbe dove mettere. |
| Cap. 14 | Il corpo regge il pensiero: le mani lavorano mentre la testa scrive. Metafore basse giuste (mulo, criceto). |
| Cap. 15 | Dettagli fisici densi, il passo di Pete, l'errore di mano che mostra il turbamento. |
| Cap. 16 v1.0-v3.2 | Troppo pieno: metafore da tradurre, rimandi, fatti ripetuti, digressioni in cinque registri. |
| Cap. 16 v4.0-v4.1 | Troppo asciutto: ripulito di tutto, scattoso, senza riso. |
| **Cap. 16 v4.9** | **Il punto giusto**: fatti, idee legate, comico di situazione, le frasi dell'autore come modello. |

La lezione del cap. 16 è che l'errore sta in entrambe le direzioni: denso non vuol dire pieno, asciutto non vuol dire spezzato.

---

## 12. Checklist prima di consegnare un capitolo

1. Letto ad alta voce, il flusso è legato? Dove singhiozza, unire con un connettivo.
2. C'è una metafora che bisogna tradurre? Sostituirla con il fatto. Quelle rimaste fanno ridere o stringono?
3. Due idee in relazione stanno in frasi separate? Ricucirle (R2).
4. Un fatto è detto più di una volta? Tenerlo dove pesa di più.
5. Le frasi brevi isolate hanno un motivo?
6. Chi parla ad alta voce? Almeno una voce oltre al narratore.
7. Cosa si sente con il corpo? Le quattro cose nelle prime righe di ogni scena.
8. C'è almeno un'immagine bassa e fisica che faccia ridere?
9. Cosa vuole il personaggio che prima non voleva?
10. Ogni fatto tecnico o storico è verificato? Le leggende sono scritte come leggende?
11. Il mistero regge su tre livelli, senza sciogliersi?
12. Regole meccaniche (`style-rules.md`): niente ", e" in narrazione, niente due punti a metà frase, numeri in lettere, caporali.
