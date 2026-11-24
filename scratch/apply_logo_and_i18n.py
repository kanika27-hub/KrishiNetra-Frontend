# -*- coding: utf-8 -*-
"""
Script to:
1. Embed Krishinetra logo into topbar brand place (using assets/krishinetra_logo.png)
2. Style the segmented pill language switcher to match the EN | HI | MR screenshot
3. Add comprehensive i18n data attributes across the entire web application
4. Add comprehensive English, Hindi, Marathi translations to TRANSLATIONS
5. Ensure setLanguage seamlessly updates every section of the UI
"""

import os
import re

html_path = "index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add .brand-logo-img CSS in topbar brand styles
brand_css_old = """.topbar-brand .logo-icon{
    width:42px;
    height:42px;
    border-radius:13px;
    background:linear-gradient(135deg,#10b981,#047857);
    display:grid;
    place-items:center;
    font-size:22px;
    box-shadow:0 4px 14px rgba(16,185,129,0.35);
}"""

brand_css_new = """.topbar-brand .brand-logo-img{
    width:42px;
    height:42px;
    border-radius:12px;
    object-fit:contain;
    background:#ffffff;
    border:1.5px solid rgba(16,185,129,0.35);
    box-shadow:0 3px 12px rgba(16,185,129,0.25);
    padding:2px;
    transition:transform .2s ease;
    flex-shrink:0;
}
.topbar-brand:hover .brand-logo-img{
    transform:scale(1.05);
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
}"""

if brand_css_old in content:
    content = content.replace(brand_css_old, brand_css_new, 1)
    print("Updated brand CSS")

# 2. Update .lang-segmented-bar CSS to match EN HI MR reference
lang_css_old = """.lang-segmented-bar{
    display:flex;
    align-items:center;
    background:#111e15;
    border:1.5px solid #1e3626;
    border-radius:30px;
    padding:3px;
    gap:1px;
    flex-shrink:0;
}
.lang-pill-btn{
    background:transparent;
    color:#4a6b52;
    border:0;
    padding:5px 14px;
    border-radius:24px;
    font-size:11.5px;
    font-weight:800;
    cursor:pointer;
    transition:all .18s ease;
    white-space:nowrap;
    line-height:1.4;
    letter-spacing:.6px;
    text-transform:uppercase;
}
.lang-pill-btn:hover{
    color:#86c48e;
}
.lang-pill-btn.active{
    background:#4ade80;
    color:#071209;
    box-shadow:0 2px 14px rgba(74,222,128,.55);
}"""

lang_css_new = """.lang-segmented-bar{
    display:inline-flex;
    align-items:center;
    background:#07140b;
    border:1.5px solid #142a19;
    border-radius:30px;
    padding:3px;
    gap:1px;
    flex-shrink:0;
    box-shadow:inset 0 1px 4px rgba(0,0,0,0.5);
}
.lang-pill-btn{
    background:transparent;
    color:#75957d;
    border:0;
    padding:5px 13px;
    border-radius:22px;
    font-size:12px;
    font-weight:800;
    cursor:pointer;
    transition:all .18s cubic-bezier(0.4, 0, 0.2, 1);
    white-space:nowrap;
    line-height:1.3;
    letter-spacing:.6px;
    text-transform:uppercase;
}
.lang-pill-btn:hover{
    color:#a9dcb3;
}
.lang-pill-btn.active{
    background:#76c820;
    color:#061408;
    box-shadow:0 2px 12px rgba(118,200,32,.45);
}"""

if lang_css_old in content:
    content = content.replace(lang_css_old, lang_css_new, 1)
    print("Updated language pill bar CSS")

# 3. Update Brand in Topbar HTML
topbar_brand_old = """    <!-- Brand Logo -->
    <div class="topbar-brand" onclick="showSectionByName('dashboard')" title="KRISHI NETRA — Home">
        <div class="logo-icon">🌱</div>
        <div>
            <h1>KRISHI NETRA</h1>
            <span data-i18n="appTagline">INTELLIGENT AGRICULTURE</span>
        </div>
    </div>"""

topbar_brand_new = """    <!-- Brand Logo -->
    <div class="topbar-brand" onclick="showSectionByName('dashboard')" title="KRISHI NETRA — Home">
        <img src="assets/krishinetra_logo.png" alt="KRISHI NETRA" class="brand-logo-img">
        <div>
            <h1 data-i18n="appName">KRISHI NETRA</h1>
            <span data-i18n="appTagline">INTELLIGENT AGRICULTURE</span>
        </div>
    </div>"""

if topbar_brand_old in content:
    content = content.replace(topbar_brand_old, topbar_brand_new, 1)
    print("Updated Topbar Brand HTML")

# 4. Update Language Segmented Bar HTML to EN, HI, MR
lang_bar_old = """        <div class="lang-segmented-bar" title="Language / भाषा">
            <button class="lang-pill-btn active" id="btnLangEn" onclick="setLanguage('en')">EN</button>
            <button class="lang-pill-btn" id="btnLangHi" onclick="setLanguage('hi')">हिंदी</button>
            <button class="lang-pill-btn" id="btnLangMr" onclick="setLanguage('mr')">मराठी</button>
        </div>"""

lang_bar_new = """        <div class="lang-segmented-bar" title="Language / भाषा / भाषा">
            <button class="lang-pill-btn active" id="btnLangEn" onclick="setLanguage('en')">EN</button>
            <button class="lang-pill-btn" id="btnLangHi" onclick="setLanguage('hi')">HI</button>
            <button class="lang-pill-btn" id="btnLangMr" onclick="setLanguage('mr')">MR</button>
        </div>"""

if lang_bar_old in content:
    content = content.replace(lang_bar_old, lang_bar_new, 1)
    print("Updated Language Segmented Bar HTML")

# 5. Add data-i18n in Sections

