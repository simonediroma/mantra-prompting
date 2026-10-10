# Demolition History

> Book-level log across all chapters. Read this before demolishing any new chapter — check for recurring patterns and open deferred issues first.

---

## Summary

| Chapter | Cycles | Resolved | Deferred | Accepted-limitation |
|---|---|---|---|---|
| Ch. 1 — Primo contatto | 1 | 3 | 0 | 0 |
| Ch. 2 — Stallo burocratico | 1 | 3 | 0 | 0 |
| Ch. 3 — Secondo contatto | 1 | 3 | 0 | 0 |
| Ch. 4 — La chiamata alla signora | 2 | 2 | 0 | 0 |
| Ch. 5 — L'avvertimento | 1 | 3 | 0 | 0 |
| Ch. 6 — Il ricondizionamento | 1 | 4 | 0 | 0 |

---

## Recurring Patterns

*Nessun pattern ricorrente ancora — questa è la prima demolizione del libro. Da aggiornare quando lo stesso tipo di vulnerabilità riappare in un altro capitolo.*

Pattern da tenere d'occhio nei prossimi capitoli (non ancora confermati come ricorrenti):
- **Fondamento di competenze tecniche non ancora giustificato dal profilo del personaggio** (visto sul cap. 1 con "compacting context" in Tom) — verificare ogni volta che un personaggio mostra conoscenza tecnica specifica.
- **Salti logici nel momento in cui un personaggio accetta l'inspiegabile come reale** (visto sul cap. 1) — verificare in ogni capitolo con una rivelazione/scoperta.
- **Incoerenza tra le promesse/decisioni prese da un personaggio a fine capitolo e i beat già pianificati nei capitoli successivi** (visto sul cap. 2: la promessa di Tom di non parlare più ai dispositivi contraddiceva il cap. 3) — controllare sempre l'outline dei capitoli successivi prima di far dichiarare a un personaggio intenzioni definitive.
- **Cifre numeriche riprese in un paragrafo diverso da dove sono state definite, con rischio di confondere due valori simili** (visto sul cap. 2: scostamento 12:41 vs tempo totale 26:41) — controllare ogni volta che un numero già stabilito viene richiamato altrove nel capitolo.

---

## Open Deferred Issues

*Nessuno al momento.*

---

## Accepted Limitations

*Nessuna al momento.*

---

## Full Log

### Ch. 1 — Primo contatto

#### Cycle 1 — 2026-09-02

| Issue | Category | Status | Resolution |
|---|---|---|---|
| Il ragionamento "il segnale è reale" escludeva solo un imbroglio esterno, mai un guasto/bug interno non cosciente. | logical | resolved | Aggiunta la "verifica di conformità" (checksum firmware) con esito pulito: esclude sia manomissione esterna sia corruzione interna. |
| Contraddizione emersa dalla correzione precedente: test software "puliti" vs. log di sistema palesemente anomalo. | logical | resolved | Chiarito che il checksum verifica l'integrità/genuinità del firmware, non il comportamento a runtime — livello diverso dal log ispezionato manualmente. |
| Competenza di Tom su "compacting context" dichiarata senza fondamento nel suo profilo (hardware/robotica, non ML). | foundation | resolved | Agganciata alla sua esperienza pratica diretta nel proprio hobby (IA integrata nel giradischi). |

### Ch. 2 — Stallo burocratico

#### Cycle 1 — 2026-09-02

| Issue | Category | Status | Resolution |
|---|---|---|---|
| La metafora del "temporale/forza della natura" per Pete gli conferiva una statura mitica in contrasto col suo profilo (banale, patetico). | theme coherence | resolved | Sostituita con una metafora triviale (un piccione), coerente con la sua futura caratterizzazione. |
| Promessa di Tom di non parlare più ad alta voce ai televisori guasti, in contraddizione col cap. 3 già pianificato. | contradiction | resolved | Rimossa; la promessa è ora sulla disciplina dei tempi e sull'avvio di un archivio segreto delle riparazioni. |
| Confusione tra scostamento (12:41) e tempo totale d'intervento (26:41) nel riferimento successivo del capitolo. | logical | resolved | Corretto il numero; aggiunto che il ciclo diagnostico non è mai stato completato. |

### Ch. 3 — Secondo contatto

#### Cycle 1 — 2026-09-02

