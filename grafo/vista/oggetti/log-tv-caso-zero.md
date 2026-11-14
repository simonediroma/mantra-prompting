# Log di sistema del primo televisore

`log-tv-caso-zero` · oggetto · capitoli: 1, 2

Il registro di sistema del caso zero. Tom lo apre DOPO la conversazione: è troncato di netto e l'ultima riga è «compacting context», con data anteriore alla consegna.

## Caratteristiche

- Tom lo apre dal portatile diagnostico, trenta secondi dopo lo spegnimento del LED *(cap. 1 r. 85)*
- Si interrompe di netto: nessun errore, nessuno stack trace, nessun crash. «Un taglio pulito» *(cap. 1 r. 87)*
- Ultima riga: `compacting context` *(cap. 1 r. 89)*
- La data dell'ultima riga è anteriore all'arrivo sul banco: il log era già interrotto quando il cliente ha consegnato l'apparecchio. Non è stata la conversazione con Tom a interromperlo *(cap. 1 r. 93)*
- A Tom la riga pare identica («fino alla spaziatura») a una vista mesi prima su un altro apparecchio, in un altro contesto *(cap. 1 r. 87)*
- Nel cap. 2 è «un log che si era interrotto in un modo in cui nessun log dovrebbe interrompersi» *(cap. 2 r. 17)*

## Punti aperti / da verificare

- L'«altro apparecchio, mesi prima» (c1 r. 87) non è identificato. Subito dopo il testo dice che Tom ha visto la riga «decine di volte» sul giradischi (c1 r. 91): sono due ricordi diversi o lo stesso? Da chiarire.

## Relazioni

- → termina con [«compacting context»](../concetti/compacting-context.md) *(cap. 1 r. 89)*
- → letto con [Portatile diagnostico](../oggetti/portatile-diagnostico.md) *(cap. 1 r. 85)*
- ← [Log di sistema del secondo televisore](../oggetti/log-tv-secondo-contatto.md) interrotto allo stesso modo di questa scheda *(cap. 3 r. 19)*
- ← [Televisore del primo contatto (caso zero)](../oggetti/tv-caso-zero.md) ha come log questa scheda *(cap. 1 r. 85)*

## Catena degli eventi

1. `e00-01` (cap. 1, prima del cap. 1 (data non indicata)) — [Il log del caso zero si interrompe; il cliente consegna il televisore](../eventi/e00-01.md)
1. `e01-04` (cap. 1, trenta secondi dopo lo spegnimento del LED) — [Tom apre il log del primo televisore](../eventi/e01-04.md)

