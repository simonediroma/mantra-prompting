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
| Onomatopee | corsivo, senza punto esclamativo; solo suoni che il personaggio sente davvero (ripresi come effetti nel podcast, vedi `podcast/plan.md → ## Sound effects`) | un *mmmmm* continuo · ❌ un "MMMMM!" |
| Serial comma | no | idraulica, cucina e yoga |
| Numbers | in lettere nella narrazione (anche sopra dieci); cifre solo in box/schermate di sistema e titoli di video | le undici passate · *in 15 minuti al giorno* |
| "mail" / "email" | sempre "mail" (una mail, la mail, le mail); "indirizzo di posta" per l'indirizzo | una mail vera · ❌ un'email vera |

---

## Writing Rules

Rules the author wants respected everywhere. Each has a right and a wrong example so the rule can't be misread.

| ID | Rule | Scope | ✅ Right | ❌ Wrong | Source |
|---|---|---|---|---|---|
| R1 | Nella narrazione niente due punti a metà frase per collegare due parti della stessa frase (spiegazione, elenco, conseguenza): usare punto, virgola o una congiunzione. Ammessi solo per introdurre discorso diretto, testo citato (Morse, quaderno, messaggi) o un nome/titolo (es. "cliccò sul nome del canale: eTv."). Prevale sulla voce em dash di `book.config.json → avoid`. | narrazione | Vardju. Un nome che suonava slavo, quasi minaccioso. | Vardju: un nome che suonava slavo, quasi minaccioso. | author, 2026-10-14 |
| R2 | Suoni d'ambiente e di oggetti presenti nella scena (ronzii, segnali, squilli, notifiche, gesti udibili) si possono usare come espediente narrativo per rafforzare immagini e ambientazione, con misura: al massimo due o tre per capitolo, solo suoni che il personaggio sente davvero, onomatopea in corsivo. Ogni suono inserito va registrato in `podcast/plan.md → ## Sound effects` per riprenderlo come effetto nel podcast. Tom: suoni meccanici e analogici; Emma: suoni digitali e puliti. | narrazione | un accordo di tre note, *din-don-dan*, pensato… | un suono per paragrafo; suoni che nessuno in scena può sentire | author, 2026-10-26 |
