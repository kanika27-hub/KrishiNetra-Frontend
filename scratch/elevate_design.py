import re

file_path = r'c:\Users\kanika lotlekar\krishi netra frontend\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Plus Jakarta Sans font import at top of <style>
font_import = """@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap');

:root{
    --green:#10b981;
    --green-dark:#059669;
    --green-deep:#047857;
    --green-light:#ecfdf5;
    --lime:#84cc16;
    --orange:#f59e0b;
    --red:#ef4444;
    --blue:#3b82f6;
    --dark:#0f172a;
    --text:#1e293b;
    --muted:#64748b;
    --bg:#f8fafc;
    --white:#ffffff;
    --border:#e2e8f0;
    --shadow:0 4px 20px -2px rgba(0,0,0,0.05), 0 2px 6px -1px rgba(0,0,0,0.03);
    --shadow-hover:0 20px 30px -10px rgba(16,185,129,0.16), 0 10px 10px -5px rgba(0,0,0,0.04);
}"""

old_root_pattern = re.compile(r':root\{[^}]+\}', re.DOTALL)
html = old_root_pattern.sub(font_import, html, count=1)

# Update font family to Plus Jakarta Sans
html = html.replace('font-family:Inter,Segoe UI,Arial,sans-serif;', "font-family:'Plus Jakarta Sans',Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;")

# 2. Upgrade Language Switcher to Segmented Pill Bar
lang_segmented_css = """
/* Segmented Language Bar */
.lang-segmented-bar{
    display:flex;
    align-items:center;
    background:#f1f5f9;
    border:1px solid var(--border);
    border-radius:24px;
    padding:3px;
    gap:2px;
}
.lang-pill-btn{
    border:0;
    background:transparent;
    font-size:11.5px;
    font-weight:700;
    color:var(--muted);
    padding:4px 10px;
    border-radius:20px;
    cursor:pointer;
    transition:all .2s ease;
    line-height:1.2;
}
.lang-pill-btn:hover{
    color:var(--text);
}
.lang-pill-btn.active{
    background:var(--green-dark);
    color:white;
    box-shadow:0 2px 8px rgba(5,150,105,.35);
}
@media(max-width:600px){
    .lang-pill-btn{ padding:3px 7px; font-size:10.5px; }
}
"""

if '.lang-segmented-bar' not in html:
    html = html.replace('.lang-selector-wrap{', lang_segmented_css + '\n.lang-selector-wrap{', 1)

# Upgrade .topbar, .weather-badge, .profile, .card, .stat styles
upgraded_styles = """
.topbar{
    background:rgba(255,255,255,.94);
    backdrop-filter:blur(14px);
    -webkit-backdrop-filter:blur(14px);
    border-bottom:1px solid var(--border);
    height:74px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:0 32px;
    position:sticky;
    top:0;
    z-index:90;
    box-shadow:0 2px 12px rgba(0,0,0,.03);
}

.weather-badge{
    display:flex;
    align-items:center;
    gap:9px;
    background:white;
    border:1.5px solid var(--border);
    padding:6px 16px;
    border-radius:30px;
    font-size:12px;
    font-weight:600;
    box-shadow:0 2px 8px rgba(0,0,0,.03);
    transition:all .2s;
}
.weather-badge:hover{
    border-color:var(--green);
    transform:translateY(-1px);
}

.weather-badge .live-dot{
    width:8px;
    height:8px;
    border-radius:50%;
    background:#10b981;
    box-shadow:0 0 8px #10b981;
    animation:pulseDot 2s infinite;
}

.profile{
    display:flex;
    align-items:center;
    gap:10px;
    cursor:pointer;
    padding:4px 10px 4px 4px;
    border-radius:30px;
    background:white;
    border:1.5px solid var(--border);
    box-shadow:0 2px 8px rgba(0,0,0,.03);
    transition:all .2s;
}
.profile:hover{
    border-color:var(--green);
    transform:translateY(-1px);
}

.avatar{
    width:34px;
    height:34px;
    background:linear-gradient(135deg,#d1fae5,#a7f3d0);
    border-radius:50%;
    display:grid;
    place-items:center;
    font-weight:800;
    font-size:12px;
    color:var(--green-deep);
}

/* REAL-TIME ADVISORY STRIP */
.realtime-advisory{
    background:linear-gradient(90deg, #ecfdf5 0%, #f0fdf4 60%, #ffffff 100%);
    border-bottom:1px solid #d1fae5;
    padding:11px 32px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    font-size:12px;
    color:#065f46;
    font-weight:600;
    box-shadow:0 2px 8px rgba(16,185,129,.04);
}

.realtime-advisory span.pulse-tag{
    background:linear-gradient(135deg,#10b981,#059669);
    color:white;
    font-size:10px;
    font-weight:800;
    padding:3px 9px;
    border-radius:20px;
    letter-spacing:.6px;
    margin-right:10px;
    box-shadow:0 2px 8px rgba(16,185,129,.35);
}

/* CARDS & STATS UPGRADE */
.card{
    background:white;
    border:1px solid var(--border);
    border-radius:20px;
    padding:22px;
    box-shadow:var(--shadow);
    transition:all .25s cubic-bezier(0.16,1,0.3,1);
}

.card:hover{
    box-shadow:0 12px 30px -6px rgba(0,0,0,0.08);
}

.stat{
    position:relative;
    overflow:hidden;
    background:white;
    border:1px solid var(--border);
}
.stat:hover{
    transform:translateY(-4px);
    box-shadow:var(--shadow-hover);
}
.stat.stat-pests{
    background:linear-gradient(180deg, rgba(236,253,245,.5) 0%, #ffffff 45%);
}
.stat.stat-alerts{
    background:linear-gradient(180deg, rgba(254,243,199,.45) 0%, #ffffff 45%);
}
.stat.stat-ecosystem{
    background:linear-gradient(180deg, rgba(240,253,244,.6) 0%, #ffffff 45%);
}

.stat-icon{
    width:46px;
    height:46px;
    display:grid;
    place-items:center;
    border-radius:14px;
    font-size:22px;
    box-shadow:0 4px 12px rgba(0,0,0,.05);
}
.stat-icon.icon-pests{
    background:linear-gradient(135deg,#d1fae5,#a7f3d0);
}
.stat-icon.icon-alerts{
    background:linear-gradient(135deg,#fef3c7,#fde68a);
}
.stat-icon.icon-eco{
    background:linear-gradient(135deg,#dcfce7,#bbf7d0);
}

.stat-number{
    font-size:36px;
    font-weight:900;
    letter-spacing:-1px;
    margin:14px 0 2px;
    color:#0f172a;
    font-feature-settings:'tnum';
}

.primary{
    background:linear-gradient(135deg,#10b981 0%,#059669 100%);
    color:white;
    padding:11px 20px;
    border-radius:12px;
    font-weight:700;
    font-size:13px;
    transition:all .2s;
    display:inline-flex;
    align-items:center;
    gap:6px;
    box-shadow:0 4px 16px rgba(16,185,129,.35);
}
.primary:hover{
    background:linear-gradient(135deg,#059669 0%,#047857 100%);
    transform:translateY(-2px);
    box-shadow:0 8px 24px rgba(16,185,129,.45);
}

.secondary{
    background:white;
    color:#1e293b;
    border:1.5px solid var(--border);
    padding:10px 18px;
    border-radius:12px;
    font-weight:700;
    font-size:13px;
    transition:all .2s;
    box-shadow:0 2px 6px rgba(0,0,0,.03);
}
.secondary:hover{
    background:#f0fdf4;
    border-color:var(--green);
    color:var(--green-deep);
    transform:translateY(-1px);
}
"""