# 5a. Dashboard
content = content.replace(
    '<div class="change">2 high priority</div>',
    '<div class="change" data-i18n="statHighPriority">2 high priority</div>'
)
content = content.replace(
    '<h3>Active Alerts</h3>\n                <span class="badge red" id="sideAlertBadge">4</span>',
    '<h3 data-i18n="activeAlertsTitle">Active Alerts</h3>\n                <span class="badge red" id="sideAlertBadge">4</span>'
)
content = content.replace(
    '<h3>Pest Activity — Last 7 Days</h3>\n            <p style="font-size:11px;color:var(--muted);margin-top:5px;">\n                Number of recorded crop pest detections\n            </p>',
    '<h3 data-i18n="pestActivityTitle">Pest Activity — Last 7 Days</h3>\n            <p style="font-size:11px;color:var(--muted);margin-top:5px;" data-i18n="pestActivitySub">\n                Number of recorded crop pest detections\n            </p>'
)
content = content.replace(
    '<strong>🎯 Recommended Action</strong>',
    '<strong data-i18n="recActionHeader">🎯 Recommended Action</strong>'
)

# 5b. Detect Section
content = content.replace(
    '<h2>AI Pest Detection &bull; All Crops Prototype</h2>\n            <p>Upload any crop photo or turn on live camera. Select a crop or let KRISHI NETRA auto-detect.</p>',
    '<h2 data-i18n="detectHeading">AI Pest Detection &bull; All Crops Prototype</h2>\n            <p data-i18n="detectSub">Upload any crop photo or turn on live camera. Select a crop or let KRISHI NETRA auto-detect.</p>'
)
content = content.replace(
    '<h3>Upload or Capture Crop Leaf</h3>\n\n                <p>\n                    Take a clear photograph of infected leaves, stems, or pests across any crop.\n                </p>',
    '<h3 data-i18n="uploadTitle">Upload or Capture Crop Leaf</h3>\n\n                <p data-i18n="uploadDesc">\n                    Take a clear photograph of infected leaves, stems, or pests across any crop.\n                </p>'
)
content = content.replace(
    '<label class="upload-btn" for="imageInput">\n                        📁 Choose Image File\n                    </label>',
    '<label class="upload-btn" for="imageInput" data-i18n="chooseImageBtn">\n                        📁 Choose Image File\n                    </label>'
)
content = content.replace(
    '<button type="button" class="secondary" id="cameraToggleBtn" onclick="toggleCamera()">\n                        📹 Live Camera Scanner\n                    </button>',
    '<button type="button" class="secondary" id="cameraToggleBtn" onclick="toggleCamera()" data-i18n="cameraBtn">\n                        📹 Live Camera Scanner\n                    </button>'
)
content = content.replace(
    'id="detectButton"\n                class="detect-btn"\n                onclick="runDetection()"\n                disabled\n            >\n                🔍 Analyze Image with KRISHI NETRA Vision\n            </button>',
    'id="detectButton"\n                class="detect-btn"\n                onclick="runDetection()"\n                disabled\n                data-i18n="analyzeBtn"\n            >\n                🔍 Analyze Image with KRISHI NETRA Vision\n            </button>'
)
content = content.replace(
    '⚡ Or 1-Click Test Verified Agricultural Leaf Samples:',
    '<span data-i18n="sampleBarTitle">⚡ Or 1-Click Test Verified Agricultural Leaf Samples:</span>'
)
content = content.replace(
    '<h3>Diagnostic Engine Ready</h3>\n                <p style="margin-top:8px;">\n                    Upload an image, snap a camera frame, or click a crop sample to run computer vision analysis.\n                </p>',
    '<h3 data-i18n="engineReadyTitle">Diagnostic Engine Ready</h3>\n                <p style="margin-top:8px;" data-i18n="engineReadyDesc">\n                    Upload an image, snap a camera frame, or click a crop sample to run computer vision analysis.\n                </p>'
)
content = content.replace(
    '<span>Severity Status</span>',
    '<span data-i18n="labelSeverity">Severity Status</span>'
)
content = content.replace(
    '<span>Crop &amp; Zone</span>',
    '<span data-i18n="labelCropZone">Crop &amp; Zone</span>'
)
content = content.replace(
    '<span>Scientific Name</span>',
    '<span data-i18n="labelScientific">Scientific Name</span>'
)
content = content.replace(
    '<span>Prototype Deterrence Freq</span>',
    '<span data-i18n="labelFrequency">Prototype Deterrence Freq</span>'
)
content = content.replace(
    '<span>Detection Status</span>\n                        <span style="color:var(--green)">Confirmed by KRISHI NETRA</span>',
    '<span data-i18n="labelStatus">Detection Status</span>\n                        <span style="color:var(--green)" data-i18n="confirmedStatus">Confirmed by KRISHI NETRA</span>'
)
content = content.replace(
    '<strong>🌿 Botanical Damage Assessment</strong>',
    '<strong data-i18n="labelDamage">🌿 Botanical Damage Assessment</strong>'
)
content = content.replace(
    '<strong>🎯 Integrated Pest Management (IPM) Next Steps</strong>',
    '<strong data-i18n="labelIPM">🎯 Integrated Pest Management (IPM) Next Steps</strong>'
)
content = content.replace(
    '✓ Save &amp; Log to Field History\n                    </button>',
    '<span data-i18n="saveHistoryBtn">✓ Save &amp; Log to Field History</span>\n                    </button>'
)
content = content.replace(
    '💬 Share on WhatsApp\n                    </button>',
    '<span data-i18n="shareWhatsAppBtn">💬 Share on WhatsApp</span>\n                    </button>'
)

