import os
import re

base_dir = r"c:\Users\user\Downloads\stitch_ai_bus_tracker_app"

def read_file(rel):
    path = os.path.join(base_dir, rel.replace('/', os.sep))
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

# Read the source files
html_14 = read_file('14_saved_routes_favourites/code.html')
html_05 = read_file('05_live_interactive_map_bus_radar/code.html')
html_06 = read_file('06_07_search_route_journey_planner/code.html')
html_16 = read_file('16_buy_ticket_transit_passes/code.html')
html_17 = read_file('17_commuter_profile_settings_hub/code.html')
html_desk = read_file('alternate_laptop_command_center_desktop_view/code.html')

def extract_main_content(html):
    m = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL)
    if not m:
        return ""
    content = m.group(1)
    # Remove any trailing script tags from main content since they will be handled uniformly
    content = re.sub(r'<script.*?</script>', '', content, flags=re.DOTALL)
    return content

main_14 = extract_main_content(html_14)
main_05 = extract_main_content(html_05)
main_06 = extract_main_content(html_06)
main_16 = extract_main_content(html_16)
main_17 = extract_main_content(html_17)

# Image fallbacks map
img_map = {
    r"https://lh3\.googleusercontent\.com/aida-public/AB6AXuBqmBTXTv9XwQUvnlZvWDaKqov8fU5c6EpC3SIsVHrSuN4y9fiH2Fl9IjBri2V_RvwXeaSN_ZyQzJZD0A_9e9AJmXd3L32pbGwz1zzPf-okEnyKJZZkycGXv1P6VHMReEVknxXmv_mUadCZSyjWiXmFMZbFGbaq7wm_WaytBoXz17STBuZVNw6UQHDU6KNMkB9P9syqXJGtoORv3DBF1ii7kZ0I2yshOJqOtKwZSHPFCuNnqGvc6veRQg": "assets/img/logo_transai.png",
    r"https://lh3\.googleusercontent\.com/aida-public/AB6AXuDy_muJZDvDqRbnvQbRbN7LuLEFlaifkTBB7eKXbCI4CZBqczbQewsgA_ortobcY4Xmb1PcIqw-F9Q0z1cNFQLpvwBbAhAVfZMUiKdMvYAWGzu6p4kZXBiaRcSeYVHzfgEqxUlICf1NcdwiT2vmNpgRf9i3Sz8M757o3zz80Mt5eifb-IMXSY0MAvG7Mefjw7banipuce5S9o_H2mPcaYMH2plGHuXTQ-Ov4vmYazHL": "assets/img/avatar_profile.png",
    r"https://lh3\.googleusercontent\.com/aida-public/AB6AXuCEZCRgqSKrU5lEE1YQp5StLNfsUh2XAYP_JDHfOP-2qo3v4DSjRTH5R5_2LRnBEyyTAWMk6P91OogeiC3J8Q9r9qEUUf4FWTjUR33My2-04ObGWZvJw1E57uxf_yms1Gtopzgl3kD7JbMknN9bOKt4LC76uPJ_7zyB1gt59SkMASpIIcsVmjuNN05eTgHogKGIdn_6Yo48S0XcoipHAkrRDrUK0oE55z5MFuUop_jmcI618rnXU68kLg": "assets/img/logo_wimb.png",
    r"https://lh3\.googleusercontent\.com/aida-public/AB6AXuAuIiWlCB17gzGlGegneK6pjLUgBV0krYq9ZE158BHDPLzHVeDBOSiyXsH75fe1oMerNoUa-qEIDYqQ6u_8QO6y8HuVpadN3AClcovC4I1QDolG7amWeM9xGFy1CbI44O7bUEaZ_bnHLuZtZtI85D-DqBmmatKk9MgjP1xM3R7SfMPUyLHoeCpfv_yzZhiY3lZm5H3T5OclwLRy6KE4r7lJ8hF7DFGTe1Gtz9Z1UEshrMlbymQYam8UPA": "assets/img/logo_home.png",
    r"https://lh3\.googleusercontent\.com/aida-public/AB6AXuBJvlrF2FxKZBHOyunPa04wdsCox4QC-oypd5wb-L3SoZizeDXY8E5Rp_CTdZ6z8A_9t3DwEZ2I-q6C-HEZjD22O2F-_uKhEezu5UtkEGjflHkB2MCmXUzqnOAgX3WEbNePUdKaiSQLXiNuqVAQ7b9giJKxnOinbR_59nszUW1C3rDX3sFOU73qdZb5O0_u7A6HOCPPcRmU8sG-CLw4OIexIBrFjqAgHbUG-zpX-fTbHvZ32biiKDaYuw": "assets/img/logo_tickets.png",
    r"https://lh3\.googleusercontent\.com/aida-public/AB6AXuCPLYtqaXGpfOCd5QtFp8RlnlU2PfTfR4eOc72RmOAtz8UFa9B5smOMe5MduJkaf_mQwHszoOEpy9Bv6H2ay_MLJ-Bunb5pHBDunY9dJOYozgunh9ZTZSLmHjNChAO3JqT-kQJ-ptGq4Edvnue_obAuTWzFHOCcv7gXJ_PlcK93JUTOB7d6ImxVq3RqlzZQw6T5vtsaoEi9Vaek0ioPOkTBrGKlZFElQoA473NqXZvAuCojB-7TtOk3NA": "assets/img/logo_profile.png",
    r"https://lh3\.googleusercontent\.com/aida-public/AB6AXuDxrVl4vHJf5tal8-qB4vKUKRVvCXt6ba11luDTmx31wHWfQWccNx4kQ5dSEZF59XobVUkqmM0drLUvnmoDkVGhnoNjAFN-Ya3Mrt7IIs52yiqoPfUw-iPpUyWnZBVmGMoZyqpyfaNSlxK6TSY7eSn2tbB5ok6mwYSmAOOjdPGERAzOf9Z9wIqbz5QX7QeFn9tHX0S6FVWeui1UAj-M2KM95R3we22qgIaBv7rkgOQH": "assets/img/portrait_alex.png",
    r"https://lh3\.googleusercontent\.com/aida-public/AB6AXuCplGITZRV9G-tk2z-FyLDUnArQvGOySAC0EMPmYF_rYDCLmmmeOF4eJQx3VdOlQ0GOJyw3dh3pxwSgNbgy7rfSfymLwmg01F2MS7iB-DfxYZn8fb3ou8J4LNaVXKh10IAEEnMxc6FoHdt8wfNTAvdg5xrLkucmoLZeRf1cCkuHJodm65yEr6mlqLsGeR0NpREwNfk6IvVHr0-tb0KjcLPt2aCS6myOChQ4O1K1NiksXuZAIzsUIF7LaA": "assets/img/logo_desktop.png"
}