# Replace old topbar / stat CSS
old_topbar_css = re.search(r'\.topbar\{.*?\.realtime-advisory span\.pulse-tag\{.*?\}', html, re.DOTALL)
if old_topbar_css:
    html = html.replace(old_topbar_css.group(0), upgraded_styles, 1)

# 3. Replace the Language Selector HTML in topbar with Segmented Pill Group + keep select synced
segmented_html = """        <div class="lang-segmented-bar" title="Language / भाषा">
            <button class="lang-pill-btn active" id="btnLangEn" onclick="setLanguage('en')">EN</button>
            <button class="lang-pill-btn" id="btnLangHi" onclick="setLanguage('hi')">हिंदी</button>
            <button class="lang-pill-btn" id="btnLangMr" onclick="setLanguage('mr')">मराठी</button>
        </div>"""

old_selector_pattern = re.search(r'<div class="lang-selector-wrap".*?</div>', html, re.DOTALL)
if old_selector_pattern:
    html = html.replace(old_selector_pattern.group(0), segmented_html, 1)

# 4. Add stat classes to the 3 dashboard stat cards
html = html.replace('<div class="card stat">\n            <div class="stat-top">\n                <div>\n                    <small style="color:var(--muted)" data-i18n="statTotalDetections">TOTAL DETECTIONS</small>\n                </div>\n                <div class="stat-icon">🐛</div>',
                    '<div class="card stat stat-pests">\n            <div class="stat-top">\n                <div>\n                    <small style="color:var(--muted);font-weight:700;letter-spacing:.6px;" data-i18n="statTotalDetections">TOTAL DETECTIONS</small>\n                </div>\n                <div class="stat-icon icon-pests">🐛</div>', 1)

html = html.replace('<div class="card stat">\n            <div class="stat-top">\n                <div>\n                    <small style="color:var(--muted)" data-i18n="statAttentionRequired">ATTENTION REQUIRED</small>\n                </div>\n                <div class="stat-icon">🚨</div>',
                    '<div class="card stat stat-alerts">\n            <div class="stat-top">\n                <div>\n                    <small style="color:var(--muted);font-weight:700;letter-spacing:.6px;" data-i18n="statAttentionRequired">ATTENTION REQUIRED</small>\n                </div>\n                <div class="stat-icon icon-alerts">🚨</div>', 1)

html = html.replace('<div class="card stat">\n            <div class="stat-top">\n                <div>\n                    <small style="color:var(--muted)" data-i18n="statEcosystemHealth">ECOSYSTEM HEALTH</small>\n                </div>\n                <div class="stat-icon">🐝</div>',
                    '<div class="card stat stat-ecosystem">\n            <div class="stat-top">\n                <div>\n                    <small style="color:var(--muted);font-weight:700;letter-spacing:.6px;" data-i18n="statEcosystemHealth">ECOSYSTEM HEALTH</small>\n                </div>\n                <div class="stat-icon icon-eco">🐝</div>', 1)

# 5. In JS setLanguage(), update segmented pill button active states
set_lang_pill_sync = """
    // Update segmented language buttons
    ['en','hi','mr'].forEach(l => {
        const btn = document.getElementById('btnLang' + l.charAt(0).toUpperCase() + l.slice(1));
        if(btn) btn.classList.toggle('active', l === lang);
    });
"""

if 'btnLangEn' not in html and 'const select = document.getElementById(\'langSelect\');' in html:
    html = html.replace("const select = document.getElementById('langSelect');",
                        set_lang_pill_sync + "\n    const select = document.getElementById('langSelect');", 1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Visual design successfully elevated and modern aesthetic applied!")