# 5c. History Section
content = content.replace(
    '<h2>Detection History &bull; All Crops Log</h2>\n            <p>Live chronological record of all farm scans with export capability.</p>',
    '<h2 data-i18n="historyHeading">Detection History &bull; All Crops Log</h2>\n            <p data-i18n="historySub">Live chronological record of all farm scans with export capability.</p>'
)
content = content.replace(
    '<button class="primary" onclick="exportHistoryCSV()">\n            📥 Download CSV Report\n        </button>',
    '<button class="primary" onclick="exportHistoryCSV()">\n            <span data-i18n="downloadCSV">📥 Download CSV Report</span>\n        </button>'
)
content = content.replace(
    'id="historySearch"\n            placeholder="Search by pest, crop, or field location..."',
    'id="historySearch"\n            placeholder="Search by pest, crop, or field location..."\n            data-i18n-placeholder="historySearchPlaceholder"'
)
content = content.replace(
    '<th>PEST / ORGANISM</th>\n                    <th>CROP LOCATION</th>\n                    <th>AI CONFIDENCE</th>\n                    <th>SEVERITY</th>\n                    <th>DETECTION TIME</th>\n                    <th>STATUS</th>',
    '<th data-i18n="thPest">PEST / ORGANISM</th>\n                    <th data-i18n="thCrop">CROP LOCATION</th>\n                    <th data-i18n="thConf">AI CONFIDENCE</th>\n                    <th data-i18n="thSev">SEVERITY</th>\n                    <th data-i18n="thTime">DETECTION TIME</th>\n                    <th data-i18n="thStatus">STATUS</th>'
)

# 5d. Alerts Section
content = content.replace(
    '<h2>Smart Alerts &amp; Telemetry Notifications</h2>\n            <p>Active biological threshold triggers and meteorological cautions.</p>',
    '<h2 data-i18n="alertsHeading">Smart Alerts &amp; Telemetry Notifications</h2>\n            <p data-i18n="alertsSub">Active biological threshold triggers and meteorological cautions.</p>'
)
content = content.replace(
    '<button class="secondary" onclick="markAlertsRead()">\n            Mark all as read\n        </button>',
    '<button class="secondary" onclick="markAlertsRead()">\n            <span data-i18n="markAllRead">Mark all as read</span>\n        </button>'
)

# 5e. Frequency Section
content = content.replace(
    '<h2>Frequency Control Prototype</h2>\n            <p>Non-chemical acoustic/ultrasonic bio-deterrence control interface.</p>',
    '<h2 data-i18n="freqHeading">Frequency Control Prototype</h2>\n            <p data-i18n="freqSub">Non-chemical acoustic/ultrasonic bio-deterrence control interface.</p>'
)
content = content.replace(
    'ACTIVE DETERRENCE FREQUENCY (PROTOTYPE)',
    '<span data-i18n="freqActiveHeader">ACTIVE DETERRENCE FREQUENCY (PROTOTYPE)</span>'
)
content = content.replace(
    '🔊 Play Audio Simulation (Demo)\n                </button>',
    '<span data-i18n="freqAudioBtn">🔊 Play Audio Simulation (Demo)</span>\n                </button>'
)
content = content.replace(
    '⚡ Auto Sweep (15–35 kHz)\n                </button>',
    '<span data-i18n="freqSweepBtn">⚡ Auto Sweep (15–35 kHz)</span>\n                </button>'
)
content = content.replace(
    '<small>MODE</small>',
    '<small data-i18n="freqModeLabel">MODE</small>'
)
content = content.replace(
    '<small>TARGET PEST</small>',
    '<small data-i18n="freqTargetLabel">TARGET PEST</small>'
)
content = content.replace(
    '<small>EMITTER STATUS</small>',
    '<small data-i18n="freqStatusLabel">EMITTER STATUS</small>'
)

# 5f. Beneficial Section
content = content.replace(
    '<h2>Beneficial Insects &bull; Biological Control Hub</h2>\n            <p>12 verified agricultural allies. Track natural predators, pollinators, and parasitoids to eliminate chemical dependency.</p>',
    '<h2 data-i18n="benHeading">Beneficial Insects &bull; Biological Control Hub</h2>\n            <p data-i18n="benSub">12 verified agricultural allies. Track natural predators, pollinators, and parasitoids to eliminate chemical dependency.</p>'
)
content = content.replace(
    '<button class="primary" onclick="logBeneficialSighting(\'ladybird\')">\n            + Quick Log Sighting\n        </button>',
    '<button class="primary" onclick="logBeneficialSighting(\'ladybird\')">\n            <span data-i18n="quickLogBtn">+ Quick Log Sighting</span>\n        </button>'
)
content = content.replace(
    '🌿 LIVE ECOSYSTEM BALANCE GAUGE',
    '<span data-i18n="benGaugeTitle">🌿 LIVE ECOSYSTEM BALANCE GAUGE</span>'
)
content = content.replace(
    '✓ CHEMICAL SPRAY LOCKOUT ACTIVE (Field 03 Protected)',
    '<span data-i18n="benLockoutBadge">✓ CHEMICAL SPRAY LOCKOUT ACTIVE (Field 03 Protected)</span>'
)
content = content.replace(
    '<small>BENEFICIAL GUARDIANS</small>',
    '<small data-i18n="meterGuardians">BENEFICIAL GUARDIANS</small>'
)
content = content.replace(
    '<small>ACTIVE PEST DETECTIONS</small>',
    '<small data-i18n="meterPests">ACTIVE PEST DETECTIONS</small>'
)
content = content.replace(
    '<small>PREDATOR : PEST RATIO</small>',
    '<small data-i18n="meterRatio">PREDATOR : PEST RATIO</small>'
)
content = content.replace(
    '<small>CHEMICAL REDUCTION INDEX</small>',
    '<small data-i18n="meterIndex">CHEMICAL REDUCTION INDEX</small>'
)
content = content.replace(
    '<h3>🌿 KRISHI NETRA Mandatory Biocontrol Protocol</h3>\n        <p style="font-size:12px;color:var(--muted);line-height:1.7;margin-top:8px;">\n            Whenever KRISHI NETRA identifies beneficial organisms (Ladybirds, Lacewings, Spiders, or Bees) in high counts,\n            it automatically locks out chemical foliar recommendations and advises natural biological conservation.\n            Maintaining border rows of mustard, coriander, and marigold preserves these species year-round.\n        </p>',
    '<h3 data-i18n="protocolTitle">🌿 KRISHI NETRA Mandatory Biocontrol Protocol</h3>\n        <p style="font-size:12px;color:var(--muted);line-height:1.7;margin-top:8px;" data-i18n="protocolDesc">\n            Whenever KRISHI NETRA identifies beneficial organisms (Ladybirds, Lacewings, Spiders, or Bees) in high counts,\n            it automatically locks out chemical foliar recommendations and advises natural biological conservation.\n            Maintaining border rows of mustard, coriander, and marigold preserves these species year-round.\n        </p>'
)

