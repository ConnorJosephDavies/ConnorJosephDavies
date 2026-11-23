"""Builds the SVG images used by the profile README.

Every image is written twice: a dark version and a light version, so the
profile matches whichever GitHub theme the visitor uses.

Run from the repository root:  python scripts/build_assets.py
"""

from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "assets"

FONT = "'Segoe UI', Inter, Helvetica, Arial, sans-serif"
MONO = "Consolas, 'Fira Code', Menlo, monospace"

THEMES = {
    "dark": {
        "bg_a": "#0b1220", "bg_b": "#121b30", "grid": "#1c2740", "frame": "#24304d",
        "card": "#0d1117", "card_border": "#30363d", "bar": "#161b22", "divider": "#21262d",
        "title": "#f0f6fc", "text": "#c9d1d9", "muted": "#8b949e", "faint": "#6e7681",
        "field": "#010409", "link": "#58a6ff", "glow": 0.32,
    },
    "light": {
        "bg_a": "#f6f8fc", "bg_b": "#e9effa", "grid": "#dde5f2", "frame": "#d0d9e8",
        "card": "#ffffff", "card_border": "#d0d7de", "bar": "#f6f8fa", "divider": "#eaeef2",
        "title": "#1f2328", "text": "#24292f", "muted": "#59636e", "faint": "#818b98",
        "field": "#f6f8fa", "link": "#0969da", "glow": 0.18,
    },
}

PYTHON_COLOUR = "#3572A5"


def escape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def write(name, theme, svg):
    OUTPUT_DIR.mkdir(exist_ok=True)
    (OUTPUT_DIR / f"{name}-{theme}.svg").write_text(svg, encoding="utf-8")


# ---------------------------------------------------------------- header

def build_header(theme_name, t):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="900" height="260" viewBox="0 0 900 260" font-family="{FONT}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{t['bg_a']}"/><stop offset="1" stop-color="{t['bg_b']}"/></linearGradient>
    <linearGradient id="accent" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2f81f7"/><stop offset="1" stop-color="#8b5cf6"/></linearGradient>
    <pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M28 0H0V28" fill="none" stroke="{t['grid']}"/></pattern>
    <radialGradient id="glow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#2f81f7" stop-opacity="{t['glow']}"/><stop offset="1" stop-color="#2f81f7" stop-opacity="0"/></radialGradient>
    <clipPath id="round"><rect width="900" height="260" rx="18"/></clipPath>
  </defs>
  <style>
    .cursor {{ animation: blink 1.1s steps(1) infinite; }}
    @keyframes blink {{ 50% {{ opacity: 0; }} }}
    .orb {{ animation: drift 12s ease-in-out infinite alternate; }}
    @keyframes drift {{ from {{ transform: translate(0px, 0px); }} to {{ transform: translate(-90px, 24px); }} }}
    .pulse {{ animation: pulse 2s ease-in-out infinite; }}
    @keyframes pulse {{ 50% {{ opacity: 0.35; }} }}
  </style>
  <g clip-path="url(#round)">
    <rect width="900" height="260" fill="url(#bg)"/>
    <rect width="900" height="260" fill="url(#grid)"/>
    <circle class="orb" cx="720" cy="120" r="200" fill="url(#glow)"/>
    <rect x="0.5" y="0.5" width="899" height="259" rx="18" fill="none" stroke="{t['frame']}"/>

    <rect x="56" y="50" width="190" height="28" rx="14" fill="#3fb950" fill-opacity="0.12" stroke="#3fb950" stroke-opacity="0.5"/>
    <circle class="pulse" cx="75" cy="64" r="4.5" fill="#3fb950"/>
    <text x="88" y="69" font-size="13" fill="{'#7ee2a0' if theme_name == 'dark' else '#1a7f37'}" font-family="{MONO}">open to opportunities</text>

    <text x="54" y="140" font-size="54" font-weight="700" fill="{t['title']}" letter-spacing="-0.5">Connor Davies</text>
    <rect x="57" y="158" width="120" height="4" rx="2" fill="url(#accent)"/>
    <text x="56" y="200" font-size="16" fill="{t['muted']}" font-family="{MONO}"><tspan fill="#2f81f7">&gt;</tspan> Applied Computing student · Python &amp; web<tspan class="cursor" fill="#2f81f7"> ▍</tspan></text>

    <rect x="590" y="52" width="260" height="156" rx="12" fill="#0d1117" stroke="#30363d"/>
    <rect x="590" y="52" width="260" height="30" rx="12" fill="#161b22"/>
    <rect x="590" y="70" width="260" height="12" fill="#161b22"/>
    <circle cx="608" cy="67" r="5" fill="#ff5f57"/><circle cx="624" cy="67" r="5" fill="#febc2e"/><circle cx="640" cy="67" r="5" fill="#28c840"/>
    <text x="838" y="71" font-size="11" fill="#6e7681" text-anchor="end" font-family="{MONO}">connor.py</text>
    <g font-family="{MONO}" font-size="13">
      <text x="608" y="110"><tspan fill="#ff7b72">class</tspan><tspan fill="#d2a8ff"> Connor</tspan><tspan fill="#c9d1d9">:</tspan></text>
      <text x="626" y="134"><tspan fill="#c9d1d9">role = </tspan><tspan fill="#a5d6ff">"student"</tspan></text>
      <text x="626" y="158"><tspan fill="#c9d1d9">since = </tspan><tspan fill="#79c0ff">2018</tspan></text>
      <text x="626" y="182"><tspan fill="#c9d1d9">loves = </tspan><tspan fill="#a5d6ff">"machine learning"</tspan></text>
    </g>
  </g>
