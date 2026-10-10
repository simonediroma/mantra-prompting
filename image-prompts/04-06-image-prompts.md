# Prompt immagini (Gemini) — Capitoli 4-6

## Come mantenere la coerenza con le immagini dei cap. 1-3

Le immagini dei capitoli precedenti sono state generate tutte nella stessa sessione Gemini, che è la vera fonte della loro coerenza (il modello ha mantenuto lo stesso aspetto di Tom da un'immagine all'altra senza bisogno di ripeterlo in dettaglio). Per i cap. 4-6:

- **Usa la stessa sessione/chat Gemini**, non aprirne una nuova: incolla questi prompt in coda alla conversazione già usata per i cap. 1-3, così il modello ha ancora in memoria l'aspetto di Tom, il taglio fotografico e la palette usati finora.
- Se generi in una sessione nuova o con un modello che non mantiene memoria tra immagini, **allega come riferimento una delle immagini di Tom già generate** (funzione immagine-di-riferimento/image-to-image, se disponibile) prima di lanciare i nuovi prompt, invece di affidarti solo alla descrizione testuale.
- Se noti che il modello si discosta dall'aspetto già stabilito (viso, corporatura, stile d'abbigliamento), correggi con un prompt di follow-up nella stessa sessione ("stesso uomo delle immagini precedenti, stessa corporatura/capelli/occhiali") invece di rigenerare da zero: è quello che ha già funzionato per i cap. 1-3.

## Stile di riferimento comune per tutte e tre: fotografia cinematografica, tono desaturato e leggermente freddo (X-Files incontra il grottesco burocratico alla Guida galattica per autostoppisti), niente elementi fantasy/soprannaturali espliciti, niente testo nell'immagine, niente volti riconoscibili di persone reali.

**Descrizione fissa di Tom** (da characters/tom.md, va ripetuta identica in ogni prompt per coerenza): a lean but not gaunt man of about 53, tall (around 190cm/6'3"), wiry and tense build, visibly veined forearms, thinning hair with a receding crown, olive skin, wearing reading glasses. Dressed in a plain, unkempt, unremarkable way that never tries to impress, e.g. a hooded sweatshirt.

## Capitolo 4 — La chiamata alla signora

```
Cinematic photo, moody desaturated color grade, cool blue-gray tones with one warm light source. A lean but not gaunt man of about 53, tall (around 190cm), wiry and tense build, visibly veined forearms, thinning hair with a receding crown, olive skin, wearing reading glasses and a plain hooded sweatshirt, sits alone at a cluttered home desk late at night, phone pressed to his ear, free hand hovering over a closed black notebook he won't open. A small desk lamp is the only light. In the background, barely in focus, an unremarkable flat-screen television sits dark and silent. The mood is quiet, private anxiety: a man doing something he's not supposed to do, from the safety of his own home. Shallow depth of field, slight film grain, no visible text, no readable screen content, no recognizable real person.
```

## Capitolo 5 — L'avvertimento

```
Cinematic photo, shaky handheld phone-camera aesthetic, dim warm domestic lighting at night. Extreme close-up, slightly out-of-focus framing of a television set from a few centimeters away, as if filmed by someone standing right in front of it. A single small LED power indicator blinks in the dark, the only sharp point of light in the frame. The rest of the room is soft shadow. Sense of unease hidden inside something completely mundane. Slight motion blur, low light grain, no visible text, no recognizable real person, no faces in frame.
```

## Capitolo 6 — Il ricondizionamento

```
Cinematic photo, flat fluorescent industrial lighting, cold desaturated palette. Wide shot of a factory repair bench inside a large sterile workshop, a dozen identical flat-screen televisions lined up in a row, each with a small yellow tag on the back. A lean but not gaunt man of about 53, tall (around 190cm), wiry and tense build, visibly veined forearms, thinning hair with a receding crown, olive skin, wearing reading glasses and plain worn work clothes, stands among the televisions, dwarfed by the row of returned appliances, focused on one unit in particular. In the background, rows of shelving and more devices fade into soft blur, suggesting a much larger, indifferent bureaucratic system. Muted colors, slight grain, no visible text on tags or screens, no recognizable real person.
```
