#!/usr/bin/env python3

import os
from jinja2 import Template, FileSystemLoader, Environment
from pathlib import Path

env = Environment()
env.loader = FileSystemLoader('.')

def main():
    carpeta = Path("../fotos/galeria")
    imagenes = [f.name for f in carpeta.iterdir() if f.suffix.lower() in (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp")]

    tmpl = env.get_template('galeria_template.html')
    html_template_string = tmpl.render(galerias=imagenes)
    template_file = open("galeria.html", 'w').write(html_template_string)

if __name__ == '__main__':
    main()