</svg>
"""


# ---------------------------------------------------------------- project cards

def window(t, x, y, w, h, title):
    """A small desktop-app window frame; returns (svg, content_top_y)."""
    svg = f"""
  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{t['card']}" stroke="{t['card_border']}"/>
  <rect x="{x}" y="{y}" width="{w}" height="24" rx="8" fill="{t['bar']}"/>
  <rect x="{x}" y="{y + 16}" width="{w}" height="8" fill="{t['bar']}"/>
  <line x1="{x}" y1="{y + 24}" x2="{x + w}" y2="{y + 24}" stroke="{t['card_border']}"/>
  <circle cx="{x + 14}" cy="{y + 12}" r="4" fill="#ff5f57"/><circle cx="{x + 27}" cy="{y + 12}" r="4" fill="#febc2e"/><circle cx="{x + 40}" cy="{y + 12}" r="4" fill="#28c840"/>
  <text x="{x + w / 2}" y="{y + 16}" font-size="11" fill="{t['muted']}" text-anchor="middle">{escape(title)}</text>"""
    return svg, y + 24


def field(t, x, y, w, text, mono=False):
    font = f' font-family="{MONO}"' if mono else ""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="22" rx="4" fill="{t["field"]}" stroke="{t["card_border"]}"/>'
            f'<text x="{x + 8}" y="{y + 15}" font-size="11" fill="{t["text"]}"{font}>{escape(text)}</text>')


def button(x, y, w, text, colour="#2f81f7"):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="22" rx="4" fill="{colour}"/>'
            f'<text x="{x + w / 2}" y="{y + 15}" font-size="11" font-weight="600" fill="#ffffff" text-anchor="middle">{escape(text)}</text>')


def label(t, x, y, text, size=11, colour=None, weight="400", mono=False):
    font = f' font-family="{MONO}"' if mono else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{colour or t["muted"]}"{font}>{escape(text)}</text>'


def slider(t, x, y, w, value_fraction, text):
    knob = x + w * value_fraction
    return (label(t, x, y, text) +
            f'<rect x="{x}" y="{y + 8}" width="{w}" height="4" rx="2" fill="{t["divider"]}"/>'
            f'<rect x="{x}" y="{y + 8}" width="{knob - x}" height="4" rx="2" fill="#2f81f7"/>'
            f'<circle cx="{knob}" cy="{y + 10}" r="6" fill="#ffffff" stroke="#2f81f7" stroke-width="2"/>')


def preview_url_shortener(t):
    frame, top = window(t, 40, 22, 340, 136, "URL Shortener")
    body = (label(t, 58, top + 22, "Enter URL:", colour=t["text"]) +
            field(t, 58, top + 30, 304, "https://www.example.com/blog/2026/how-to-write-a-good-readme") +
            button(58, top + 62, 80, "Shorten") +
            label(t, 150, top + 77, "Shortened URL copied to clipboard!", colour="#3fb950", weight="600"))
    return frame + body


def preview_password_generator(t):
    frame, top = window(t, 40, 22, 340, 136, "Password Generator")
    body = (label(t, 58, top + 18, "Password Strength:", colour=t["text"]) +
            f'<rect x="170" y="{top + 6}" width="110" height="18" rx="4" fill="{t["field"]}" stroke="{t["card_border"]}"/>'
            f'<text x="178" y="{top + 19}" font-size="11" fill="{t["text"]}">Very Strong   ▾</text>' +
            slider(t, 58, top + 42, 130, 0.3, "Digits: 3") +
            slider(t, 214, top + 42, 130, 0.2, "Special characters: 2") +
            button(58, top + 70, 120, "Generate Password") +
            label(t, 190, top + 85, "kQ7r$Lw2nX9!", size=12, colour=t["title"], weight="700", mono=True))
    return frame + body


def preview_strength_checker(t):
    frame, top = window(t, 40, 22, 340, 136, "Password Strength Checker")
    body = (label(t, 58, top + 22, "Password:", colour=t["text"]) +
            field(t, 116, top + 8, 150, "••••••••••••") +
            f'<rect x="278" y="{top + 12}" width="13" height="13" rx="3" fill="none" stroke="{t["muted"]}"/>' +
            label(t, 297, top + 22, "Show") +
            button(150, top + 38, 120, "Check Password") +
            label(t, 92, top + 78, "Strong: Password strength score: 4/5", colour=t["text"], weight="600") +
            f'<rect x="70" y="{top + 88}" width="280" height="8" rx="4" fill="{t["divider"]}"/>'
            f'<rect x="70" y="{top + 88}" width="280" height="8" rx="4" fill="#3fb950"/>')
    return frame + body


def preview_word_counter(t):
    lines = [
        ("#3fb950", "$ ", "python word_counter_program.py"),
        (t["faint"], "", "Word count completed and saved to word_count.txt"),
        ("#3fb950", "$ ", "head -4 word_count.txt"),
        ("#a5d6ff", "", "the: 42"),
        ("#a5d6ff", "", "and: 31"),
        ("#a5d6ff", "", "python: 18"),
        ("#a5d6ff", "", "code: 12"),
    ]
    svg = (f'<rect x="40" y="22" width="340" height="136" rx="8" fill="#0d1117" stroke="{t["card_border"]}"/>'
           f'<circle cx="54" cy="34" r="4" fill="#ff5f57"/><circle cx="67" cy="34" r="4" fill="#febc2e"/><circle cx="80" cy="34" r="4" fill="#28c840"/>'
           f'<text x="210" y="38" font-size="11" fill="#6e7681" text-anchor="middle" font-family="{MONO}">terminal</text>')
    for i, (colour, prompt, text) in enumerate(lines):
        y = 62 + i * 14
        text_colour = "#c9d1d9" if prompt else colour
        svg += (f'<text x="54" y="{y}" font-size="11" font-family="{MONO}">'
                f'<tspan fill="{colour}">{escape(prompt)}</tspan><tspan fill="{text_colour}">{escape(text)}</tspan></text>')
    return svg


PROJECTS = [
    ("url-shortener", "URL Shortener", "Desktop app that shortens links via TinyURL",
     "and copies them to your clipboard.", "Tkinter", preview_url_shortener),
    ("password-generator", "Password Generator", "Pick a strength, digits and symbols, and get a",
     "random password copied to your clipboard.", "PyQt5", preview_password_generator),
    ("password-strength-checker", "Password Strength Checker", "Scores passwords, checks them against a list",
     "of common passwords and suggests fixes.", "CustomTkinter", preview_strength_checker),
    ("word-counter", "Word Counter", "Counts how often each word appears in a text",
     "file and saves a ranked list.", "Standard library", preview_word_counter),
]


def build_card(t, project):
    _, title, line1, line2, library, preview = project
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="420" height="270" viewBox="0 0 420 270" font-family="{FONT}">
  <rect x="0.5" y="0.5" width="419" height="269" rx="12" fill="{t['card']}" stroke="{t['card_border']}"/>
  <rect x="1" y="1" width="418" height="178" rx="12" fill="{t['bar']}"/>
  <rect x="1" y="160" width="418" height="20" fill="{t['bar']}"/>
  <line x1="0.5" y1="180" x2="419.5" y2="180" stroke="{t['card_border']}"/>
  {preview(t)}
  <text x="22" y="206" font-size="16" font-weight="700" fill="{t['title']}">{escape(title)}</text>
  <text x="22" y="226" font-size="12" fill="{t['muted']}">{escape(line1)}</text>
  <text x="22" y="242" font-size="12" fill="{t['muted']}">{escape(line2)}</text>
  <text x="398" y="206" font-size="11" fill="{t['muted']}" text-anchor="end"><tspan fill="{PYTHON_COLOUR}">●</tspan> Python · {escape(library)}</text>
  <text x="398" y="252" font-size="12" font-weight="600" fill="{t['link']}" text-anchor="end">View repo →</text>
</svg>
"""


