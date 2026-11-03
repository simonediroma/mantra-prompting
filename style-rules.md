# Style Rules

> The book's writing rules. Read by `write`, `integrate` and `revise` — every new text must respect them, every revision checks them.
> Add rules with `/ghost-writer:rules add "..."`, or edit this file directly. Rules also come from `corrections` when a note is general ("always…", "never…").

---

## Punctuation Conventions

Mechanical conventions. One value per row — mixing forms in the book is always an error.

| Element | Convention | Example |
|---|---|---|
| Dialogue | «» caporali | «Vieni» disse. |
| Thoughts / inserted phrases | "" alte | Pensò: "non ora". |
| Quotes inside quotes | "" dentro «» | «Mi ha detto "domani"» |
| Dash | nessun trattino lungo in narrazione (vedi `book.config.json → avoid` e R1): virgola, punto o parentesi | lui, disse, no |
| Ellipsis | … carattere singolo | Vieni… |
| Serial comma | no | idraulica, cucina e yoga |
| Numbers | in lettere nella narrazione (anche sopra dieci); cifre solo in box/schermate di sistema e titoli di video | le undici passate · *in 15 minuti al giorno* |
| "mail" / "email" | sempre "mail" (una mail, la mail, le mail); "indirizzo di posta" per l'indirizzo | una mail vera · ❌ un'email vera |

---

## Writing Rules

Rules the author wants respected everywhere. Each has a right and a wrong example so the rule can't be misread.

| ID | Rule | Scope | ✅ Right | ❌ Wrong | Source |
|---|---|---|---|---|---|
| R1 | Nella narrazione niente due punti a metà frase per collegare due parti della stessa frase (spiegazione, elenco, conseguenza): usare punto, virgola o una congiunzione. Ammessi solo per introdurre discorso diretto, testo citato (Morse, quaderno, messaggi) o un nome/titolo (es. "cliccò sul nome del canale: eTv."). Prevale sulla voce em dash di `book.config.json → avoid`. | narrazione | Vardju. Un nome che suonava slavo, quasi minaccioso. | Vardju: un nome che suonava slavo, quasi minaccioso. | author, 2026-10-14 |
| R2 | Due idee in relazione (contrapposizione, causa, confronto) vanno nella stessa frase, collegate da una congiunzione o un inciso (senza, come invece, mentre, perché), non separate in frasi o paragrafi diversi che il lettore deve ricucire da solo. | narrazione | I proprietari l'avevano scelto perché era un'insegna che si faceva notare, senza nessuna allusione al santo laico dell'informatica, come invece si dice del logo che Jobs scelse per la sua Apple. | I proprietari l'avevano scelto perché sembrava provocante. Secondo una leggenda, invece, la mela della Apple era un omaggio a Turing. Il designer l'aveva smentita. | author, 2026-11-03 (cap. 16) |
