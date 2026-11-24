file_path = r'c:\Users\kanika lotlekar\krishi netra frontend\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Layout CSS: Remove fixed sidebar width from .main and .app
old_main_css = """.main{
    margin-left:260px;
    width:calc(100% - 260px);
}"""

new_main_css = """/* FULL WIDTH APP & MAIN */
.app{
    display:flex;
    flex-direction:column;
    min-height:100vh;
    background:var(--bg);
}

.main{
    margin-left:0 !important;
    width:100% !important;
    display:flex;
    flex-direction:column;
    min-height:100vh;
}"""

html = html.replace(old_main_css, new_main_css, 1)

# 2. Add Top Navigation styling
top_nav_css = """
/* TOPBAR BRAND */
.topbar-brand{
    display:flex;
    align-items:center;
    gap:12px;
    cursor:pointer;
    flex-shrink:0;
    text-decoration:none;
}
.topbar-brand .logo-icon{
    width:42px;
    height:42px;
    border-radius:13px;
    background:linear-gradient(135deg,#10b981,#047857);
    display:grid;
    place-items:center;
    font-size:22px;
    box-shadow:0 4px 14px rgba(16,185,129,0.35);
}
.topbar-brand h1{
    font-size:18px;
    font-weight:900;
    letter-spacing:.3px;
    color:#0f172a;
    line-height:1.15;
}
.topbar-brand span{
    display:block;
    color:#059669;
    font-size:9.5px;
    font-weight:800;
    letter-spacing:.8px;
    margin-top:2px;
}

/* HORIZONTAL TOP NAVIGATION */
.top-nav{
    display:flex;
    align-items:center;
    gap:6px;
    background:#f1f5f9;
    border:1px solid var(--border);
    border-radius:30px;
    padding:4px;
    flex-wrap:nowrap;
    overflow-x:auto;
    scrollbar-width:none;
}
.top-nav::-webkit-scrollbar{
    display:none;
}
.top-nav button{
    color:#475569;
    background:transparent;
    padding:8px 14px;
    border-radius:24px;
    display:flex;
    gap:7px;
    align-items:center;
    transition:all .2s ease;
    font-size:12.5px;
    font-weight:700;
    white-space:nowrap;
    border:0;
    cursor:pointer;
}
.top-nav button:hover{
    color:#0f172a;
    background:#e2e8f0;
}
.top-nav button.active{
    background:#10b981;
    color:white;
    box-shadow:0 3px 10px rgba(16,185,129,.35);
}
.top-nav button.active .nav-badge{
    background:white;
    color:#dc2626;
}
.top-nav .nav-icon{
    font-size:14px;
}
.top-nav .nav-badge{
    background:#fee2e2;
    color:#dc2626;
    padding:1px 6px;
    border-radius:10px;
    font-size:9.5px;
    font-weight:800;
}
"""

# Insert top_nav_css above .topbar{
html = html.replace('.topbar{', top_nav_css + '\n.topbar{', 1)

# 3. Update topbar min-height and padding
html = html.replace('height:74px;', 'min-height:76px;', 1)

# 4. Remove the <aside class="sidebar">...</aside> block and replace <header class="topbar">
sidebar_pattern_start = '<!-- SIDEBAR -->'
sidebar_pattern_end = '</header>'

start_pos = html.find(sidebar_pattern_start)
end_pos = html.find(sidebar_pattern_end, start_pos)

if start_pos != -1 and end_pos != -1:
    end_pos += len(sidebar_pattern_end)
    
    new_header_html = """<!-- TOPBAR WITH INTEGRATED BRAND & HORIZONTAL NAVIGATION -->
<main class="main">

<header class="topbar">

    <!-- Brand Logo -->
    <div class="topbar-brand" onclick="showSectionByName('dashboard')" title="KRISHI NETRA — Home">
        <div class="logo-icon">🌱</div>
        <div>
            <h1>KRISHI NETRA</h1>
            <span data-i18n="appTagline">INTELLIGENT AGRICULTURE</span>
        </div>
    </div>

    <!-- Center Horizontal Navigation -->
    <nav class="top-nav" id="topNav">
        <button class="active" onclick="showSection('dashboard',this)">
            <span class="nav-icon">⌂</span> <span data-i18n="navDashboard">Dashboard</span>
        </button>

        <button onclick="showSection('detect',this)">
            <span class="nav-icon">🔍</span> <span data-i18n="navDetect">Detect Pest</span>
        </button>

        <button onclick="showSection('history',this)">
            <span class="nav-icon">🕘</span> <span data-i18n="navHistory">Detection History</span>
        </button>

        <button onclick="showSection('alerts',this)">
            <span class="nav-icon">🔔</span> <span data-i18n="navAlerts">Alerts</span>
            <span class="nav-badge" id="navAlertBadge">4</span>
        </button>

        <button onclick="showSection('frequency',this)">
            <span class="nav-icon">〰️</span> <span data-i18n="navFrequency">Frequency Control</span>
        </button>

        <button onclick="showSection('beneficial',this)">
            <span class="nav-icon">🐝</span> <span data-i18n="navBeneficial">Beneficial Insects</span>
        </button>
    </nav>

    <!-- Right Actions: Language, Weather, Notifications, Profile -->
    <div class="top-actions">
        <div class="lang-segmented-bar" title="Language / भाषा">
            <button class="lang-pill-btn active" id="btnLangEn" onclick="setLanguage('en')">EN</button>
            <button class="lang-pill-btn" id="btnLangHi" onclick="setLanguage('hi')">हिंदी</button>
            <button class="lang-pill-btn" id="btnLangMr" onclick="setLanguage('mr')">मराठी</button>
        </div>

        <div class="weather-badge" id="weatherDisplay" title="Live meteorological telemetry">
            <span class="live-dot"></span>
            <span id="weatherIcon">☀️</span>
            <span id="weatherTemp">24.0°C</span>
            <span style="color:var(--muted);font-size:11px;" id="weatherWind">Wind 5.8 km/h</span>
        </div>

        <button class="icon-btn" onclick="showSectionByName('alerts'); showToast('Showing active alerts')">
            🔔
            <span class="notification-dot" id="topNotificationDot"></span>
        </button>

        <div class="profile" onclick="showSectionByName('profile')">
            <div class="avatar" id="topAvatar">SY</div>
            <span style="font-size:12px;font-weight:700;" id="topFarmerName">shivil yadav</span>
        </div>
    </div>

</header>"""
    
    html = html[:start_pos] + new_header_html + html[end_pos:]
    print("Sidebar replaced with Top Navigation Bar in Header!")
else:
    print("Warning: Could not locate sidebar / header boundary!")

# 5. In JS showSection, make button selector check both .top-nav button and .nav button
html = html.replace('document.querySelectorAll(".nav button").forEach', 'document.querySelectorAll(".top-nav button, .nav button").forEach')
html = html.replace('document.querySelector(`.nav button[onclick*="\'${id}\'"]`)', 'document.querySelector(`.top-nav button[onclick*="\'${id}\'"], .nav button[onclick*="\'${id}\'"]`)')
html = html.replace('document.querySelectorAll(".nav button")', 'document.querySelectorAll(".top-nav button, .nav button")')

# Remove duplicate </aside> if any
html = html.replace('</aside>', '')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html successfully!")