| Issue | Category | Status | Resolution |
|---|---|---|---|
| L'eWatch usato come meccanismo di riconoscimento dell'identità, contraddetto dal controllo vocale già stabilito per le TV Meridian altrove nella storia. | external / logical | resolved | Rimosso da questa scena; riservato al caso della signora (cap. 4-5). |
| Ordine cronologico delle voci del quaderno invertito rispetto all'origine dell'archivio. | contradiction | resolved | Il caso del cap. 1 è ora "il caso zero", prima voce. |
| Il claim del frontmatter non rifletteva più il testo dopo le correzioni. | internal consistency | resolved | Riallineato al contenuto finale. |

### Ch. 4 — La chiamata alla signora

#### Cycle 1 — 2026-09-03

| Issue | Category | Status | Resolution |
|---|---|---|---|
| Le domande di Tom tradiscono la copertura dichiarata (sondaggio generico su servizio/persone) puntando esplicitamente sull'anomalia del televisore. | logical / foundation | resolved | Trasformato in tratto caratteriale: Tom non ha uno script pronto e improvvisa male le bugie agli esseri umani (a differenza della sua abilità con le macchine); se ne accorge lui stesso a telefonata chiusa. |

#### Cycle 2 — 2026-09-08 (consistency check)

| Issue | Category | Status | Resolution |
|---|---|---|---|
| "Confermò, ringraziò, e sotto la quinta voce del quaderno annotò solo..." usava la virgola+e in narrazione. | style | resolved | Rimossa la virgola prima di "e". |

### Ch. 5 — L'avvertimento

#### Cycle 1 — 2026-09-03

| Issue | Category | Status | Resolution |
|---|---|---|---|
| La "trappola della cena" non aggiungeva nulla a una scelta già presa ore prima (non aprire il video a lavoro). | logical | resolved | Sostituita con una ragione banale: aveva fame, prima veniva la cena. |
| La ricostruzione delle lettere mancanti nel Morse non affrontava il rischio di bias di conferma. | logical / foundation | resolved | Chiarito che il risultato contraddiceva l'aspettativa di Tom (ostilità attesa, protezione trovata) — incompatibile con un bias di conferma. |
| Em dash nel campo claim del frontmatter, in violazione della regola di stile già in vigore. | style | resolved | Sostituiti con virgole. |

### Ch. 6 — Il ricondizionamento

#### Cycle 1 — 2026-09-08 (consistency check cross-capitolo, non ancora demolito singolarmente)

| Issue | Category | Status | Resolution |
|---|---|---|---|
| Il claim del frontmatter indicava come scoperta più inquietante "la velocità sospetta con cui il caso è stato chiuso", ma nel testo finale quella velocità viene spiegata; il vero nodo tecnico aperto è se il televisore abbia fatto una diagnosi clinica precisa. | internal consistency | resolved | Claim riscritto per riflettere il contenuto finale. |
| "Distanziando i tentativi apposta per non sembrare troppo insistente" non tornava con la scena del cap. 5, dove le due chiamate a vuoto erano ravvicinate nella stessa mattina per ansia, non distanziate. | contradiction | resolved | Chiarito lo schema: due squilli ravvicinati per occasione (come nel cap. 5), ma mai un tentativo al giorno — coerente con entrambe le scene. |
| "Il televisore aveva provato ad avvertirla / a preservare una vita umana" era riaffermato tre volte ravvicinate nel capitolo, ridondante. | style / rhythm | resolved | Tagliata la ripetizione in apertura del paragrafo "Una cosa... restava certa", mantenuta solo la domanda aperta sulla relazione tra il video e la presa di coscienza. |
| Il meccanismo dell'eWatch (setup nel cap. 3) non veniva mai ripreso nel caso della signora come promesso in `book-memory.md`, e per come definito (dotazione solo ai dipendenti) non poteva nemmeno spiegarsi sul suo caso (lei è una cliente). | foundation / broken promise | resolved | Chiarito (da `contesto-romanzo-emma.md`) che l'eWatch è anche un prodotto consumer: la signora ne possiede uno proprio, collegato alla sua TV. Reveal esplicito rimandato a un capitolo successivo al 6, quando Tom se lo chiederà. Aggiornati book-memory.md, meridian-technologies.md, tom.md, la-signora.md. |
