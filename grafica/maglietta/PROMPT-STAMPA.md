# Prompt per grafiche da stampare su maglietta (DTG/DTF)

Da incollare in testa alla richiesta, in Gemini o in un'altra sessione.

```
This artwork will be printed on a black T-shirt with DTG/DTF printing.
Printers cannot reproduce soft glows, blurs, gradients or semi-transparency:
they turn into grey speckled halftone patches. Follow these rules strictly:

- FLAT COLORS ONLY: every pixel is either a fully opaque solid color or pure background.
- NO glow, NO blur, NO bloom, NO outer glow, NO soft shadow, NO gradient, NO airbrush, NO haze, NO light rays, NO texture, NO noise.
- To suggest a neon effect, use 2–3 concentric SOLID outlines with hard edges
  (e.g. dark red outer band, bright red tube, light pink thin core), like a vector sticker or screen print.
- Maximum 6 colors, crisp vector-style edges, minimum line thickness 3 mm at print size.
- Solid pure black background (#000000) only, to be removed later. Nothing semi-dark near the artwork.
- Style reference: screen-printed band merch, vector illustration, NOT a photo of a real neon sign.
```

## Prima di caricare sul sito di stampa
1. Togli lo sfondo e controlla che non restino pixel semitrasparenti (in Photopea: Selezione > Gamma colori sul nero, elimina; poi Livello > Opzioni di fusione: nessun effetto).
2. Risoluzione: almeno 3600×4800 px (30×40 cm a 300 dpi).
3. Se vedi ancora aloni sfumati nell'immagine, rigenera: non si sistemano in stampa.