# ---------------------------------------------------------------- now building

NOW_BUILDING = [
    ("Websites for local businesses", "Designing and launching sites for real clients", "#2f81f7"),
    ("Open-sourcing my past projects", "Cleaning up code and writing proper docs", "#8b5cf6"),
    ("Learning machine learning", "Understanding the theory behind my bots", "#3fb950"),
]


def build_now(t):
    rows = ""
    for i, (title, detail, colour) in enumerate(NOW_BUILDING):
        y = 70 + i * 50
        rows += f"""
  <rect x="24" y="{y}" width="852" height="40" rx="8" fill="{t['bar']}" stroke="{t['divider']}"/>
  <rect x="24" y="{y}" width="4" height="40" rx="2" fill="{colour}"/>
  <text x="44" y="{y + 25}" font-size="14" font-weight="600" fill="{t['title']}">{escape(title)}</text>
  <text x="330" y="{y + 25}" font-size="13" fill="{t['muted']}">{escape(detail)}</text>
  <rect x="766" y="{y + 10}" width="96" height="20" rx="10" fill="{colour}" fill-opacity="0.14" stroke="{colour}" stroke-opacity="0.5"/>
  <circle class="pulse" cx="780" cy="{y + 20}" r="3.5" fill="{colour}"/>
  <text x="790" y="{y + 24}" font-size="11" font-weight="600" fill="{colour}">in progress</text>"""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="900" height="230" viewBox="0 0 900 230" font-family="{FONT}">
  <style>.pulse {{ animation: pulse 2s ease-in-out infinite; }} @keyframes pulse {{ 50% {{ opacity: 0.3; }} }}</style>
  <rect x="0.5" y="0.5" width="899" height="229" rx="12" fill="{t['card']}" stroke="{t['card_border']}"/>
  <text x="24" y="44" font-size="18" font-weight="700" fill="{t['title']}">Currently building</text>
  <text x="876" y="44" font-size="12" fill="{t['faint']}" text-anchor="end" font-family="{MONO}">updated Nov 2026</text>{rows}
