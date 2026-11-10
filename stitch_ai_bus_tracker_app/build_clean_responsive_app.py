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
    content = re.sub(r'<script.*?</script>', '', content, flags=re.DOTALL)
    return content

main_14 = extract_main_content(html_14)
main_05 = extract_main_content(html_05)
main_06 = extract_main_content(html_06)
main_16 = extract_main_content(html_16)
main_17 = extract_main_content(html_17)

# Image map for local assets with CDN fallback
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
desktop_body = re.sub(r'<script.*?</script>', '', desktop_body, flags=re.DOTALL)
desktop_body = localize_images(desktop_body)

# Replace INR balance displays with reactive span
main_16 = main_16.replace("₹350.00", '<span class="wallet-balance-val">₹350.00</span>')
desktop_body = desktop_body.replace("₹350.00", '<span class="wallet-balance-val">₹350.00</span>')

# Build clean responsive HTML
html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>Where Is My Bus — TransAI Mobility</title>

    <!-- Material Symbols & Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
    <link href="https://fonts.googleapis.com" rel="preconnect">
    <link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">

    <!-- Tailwind CSS with custom design tokens -->
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
                background: #f8f9ff;
                color: #0b1c30;
                overflow-x: hidden;
            }}
            ::-webkit-scrollbar {{
                width: 6px;
                height: 6px;
                display: none;
            }}
        }}

        /* Responsive Viewport Visibility */
        @media (min-width: 1024px) {{
            .mobile-only-view {{
                display: none !important;
            }}
            .desktop-only-view {{
                display: block !important;
            }}
        }}

        @media (max-width: 1023px) {{
            .mobile-only-view {{
                display: block !important;
            }}
            .desktop-only-view {{
                display: none !important;
            }}
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

    <!-- ========================================================================= -->
    <!-- 1. DESKTOP VIEW (Displayed naturally on Laptops & Desktops: width >= 1024px) -->
    <!-- ========================================================================= -->
    <div id="desktopAppContainer" class="desktop-only-view w-full min-h-screen">
        {desktop_body}
    </div>

    <!-- ========================================================================= -->
    <!-- 2. MOBILE VIEW (Displayed naturally edge-to-edge on Phones: width < 1024px) -->
    <!-- ========================================================================= -->
    <div id="mobileAppContainer" class="mobile-only-view w-full min-h-screen flex flex-col relative bg-surface">

        <!-- Mobile Header (Fixed Edge-to-Edge) -->
        <header class="fixed top-0 inset-x-0 h-16 z-40 bg-surface/85 backdrop-blur-xl border-b border-surface-container-high px-4 flex items-center justify-between shadow-xs">
            <div class="flex items-center gap-2.5">
                <img alt="Where Is My Bus" class="h-8 w-auto object-contain" src="assets/img/logo_wimb.png" onerror="this.src='https://lh3.googleusercontent.com/aida-public/AB6AXuCEZCRgqSKrU5lEE1YQp5StLNfsUh2XAYP_JDHfOP-2qo3v4DSjRTH5R5_2LRnBEyyTAWMk6P91OogeiC3J8Q9r9qEUUf4FWTjUR33My2-04ObGWZvJw1E57uxf_yms1Gtopzgl3kD7JbMknN9bOKt4LC76uPJ_7zyB1gt59SkMASpIIcsVmjuNN05eTgHogKGIdn_6Yo48S0XcoipHAkrRDrUK0oE55z5MFuUop_jmcI618rnXU68kLg'">
                <div class="flex flex-col">
                    <div class="flex items-center gap-1.5">
                        <span class="font-label-sm text-primary uppercase tracking-wider text-[10px] font-bold">TransAI</span>
                        <span class="inline-flex items-center gap-1 px-1.5 py-0.2 rounded-full bg-surface-container-high text-tertiary font-label-sm text-[9px]">
                            <span class="w-1.5 h-1.5 rounded-full bg-tertiary-container animate-pulse"></span>Live Sync
                        </span>
                    </div>
                    <span class="font-headline-sm text-headline-sm text-on-surface leading-tight text-sm font-semibold">Where Is My Bus</span>
                </div>
            </div>

            <div class="flex items-center gap-2">
                <button aria-label="Notifications" class="relative w-9 h-9 flex items-center justify-center rounded-full text-on-surface-variant hover:text-on-surface hover:bg-surface-container-high transition-colors" onclick="showFeedbackToast('All 418 buses on-time across corridor')">
                    <span class="material-symbols-outlined text-[22px]">notifications</span>
                    <span class="absolute top-2 right-2 w-2 h-2 rounded-full bg-primary-container ring-2 ring-surface"></span>
                </button>
                <button class="w-9 h-9 flex items-center justify-center rounded-full cursor-pointer ring-2 ring-primary/20" onclick="switchMobileTab('profile')">
                    <img alt="Alex Mercer Profile" class="w-8 h-8 rounded-full object-cover" src="assets/img/avatar_profile.png" onerror="this.src='https://lh3.googleusercontent.com/aida-public/AB6AXuDy_muJZDvDqRbnvQbRbN7LuLEFlaifkTBB7eKXbCI4CZBqczbQewsgA_ortobcY4Xmb1PcIqw-F9Q0z1cNFQLpvwBbAhAVfZMUiKdMvYAWGzu6p4kZXBiaRcSeYVHzfgEqxUlICf1NcdwiT2vmNpgRf9i3Sz8M757o3zz80Mt5eifb-IMXSY0MAvG7Mefjw7banipuce5S9o_H2mPcaYMH2plGHuXTQ-Ov4vmYazHL'">
                </button>
            </div>
        </header>

        <!-- Main Mobile Content Panes (Switchable via Bottom Tabs) -->
        <main class="w-full pt-16 pb-20 flex-1">

            <!-- TAB 1: HOME (Saved Corridors + Animated Mascot Bus) -->
            <div id="mobileTab_home" class="mobile-tab-pane w-full">
                {main_14}
            </div>

            <!-- TAB 2: EXPLORE (Trip Planner + Suggested Routes) -->
            <div id="mobileTab_explore" class="mobile-tab-pane w-full hidden">
                {main_06}
            </div>

            <!-- TAB 3: LIVE TRACK (Interactive Vector Radar Map + Draggable Bottom Sheet) -->
            <div id="mobileTab_live-tracking" class="mobile-tab-pane w-full hidden">
                {main_05}
            </div>

            <!-- TAB 4: TICKETS (Aether Mobility Wallet + Fares & Passes) -->
            <div id="mobileTab_tickets" class="mobile-tab-pane w-full hidden">
                {main_16}
            </div>

            <!-- TAB 5: PROFILE (Alex Mercer ID + Commute Engine Settings) -->
            <div id="mobileTab_profile" class="mobile-tab-pane w-full hidden">
                {main_17}
            </div>

        </main>

        <!-- Native Mobile Bottom Navigation Bar (Fixed Edge-to-Edge) -->
        <nav class="fixed bottom-0 inset-x-0 h-16 z-40 pb-safe bg-surface/90 backdrop-blur-xl border-t border-surface-container-high shadow-lg">
            <div class="flex justify-around items-center h-full px-2">
                <button class="mobile-nav-btn flex flex-col items-center justify-center gap-0.5 min-w-[56px] text-primary-container font-semibold transition-colors" data-tab="home" onclick="switchMobileTab('home')">
                    <span class="material-symbols-outlined text-[24px]">home</span>
                    <span class="font-label-sm text-label-sm text-[11px]">Home</span>
                </button>
                <button class="mobile-nav-btn flex flex-col items-center justify-center gap-0.5 min-w-[56px] text-on-surface-variant hover:text-primary transition-colors" data-tab="explore" onclick="switchMobileTab('explore')">
                    <span class="material-symbols-outlined text-[24px]">explore</span>
                    <span class="font-label-sm text-label-sm text-[11px]">Explore</span>
                </button>
                <button class="mobile-nav-btn flex flex-col items-center justify-center gap-0.5 min-w-[56px] text-on-surface-variant hover:text-primary transition-colors" data-tab="live-tracking" onclick="switchMobileTab('live-tracking')">
                    <span class="material-symbols-outlined text-[24px]">directions_bus</span>
                    <span class="font-label-sm text-label-sm text-[11px]">Live Track</span>
                </button>
                <button class="mobile-nav-btn flex flex-col items-center justify-center gap-0.5 min-w-[56px] text-on-surface-variant hover:text-primary transition-colors" data-tab="tickets" onclick="switchMobileTab('tickets')">
                    <span class="material-symbols-outlined text-[24px]">confirmation_number</span>
                    <span class="font-label-sm text-label-sm text-[11px]">Tickets</span>
                </button>
                <button class="mobile-nav-btn flex flex-col items-center justify-center gap-0.5 min-w-[56px] text-on-surface-variant hover:text-primary transition-colors" data-tab="profile" onclick="switchMobileTab('profile')">
                    <span class="material-symbols-outlined text-[24px]">person</span>
                    <span class="font-label-sm text-label-sm text-[11px]">Profile</span>
                </button>
            </div>
        </nav>

        <!-- Turnstile QR Drawer Modal -->
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

    <!-- Shared Reactive State Engine -->
    <script src="assets/js/stitch-app.js"></script>

    <script>
    // Mobile Tab Switching
    function switchMobileTab(tabId) {{
        document.querySelectorAll('.mobile-tab-pane').forEach(el => {{
            el.classList.add('hidden');
        }});

        const target = document.getElementById('mobileTab_' + tabId);
        if (target) {{
            target.classList.remove('hidden');
        }}

        document.querySelectorAll('.mobile-nav-btn').forEach(btn => {{
            if (btn.getAttribute('data-tab') === tabId) {{
                btn.classList.add('text-primary-container', 'font-semibold');
                btn.classList.remove('text-on-surface-variant');
            }} else {{
                btn.classList.remove('text-primary-container', 'font-semibold');
                btn.classList.add('text-on-surface-variant');
            }}
        }});

        window.scrollTo(0, 0);
    }}
    </script>

</body>
</html>
'''

output_path = os.path.join(base_dir, 'index.html')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated clean responsive {output_path} ({len(html_content)} chars)")
