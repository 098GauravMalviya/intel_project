# Rebuilds ../index.html from the template and the data block.
# Usage: python3 build.py
from pathlib import Path
here = Path(__file__).parent
t = (here / 'app.template.html').read_text(encoding='utf-8')
d = (here / 'data.js').read_text(encoding='utf-8')
(here.parent / 'index.html').write_text(t.replace('/*__DATA__*/', d), encoding='utf-8')
print('Built index.html')