</svg>
"""


# ---------------------------------------------------------------- featured project

FEATURED_STATS = [
    ("200k", "peak steps / second"),
    ("4,096", "arenas at once"),
    ("1 GPU", "RTX 3070"),
]

FEATURED_TAGS = [("C++", "#f34b7d"), ("CUDA", "#3fb950"), ("LibTorch", "#ee4c2c"), ("PPO", "#8b5cf6"), ("CMake", "#58a6ff")]


def build_featured(t):
    # Right-hand visual: a grid of tiny arenas, each with a ball, pulsing in waves
    # to suggest thousands of matches being simulated in one batch.
    arenas = ""
    cols, rows, cell_w, cell_h, gap = 10, 7, 26, 18, 5
    x0, y0 = 548, 62
    for row in range(rows):
        for col in range(cols):
            x = x0 + col * (cell_w + gap)
            y = y0 + row * (cell_h + gap)
            delay = (col + row) * 0.12
            ball_x = x + 5 + ((col * 7 + row * 11) % (cell_w - 10))
            ball_y = y + 4 + ((col * 5 + row * 3) % (cell_h - 8))
            arenas += (f'<rect class="arena" style="animation-delay:{delay:.2f}s" x="{x}" y="{y}" width="{cell_w}" height="{cell_h}" rx="4" '
                       f'fill="#2f81f7" fill-opacity="0.10" stroke="#2f81f7" stroke-opacity="0.35"/>'
                       f'<line x1="{x + cell_w / 2}" y1="{y + 2}" x2="{x + cell_w / 2}" y2="{y + cell_h - 2}" stroke="#2f81f7" stroke-opacity="0.25"/>'
                       f'<circle cx="{ball_x}" cy="{ball_y}" r="2" fill="#f0f6fc" fill-opacity="0.85"/>')

    stats = ""
    for i, (value, caption) in enumerate(FEATURED_STATS):
        x = 40 + i * 150
        stats += (f'<text x="{x}" y="200" font-size="26" font-weight="700" fill="{t["title"]}">{escape(value)}</text>'
                  f'<text x="{x}" y="220" font-size="12" fill="{t["muted"]}">{escape(caption)}</text>')

    tags, tag_x = "", 40
    for name, colour in FEATURED_TAGS:
        width = 16 + 7.2 * len(name)
        tags += (f'<rect x="{tag_x}" y="246" width="{width:.0f}" height="22" rx="11" fill="{colour}" fill-opacity="0.14" stroke="{colour}" stroke-opacity="0.5"/>'
                 f'<text x="{tag_x + width / 2:.0f}" y="261" font-size="11.5" font-weight="600" fill="{colour}" text-anchor="middle">{escape(name)}</text>')
        tag_x += width + 8

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="900" height="300" viewBox="0 0 900 300" font-family="{FONT}">
  <defs>
    <linearGradient id="fbg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{t['bg_a']}"/><stop offset="1" stop-color="{t['bg_b']}"/></linearGradient>
    <linearGradient id="faccent" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2f81f7"/><stop offset="1" stop-color="#8b5cf6"/></linearGradient>
    <radialGradient id="fglow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#8b5cf6" stop-opacity="0.25"/><stop offset="1" stop-color="#8b5cf6" stop-opacity="0"/></radialGradient>
    <clipPath id="fround"><rect width="900" height="300" rx="16"/></clipPath>
  </defs>
  <style>
    .arena {{ animation: wave 2.4s ease-in-out infinite; }}
    @keyframes wave {{ 0%, 100% {{ fill-opacity: 0.08; }} 50% {{ fill-opacity: 0.32; }} }}
    .pulse {{ animation: pulse 2s ease-in-out infinite; }}
    @keyframes pulse {{ 50% {{ opacity: 0.35; }} }}
  </style>
  <g clip-path="url(#fround)">
    <rect width="900" height="300" fill="url(#fbg)"/>
    <circle cx="720" cy="150" r="230" fill="url(#fglow)"/>
    <rect x="0" y="0" width="900" height="4" fill="url(#faccent)"/>
    <rect x="0.5" y="0.5" width="899" height="299" rx="16" fill="none" stroke="{t['frame']}"/>

    <rect x="40" y="34" width="150" height="24" rx="12" fill="#f0883e" fill-opacity="0.14" stroke="#f0883e" stroke-opacity="0.55"/>
    <circle class="pulse" cx="56" cy="46" r="4" fill="#f0883e"/>
    <text x="68" y="50.5" font-size="11.5" font-weight="700" fill="#f0883e" letter-spacing="0.6">FEATURED PROJECT</text>

    <text x="40" y="104" font-size="38" font-weight="700" fill="{t['title']}" letter-spacing="-0.5">GigaLearnGPU</text>
    <text x="40" y="134" font-size="15" fill="{t['text']}">Trains Rocket League bots with reinforcement learning,</text>
    <text x="40" y="154" font-size="15" fill="{t['text']}">running thousands of matches at once on one GPU.</text>
    {stats}
    {tags}

    <text x="548" y="50" font-size="11" fill="{t['faint']}" font-family="{MONO}">batched CUDA physics · every arena, one step</text>
    {arenas}
    <text x="852" y="250" font-size="11" fill="{t['faint']}" text-anchor="end" font-family="{MONO}">70 of 4,096 arenas shown</text>
    <text x="852" y="276" font-size="13" font-weight="600" fill="{t['link']}" text-anchor="end">View repo →</text>
  </g>
</svg>
"""


def main():
    for name, t in THEMES.items():
        write("featured", name, build_featured(t))
        write("header", name, build_header(name, t))
        write("now", name, build_now(t))
        for project in PROJECTS:
            write(project[0], name, build_card(t, project))
    print("Built assets in", OUTPUT_DIR)


if __name__ == "__main__":
    main()
