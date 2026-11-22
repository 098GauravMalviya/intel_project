# Rebuilds ../index.html and ../../index.html from the template and the data block.
# Usage: python build.py
from pathlib import Path
here = Path(__file__).parent
t = (here / 'app.template.html').read_text(encoding='utf-8')
d = (here / 'data.js').read_text(encoding='utf-8')
content = t.replace('/*__DATA__*/', d)
(here.parent / 'index.html').write_text(content, encoding='utf-8')
root_index = here.parent.parent / 'index.html'
if root_index.exists():
    root_index.write_text(content, encoding='utf-8')
print('Built rtx-spark-intelligence/index.html and root index.html')
