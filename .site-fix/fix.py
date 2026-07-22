from pathlib import Path
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")

replacements = {
    'alternateNamn': 'alternateName',
    'American football in Dalarna': 'Amerikansk fotboll i Dalarna',
    'Dalarna, Sweden': 'Dalarna, Sverige',
    '"sport":"American football"': '"sport":"Amerikansk fotboll"',
    'Diagram reading every strength has a position': 'Diagram som visar att varje styrka har en position',
    '>24–26 July<': '>24–26 juli<',
    '>31 July–2 August<': '>31 juli–2 augusti<',
    '>22 August<': '>22 augusti<',
    '>28 May 2026<': '>28 maj 2026<',
    '>26 May 2026<': '>26 maj 2026<',
    '>14 February 2026<': '>14 februari 2026<',
    '>18 July 2026<': '>18 juli 2026<',
    'checked on 18 July 2026': 'kontrollerad den 18 juli 2026',
}

for page in root.glob('*.html'):
    text = page.read_text(encoding='utf-8')
    for old, new in replacements.items():
        text = text.replace(old, new)

    english_url = 'https://dalecarliarebel.com/' if page.name == 'index.html' else f'https://dalecarliarebel.com/{page.name}'
    text = text.replace(
        'href="https://dalecarliarebel.com/" hreflang="en" lang="en"',
        f'href="{english_url}" hreflang="en" lang="en"'
    )
    page.write_text(text, encoding='utf-8')

# Keep the Swedish domain and repository documentation explicit.
(root / 'CNAME').write_text('dalecarliarebels.se\n', encoding='utf-8')
(root / 'README.md').write_text(
    '# Dalecarlia Rebels – svensk webbplats\n\n'
    'Svensk version av Dalecarlia Rebels webbplats. Källan är den engelska '\
    'webbplatsen i `cjram71/dalecarliarebel`, med svensk text, metadata, '\
    'navigering och tillgänglighetsinformation.\n',
    encoding='utf-8'
)
