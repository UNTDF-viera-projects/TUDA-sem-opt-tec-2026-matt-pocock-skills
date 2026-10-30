"""Genera slides/index.html a partir de slides/index.src.html.

Cada <code ... data-incluir="ruta/al/archivo"></code> se completa con el contenido
real de ese archivo (relativo a la raíz del repo), así el código de las slides
siempre coincide con los ejemplos.

Uso:  python3 slides/build.py
"""

import html
import re
import sys
from pathlib import Path

SLIDES = Path(__file__).resolve().parent
RAIZ = SLIDES.parent
PATRON = re.compile(r'(<code\b[^>]*\bdata-incluir="([^"]+)"[^>]*>)\s*(</code>)')


def incluir(match: re.Match) -> str:
    apertura, ruta, cierre = match.groups()
    archivo = RAIZ / ruta
    if not archivo.is_file():
        sys.exit(f"build.py: no existe {ruta}")
    contenido = archivo.read_text(encoding="utf-8").rstrip("\n")
    return f"{apertura}{html.escape(contenido, quote=False)}{cierre}"


def main() -> None:
    fuente = (SLIDES / "index.src.html").read_text(encoding="utf-8")
    salida, cantidad = PATRON.subn(incluir, fuente)
    aviso = "<!-- GENERADO por slides/build.py: editar index.src.html -->\n"
    (SLIDES / "index.html").write_text(aviso + salida, encoding="utf-8")
    print(f"index.html generado ({cantidad} archivos incluidos)")


if __name__ == "__main__":
    main()