# 5g. Profile Section
content = content.replace(
    '<h2>Farmer Profile &amp; Land Configuration</h2>\n            <p>Manage farm location, crop acreage, and telemetry preferences.</p>',
    '<h2 data-i18n="profileHeading">Farmer Profile &amp; Land Configuration</h2>\n            <p data-i18n="profileSub">Manage farm location, crop acreage, and telemetry preferences.</p>'
)
content = content.replace('<label>FARMER NAME</label>', '<label data-i18n="lblFarmerName">FARMER NAME</label>')
content = content.replace('<label>PHONE (WHATSAPP ALERTS)</label>', '<label data-i18n="lblPhone">PHONE (WHATSAPP ALERTS)</label>')
content = content.replace('<label>FARM LOCATION</label>', '<label data-i18n="lblLocation">FARM LOCATION</label>')
content = content.replace('<label>PRIMARY CROP</label>', '<label data-i18n="lblPrimaryCrop">PRIMARY CROP</label>')
content = content.replace('<label>FARM SIZE</label>', '<label data-i18n="lblFarmSize">FARM SIZE</label>')
content = content.replace('<label>MONITORING MODE</label>', '<label data-i18n="lblMonitoringMode">MONITORING MODE</label>')

print("Added data-i18n across sections")

# 6. Now let's replace TRANSLATIONS object with the comprehensive dictionary!
translations_code = """const TRANSLATIONS = {
    en: {
        appName: "KRISHI NETRA",
        appTagline: "INTELLIGENT AGRICULTURE",
        mainMenu: "MAIN MENU",
        navDashboard: "Dashboard",
        navDetect: "Detect Pest",
        navHistory: "Detection History",
        navAlerts: "Alerts",
        navFrequency: "Frequency Control",
        navBeneficial: "Beneficial Insects",

        liveAdvisoryTag: "LIVE ADVISORY",
        titleDashboard: "Farmer Dashboard & Live Farm Telemetry",
        titleDetect: "AI Pest Detection Studio & Live Vision",
        titleHistory: "Detection History & Scouting Log",
        titleAlerts: "Smart Alerts & Real-Time Notifications",
        titleFrequency: "Acoustic Deterrence & Frequency Control",
        titleBeneficial: "Beneficial Ecosystem Guardians & Biocontrol Hub",
        titleProfile: "Farmer Profile & Farm Settings",

        greetingMorning: "Good morning",
        greetingAfternoon: "Good afternoon",
        greetingEvening: "Good evening",
        dashboardSubtitle: "Real-time agricultural monitoring across all 10 crop zones.",
        exportCSV: "📥 Export Log (CSV)",
        newDetection: "+ New Detection",

        statTotalDetections: "TOTAL DETECTIONS",
        statPestsDetected: "Pests Detected",
        statPestsChange: "↑ Updated in real-time",
        statAttentionRequired: "ATTENTION REQUIRED",
        statActiveAlerts: "Active Alerts",
        statHighPriority: "2 high priority",
        statEcosystemHealth: "ECOSYSTEM HEALTH",
        statBeneficialInsects: "Beneficial Insects",
        statBeneficialSub: "↑ Healthy biological predator balance",

        latestDetection: "Latest Detection",
        recActionHeader: "🎯 Recommended Action",
        activeAlertsTitle: "Active Alerts",
        pestActivityTitle: "Pest Activity — Last 7 Days",
        pestActivitySub: "Number of recorded crop pest detections",

        detectHeading: "AI Pest Detection • All Crops Prototype",
        detectSub: "Upload any crop photo or turn on live camera. Select a crop or let KRISHI NETRA auto-detect.",
        uploadTitle: "Upload or Capture Crop Leaf",
        uploadDesc: "Take a clear photograph of infected leaves, stems, or pests across any crop.",
        chooseImageBtn: "📁 Choose Image File",
        cameraBtn: "📹 Live Camera Scanner",
        analyzeBtn: "🔍 Analyze Image with KRISHI NETRA Vision",
        sampleBarTitle: "⚡ Or 1-Click Test Verified Agricultural Leaf Samples:",
        engineReadyTitle: "Diagnostic Engine Ready",
        engineReadyDesc: "Upload an image, snap a camera frame, or click a crop sample to run computer vision analysis.",
        labelSeverity: "Severity Status",
        labelCropZone: "Crop & Zone",
        labelScientific: "Scientific Name",
        labelFrequency: "Prototype Deterrence Freq",
        labelStatus: "Detection Status",
        confirmedStatus: "Confirmed by KRISHI NETRA",
        labelDamage: "🌿 Botanical Damage Assessment",
        labelIPM: "🎯 Integrated Pest Management (IPM) Next Steps",
        saveHistoryBtn: "✓ Save & Log to Field History",
        shareWhatsAppBtn: "💬 Share on WhatsApp",

        historyHeading: "Detection History • All Crops Log",
        historySub: "Live chronological record of all farm scans with export capability.",
        downloadCSV: "📥 Download CSV Report",
        historySearchPlaceholder: "Search by pest, crop, or field location...",
        thPest: "PEST / ORGANISM",
        thCrop: "CROP LOCATION",
        thConf: "AI CONFIDENCE",
        thSev: "SEVERITY",
        thTime: "DETECTION TIME",
        thStatus: "STATUS",

        alertsHeading: "Smart Alerts & Telemetry Notifications",
        alertsSub: "Active biological threshold triggers and meteorological cautions.",
        markAllRead: "Mark all as read",

        freqHeading: "Frequency Control Prototype",
        freqSub: "Non-chemical acoustic/ultrasonic bio-deterrence control interface.",
        freqActiveHeader: "ACTIVE DETERRENCE FREQUENCY (PROTOTYPE)",
        freqAudioBtn: "🔊 Play Audio Simulation (Demo)",
        freqSweepBtn: "⚡ Auto Sweep (15–35 kHz)",
        freqModeLabel: "MODE",
        freqTargetLabel: "TARGET PEST",
        freqStatusLabel: "EMITTER STATUS",

        benHeading: "Beneficial Insects • Biological Control Hub",
        benSub: "12 verified agricultural allies. Track natural predators, pollinators, and parasitoids to eliminate chemical dependency.",
        quickLogBtn: "+ Quick Log Sighting",
        benGaugeTitle: "🌿 LIVE ECOSYSTEM BALANCE GAUGE",
        benLockoutBadge: "✓ CHEMICAL SPRAY LOCKOUT ACTIVE (Field 03 Protected)",
        meterGuardians: "BENEFICIAL GUARDIANS",
        meterPests: "ACTIVE PEST DETECTIONS",
        meterRatio: "PREDATOR : PEST RATIO",
        meterIndex: "CHEMICAL REDUCTION INDEX",
        protocolTitle: "🌿 KRISHI NETRA Mandatory Biocontrol Protocol",
        protocolDesc: "Whenever KRISHI NETRA identifies beneficial organisms (Ladybirds, Lacewings, Spiders, or Bees) in high counts, it automatically locks out chemical foliar recommendations and advises natural biological conservation. Maintaining border rows of mustard, coriander, and marigold preserves these species year-round.",

        profileHeading: "Farmer Profile & Land Configuration",
        profileSub: "Manage farm location, crop acreage, and telemetry preferences.",
        lblFarmerName: "FARMER NAME",
        lblPhone: "PHONE (WHATSAPP ALERTS)",
        lblLocation: "FARM LOCATION",
        lblPrimaryCrop: "PRIMARY CROP",
        lblFarmSize: "FARM SIZE",
        lblMonitoringMode: "MONITORING MODE",

        aiTitle: "Krishi AI Assistant",
        aiSubtitle: "Your Smart Farming Advisor",
        aiStatus: "Online • Farming Expert Mode",
        aiChatTab: "💬 Chat",
        aiVoiceTab: "🎙️ Voice",
        aiPlaceholder: "Ask me anything about farming, pests, crops...",
        aiVoiceStatus: "Tap mic to speak",
        aiVoiceHint: "Ask your farming question in English, हिंदी, or मराठी.",
        aiHoldSpeak: "🎙️ Hold & Speak",
        aiFabTooltip: "Ask Krishi AI ✨",
        langToast: "Language changed to English 🌐",
        weatherSafe: "Wind 5.2 km/h · Safe conditions"
    },
    hi: {
        appName: "कृषि नेत्रा",
        appTagline: "स्मार्ट एवं आधुनिक कृषि",
        mainMenu: "मुख्य मेनू",
        navDashboard: "डैशबोर्ड",
        navDetect: "कीट पहचान",
        navHistory: "पहचान इतिहास",
        navAlerts: "अलर्ट सूचनाएं",
        navFrequency: "आवृत्ति नियंत्रण",
        navBeneficial: "मित्र कीट",

        liveAdvisoryTag: "लाइव सलाह",
        titleDashboard: "किसान डैशबोर्ड एवं लाइव कृषि स्थिति",
        titleDetect: "एआई कीट पहचान स्टूडियो एवं लाइव विज़न",
        titleHistory: "कीट पहचान इतिहास एवं निगरानी लॉग",
        titleAlerts: "स्मार्ट अलर्ट एवं तुरंत सूचनाएं",
        titleFrequency: "ध्वनि निवारण एवं आवृत्ति नियंत्रण",
        titleBeneficial: "मित्र कीट संरक्षक एवं जैव नियंत्रण",
        titleProfile: "किसान प्रोफ़ाइल एवं सेटिंग्स",

        greetingMorning: "शुभ प्रभात",
        greetingAfternoon: "शुभ दोपहर",
        greetingEvening: "शुभ संध्या",
        dashboardSubtitle: "सभी 10 फसल क्षेत्रों में वास्तविक समय में कृषि निगरानी।",
        exportCSV: "📥 डेटा डाउनलोड (CSV)",
        newDetection: "+ नई कीट जांच",

        statTotalDetections: "कुल कीट पहचान",
        statPestsDetected: "पहचाने गए कीट",
        statPestsChange: "↑ तुरंत अपडेटेड",
        statAttentionRequired: "ध्यान देने योग्य",
        statActiveAlerts: "सक्रिय अलर्ट",
        statHighPriority: "2 उच्च प्राथमिकता",
        statEcosystemHealth: "पारिस्थितिकी स्वास्थ्य",
        statBeneficialInsects: "मित्र कीट",
        statBeneficialSub: "↑ प्राकृतिक शिकारी कीटों का स्वस्थ संतुलन",

        latestDetection: "ताज़ा कीट पहचान",
        recActionHeader: "🎯 अनुशंसित कार्रवाई",
        activeAlertsTitle: "सक्रिय अलर्ट",
        pestActivityTitle: "कीट गतिविधि — पिछले 7 दिन",
        pestActivitySub: "रिकॉर्ड की गई फसल कीट पहचान संख्या",

        detectHeading: "एआई कीट पहचान • सभी फसलें मॉडल",
        detectSub: "फसल की फोटो अपलोड करें या लाइव कैमरा चालू करें। फसल चुनें या कृषि नेत्रा को स्वतः पहचानने दें।",
        uploadTitle: "फसल पत्ती की फोटो अपलोड या कैप्चर करें",
        uploadDesc: "किसी भी फसल की संक्रमित पत्तियों, तनों या कीटों की स्पष्ट फोटो लें।",
        chooseImageBtn: "📁 फोटो फ़ाइल चुनें",
        cameraBtn: "📹 लाइव कैमरा स्कैनर",
        analyzeBtn: "🔍 कृषि नेत्रा विज़न से जांच करें",
        sampleBarTitle: "⚡ या 1-क्लिक में जांची हुई पत्तियों के नमूने देखें:",
        engineReadyTitle: "निदान इंजन तैयार है",
        engineReadyDesc: "कंप्यूटर विज़न विश्लेषण चलाने के लिए फोटो अपलोड करें, कैमरा फ्रेम लें, या किसी नमूने पर क्लिक करें।",
        labelSeverity: "गंभीरता स्थिति",
        labelCropZone: "फसल एवं क्षेत्र",
        labelScientific: "वैज्ञानिक नाम",
        labelFrequency: "निवारक ध्वनि आवृत्ति",
        labelStatus: "पहचान स्थिति",
        confirmedStatus: "कृषि नेत्रा द्वारा पुष्टीकृत",
        labelDamage: "🌿 वानस्पतिक नुकसान मूल्यांकन",
        labelIPM: "🎯 एकीकृत कीट प्रबंधन (IPM) अगले कदम",
        saveHistoryBtn: "✓ खेत इतिहास में सुरक्षित करें",
        shareWhatsAppBtn: "💬 व्हाट्सएप पर साझा करें",

        historyHeading: "पहचान इतिहास • फसल जांच लॉग",
        historySub: "डाउनलोड सुविधा के साथ सभी खेत स्कैन का लाइव समयवार रिकॉर्ड।",
        downloadCSV: "📥 सीएसवी रिपोर्ट डाउनलोड करें",
        historySearchPlaceholder: "कीट, फसल या खेत के स्थान से खोजें...",
        thPest: "कीट / जीव",
        thCrop: "फसल स्थान",
        thConf: "एआई सटीकता",
        thSev: "गंभीरता",
        thTime: "जांच समय",
        thStatus: "स्थिति",

        alertsHeading: "स्मार्ट अलर्ट एवं टेलीमेट्री सूचनाएं",
        alertsSub: "सक्रिय जैविक सीमा चेतावनी और मौसमी सावधानियां।",
        markAllRead: "सभी को पढ़ा हुआ चिह्नित करें",

        freqHeading: "ध्वनि आवृत्ति नियंत्रण प्रणाली",
        freqSub: "रासायनिक मुक्त जैविक ध्वनि/अल्ट्रासोनिक कीट निवारण इंटरफ़ेस।",
        freqActiveHeader: "सक्रिय निवारण ध्वनि आवृत्ति (प्रोटोटाइप)",
        freqAudioBtn: "🔊 ऑडियो सिमुलेशन चलाएं (डेमो)",
        freqSweepBtn: "⚡ ऑटो स्वीप (15–35 kHz)",
        freqModeLabel: "मोड",
        freqTargetLabel: "लक्षित कीट",
        freqStatusLabel: "उत्सर्जक स्थिति",

        benHeading: "मित्र कीट • जैविक नियंत्रण केंद्र",
        benSub: "12 प्रमाणित कृषि मित्र कीट। रासायनिक निर्भरता समाप्त करने के लिए प्राकृतिक शिकारियों और परागणकों की निगरानी करें।",
        quickLogBtn: "+ मित्र कीट उपस्थिति दर्ज करें",
        benGaugeTitle: "🌿 लाइव पारिस्थितिकी संतुलन मीटर",
        benLockoutBadge: "✓ कीटनाशक छिड़काव लॉक सक्रिय (खेत 03 सुरक्षित)",
        meterGuardians: "मित्र कीट संरक्षक",
        meterPests: "सक्रिय हानिकारक कीट",
        meterRatio: "शिकारी : कीट अनुपात",
        meterIndex: "कीटनाशक बचत सूचकांक",
        protocolTitle: "🌿 कृषि नेत्रा अनिवार्य जैव-नियंत्रण नियम",
        protocolDesc: "जब भी कृषि नेत्रा में मित्र कीटों (लेडीबर्ड, क्राइसोपा, मकड़ी या मधुमक्खी) की संख्या अधिक पाई जाती है, तो यह रासायनिक छिड़काव की सिफारिश को रोककर प्राकृतिक संरक्षण की सलाह देता है। सरसों, धनिया और गेंदा की मेड़ लगाने से ये मित्र कीट पूरे वर्ष सुरक्षित रहते हैं।",

        profileHeading: "किसान प्रोफ़ाइल एवं भूमि विवरण",
        profileSub: "खेत का स्थान, फसल का रकबा और अलर्ट प्राथमिकताएं प्रबंधित करें।",
        lblFarmerName: "किसान का नाम",
        lblPhone: "फ़ोन (व्हाट्सएप अलर्ट)",
        lblLocation: "खेत का स्थान",
        lblPrimaryCrop: "मुख्य फसल",
        lblFarmSize: "खेत का आकार",
        lblMonitoringMode: "निगरानी मोड",

        aiTitle: "कृषि एआई सहायक",
        aiSubtitle: "आपका स्मार्ट कृषि सलाहकार",
        aiStatus: "ऑनलाइन • कृषि विशेषज्ञ मोड",
        aiChatTab: "💬 चैट",
        aiVoiceTab: "🎙️ बोलकर पूछें",
        aiPlaceholder: "फसल, कीट, खाद या मौसम के बारे में कुछ भी पूछें...",
        aiVoiceStatus: "बोलने के लिए माइक दबाएं",
        aiVoiceHint: "अपना सवाल हिंदी, मराठी या अंग्रेजी में पूछें।",
        aiHoldSpeak: "🎙️ दबाकर बोलें",
        aiFabTooltip: "कृषि एआई से पूछें ✨",
        langToast: "भाषा बदलकर हिंदी कर दी गई 🌐",
        weatherSafe: "हवा 5.2 km/h · अनुकूल मौसम"
    },
    mr: {
        appName: "कृषी नेत्रा",
        appTagline: "स्मार्ट आणि प्रगत शेती",
        mainMenu: "मुख्य मेनू",
        navDashboard: "डॅशबोर्ड",
        navDetect: "कीड ओळख",
        navHistory: "तपासणी इतिहास",
        navAlerts: "सतर्कता सूचना",
        navFrequency: "वारंवारता नियंत्रण",
        navBeneficial: "उपयुक्त मित्र कीटक",

        liveAdvisoryTag: "थेट कृषी सल्ला",
        titleDashboard: "शेतकरी डॅशबोर्ड आणि थेट शेती स्थिती",
        titleDetect: "एआई कीड ओळख स्टुडिओ आणि थेट स्कॅनर",
        titleHistory: "कीड तपासणी इतिहास आणि नोंदवही",
        titleAlerts: "स्मार्ट अलर्ट आणि त्वरित सूचना",
        titleFrequency: "ध्वनी प्रतिबंधक आणि वारंवारता नियंत्रण",
        titleBeneficial: "मित्र कीटक संरक्षक आणि जैविक नियंत्रण केंद्र",
        titleProfile: "शेतकरी माहिती आणि सेटिंग्ज",

        greetingMorning: "शुभ सकाळ",
        greetingAfternoon: "शुभ दुपार",
        greetingEvening: "शुभ संध्याकाळ",
        dashboardSubtitle: "सर्व 10 पीक विभागांमधील थेट शेती निरीक्षण.",
        exportCSV: "📥 नोंदवही डाउनलोड (CSV)",
        newDetection: "+ नवीन कीड तपासणी",

        statTotalDetections: "एकूण कीड तपासण्या",
        statPestsDetected: "आढळलेली कीड",
        statPestsChange: "↑ रिअल-टाइम मध्ये अद्ययावत",
        statAttentionRequired: "लक्ष देण्याची गरज",
        statActiveAlerts: "सक्रिय अलर्ट",
        statHighPriority: "2 उच्च प्राधान्य",
        statEcosystemHealth: "परिसंस्था आरोग्य",
        statBeneficialInsects: "उपयुक्त मित्र कीटक",
        statBeneficialSub: "↑ निसर्गपूरक मित्र कीटकांचे उत्तम संतुलन",

        latestDetection: "नुकतीच झालेली तपासणी",
        recActionHeader: "🎯 शिफारस केलेली कृती",
        activeAlertsTitle: "सक्रिय अलर्ट",
        pestActivityTitle: "कीड प्रादुर्भाव — मागील 7 दिवस",
        pestActivitySub: "नोंदवलेली पीक कीड संख्या",

        detectHeading: "एआय कीड ओळख • सर्व पिके मॉडेल",
        detectSub: "कोणत्याही पिकाचा फोटो अपलोड करा किंवा थेट कॅमेरा सुरू करा. पीक निवडा किंवा कृषी नेत्राला स्वतः ओळखू द्या.",
        uploadTitle: "पिकाच्या पानाचा फोटो अपलोड किंवा कॅमेरा स्कॅन करा",
        uploadDesc: "कोणत्याही पिकावरील बाधित पाने, खोड किंवा किडींचा स्पष्ट फोटो काढा.",
        chooseImageBtn: "📁 फोटो फाइल निवडा",
        cameraBtn: "📹 थेट कॅमेरा स्कॅनर",
        analyzeBtn: "🔍 कृषी नेत्रा व्हिजन द्वारे तपासणी करा",
        sampleBarTitle: "⚡ किंवा 1-क्लिकमध्ये तपासलेली पाने नमुने पहा:",
        engineReadyTitle: "निदान प्रणाली सज्ज आहे",
        engineReadyDesc: "संगणकीय व्हिजन तपासणीसाठी फोटो अपलोड करा, कॅमेऱ्याने फोटो घ्या किंवा नमुन्यावर क्लिक करा.",
        labelSeverity: "तीव्रता स्थिती",
        labelCropZone: "पीक आणि विभाग",
        labelScientific: "शास्त्रीय नाव",
        labelFrequency: "प्रतिबंधक ध्वनी वारंवारता",
        labelStatus: "तपासणी स्थिती",
        confirmedStatus: "कृषी नेत्रा द्वारे प्रमाणित",
        labelDamage: "🌿 वनस्पती नुकसान मूल्यमापन",
        labelIPM: "🎯 एकात्मिक कीड व्यवस्थापन (IPM) पुढील उपाय",
        saveHistoryBtn: "✓ शेत नोंदवहीत जतन करा",
        shareWhatsAppBtn: "💬 व्हॉट्सअ‍ॅपवर पाठवा",

        historyHeading: "तपासणी इतिहास • शेती नोंदवही",
        historySub: "डाउनलोड सुविधेसह शेतातील सर्व तपासण्यांची थेट नोंदवही.",
        downloadCSV: "📥 सीएसव्ही अहवाल डाउनलोड करा",
        historySearchPlaceholder: "कीड, पीक किंवा शेताच्या ठिकाणावरून शोधा...",
        thPest: "कीड / कीटक",
        thCrop: "पिकाचे ठिकाण",
        thConf: "एआय अचूकता",
        thSev: "तीव्रता",
        thTime: "तपासणी वेळ",
        thStatus: "स्थिती",

        alertsHeading: "स्मार्ट अलर्ट आणि थेट सूचना",
        alertsSub: "सक्रिय जैविक मर्यादा आणि हवामान धोक्याच्या सूचना.",
        markAllRead: "सर्व वाचलेले चिन्हांकित करा",

        freqHeading: "ध्वनी वारंवारता नियंत्रण प्रणाली",
        freqSub: "रासायनिक खतांशिवाय जैविक ध्वनी/अल्ट्रासोनिक कीड नियंत्रण इंटरफेस.",
        freqActiveHeader: "सक्रिय कीड प्रतिबंधक वारंवारता (प्रोटोटाइप)",
        freqAudioBtn: "🔊 ऑडिओ चाचणी ऐका (डेमो)",
        freqSweepBtn: "⚡ ऑटो स्वीप (15–35 kHz)",
        freqModeLabel: "मोड",
        freqTargetLabel: "लक्षित कीड",
        freqStatusLabel: "उत्सर्जक स्थिती",

        benHeading: "उपयुक्त मित्र कीटक • जैविक नियंत्रण केंद्र",
        benSub: "12 प्रमाणित शेती मित्र कीटक. रासायनिक अवलंबित्व संपवण्यासाठी नैसर्गिक शिकारी आणि परागीभवन करणाऱ्या कीटकांची नोंद ठेवा.",
        quickLogBtn: "+ मित्र कीटक नोंद करा",
        benGaugeTitle: "🌿 थेट परिसंस्था संतुलन मीटर",
        benLockoutBadge: "✓ कीटकनाशक फवारणी लॉक सक्रिय (शेत 03 संरक्षित)",
        meterGuardians: "मित्र कीटक रक्षक",
        meterPests: "सक्रिय उपद्रवी कीड",
        meterRatio: "शिकारी : कीड प्रमाण",
        meterIndex: "कीटकनाशक बचत निर्देशांक",
        protocolTitle: "🌿 कृषी नेत्रा अनिवार्य जैविक नियंत्रण नियम",
        protocolDesc: "जेव्हा जेव्हा कृषी नेत्रा प्रणालीमध्ये मित्र कीटक (लेडीबर्ड, क्रायसोपा, कोळी किंवा मधमाश्या) जास्त संख्येत आढळतात, तेव्हा ती रासायनिक फवारणी तात्काळ रोखून नैसर्गिक जैविक संवर्धनाचा सल्ला देते. मोहरी, कोथिंबीर आणि झेंडूच्या बांधावरील पिकांमुळे हे मित्र कीटक वर्षभर टिकून राहतात.",

        profileHeading: "शेतकरी माहिती आणि जमीन तपशील",
        profileSub: "शेताचे स्थान, पिकांचे क्षेत्रफळ आणि अलर्ट प्राधान्ये व्यवस्थापित करा.",
        lblFarmerName: "शेतकऱ्याचे नाव",
        lblPhone: "फोन (व्हॉट्सअ‍ॅप अलर्ट)",
        lblLocation: "शेताचे स्थान",
        lblPrimaryCrop: "मुख्य पीक",
        lblFarmSize: "शेताचे क्षेत्रफळ",
        lblMonitoringMode: "निरीक्षण पद्धत",

        aiTitle: "कृषी एआय सहाय्यक",
        aiSubtitle: "तुमचा स्मार्ट शेती सल्लागार",
        aiStatus: "ऑनलाइन • कृषी तज्ज्ञ मोड",
        aiChatTab: "💬 चॅट",
        aiVoiceTab: "🎙️ बोलून विचारा",
        aiPlaceholder: "पीक, कीड, खते किंवा हवामानाबद्दल काहीही विचारा...",
        aiVoiceStatus: "बोलण्यासाठी माइकवर टॅप करा",
        aiVoiceHint: "तुमचा प्रश्न मराठी, हिंदी किंवा इंग्रजीत विचारा.",
        aiHoldSpeak: "🎙️ दाबून बोला",
        aiFabTooltip: "कृषी एआय ला विचारा ✨",
        langToast: "भाषा मराठी मध्ये बदलली 🌐",
        weatherSafe: "वारा 5.2 km/h · अनुकूल हवामान"
    }
};"""