def localize_images(content):
    for pattern, local_path in img_map.items():
        content = re.sub(pattern, local_path, content)
    return content

main_14 = localize_images(main_14)
main_05 = localize_images(main_05)
main_06 = localize_images(main_06)
main_16 = localize_images(main_16)
main_17 = localize_images(main_17)

# Extract desktop layout: body contents
m_desk = re.search(r'<body[^>]*>(.*?)</body>', html_desk, re.DOTALL)
desktop_body = m_desk.group(1) if m_desk else ""
# Remove tailwind scripts and trailing script tags inside desktop body
desktop_body = re.sub(r'<script.*?</script>', '', desktop_body, flags=re.DOTALL)
desktop_body = localize_images(desktop_body)

# Replace hardcoded INR display with reactive span in main_16
main_16 = main_16.replace("₹350.00", '<span class="wallet-balance-val">₹350.00</span>')
desktop_body = desktop_body.replace("₹350.00", '<span class="wallet-balance-val">₹350.00</span>')

# Build the unified index.html
unified_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover" name="viewport">
    <title>Where Is My Bus — TransAI Mobility Suite (Aether Transit)</title>
    
    <!-- Material Symbols & Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
    <link href="https://fonts.googleapis.com" rel="preconnect">
    <link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script id="tailwind-config">
    tailwind.config = {{
        darkMode: "class",
        theme: {{
            extend: {{
                "colors": {{
                    "surface": "#f8f9ff",
                    "surface-dim": "#cbdbf5",
                    "surface-bright": "#f8f9ff",
                    "surface-container-lowest": "#ffffff",
                    "surface-container-low": "#eff4ff",
                    "surface-container": "#e5eeff",
                    "surface-container-high": "#dce9ff",
                    "surface-container-highest": "#d3e4fe",
                    "on-surface": "#0b1c30",
                    "on-surface-variant": "#434655",
                    "inverse-surface": "#213145",
                    "inverse-on-surface": "#eaf1ff",
                    "outline": "#737686",
                    "outline-variant": "#c3c6d7",
                    "surface-tint": "#0053db",
                    "primary": "#004ac6",
                    "on-primary": "#ffffff",
                    "primary-container": "#2563eb",
                    "on-primary-container": "#eeefff",
                    "inverse-primary": "#b4c5ff",
                    "secondary": "#565e71",
                    "on-secondary": "#ffffff",
                    "secondary-container": "#dbe2f9",
                    "on-secondary-container": "#5c6477",
                    "tertiary": "#005e6e",
                    "on-tertiary": "#ffffff",
                    "tertiary-container": "#00788c",
                    "on-tertiary-container": "#d7f6ff",
                    "error": "#ba1a1a",
                    "on-error": "#ffffff",
                    "error-container": "#ffdad6",
                    "on-error-container": "#93000a",
                    "primary-fixed": "#dbe1ff",
                    "primary-fixed-dim": "#b4c5ff",
                    "on-primary-fixed": "#00174b",
                    "on-primary-fixed-variant": "#003ea8",
                    "secondary-fixed": "#dbe2f9",
                    "secondary-fixed-dim": "#bfc6dc",
                    "on-secondary-fixed": "#141b2c",
                    "on-secondary-fixed-variant": "#3f4759",
                    "tertiary-fixed": "#acedff",
                    "tertiary-fixed-dim": "#4cd7f6",
                    "on-tertiary-fixed": "#001f26",
                    "on-tertiary-fixed-variant": "#004e5c",
                    "background": "#f8f9ff",
                    "on-background": "#0b1c30",
                    "surface-variant": "#d3e4fe"
                }},
                "borderRadius": {{
                    "DEFAULT": "0.25rem",
                    "lg": "0.5rem",
                    "xl": "0.75rem",
                    "full": "9999px"
                }},
                "spacing": {{
                    "gutter-desktop": "2rem",
                    "space-lg": "1.5rem",
                    "margin": "1rem",
                    "space-xs": "0.25rem",
                    "space-md": "1rem",
                    "margin-desktop": "3rem",
                    "space-xl": "2rem",
                    "space-sm": "0.5rem",
                    "gutter-tablet": "1.5rem",
                    "gutter": "1rem",
                    "margin-tablet": "2rem"
                }},
                "fontFamily": {{
                    "headline-lg": ["Inter", "sans-serif"],
                    "body-lg": ["Inter", "sans-serif"],
                    "headline-md": ["Inter", "sans-serif"],
                    "label-lg": ["Inter", "sans-serif"],
                    "body-sm": ["Inter", "sans-serif"],
                    "headline-xl": ["Inter", "sans-serif"],
                    "headline-xl-mobile": ["Inter", "sans-serif"],
                    "headline-sm": ["Inter", "sans-serif"],
                    "label-md": ["Inter", "sans-serif"],
                    "label-sm": ["Inter", "sans-serif"],
                    "body-md": ["Inter", "sans-serif"]
                }}
            }}
        }}
    }};
    </script>

    <style>
        @layer base {{
            html, body {{
                margin: 0;
                padding: 0;
                font-family: 'Inter', -apple-system, sans-serif;
            }}
            ::-webkit-scrollbar {{
                width: 6px;
                height: 6px;
                display: none;
            }}
        }}

        /* App Viewport Container */
        .app-master-container {{
            background: #eef2f8;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }}

        /* Top Operational Ribbon */
        .top-operational-bar {{
            background: #ffffff;
            border-bottom: 1px solid #e2e8f0;
            padding: 10px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            position: sticky;
            top: 0;
            z-index: 90;
            box-shadow: 0 1px 4px rgba(11, 28, 48, 0.04);
        }}

        .brand-badge {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .view-mode-pill-bar {{
            display: flex;
            align-items: center;
            gap: 6px;
            background: #eff4ff;
            padding: 4px;
            border-radius: 9999px;
            border: 1px solid #dce9ff;
        }}

        .view-mode-pill {{
            padding: 6px 16px;
            border-radius: 9999px;
            font-size: 13px;
            font-weight: 600;
            color: #434655;
            transition: all 0.2s ease;
            cursor: pointer;
            border: none;
            background: transparent;
        }}

        .view-mode-pill.active {{
            background: #2563eb;
            color: #ffffff;
            box-shadow: 0 2px 8px rgba(37, 99, 235, 0.25);
        }}

        /* Screen Quick Jump Bar */
        .screen-quick-nav {{
            background: #f8f9ff;
            border-bottom: 1px solid #e2e8f0;
            padding: 8px 16px;
            display: flex;
            align-items: center;
            gap: 8px;
            overflow-x: auto;
            white-space: nowrap;
        }}

        .screen-pill-btn {{
            padding: 5px 12px;
            border-radius: 9999px;
            font-size: 11px;
            font-weight: 600;
            background: #ffffff;
            color: #434655;
            border: 1px solid #dce9ff;
            cursor: pointer;
            transition: all 0.15s ease;
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }}

        .screen-pill-btn:hover {{
            background: #eff4ff;
            color: #004ac6;
            border-color: #2563eb;
        }}

        .screen-pill-btn.active {{
            background: #004ac6;
            color: #ffffff;
            border-color: #004ac6;
            box-shadow: 0 1px 4px rgba(0, 74, 198, 0.2);
        }}

        /* Mobile Phone Simulator Chassis */
        .phone-simulator-frame {{
            width: 412px;
            height: 884px;
            max-height: 92vh;
            background: #ffffff;
            border-radius: 46px;
            box-shadow: 0 25px 60px -15px rgba(11, 28, 48, 0.25), 0 0 0 12px #101828, 0 0 0 14px #334155;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            margin: 24px auto;
        }}

        .phone-dynamic-island {{
            position: absolute;
            top: 10px;
            left: 50%;
            transform: translateX(-50%);
            width: 108px;
            height: 24px;
            background: #000000;
            border-radius: 16px;
            z-index: 80;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 10px;
        }}

        .dynamic-island-cam {{
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: #111e38;
            border: 1.5px solid #1a2a4c;
        }}

        .dynamic-island-sensor {{
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: #16223b;
        }}

        .phone-scroll-area {{
            flex: 1;
            overflow-y: auto;
            position: relative;
            background: #f8f9ff;
            -webkit-overflow-scrolling: touch;
        }}

        /* Gallery Layout */
        .gallery-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
            gap: 24px;
            padding: 24px;
            max-width: 1600px;
            margin: 0 auto;
            width: 100%;
        }}

        .gallery-card {{
            background: #ffffff;
            border-radius: 24px;
            border: 1px solid #e2e8f0;
            box-shadow: 0 4px 20px rgba(11, 28, 48, 0.06);
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }}

        .gallery-card-header {{
            padding: 12px 18px;
            background: #f8f9ff;
            border-bottom: 1px solid #e2e8f0;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        .gallery-card-body {{
            max-height: 520px;
            overflow-y: auto;
            background: #f8f9ff;
        }}

        /* Turnstile QR Modal styles */
        #pass-modal {{
            transition: opacity 0.3s ease;
        }}
        #pass-sheet {{
            transition: transform 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
        }}
    </style>
