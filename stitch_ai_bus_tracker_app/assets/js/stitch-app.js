/**
 * Stitch AI Bus Tracker — Aether Transit Unified Engine
 * Shared Reactive State & Micro-Interactions across all 18 Screens
 */

(function () {
    const StitchState = {
        walletBalance: 350.00,
        currency: '₹',
        activeScreen: '14_home', // default: 14_home (Commuter Home)
        viewMode: 'mobile',      // 'mobile' | 'desktop' | 'gallery'
        autoReload: true,
        selectedTicketPrice: 25.00,
        selectedTicketName: 'Single Metro & Bus Ride',
        passExpirySeconds: 5052, // 1h 24m 12s
        activeFilter: 'all',
        trafficLayerActive: false
    };

    window.StitchState = StitchState;

    // --- State Persistence & Sync ---
    function updateWalletDisplays() {
        document.querySelectorAll('.wallet-balance-val').forEach(el => {
            el.textContent = `${StitchState.currency}${StitchState.walletBalance.toFixed(2)}`;
        });
    }

    function addBalance(amount) {
        StitchState.walletBalance += amount;
        updateWalletDisplays();
        showFeedbackToast(`+${StitchState.currency}${amount} added to Aether Mobility Wallet!`);
    }
    window.addBalance = addBalance;

    function toggleAutoReload() {
        StitchState.autoReload = !StitchState.autoReload;
        const btn = document.getElementById('toggle-autoreload');
        if (btn) {
            btn.innerHTML = StitchState.autoReload ? `
                <span class="relative flex h-2 w-2">
                    <span class="absolute inline-flex h-full w-full animate-ping rounded-full bg-tertiary-fixed opacity-75"></span>
                    <span class="relative inline-flex h-2 w-2 rounded-full bg-tertiary-fixed"></span>
                </span>
                <span class="font-label-sm text-label-sm text-on-primary font-medium tracking-wide">Auto-Reload Active</span>
            ` : `
                <span class="relative flex h-2 w-2">
                    <span class="relative inline-flex h-2 w-2 rounded-full bg-outline-variant"></span>
                </span>
                <span class="font-label-sm text-label-sm text-on-primary/80 font-medium tracking-wide">Auto-Reload Paused</span>
            `;
        }
        showFeedbackToast(StitchState.autoReload ? 'Auto-reload enabled at ₹100 threshold' : 'Auto-reload paused');
    }
    window.toggleAutoReload = toggleAutoReload;

    // --- Navigation & Screen Switcher ---
    function setScreen(screenId) {
        StitchState.activeScreen = screenId;
        
        // Hide all screens in mobile viewport
        document.querySelectorAll('.stitch-screen-view').forEach(el => {
            el.classList.add('hidden');
        });

        // Show target screen
        const target = document.getElementById(`screen_${screenId}`);
        if (target) {
            target.classList.remove('hidden');
        }

        // Update mobile bottom nav active states
        document.querySelectorAll('.mobile-bottom-nav a').forEach(link => {
            const path = link.getAttribute('data-path');
            if (
                (path === 'home' && (screenId === '14_home' || screenId === '01_mascot')) ||
                (path === 'explore' && (screenId === '06_search' || screenId === '07_planner' || screenId === '08_comparison')) ||
                (path === 'live-tracking' && (screenId === '05_radar' || screenId === '03_vector_map' || screenId === '04_hud')) ||
                (path === 'tickets' && (screenId === '16_wallet' || screenId === '10_pass' || screenId === '11_fares' || screenId === '12_qr_modal')) ||
                (path === 'profile' && (screenId === '17_profile' || screenId === '13_identity' || screenId === '14_impact' || screenId === '15_optimization' || screenId === '16_payments' || screenId === '17_system_settings'))
            ) {
                link.classList.add('text-primary-container', 'font-semibold');
                link.classList.remove('text-on-surface-variant');
            } else {
                link.classList.remove('text-primary-container', 'font-semibold');
                link.classList.add('text-on-surface-variant');
            }
        });

        // Update active quick pill in screen selector
        document.querySelectorAll('.screen-pill-btn').forEach(btn => {
            if (btn.getAttribute('data-screen') === screenId) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });

        // Scroll mobile container to top
        const phoneViewport = document.getElementById('phoneScrollableArea');
        if (phoneViewport) phoneViewport.scrollTop = 0;
    }
    window.setScreen = setScreen;

    function setViewMode(mode) {
        StitchState.viewMode = mode;
        const mobileContainer = document.getElementById('mobileShellWrapper');
        const desktopContainer = document.getElementById('desktopShellWrapper');
        const galleryContainer = document.getElementById('galleryShellWrapper');

        document.querySelectorAll('.view-mode-pill').forEach(btn => {
            btn.classList.toggle('active', btn.getAttribute('data-mode') === mode);
        });

        if (mode === 'mobile') {
            if (mobileContainer) mobileContainer.style.display = 'flex';
            if (desktopContainer) desktopContainer.style.display = 'none';
            if (galleryContainer) galleryContainer.style.display = 'none';
        } else if (mode === 'desktop') {
            if (mobileContainer) mobileContainer.style.display = 'none';
            if (desktopContainer) desktopContainer.style.display = 'block';
            if (galleryContainer) galleryContainer.style.display = 'none';
        } else if (mode === 'gallery') {
            if (mobileContainer) mobileContainer.style.display = 'none';
            if (desktopContainer) desktopContainer.style.display = 'none';
            if (galleryContainer) galleryContainer.style.display = 'grid';
        }
    }
    window.setViewMode = setViewMode;

    // --- Interactive Turnstile QR Modal ---
    function openPassModal() {
        const modal = document.getElementById('pass-modal');
        const sheet = document.getElementById('pass-sheet');
        if (modal && sheet) {
            modal.classList.remove('pointer-events-none', 'opacity-0');
            modal.classList.add('opacity-100');
            sheet.classList.remove('translate-y-full');
            sheet.classList.add('translate-y-0');
        }
    }
    window.openPassModal = openPassModal;

    function closePassModal() {
        const modal = document.getElementById('pass-modal');
        const sheet = document.getElementById('pass-sheet');
        if (modal && sheet) {
            modal.classList.add('opacity-0', 'pointer-events-none');
            modal.classList.remove('opacity-100');
            sheet.classList.add('translate-y-full');
            sheet.classList.remove('translate-y-0');
        }
    }
    window.closePassModal = closePassModal;

    // --- Ticket Selection in Screen 16 ---
    function selectTicketCard(cardElement, price, name) {
        document.querySelectorAll('.ticket-card').forEach(el => {
            el.classList.remove('ring-2', 'ring-primary');
            const radioIcon = el.querySelector('.material-symbols-outlined[style*="FILL"]');
            if (radioIcon) {
                radioIcon.textContent = 'radio_button_unchecked';
                radioIcon.style.color = '#737686';
                radioIcon.style.fontVariationSettings = '"FILL" 0';
            }
        });

        cardElement.classList.add('ring-2', 'ring-primary');
        const radio = cardElement.querySelector('.material-symbols-outlined');
        if (radio) {
            radio.textContent = 'radio_button_checked';
            radio.style.color = '#004ac6';
            radio.style.fontVariationSettings = '"FILL" 1';
        }

        StitchState.selectedTicketPrice = price;
        StitchState.selectedTicketName = name;

        const ctaText = document.getElementById('cta-text');
        if (ctaText) {
            ctaText.textContent = `Purchase Ticket • ${StitchState.currency}${price.toFixed(2)}`;
        }
    }
    window.selectTicketCard = selectTicketCard;

    function purchaseSelectedTicket() {
        if (StitchState.walletBalance < StitchState.selectedTicketPrice) {
            showFeedbackToast('Insufficient balance. Please top up your wallet first.');
            return;
        }
        StitchState.walletBalance -= StitchState.selectedTicketPrice;
        updateWalletDisplays();
        openPassModal();
        showFeedbackToast(`Ticket Purchased: ${StitchState.selectedTicketName}`);
    }
    window.purchaseSelectedTicket = purchaseSelectedTicket;

    // --- Map Radar Micro-Interactions (Screen 05) ---
    function triggerGpsPulse() {
        const userMarker = document.getElementById('userGpsMarker');
        if (userMarker) {
            userMarker.style.transition = 'transform 0.5s ease-out';
            userMarker.setAttribute('transform', 'translate(200, 180) scale(1.15)');
            setTimeout(() => {
                userMarker.setAttribute('transform', 'translate(196, 175) scale(1)');
            }, 500);
        }
        showFeedbackToast('RTK GPS Locked: Grand Central Platform 3A (±0.4m)');
    }
    window.triggerGpsPulse = triggerGpsPulse;

    function recenterMap() {
        triggerGpsPulse();
    }
    window.recenterMap = recenterMap;

    function toggleMapLayer(btn) {
        StitchState.trafficLayerActive = !StitchState.trafficLayerActive;
        const icon = btn.querySelector('.material-symbols-outlined');
        if (icon) {
            icon.style.transform = StitchState.trafficLayerActive ? 'rotate(180deg)' : 'rotate(0deg)';
            icon.style.transition = 'transform 0.3s ease';
        }
        showFeedbackToast(StitchState.trafficLayerActive ? '3D Traffic Layer Enabled' : 'Standard Vector Map');
    }
    window.toggleMapLayer = toggleMapLayer;

    function zoomMap(delta) {
        const bus = document.getElementById('busMarker42');
        if (bus) {
            bus.style.transition = 'transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1)';
            const currentScale = delta > 0 ? 'scale(1.1)' : 'scale(0.95)';
            bus.setAttribute('transform', 'translate(172, 118) ' + currentScale);
            setTimeout(() => {
                bus.setAttribute('transform', 'translate(172, 118) scale(1)');
            }, 400);
        }
    }
    window.zoomMap = zoomMap;

    function trackJourney(btn) {
        const originalText = btn.innerHTML;
        btn.innerHTML = '<span class="material-symbols-outlined text-[20px] animate-spin">sync</span><span>Syncing Route...</span>';
        setTimeout(() => {
            btn.innerHTML = '<span class="material-symbols-outlined text-[20px]">check_circle</span><span>Tracking Active</span>';
            btn.classList.remove('bg-primary-container');
            btn.classList.add('bg-emerald-600');
            showFeedbackToast('Live Journey Navigation Active: Arriving in 2m 40s');
        }, 800);
    }
    window.trackJourney = trackJourney;

    function shareLiveEta(btn) {
        const originalContent = btn.innerHTML;
        btn.innerHTML = '<span class="material-symbols-outlined text-[19px] text-emerald-600">done</span><span>Copied!</span>';
        if (navigator.clipboard) {
            navigator.clipboard.writeText('Line 42 Express arrives in 2m 40s at Grand Central Platform 3A. Track live via TransAI: https://transai.transit');
        }
        setTimeout(() => {
            btn.innerHTML = originalContent;
        }, 1600);
        showFeedbackToast('Live ETA Link copied to clipboard!');
    }
    window.shareLiveEta = shareLiveEta;

    // --- Route Planner Waypoint Swap (Screen 07 & Desktop) ---
    function swapRouteWaypoints() {
        const originInput = document.getElementById('originInput') || document.querySelector('input[value*="Grand Central"]');
        const destInput = document.getElementById('destInput') || document.querySelector('input[value*="Tech Park"]');
        if (originInput && destInput) {
            const temp = originInput.value;
            originInput.value = destInput.value;
            destInput.value = temp;
            showFeedbackToast('Origin & Destination Waypoints Swapped');
        }
    }
    window.swapRouteWaypoints = swapRouteWaypoints;

    // --- Toast Feedback ---
    function showFeedbackToast(msg) {
        let toast = document.getElementById('stitchToast');
        if (!toast) {
            toast = document.createElement('div');
            toast.id = 'stitchToast';
            toast.className = 'fixed bottom-20 left-1/2 -translate-x-1/2 z-[100] bg-inverse-surface/95 text-inverse-on-surface px-4 py-2.5 rounded-full shadow-2xl backdrop-blur-md flex items-center gap-2 font-label-md text-label-md transition-all duration-300 opacity-0 pointer-events-none transform translate-y-3';
            document.body.appendChild(toast);
        }
        toast.innerHTML = `<span class="material-symbols-outlined text-[18px] text-tertiary-fixed">info</span><span>${msg}</span>`;
        toast.classList.remove('opacity-0', 'pointer-events-none', 'translate-y-3');
        toast.classList.add('opacity-100', 'translate-y-0');

        clearTimeout(toast._timeout);
        toast._timeout = setTimeout(() => {
            toast.classList.remove('opacity-100', 'translate-y-0');
            toast.classList.add('opacity-0', 'pointer-events-none', 'translate-y-3');
        }, 2600);
    }
    window.showFeedbackToast = showFeedbackToast;

    // --- Pass Timer Countdown ---
    setInterval(() => {
        if (StitchState.passExpirySeconds > 0) {
            StitchState.passExpirySeconds--;
            const h = Math.floor(StitchState.passExpirySeconds / 3600);
            const m = Math.floor((StitchState.passExpirySeconds % 3600) / 60);
            const s = StitchState.passExpirySeconds % 60;
            const timerEl = document.getElementById('pass-timer');
            if (timerEl) {
                timerEl.textContent = `Expires in ${String(h).padStart(2, '0')}h:${String(m).padStart(2, '0')}m:${String(s).padStart(2, '0')}s`;
            }
        }
    }, 1000);

})();