# Replace TRANSLATIONS definition in content
trans_start = content.find("const TRANSLATIONS = {")
trans_end = content.find("const AI_SUGGESTIONS_BY_LANG = {")
if trans_start != -1 and trans_end != -1:
    content = content[:trans_start] + translations_code + "\n\n" + content[trans_end:]
    print("Replaced TRANSLATIONS dictionary successfully")

# 7. Update setLanguage function to also update chart days and any dynamic text
new_set_language_js = """function setLanguage(lang, silent = false){
    if(!TRANSLATIONS[lang]) lang = 'en';
    currentLanguage = lang;
    localStorage.setItem('krishi_language', lang);
    document.documentElement.lang = lang;

    const select = document.getElementById('langSelect');
    if(select) select.value = lang;

    // Update topbar language pill active state
    document.querySelectorAll('.lang-pill-btn').forEach(btn => btn.classList.remove('active'));
    const activePill = document.getElementById('btnLang' + lang.charAt(0).toUpperCase() + lang.slice(1));
    if(activePill) activePill.classList.add('active');

    // Update all data-i18n elements
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if(TRANSLATIONS[lang] && TRANSLATIONS[lang][key] !== undefined){
            el.textContent = TRANSLATIONS[lang][key];
        }
    });

    // Update all placeholders
    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
        const key = el.getAttribute('data-i18n-placeholder');
        if(TRANSLATIONS[lang] && TRANSLATIONS[lang][key] !== undefined){
            el.placeholder = TRANSLATIONS[lang][key];
        }
    });

    // Update 7-day chart days labels
    const dayLabels = {
        en: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        hi: ['सोम', 'मंगल', 'बुध', 'गुरु', 'शुक्र', 'शनि', 'रवि'],
        mr: ['सोम', 'मंगळ', 'बुध', 'गुरू', 'शुक्र', 'शनि', 'रवि']
    };
    const chartLabels = document.querySelectorAll('.chart .bar-label');
    if(chartLabels.length >= 7 && dayLabels[lang]){
        chartLabels.forEach((el, idx) => {
            if(dayLabels[lang][idx]) el.textContent = dayLabels[lang][idx];
        });
    }

    // Update active page title (document title)
    const activeSection = document.querySelector('.section.active');
    if(activeSection){
        const secId = activeSection.id;
        const titleKey = 'title' + secId.charAt(0).toUpperCase() + secId.slice(1);
        if(TRANSLATIONS[lang] && TRANSLATIONS[lang][titleKey]){
            document.title = TRANSLATIONS[lang][titleKey] + " | KRISHI NETRA";
        }
    }

    // Update dynamic dashboard greeting
    updateGreetingText();

    // Update AI suggestion chips
    updateAISuggestionChips(lang);

    // Update speech recognition language if active
    if(typeof voiceRecognition !== 'undefined' && voiceRecognition){
        const langMap = { en: 'en-IN', hi: 'hi-IN', mr: 'mr-IN' };
        voiceRecognition.lang = langMap[lang] || 'en-IN';
    }

    if(!silent && typeof showToast === 'function'){
        showToast(TRANSLATIONS[lang].langToast);
    }
}"""

old_set_lang_start = content.find("function setLanguage(lang, silent = false){")
old_set_lang_end = content.find("function updateGreetingText(){")
if old_set_lang_start != -1 and old_set_lang_end != -1:
    content = content[:old_set_lang_start] + new_set_language_js + "\n\n" + content[old_set_lang_end:]
    print("Updated setLanguage function with chart labels and dynamic updates")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully written to index.html!")