</head>
<body class="bg-surface font-body-md text-on-surface antialiased">

<div class="app-master-container">

    <!-- Top Operational Bar -->
    <header class="top-operational-bar">
        <div class="brand-badge">
            <img src="assets/img/logo_desktop.png" alt="Aether Transit Logo" class="h-8 w-auto object-contain" onerror="this.src='https://lh3.googleusercontent.com/aida-public/AB6AXuCplGITZRV9G-tk2z-FyLDUnArQvGOySAC0EMPmYF_rYDCLmmmeOF4eJQx3VdOlQ0GOJyw3dh3pxwSgNbgy7rfSfymLwmg01F2MS7iB-DfxYZn8fb3ou8J4LNaVXKh10IAEEnMxc6FoHdt8wfNTAvdg5xrLkucmoLZeRf1cCkuHJodm65yEr6mlqLsGeR0NpREwNfk6IvVHr0-tb0KjcLPt2aCS6myOChQ4O1K1NiksXuZAIzsUIF7LaA'">
            <div class="flex flex-col">
                <span class="font-headline-sm text-headline-sm text-on-surface font-bold leading-tight">Where Is My Bus</span>
                <span class="font-label-sm text-[10px] text-tertiary font-bold tracking-wider uppercase">TransAI • Aether Mobility Suite</span>
            </div>
        </div>

        <!-- Mode Switcher -->
        <div class="view-mode-pill-bar">
            <button class="view-mode-pill active" data-mode="mobile" onclick="setViewMode('mobile')">
                📱 Mobile App
            </button>
            <button class="view-mode-pill" data-mode="desktop" onclick="setViewMode('desktop')">
                🖥️ Command Center
            </button>
            <button class="view-mode-pill" data-mode="gallery" onclick="setViewMode('gallery')">
                🖼️ All 18 Screens Gallery
            </button>
        </div>

        <div class="flex items-center gap-3">
            <a href="../BUS TRAKER/index.html" class="hidden sm:flex items-center gap-1.5 px-3 py-1.5 rounded-xl border border-slate-200 bg-surface-container-low text-xs font-semibold text-on-surface-variant hover:text-on-surface hover:bg-surface-container transition-all">
                <span>← TransitPulse Suite</span>
            </a>
            <div class="hidden md:flex items-center gap-2 px-3 py-1.5 rounded-full bg-emerald-500/10 text-emerald-800 text-xs font-semibold">
                <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                <span>RTK GPS Fixed (±0.4m)</span>
            </div>
            <div class="flex items-center gap-2 px-3.5 py-1.5 rounded-xl bg-primary-container text-on-primary-container font-label-md text-label-md shadow-sm">
                <span class="material-symbols-outlined text-[18px]">account_balance_wallet</span>
                <span class="wallet-balance-val font-bold">₹350.00</span>
            </div>
        </div>
    </header>

    <!-- Screen Quick Navigation Pills (18 Screens) -->
    <nav class="screen-quick-nav">
        <span class="font-label-sm text-[10px] text-outline font-bold uppercase tracking-wider pl-1">Jump Screen:</span>
        <button class="screen-pill-btn active" data-screen="14_home" onclick="setScreen('14_home')">
            <span>01</span> Commuter Home & Mascot
        </button>
        <button class="screen-pill-btn" data-screen="02_saved_corridors" onclick="setScreen('02_saved_corridors')">
            <span>02</span> Saved Corridors
        </button>
        <button class="screen-pill-btn" data-screen="05_radar" onclick="setScreen('05_radar')">
            <span>03</span> Vector Map & Radar
        </button>
        <button class="screen-pill-btn" data-screen="04_hud" onclick="setScreen('04_hud')">
            <span>04</span> Velocity HUD & Controls
        </button>
        <button class="screen-pill-btn" data-screen="05_bottom_sheet" onclick="setScreen('05_bottom_sheet')">
            <span>05</span> Telemetry Bottom Sheet
        </button>
        <button class="screen-pill-btn" data-screen="06_search" onclick="setScreen('06_search')">
            <span>06</span> Corridor Search
        </button>
        <button class="screen-pill-btn" data-screen="07_planner" onclick="setScreen('07_planner')">
            <span>07</span> Trip & Journey Planner
        </button>
        <button class="screen-pill-btn" data-screen="08_comparison" onclick="setScreen('08_comparison')">
            <span>08</span> Suggested Routes
        </button>
        <button class="screen-pill-btn" data-screen="16_wallet" onclick="setScreen('16_wallet')">
            <span>09</span> Mobility Wallet (INR)
        </button>
        <button class="screen-pill-btn" data-screen="10_pass" onclick="setScreen('10_pass')">
            <span>10</span> Tap-to-Ride NFC
        </button>
        <button class="screen-pill-btn" data-screen="11_fares" onclick="setScreen('11_fares')">
            <span>11</span> Fare & Pass Catalog
        </button>
        <button class="screen-pill-btn" data-screen="12_qr_modal" onclick="openPassModal()">
            <span>12</span> Turnstile QR Token
        </button>
        <button class="screen-pill-btn" data-screen="17_profile" onclick="setScreen('17_profile')">
            <span>13</span> Alex Mercer ID
        </button>
        <button class="screen-pill-btn" data-screen="14_impact" onclick="setScreen('14_impact')">
            <span>14</span> Eco Impact Bento
        </button>
        <button class="screen-pill-btn" data-screen="15_optimization" onclick="setScreen('15_optimization')">
            <span>15</span> Optimization Engine
        </button>
        <button class="screen-pill-btn" data-screen="16_alerts" onclick="setScreen('16_alerts')">
            <span>16</span> AI Sentinel Alerts
        </button>
        <button class="screen-pill-btn" data-screen="17_settings" onclick="setScreen('17_settings')">
            <span>17</span> Core System Settings
        </button>
        <button class="screen-pill-btn" data-screen="18_desktop" onclick="setViewMode('desktop')">
            <span>18</span> Command Center Desktop
        </button>
    </nav>

    <!-- ==================== 1. MOBILE APP SIMULATOR VIEW ==================== -->
    <div id="mobileShellWrapper" class="flex-1 flex items-center justify-center p-4">
        <div class="phone-simulator-frame">
            <div class="phone-dynamic-island">
                <div class="dynamic-island-sensor"></div>
                <div class="dynamic-island-cam"></div>
            </div>

            <!-- Mobile App Header (Fixed) -->
            <header class="w-full z-40 pt-8 pb-2 px-4 bg-surface/85 backdrop-blur-xl border-b border-surface-container-high flex items-center justify-between shrink-0 shadow-xs">
                <div class="flex items-center gap-2">
                    <img alt="Where Is My Bus" class="h-7 w-auto object-contain" src="assets/img/logo_wimb.png" onerror="this.src='https://lh3.googleusercontent.com/aida-public/AB6AXuCEZCRgqSKrU5lEE1YQp5StLNfsUh2XAYP_JDHfOP-2qo3v4DSjRTH5R5_2LRnBEyyTAWMk6P91OogeiC3J8Q9r9qEUUf4FWTjUR33My2-04ObGWZvJw1E57uxf_yms1Gtopzgl3kD7JbMknN9bOKt4LC76uPJ_7zyB1gt59SkMASpIIcsVmjuNN05eTgHogKGIdn_6Yo48S0XcoipHAkrRDrUK0oE55z5MFuUop_jmcI618rnXU68kLg'">
                    <div class="flex flex-col">
                        <div class="flex items-center gap-1.5">
                            <span class="font-label-sm text-primary uppercase tracking-wider text-[10px] font-bold">TransAI</span>
                            <span class="inline-flex items-center gap-1 px-1.5 py-0.2 rounded-full bg-surface-container-high text-tertiary font-label-sm text-[9px]">
                                <span class="w-1.5 h-1.5 rounded-full bg-tertiary-container animate-pulse"></span>Live
                            </span>
                        </div>
                        <span class="font-headline-sm text-headline-sm text-on-surface leading-tight text-sm font-semibold">Where Is My Bus</span>
                    </div>
                </div>

                <div class="flex items-center gap-1">
                    <button aria-label="Notifications" class="relative w-9 h-9 flex items-center justify-center rounded-full text-on-surface-variant hover:text-on-surface hover:bg-surface-container-high/60 transition-colors" onclick="showFeedbackToast('No service disruptions on Line 42 Express')">
                        <span class="material-symbols-outlined text-[20px]">notifications</span>
                        <span class="absolute top-2 right-2 w-2 h-2 rounded-full bg-primary-container ring-2 ring-surface"></span>
                    </button>
                    <a class="w-9 h-9 flex items-center justify-center rounded-full cursor-pointer" onclick="setScreen('17_profile')">
                        <img alt="Commuter Profile" class="w-7 h-7 rounded-full object-cover ring-2 ring-primary/20" src="assets/img/avatar_profile.png" onerror="this.src='https://lh3.googleusercontent.com/aida-public/AB6AXuDy_muJZDvDqRbnvQbRbN7LuLEFlaifkTBB7eKXbCI4CZBqczbQewsgA_ortobcY4Xmb1PcIqw-F9Q0z1cNFQLpvwBbAhAVfZMUiKdMvYAWGzu6p4kZXBiaRcSeYVHzfgEqxUlICf1NcdwiT2vmNpgRf9i3Sz8M757o3zz80Mt5eifb-IMXSY0MAvG7Mefjw7banipuce5S9o_H2mPcaYMH2plGHuXTQ-Ov4vmYazHL'">
                    </a>
                </div>
            </header>

            <!-- Scrollable Viewport Mount -->
            <div id="phoneScrollableArea" class="phone-scroll-area pb-20">

                <!-- SCREEN VIEW 1 & 2: 14_saved_routes_favourites (Home & Saved Corridors) -->
                <div id="screen_14_home" class="stitch-screen-view">
                    {main_14}
                </div>

                <div id="screen_02_saved_corridors" class="stitch-screen-view hidden">
                    {main_14}
                </div>

                <!-- SCREEN VIEW 3, 4, 5: 05_live_interactive_map_bus_radar -->
                <div id="screen_05_radar" class="stitch-screen-view hidden">
                    {main_05}
                </div>

                <div id="screen_04_hud" class="stitch-screen-view hidden">
                    {main_05}
                </div>

                <div id="screen_05_bottom_sheet" class="stitch-screen-view hidden">
                    {main_05}
                </div>

                <!-- SCREEN VIEW 6, 7, 8: 06_07_search_route_journey_planner -->
                <div id="screen_06_search" class="stitch-screen-view hidden">
                    {main_06}
                </div>

                <div id="screen_07_planner" class="stitch-screen-view hidden">
                    {main_06}
                </div>

                <div id="screen_08_comparison" class="stitch-screen-view hidden">
                    {main_06}
                </div>

                <!-- SCREEN VIEW 9, 10, 11: 16_buy_ticket_transit_passes -->
                <div id="screen_16_wallet" class="stitch-screen-view hidden">
                    {main_16}
                </div>

                <div id="screen_10_pass" class="stitch-screen-view hidden">
                    {main_16}
                </div>

                <div id="screen_11_fares" class="stitch-screen-view hidden">
                    {main_16}
                </div>

                <!-- SCREEN VIEW 13, 14, 15, 16, 17: 17_commuter_profile_settings_hub -->
                <div id="screen_17_profile" class="stitch-screen-view hidden">
                    {main_17}
                </div>

                <div id="screen_14_impact" class="stitch-screen-view hidden">
                    {main_17}
                </div>

                <div id="screen_15_optimization" class="stitch-screen-view hidden">
                    {main_17}
                </div>

                <div id="screen_16_alerts" class="stitch-screen-view hidden">
                    {main_17}
                </div>

                <div id="screen_17_settings" class="stitch-screen-view hidden">
                    {main_17}
                </div>

            </div>

            <!-- Mobile App Bottom Navigation Bar (Fixed) -->
            <nav class="mobile-bottom-nav absolute bottom-0 inset-x-0 z-40 pb-safe bg-surface/90 backdrop-blur-xl border-t border-surface-container-high shadow-lg">
                <div class="flex justify-around items-center h-16 px-1">
                    <a class="flex flex-col items-center justify-center gap-0.5 min-w-[56px] min-h-[44px] text-primary-container font-semibold transition-colors cursor-pointer" data-path="home" onclick="setScreen('14_home')">
                        <span class="material-symbols-outlined text-[24px]">home</span>
                        <span class="font-label-sm text-label-sm text-[11px]">Home</span>
                    </a>
                    <a class="flex flex-col items-center justify-center gap-0.5 min-w-[56px] min-h-[44px] text-on-surface-variant hover:text-primary transition-colors cursor-pointer" data-path="explore" onclick="setScreen('06_search')">
                        <span class="material-symbols-outlined text-[24px]">explore</span>
                        <span class="font-label-sm text-label-sm text-[11px]">Explore</span>
                    </a>
                    <a class="flex flex-col items-center justify-center gap-0.5 min-w-[56px] min-h-[44px] text-on-surface-variant hover:text-primary transition-colors cursor-pointer" data-path="live-tracking" onclick="setScreen('05_radar')">
                        <span class="material-symbols-outlined text-[24px]">directions_bus</span>
                        <span class="font-label-sm text-label-sm text-[11px]">Live Track</span>
                    </a>
                    <a class="flex flex-col items-center justify-center gap-0.5 min-w-[56px] min-h-[44px] text-on-surface-variant hover:text-primary transition-colors cursor-pointer" data-path="tickets" onclick="setScreen('16_wallet')">
                        <span class="material-symbols-outlined text-[24px]">confirmation_number</span>
                        <span class="font-label-sm text-label-sm text-[11px]">Tickets</span>
                    </a>
                    <a class="flex flex-col items-center justify-center gap-0.5 min-w-[56px] min-h-[44px] text-on-surface-variant hover:text-primary transition-colors cursor-pointer" data-path="profile" onclick="setScreen('17_profile')">
                        <span class="material-symbols-outlined text-[24px]">person</span>
                        <span class="font-label-sm text-label-sm text-[11px]">Profile</span>
                    </a>
                </div>
            </nav>

            <!-- Optical Turnstile QR Modal Drawer -->
            <div class="fixed inset-0 z-50 flex items-end justify-center bg-inverse-surface/60 backdrop-blur-md transition-opacity duration-300 opacity-0 pointer-events-none" id="pass-modal" onclick="closePassModal()">
                <div class="w-full max-w-lg rounded-t-2xl bg-surface p-space-md shadow-2xl transition-transform duration-300 transform translate-y-full flex flex-col space-y-space-md" id="pass-sheet" onclick="event.stopPropagation()">
                    <div class="mx-auto h-1 w-12 rounded-full bg-outline-variant cursor-pointer" onclick="closePassModal()"></div>
                    
                    <div class="flex items-center justify-between border-b border-surface-container-high pb-2">
                        <div class="flex items-center space-x-2">
                            <span class="material-symbols-outlined text-[24px] text-primary">qr_code_2</span>
                            <span class="font-headline-sm text-headline-sm font-bold text-on-surface">Digital Turnstile Gate Pass</span>
                        </div>
                        <button class="flex h-8 w-8 items-center justify-center rounded-full bg-surface-container text-on-surface-variant hover:bg-surface-container-high" onclick="closePassModal()">
                            <span class="material-symbols-outlined text-[18px]">close</span>
                        </button>
                    </div>

                    <div class="flex flex-col items-center justify-center py-2 text-center">
                        <div class="relative flex h-52 w-52 items-center justify-center rounded-2xl bg-surface-container-lowest p-3 shadow-md ring-4 ring-primary/20">
                            <!-- High-Tech Animated Turnstile QR Pattern -->
                            <svg class="h-44 w-44 text-on-surface" fill="currentColor" viewBox="0 0 24 24">
                                <path d="M2 2h8v8H2V2zm2 2v4h4V4H4zm10-2h8v8h-8V2zm2 2v4h4V4h-4zM2 14h8v8H2v-8zm2 2v4h4v-4H4zm14 0h4v2h-4v-2zm-4 0h2v4h-2v-4zm4 4h4v2h-4v-2zm-2-2h2v2h-2v-2zm-2 2h2v2h-2v-2z"></path>
                            </svg>
                            <div class="absolute inset-0 rounded-2xl border-2 border-emerald-500 animate-pulse pointer-events-none"></div>
                        </div>

                        <span class="mt-3 font-mono text-[12px] font-bold uppercase tracking-widest text-emerald-700 bg-emerald-500/10 px-3 py-1 rounded-full">
                            TOKEN: #AETHER-8924-GATE-OK
                        </span>
                        <span class="mt-1 font-label-sm text-label-sm font-bold text-on-surface-variant" id="pass-timer">
                            Expires in 01h:24m:12s
                        </span>
                        <p class="mt-1 font-body-sm text-body-sm text-on-surface-variant max-w-xs">
                            Hold screen 2 inches from optical reader or NFC turnstile validator.
                        </p>
                    </div>

                    <div class="pt-2">
                        <button class="w-full py-3 rounded-xl bg-primary text-on-primary font-label-lg text-label-lg font-bold shadow-md hover:bg-primary-container transition-all" onclick="closePassModal()">
                            Done & Return
                        </button>
                    </div>
                </div>
            </div>

        </div>
    </div>

    <!-- ==================== 2. COMMAND CENTER DESKTOP VIEW ==================== -->
    <div id="desktopShellWrapper" class="w-full relative" style="display: none;">
        {desktop_body}
    </div>

    <!-- ==================== 3. ALL 18 SCREENS GALLERY VIEW ==================== -->
    <div id="galleryShellWrapper" class="gallery-grid" style="display: none;">
        <!-- Card 1 -->
        <div class="gallery-card">
            <div class="gallery-card-header">
                <div>
                    <h3 class="font-headline-sm text-sm font-bold">01. Commuter Home & Mascot</h3>
                    <span class="text-xs text-outline">3D Vector Mascot Bus</span>
                </div>
                <button class="px-2.5 py-1 rounded-lg bg-primary text-on-primary text-xs font-semibold" onclick="setViewMode('mobile'); setScreen('14_home')">Preview</button>
            </div>
            <div class="gallery-card-body p-3">
                {main_14}
            </div>
        </div>

        <!-- Card 2 -->
        <div class="gallery-card">
            <div class="gallery-card-header">
                <div>
                    <h3 class="font-headline-sm text-sm font-bold">02. Saved Corridors</h3>
                    <span class="text-xs text-outline">Filter tabs & Favorites</span>
                </div>
                <button class="px-2.5 py-1 rounded-lg bg-primary text-on-primary text-xs font-semibold" onclick="setViewMode('mobile'); setScreen('02_saved_corridors')">Preview</button>
            </div>
            <div class="gallery-card-body p-3">
                {main_14}
            </div>
        </div>

        <!-- Card 3 -->
        <div class="gallery-card">
            <div class="gallery-card-header">
                <div>
                    <h3 class="font-headline-sm text-sm font-bold">03. Vector Map & Radar</h3>
                    <span class="text-xs text-outline">SVG cartography & sweep</span>
                </div>
                <button class="px-2.5 py-1 rounded-lg bg-primary text-on-primary text-xs font-semibold" onclick="setViewMode('mobile'); setScreen('05_radar')">Preview</button>
            </div>
            <div class="gallery-card-body p-3">
                {main_05}
            </div>
        </div>

        <!-- Card 4 -->
        <div class="gallery-card">
            <div class="gallery-card-header">
                <div>
                    <h3 class="font-headline-sm text-sm font-bold">04. Telemetry Bottom Sheet</h3>
                    <span class="text-xs text-outline">Line 42 ETA & occupancy</span>
                </div>
                <button class="px-2.5 py-1 rounded-lg bg-primary text-on-primary text-xs font-semibold" onclick="setViewMode('mobile'); setScreen('05_bottom_sheet')">Preview</button>
            </div>
            <div class="gallery-card-body p-3">
                {main_05}
            </div>
        </div>

        <!-- Card 5 -->
        <div class="gallery-card">
            <div class="gallery-card-header">
                <div>
                    <h3 class="font-headline-sm text-sm font-bold">06. Corridor Search</h3>
                    <span class="text-xs text-outline">Live GPS search & chips</span>
                </div>
                <button class="px-2.5 py-1 rounded-lg bg-primary text-on-primary text-xs font-semibold" onclick="setViewMode('mobile'); setScreen('06_search')">Preview</button>
            </div>
            <div class="gallery-card-body p-3">
                {main_06}
            </div>
        </div>

        <!-- Card 6 -->
        <div class="gallery-card">
            <div class="gallery-card-header">
                <div>
                    <h3 class="font-headline-sm text-sm font-bold">07. Trip & Journey Planner</h3>
                    <span class="text-xs text-outline">Waypoint swap & itinerary</span>
                </div>
                <button class="px-2.5 py-1 rounded-lg bg-primary text-on-primary text-xs font-semibold" onclick="setViewMode('mobile'); setScreen('07_planner')">Preview</button>
            </div>
            <div class="gallery-card-body p-3">
                {main_06}
            </div>
        </div>

        <!-- Card 7 -->
        <div class="gallery-card">
            <div class="gallery-card-header">
                <div>
                    <h3 class="font-headline-sm text-sm font-bold">09. Mobility Wallet (INR)</h3>
                    <span class="text-xs text-outline">₹350.00 Balance & Top-up</span>
                </div>
                <button class="px-2.5 py-1 rounded-lg bg-primary text-on-primary text-xs font-semibold" onclick="setViewMode('mobile'); setScreen('16_wallet')">Preview</button>
            </div>
            <div class="gallery-card-body p-3">
                {main_16}
            </div>
        </div>

        <!-- Card 8 -->
        <div class="gallery-card">
            <div class="gallery-card-header">
                <div>
                    <h3 class="font-headline-sm text-sm font-bold">11. Fare & Pass Catalog</h3>
                    <span class="text-xs text-outline">Single, Day, Commuter, Month</span>
                </div>
                <button class="px-2.5 py-1 rounded-lg bg-primary text-on-primary text-xs font-semibold" onclick="setViewMode('mobile'); setScreen('11_fares')">Preview</button>
            </div>
            <div class="gallery-card-body p-3">
                {main_16}
            </div>
        </div>

        <!-- Card 9 -->
        <div class="gallery-card">
            <div class="gallery-card-header">
                <div>
                    <h3 class="font-headline-sm text-sm font-bold">13. Alex Mercer ID</h3>
                    <span class="text-xs text-outline">Gold Member & RFID</span>
                </div>
                <button class="px-2.5 py-1 rounded-lg bg-primary text-on-primary text-xs font-semibold" onclick="setViewMode('mobile'); setScreen('17_profile')">Preview</button>
            </div>
            <div class="gallery-card-body p-3">
                {main_17}
            </div>
        </div>

        <!-- Card 10 -->
        <div class="gallery-card">
            <div class="gallery-card-header">
                <div>
                    <h3 class="font-headline-sm text-sm font-bold">18. Command Center Desktop</h3>
                    <span class="text-xs text-outline">3-Column Dispatch Station</span>
                </div>
                <button class="px-2.5 py-1 rounded-lg bg-primary text-on-primary text-xs font-semibold" onclick="setViewMode('desktop')">Open Full</button>
            </div>
            <div class="gallery-card-body p-3">
                <img src="alternate_laptop_command_center_desktop_view/screen.png" alt="Command Center Desktop Preview" class="w-full h-auto rounded-xl">
            </div>
        </div>
    </div>

</div>

<!-- Shared Reactive State Engine -->
<script src="assets/js/stitch-app.js"></script>

</body>
</html>
'''

output_path = os.path.join(base_dir, 'index.html')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(unified_html)

print(f"Successfully generated unified {output_path} ({len(unified_html)} chars)")
