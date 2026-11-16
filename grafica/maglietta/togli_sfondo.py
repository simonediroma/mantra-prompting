"""Toglie lo sfondo nero e salva un PNG trasparente alla stessa risoluzione.

Uso:  python3 togli_sfondo.py immagine.png  [uscita.png]

Metodo "unmultiply": l'alpha di ogni pixel = la sua luminosità sul nero.
Così l'alone del neon resta morbido e semitrasparente invece di diventare
un bordo nero. Il rumore quasi nero (artefatti JPEG) diventa trasparente.
"""
import sys
import numpy as np
from PIL import Image

SOGLIA = 14  # 0-255: sotto questo valore il pixel è considerato sfondo

src = sys.argv[1]
dst = sys.argv[2] if len(sys.argv) > 2 else src.rsplit(".", 1)[0] + "-trasparente.png"

img = Image.open(src).convert("RGB")
rgb = np.asarray(img).astype(np.float32)

a = rgb.max(axis=2)                                   # alpha = canale più luminoso
a = np.clip((a - SOGLIA) * 255.0 / (255 - SOGLIA), 0, 255)
safe = np.maximum(a, 1)[..., None]
col = np.clip(rgb * 255.0 / safe, 0, 255)             # colore "pieno" senza il nero

out = np.dstack([col, a]).astype(np.uint8)
Image.fromarray(out, "RGBA").save(dst, dpi=(300, 300))
print(f"{dst}  {img.size[0]}x{img.size[1]} px")
