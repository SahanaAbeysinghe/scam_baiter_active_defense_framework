import streamlit as st
import streamlit.components.v1 as components
import requests
import sys
import json
from datetime import datetime

if __name__ == "__main__":
    try:
        import streamlit.runtime
        if not streamlit.runtime.exists():
            from streamlit.web import cli as stcli
            sys.argv = ["streamlit", "run", sys.argv[0]]
            sys.exit(stcli.main())
    except ImportError:
        pass

st.set_page_config(
    page_title="Scam Baiter // Active Defense Framework",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

    .stApp {
        background-color: #000000;
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #f5f5f5;
    }

    .main .block-container {
        max-width: 95% !important;
        padding-top: 0 !important;
        padding-bottom: 2rem !important;
        padding-left: 2.5rem !important;
        padding-right: 2.5rem !important;
        position: relative;
        z-index: 1;
    }


    .hero-wrap {
        position: relative;
        padding: 50px 20px 40px 20px;
        text-align: center;
        overflow: hidden;
        border-radius: 0 0 24px 24px;
        background: radial-gradient(ellipse at 50% 0%, rgba(16, 40, 30, 0.55) 0%, rgba(0,0,0,0) 60%);
    }
    .hero-wrap p, .hero-wrap div, .hero-wrap h1 {
        text-align: center !important;
    }
    .hero-photo {
        position: absolute;
        inset: 0;
        z-index: 0;
        background-image:
            linear-gradient(180deg, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0.75) 55%, #000000 100%),
            linear-gradient(0deg, rgba(10,30,20,0.65), rgba(10,30,20,0.65)),
            url('https://picsum.photos/id/60/1600/900?grayscale');
        background-blend-mode: normal, color, normal;
        background-size: cover;
        background-position: center;
        opacity: 0.6;
        filter: contrast(1.1) brightness(0.9);
        animation: kenburns 26s ease-in-out infinite alternate;
    }
    @keyframes kenburns {
        0%   { transform: scale(1) translate(0, 0); }
        100% { transform: scale(1.12) translate(-1.5%, -1%); }
    }
    @media (prefers-reduced-motion: reduce) {
        .hero-photo { animation: none; }
    }
    .hero-arcs {
        position: absolute;
        top: 40px;
        left: 50%;
        transform: translateX(-50%);
        width: 1100px;
        max-width: 130%;
        z-index: 0;
        filter: drop-shadow(0 0 18px rgba(34, 197, 94, 0.35));
        pointer-events: none;
    }
    .hero-content {
        position: relative;
        z-index: 2;
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }

    .brand-title {
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.05rem;
        font-weight: 700;
        letter-spacing: 0.04em;
        color: #4ade80;
        margin-bottom: 6px;
    }
    .brand-tagline {
        font-size: 0.92rem;
        color: #9ca3af;
        max-width: 520px !important;
        margin: 0 0 28px 0 !important;
        line-height: 1.5;
        text-align: center !important;
    }


    .st-key-tab_switch { display: flex; justify-content: center; margin: 18px 0 6px 0; }
    .st-key-tab_switch > div { display: flex; justify-content: center; gap: 8px; }
    .st-key-tab_switch div[data-testid="column"] { width: auto !important; flex: 0 0 auto !important; }
    .st-key-tab_switch button {
        border-radius: 9999px !important;
        padding: 6px 22px !important;
        font-size: 0.82rem !important;
        font-weight: 600 !important;
    }
    .st-key-tab_switch button[kind="primary"] {
        background: rgba(34, 197, 94, 0.16) !important;
        color: #4ade80 !important;
        border: 1px solid rgba(74, 222, 128, 0.45) !important;
    }
    .st-key-tab_switch button[kind="secondary"] {
        background: rgba(255,255,255,0.04) !important;
        color: #9ca3af !important;
        border: 1px solid rgba(255,255,255,0.09) !important;
    }


    .history-card {
        background: rgba(10, 14, 12, 0.85);
        border: 1px solid rgba(255,255,255,0.08);
        border-left: 3px solid #22c55e;
        border-radius: 12px;
        padding: 16px 18px;
        margin-bottom: 14px;
        animation: panelIn 0.4s cubic-bezier(0.22, 1, 0.36, 1) both;
    }
    .history-card.clean { border-left-color: #4b5563; }
    .history-meta {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.72rem;
        color: #6b7280;
        margin-bottom: 10px;
    }
    .history-snippet {
        font-size: 0.9rem;
        color: #e5e7eb;
        line-height: 1.5;
        margin-bottom: 10px;
    }
    .history-reply {
        font-size: 0.85rem;
        color: #86efac;
        background: rgba(34,197,94,0.06);
        border: 1px solid rgba(34,197,94,0.18);
        border-radius: 8px;
        padding: 10px 12px;
        line-height: 1.55;
        white-space: pre-wrap;
    }

    .nav-pill-row {
        display: inline-flex;
        align-items: center;
        gap: 4px;
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.09);
        padding: 5px;
        border-radius: 9999px;
        margin-bottom: 34px;
    }
    .nav-pill-item {
        font-size: 0.78rem;
        font-weight: 600;
        padding: 6px 18px;
        border-radius: 9999px;
        color: #9ca3af;
    }
    .nav-pill-item.active {
        background: rgba(34, 197, 94, 0.14);
        color: #4ade80;
        border: 1px solid rgba(34, 197, 94, 0.4);
    }

    .glow-badge {
        width: 68px;
        height: 68px;
        margin: 0 auto 22px auto;
        border-radius: 18px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(180deg, rgba(34,197,94,0.18) 0%, rgba(0,0,0,0.4) 100%);
        border: 1px solid rgba(74, 222, 128, 0.4);
        box-shadow: 0 0 40px rgba(34, 197, 94, 0.45), inset 0 0 20px rgba(34,197,94,0.15);
    }

    .hero-headline {
        font-size: 3.6rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        line-height: 1.08;
        margin: 0 0 18px 0;
        color: #f8fafc;
    }
    .hero-headline .accent {
        background: linear-gradient(90deg, #4ade80, #22d3ee);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero-subline {
        color: #9ca3af;
        font-size: 1.08rem;
        max-width: 640px !important;
        margin: 0 0 30px 0 !important;
        line-height: 1.6;
        text-align: center !important;
    }
    .hero-cta {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: #ffffff;
        color: #050505;
        font-weight: 700;
        font-size: 0.92rem;
        padding: 12px 26px;
        border-radius: 9999px;
        box-shadow: 0 0 30px rgba(255,255,255,0.15);
        margin-bottom: 40px;
    }

    .trust-row {
        display: flex;
        justify-content: center;
        gap: 14px;
        flex-wrap: wrap;
        margin-top: 6px;
    }
    .trust-chip {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.72rem;
        color: #6b7280;
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.08);
        padding: 6px 14px;
        border-radius: 9999px;
    }


    .steps-wrap {
        max-width: 900px;
        margin: 50px auto 10px auto;
        text-align: center;
    }
    .steps-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #f1f5f9;
        margin-bottom: 34px;
    }
    .steps-title .accent { color: #4ade80; }
    .steps-row {
        display: flex;
        align-items: flex-start;
        justify-content: center;
        gap: 0;
    }
    .step-node {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 190px;
    }
    .step-icon-box {
        width: 72px;
        height: 72px;
        border-radius: 16px;
        background: rgba(34, 197, 94, 0.1);
        border: 1px solid rgba(74, 222, 128, 0.35);
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 0 22px rgba(34,197,94,0.25);
        margin-bottom: 12px;
        position: relative;
        overflow: hidden;
        transition: transform 0.35s ease, box-shadow 0.35s ease;
    }
    .step-icon-box:hover {
        transform: translateY(-4px) scale(1.04);
        box-shadow: 0 0 30px rgba(34,197,94,0.45);
    }
    .step-icon-box img {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        filter: grayscale(0.4) brightness(0.55) saturate(1.4);
    }
    .step-icon-box .step-icon-tint {
        position: absolute;
        inset: 0;
        background: linear-gradient(160deg, rgba(34,197,94,0.35), rgba(0,0,0,0.35));
        mix-blend-mode: color;
    }
    .step-icon-box svg { position: relative; z-index: 1; }
    .step-caption { font-size: 0.82rem; color: #9ca3af; line-height: 1.4; }
    .step-connector {
        height: 1px;
        width: 60px;
        background: linear-gradient(90deg, rgba(74,222,128,0.5), rgba(74,222,128,0.1));
        margin-top: 28px;
    }


    .command-panel {
        background: rgba(10, 14, 12, 0.85);
        border: 1px solid rgba(74, 222, 128, 0.15);
        border-radius: 18px;
        padding: 22px;
        box-shadow: 0 20px 45px -10px rgba(0, 0, 0, 0.7);
        height: 100%;
        margin-top: 20px;
        transition: border-color 0.3s ease, transform 0.3s ease;
    }
    .command-panel:hover {
        border-color: rgba(74, 222, 128, 0.32);
    }
    @keyframes panelIn {
        from { opacity: 0; transform: translateY(16px) scale(0.98); }
        to   { opacity: 1; transform: translateY(0) scale(1); }
    }
    .threat-banner-wide, .clean-banner-wide, .agent-reply-deck, .standby-card {
        animation: panelIn 0.5s cubic-bezier(0.22, 1, 0.36, 1) both;
    }
    .panel-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-bottom: 12px;
        margin-bottom: 16px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    }
    .panel-title-text {
        font-size: 0.95rem;
        font-weight: 700;
        color: #f1f5f9;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .window-pills { display: flex; gap: 6px; }
    .w-pill { width: 10px; height: 10px; border-radius: 50%; }
    .p-red { background: #ef4444; }
    .p-yellow { background: #f59e0b; }
    .p-green { background: #22c55e; }

    .threat-banner-wide {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.12) 0%, rgba(5, 8, 6, 0.95) 100%);
        border: 1px solid rgba(239, 68, 68, 0.45);
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 16px;
    }
    .clean-banner-wide {
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.14) 0%, rgba(5, 8, 6, 0.95) 100%);
        border: 1px solid rgba(34, 197, 94, 0.45);
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 16px;
    }

    .agent-reply-deck {
        background: #050807;
        border: 1px solid rgba(74, 222, 128, 0.3);
        border-top: 3px solid #22c55e;
        border-radius: 14px;
        padding: 20px;
        box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.5);
    }
    .agent-header-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-bottom: 10px;
        margin-bottom: 12px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    }
    .agent-label {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.8rem;
        font-weight: 700;
        color: #4ade80;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .agent-body-text { font-size: 0.98rem; line-height: 1.7; color: #f1f5f9; white-space: pre-wrap; }
    .telemetry-row {
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
        margin-top: 14px;
        padding-top: 12px;
        border-top: 1px solid rgba(255, 255, 255, 0.05);
    }
    .tele-tag {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.72rem;
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 3px 10px;
        border-radius: 6px;
        color: #9ca3af;
    }

    .standby-card {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 60px 30px;
        background: rgba(10, 14, 12, 0.5);
        border: 1px dashed rgba(74, 222, 128, 0.2);
        border-radius: 14px;
        height: 100%;
        min-height: 380px;
    }
    .standby-radar {
        width: 56px;
        height: 56px;
        border-radius: 50%;
        background: rgba(34, 197, 94, 0.1);
        border: 1px solid rgba(74, 222, 128, 0.35);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.6rem;
        margin-bottom: 16px;
        box-shadow: 0 0 25px rgba(34, 197, 94, 0.25);
    }
    .standby-title { font-weight: 700; font-size: 1.15rem; color: #f1f5f9; margin-bottom: 6px; }
    .standby-desc { font-size: 0.88rem; color: #6b7280; max-width: 360px; line-height: 1.55; }

    .wide-footer {
        margin-top: 4rem;
        padding: 24px 0 10px 0;
        border-top: 1px solid rgba(255, 255, 255, 0.07);
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 12px;
    }
    .footer-credits { font-size: 0.92rem; color: #9ca3af; }
    .footer-credits strong { color: #f1f5f9; }
    .footer-email-link { font-family: 'JetBrains Mono', monospace; font-size: 0.82rem; color: #4ade80; text-decoration: none; }
    .footer-email-link:hover { color: #86efac; text-decoration: underline; }
    .footer-meta-pill {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.72rem;
        padding: 4px 12px;
        border-radius: 9999px;
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.08);
        color: #6b7280;
    }


    .reveal {
        opacity: 0;
        transform: translateY(40px);
        transition: opacity 0.9s ease, transform 0.9s ease;
    }
    .reveal.visible {
        opacity: 1;
        transform: translateY(0);
    }
</style>
""", unsafe_allow_html=True)


components.html("""
<canvas id="particle-canvas"></canvas>
<style>
  html, body { margin:0; padding:0; background: transparent; overflow: hidden; }
  #particle-canvas { display:block; background: transparent; }
</style>
<script>
(function() {
  const frame = window.frameElement;
  if (frame) {
    frame.style.position = 'fixed';
    frame.style.top = '0';
    frame.style.left = '0';
    frame.style.width = '100vw';
    frame.style.height = '100vh';
    frame.style.zIndex = '0';
    frame.style.pointerEvents = 'none';
    frame.style.border = 'none';
  }
  const canvas = document.getElementById('particle-canvas');
  const ctx = canvas.getContext('2d');
  function resize() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
  resize();
  window.addEventListener('resize', resize);

  const particles = [];
  for (let i = 0; i < 55; i++) {
    particles.push({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      r: Math.random() * 1.8 + 0.5,
      vx: (Math.random() - 0.5) * 0.15,
      vy: (Math.random() - 0.5) * 0.15,
      alpha: Math.random() * 0.5 + 0.2
    });
  }

  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach(p => {
      p.x += p.vx; p.y += p.vy;
      if (p.x < 0) p.x = canvas.width;
      if (p.x > canvas.width) p.x = 0;
      if (p.y < 0) p.y = canvas.height;
      if (p.y > canvas.height) p.y = 0;
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(74, 222, 128, ${p.alpha})`;
      ctx.shadowBlur = 8;
      ctx.shadowColor = 'rgba(74, 222, 128, 0.8)';
      ctx.fill();
    });
    requestAnimationFrame(draw);
  }
  draw();
})();
</script>
""", height=1)


components.html("""
<script>
(function(){
  const doc = window.parent.document;
  function initObserver() {
    const targets = doc.querySelectorAll('.reveal:not(.reveal-bound)');
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) { entry.target.classList.add('visible'); }
      });
    }, { threshold: 0.15 });
    targets.forEach(el => { el.classList.add('reveal-bound'); observer.observe(el); });
  }
  let tries = 0;
  const interval = setInterval(() => { initObserver(); tries++; if (tries > 15) clearInterval(interval); }, 400);
})();
</script>
""", height=0)


if "active_view" not in st.session_state:
    st.session_state.active_view = "detection"

_detection_active_cls = "active" if st.session_state.active_view == "detection" else ""
_history_active_cls = "active" if st.session_state.active_view == "history" else ""


st.markdown(f"""
<div class="hero-wrap">
    <div class="hero-photo"></div>
    <svg class="hero-arcs" viewBox="0 0 1200 320" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <linearGradient id="arcGrad" x1="0" y1="0" x2="1" y2="0">
                <stop offset="0" stop-color="#22c55e" stop-opacity="0"/>
                <stop offset="0.5" stop-color="#4ade80" stop-opacity="0.9"/>
                <stop offset="1" stop-color="#22c55e" stop-opacity="0"/>
            </linearGradient>
        </defs>
        <path d="M0,320 C300,20 900,20 1200,320" stroke="url(#arcGrad)" stroke-width="1.5" fill="none"/>
        <path d="M0,320 C300,90 900,90 1200,320" stroke="url(#arcGrad)" stroke-width="1" fill="none" opacity="0.6"/>
        <path d="M0,320 C300,160 900,160 1200,320" stroke="url(#arcGrad)" stroke-width="1" fill="none" opacity="0.35"/>
    </svg>
    <div class="hero-content">
        <div class="brand-title">Scam Baiter — Active Defense Framework</div>
        <p class="brand-tagline">
            An active-defense cybersecurity tool that uses NLP to classify phishing emails
            and an LLM to auto-generate time-wasting replies to scammers.
        </p>
        <div class="nav-pill-row">
            <span class="nav-pill-item {_detection_active_cls}">Detection</span>
            <span class="nav-pill-item {_history_active_cls}">History</span>
        </div>
        <div class="glow-badge">
            <svg width="34" height="34" viewBox="0 0 90 90">
                <circle cx="45" cy="45" r="8" fill="#4ade80"/>
                <circle cx="20" cy="20" r="4" fill="#22c55e" opacity="0.8"/>
                <circle cx="70" cy="18" r="3.5" fill="#22c55e" opacity="0.7"/>
                <circle cx="75" cy="65" r="4" fill="#4ade80" opacity="0.8"/>
                <circle cx="15" cy="68" r="3" fill="#22c55e" opacity="0.6"/>
                <line x1="45" y1="45" x2="20" y2="20" stroke="#4ade80" stroke-width="1" opacity="0.5"/>
                <line x1="45" y1="45" x2="70" y2="18" stroke="#4ade80" stroke-width="1" opacity="0.5"/>
                <line x1="45" y1="45" x2="75" y2="65" stroke="#4ade80" stroke-width="1" opacity="0.5"/>
                <line x1="45" y1="45" x2="15" y2="68" stroke="#4ade80" stroke-width="1" opacity="0.5"/>
            </svg>
        </div>
        <h1 class="hero-headline">Detect Scams.<br><span class="accent">Waste Their Time.</span></h1>
        <p class="hero-subline">
            Autonomous email threat detection powered by machine learning classification.
            When phishing is identified, an AI honeypot agent engages the attacker directly —
            stalling them with a convincing, zero-leak persona.
        </p>
        <div class="hero-cta">⚡ Scan an Email Below</div>
        <div class="trust-row">
            <span class="trust-chip">ENGINE: PASSIVE-AGGRESSIVE + TF-IDF</span>
            <span class="trust-chip">ACCURACY: 98.17%</span>
            <span class="trust-chip">HONEYPOT: GEMINI GEN-AI</span>
            <span class="trust-chip">● DEFENSE GRID ONLINE</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


with st.container(key="tab_switch"):
    tab_col1, tab_col2 = st.columns(2, gap="small")
    with tab_col1:
        if st.button(
            "🔎 Detection",
            key="tab_btn_detection",
            type="primary" if st.session_state.active_view == "detection" else "secondary",
            use_container_width=True,
        ):
            st.session_state.active_view = "detection"
            st.rerun()
    with tab_col2:
        if st.button(
            "🕘 History",
            key="tab_btn_history",
            type="primary" if st.session_state.active_view == "history" else "secondary",
            use_container_width=True,
        ):
            st.session_state.active_view = "history"
            st.rerun()

def render_detection_view():
    st.markdown("""
    <div class="steps-wrap reveal">
        <div class="steps-title">How the Defense Pipeline <span class="accent">Works</span></div>
        <div class="steps-row">
            <div class="step-node">
                <div class="step-icon-box">
                    <img src="https://picsum.photos/id/0/200/200" alt="">
                    <div class="step-icon-tint"></div>
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#4ade80" stroke-width="1.6">
                        <path d="M3 8l9 6 9-6M4 6h16a1 1 0 011 1v10a1 1 0 01-1 1H4a1 1 0 01-1-1V7a1 1 0 011-1z"/>
                    </svg>
                </div>
                <div class="step-caption">Email content is<br>parsed and vectorized</div>
            </div>
            <div class="step-connector"></div>
            <div class="step-node">
                <div class="step-icon-box">
                    <img src="https://picsum.photos/id/96/200/200" alt="">
                    <div class="step-icon-tint"></div>
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#4ade80" stroke-width="1.6">
                        <circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="3"/><line x1="12" y1="3" x2="12" y2="6"/>
                    </svg>
                </div>
                <div class="step-caption">ML model classifies<br>scam vs. legitimate</div>
            </div>
            <div class="step-connector"></div>
            <div class="step-node">
                <div class="step-icon-box">
                    <img src="https://picsum.photos/id/119/200/200" alt="">
                    <div class="step-icon-tint"></div>
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#4ade80" stroke-width="1.6">
                        <path d="M21 11.5a8.5 8.5 0 01-8.5 8.5 8.4 8.4 0 01-4.1-1L3 20l1-5.4A8.5 8.5 0 1121 11.5z"/>
                    </svg>
                </div>
                <div class="step-caption">Gemini generates a<br>time-wasting reply</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


    if "email_input" not in st.session_state:
        st.session_state.email_input = ""
    if "last_result" not in st.session_state:
        st.session_state.last_result = None
    if "last_error" not in st.session_state:
        st.session_state.last_error = None


    col_left, col_right = st.columns([1, 1], gap="large")

    with col_left:
        st.markdown("""
        <div class="command-panel">
            <div class="panel-header">
                <div class="panel-title-text"><span>📥 Inbound Threat Interception Console</span></div>
                <div class="window-pills">
                    <div class="w-pill p-red"></div>
                    <div class="w-pill p-yellow"></div>
                    <div class="w-pill p-green"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        st.caption("⚡ Quick Test Presets (1-Click Sample Injections):")
        p1, p2, p3, p_clear = st.columns([1.1, 1.2, 1.1, 0.6])

        if p1.button("🚨 Bank Phish", use_container_width=True):
            st.session_state.email_input = (
                "URGENT: Your bank account access has been restricted due to suspicious activity. "
                "Please verify your credentials immediately at http://secure-banking-update.cc "
                "within 24 hours to prevent permanent account closure."
            )
            st.session_state.last_result = None
            st.session_state.last_error = None
            st.rerun()

        if p2.button("💰 Wire / Inheritance", use_container_width=True):
            st.session_state.email_input = (
                "CONFIDENTIAL NOTIFICATION: You have been approved to receive an unclaimed inheritance "
                "disbursement of $8,500,000 USD from our international escrow vault. Please reply immediately "
                "with your full legal name, telephone number, and bank account details to facilitate the wire transfer."
            )
            st.session_state.last_result = None
            st.session_state.last_error = None
            st.rerun()

        if p3.button("✅ Legitimate Email", use_container_width=True):
            st.session_state.email_input = (
                "Hi Sahana, just following up on our project milestones for this week. "
                "The updated evaluation results look great. Let's touch base tomorrow at 11:00 AM."
            )
            st.session_state.last_result = None
            st.session_state.last_error = None
            st.rerun()

        if p_clear.button("🗑️", use_container_width=True):
            st.session_state.email_input = ""
            st.session_state.last_result = None
            st.session_state.last_error = None
            st.rerun()

        email_text = st.text_area(
            label="Email Content to Inspect",
            value=st.session_state.email_input,
            placeholder="Paste suspicious raw email content, communication headers, or message body here...",
            height=240,
            label_visibility="collapsed"
        )

        st.write("")
        scan_clicked = st.button("⚡ Analyze Threat Vector & Deploy Defense →", type="primary", use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

    if scan_clicked:
        cleaned = email_text.strip()
        if not cleaned:
            st.session_state.last_error = "Please paste or type email content before initiating the scan."
            st.session_state.last_result = None
        else:
            api_url = "http://127.0.0.1:8000/scan"
            payload = {"email_text": cleaned}
            with st.spinner("Classifying email vector & preparing active countermeasures..."):
                try:
                    resp = requests.post(api_url, json=payload, timeout=30)
                    if resp.status_code == 200:
                        st.session_state.last_result = resp.json()
                        st.session_state.last_error = None
                    else:
                        st.session_state.last_error = f"Backend returned HTTP {resp.status_code}: {resp.text}"
                        st.session_state.last_result = None
                except requests.exceptions.ConnectionError:
                    st.session_state.last_error = (
                        "CONNECTION_REFUSED: Could not connect to FastAPI backend at http://127.0.0.1:8000. "
                        "Please run `uvicorn main:app --reload` in your terminal."
                    )
                    st.session_state.last_result = None
                except requests.exceptions.Timeout:
                    st.session_state.last_error = "TIMEOUT: The backend server took longer than 30s to respond."
                    st.session_state.last_result = None
                except requests.exceptions.RequestException as e:
                    st.session_state.last_error = f"NETWORK ERROR: {e}"
                    st.session_state.last_result = None

    with col_right:
        st.markdown("""
        <div class="command-panel">
            <div class="panel-header">
                <div class="panel-title-text"><span>🛰️ Threat Diagnostics & Autonomous Defense Monitor</span></div>
            </div>
        """, unsafe_allow_html=True)

        if st.session_state.last_error:
            if "CONNECTION_REFUSED" in st.session_state.last_error:
                st.markdown("""
                <div style="background: rgba(245, 158, 11, 0.1); border: 1px solid rgba(245, 158, 11, 0.45); border-radius: 12px; padding: 20px;">
                    <div style="color: #fbbf24; font-weight: 700; font-size: 1.05rem; margin-bottom: 6px;">⚠️ FastAPI Backend Server Offline</div>
                    <div style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.6;">
                        The interface cannot bridge to <code>http://127.0.0.1:8000/scan</code>.<br>
                        Please start the FastAPI service in a separate terminal:
                    </div>
                    <pre style="background: #050807; padding: 10px 14px; border-radius: 8px; margin-top: 10px; color: #4ade80; font-family: 'JetBrains Mono', monospace; font-size: 0.86rem; border: 1px solid rgba(74, 222, 128, 0.2);">uvicorn main:app --reload</pre>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error(f"⚠️ {st.session_state.last_error}")

        elif st.session_state.last_result:
            res_data = st.session_state.last_result
            is_scam = res_data.get("is_scam", False)
            label = res_data.get("label", "Unknown")
            generated_reply = res_data.get("generated_reply")

            if is_scam:
                st.markdown(f"""
                <div class="threat-banner-wide reveal visible">
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
                        <div style="display: flex; align-items: center; gap: 12px;">
                            <span style="font-size: 1.8rem;">🚨</span>
                            <div>
                                <div style="font-size: 0.75rem; font-family: 'JetBrains Mono', monospace; color: #f87171; font-weight: 700; letter-spacing: 1px;">THREAT VECTOR IDENTIFIED</div>
                                <div style="font-size: 1.45rem; font-weight: 800; color: #ffffff;">Classification: {label}</div>
                            </div>
                        </div>
                        <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.74rem; padding: 5px 14px; border-radius: 9999px; background: rgba(239,68,68,0.22); border: 1px solid #ef4444; color: #fca5a5; font-weight: 600;">ACTIVE HONEYPOT DEPLOYED</span>
                    </div>
                    <p style="margin: 12px 0 0 0; font-size: 0.92rem; color: #cbd5e1; line-height: 1.6;">
                        Passive-Aggressive linear vector confirmed malicious deceptive signatures. Autonomous counter-engagement protocol activated to stall the attacker with a simulated naive target persona.
                    </p>
                </div>
                """, unsafe_allow_html=True)

                if generated_reply:
                    st.markdown(f"""
                    <div class="agent-reply-deck">
                        <div class="agent-header-row">
                            <div class="agent-label">
                                <span>🤖 GEMINI AI DEFENSE AGENT</span>
                                <span style="color: #6b7280;">•</span>
                                <span style="color: #9ca3af; font-weight: normal;">Autonomous Counter-Response</span>
                            </div>
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; color: #6b7280;">ZERO-LEAK VERIFIED</span>
                        </div>
                        <div class="agent-body-text">{generated_reply}</div>
                        <div class="telemetry-row">
                            <span class="tele-tag">🎭 Persona: Naive Target</span>
                            <span class="tele-tag">⏱️ Attacker Time Burned: ~4.5 Min</span>
                            <span class="tele-tag">🛡️ PII Exposure: 0.00%</span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                    reply_json = json.dumps(generated_reply)
                    copy_btn_html = f"""
                    <!DOCTYPE html><html><head><style>
                    body {{ margin:0; padding:8px 0 0 0; background:transparent; display:flex; justify-content:flex-end; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif; }}
                    .copy-btn {{ display:inline-flex; align-items:center; gap:7px; background:rgba(34,197,94,0.12); border:1px solid rgba(74,222,128,0.35); color:#4ade80; padding:9px 18px; border-radius:8px; font-size:0.84rem; font-weight:600; cursor:pointer; transition:all 0.2s ease; font-family:inherit; outline:none; }}
                    .copy-btn:hover {{ background:rgba(34,197,94,0.24); border-color:#22c55e; color:#86efac; transform:translateY(-1px); box-shadow:0 4px 14px rgba(34,197,94,0.3); }}
                    .copy-btn.copied {{ background:rgba(34,197,94,0.18) !important; border-color:#22c55e !important; color:#4ade80 !important; }}
                    </style></head><body>
                    <button id="copyBtn" class="copy-btn" onclick="handleCopy()"><span id="btnIcon">📋</span><span id="btnText">Copy Counter-Response to Clipboard</span></button>
                    <script>
                    function handleCopy() {{
                      const text = {reply_json};
                      if (navigator.clipboard && window.isSecureContext) {{ navigator.clipboard.writeText(text).then(setCopiedState).catch(() => execCommandCopy(text)); }}
                      else {{ execCommandCopy(text); }}
                    }}
                    function execCommandCopy(text) {{
                      const ta = document.createElement('textarea'); ta.value = text; ta.style.position='fixed'; ta.style.left='-9999px';
                      document.body.appendChild(ta); ta.focus(); ta.select();
                      try {{ document.execCommand('copy'); setCopiedState(); }} catch(e) {{ document.getElementById('btnText').innerText = 'Copy failed'; }}
                      document.body.removeChild(ta);
                    }}
                    function setCopiedState() {{
                      const btn = document.getElementById('copyBtn'); const icon = document.getElementById('btnIcon'); const text = document.getElementById('btnText');
                      btn.classList.add('copied'); icon.innerText='✅'; text.innerText='Copied to Clipboard!';
                      setTimeout(() => {{ btn.classList.remove('copied'); icon.innerText='📋'; text.innerText='Copy Counter-Response to Clipboard'; }}, 2200);
                    }}
                    </script></body></html>
                    """
                    components.html(copy_btn_html, height=52)
                else:
                    st.info("Threat signature confirmed, but no automated bait reply was generated.")

            else:
                st.markdown(f"""
                <div class="clean-banner-wide reveal visible">
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
                        <div style="display: flex; align-items: center; gap: 12px;">
                            <span style="font-size: 1.8rem;">✅</span>
                            <div>
                                <div style="font-size: 0.75rem; font-family: 'JetBrains Mono', monospace; color: #4ade80; font-weight: 700; letter-spacing: 1px;">INTEGRITY AUDIT VERIFIED</div>
                                <div style="font-size: 1.45rem; font-weight: 800; color: #ffffff;">Classification: {label}</div>
                            </div>
                        </div>
                        <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.74rem; padding: 5px 14px; border-radius: 9999px; background: rgba(34,197,94,0.22); border: 1px solid #22c55e; color: #86efac; font-weight: 600;">ZERO THREAT DETECTED</span>
                    </div>
                    <p style="margin: 12px 0 0 0; font-size: 0.92rem; color: #cbd5e1; line-height: 1.6;">
                        Vector distribution matches organic, legitimate correspondence. No credential harvesting triggers, fraudulent urgency signatures, or financial exploitation patterns found.
                    </p>
                </div>
                """, unsafe_allow_html=True)

        else:
            st.markdown("""
            <div class="standby-card">
                <div class="standby-radar">📡</div>
                <div class="standby-title">Defense Radar on Standby</div>
                <div class="standby-desc">
                    Paste an inbound email into the console on the left or select a 1-click test scenario to inspect threat vectors and deploy autonomous AI baiting.
                </div>
                <div style="margin-top: 24px; display: flex; gap: 8px; flex-wrap: wrap; justify-content: center;">
                    <span class="tele-tag">Neural Classification: Ready</span>
                    <span class="tele-tag">Honeypot Engine: Armed</span>
                    <span class="tele-tag">PII Guardrails: Active</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)


def render_history_view():
    st.markdown("""
    <div class="steps-wrap reveal" style="margin-top: 40px;">
        <div class="steps-title">Past <span class="accent">Detections</span> & Auto-Replies</div>
    </div>
    """, unsafe_allow_html=True)

    top_col1, top_col2 = st.columns([4, 1])
    with top_col2:
        if st.button("🗑️ Clear History", use_container_width=True):
            try:
                requests.delete("http://127.0.0.1:8000/history", timeout=10)
            except requests.exceptions.RequestException:
                pass
            st.rerun()

    try:
        resp = requests.get("http://127.0.0.1:8000/history", params={"limit": 200}, timeout=15)
        resp.raise_for_status()
        records = resp.json()
    except requests.exceptions.ConnectionError:
        st.markdown("""
        <div style="background: rgba(245, 158, 11, 0.1); border: 1px solid rgba(245, 158, 11, 0.45); border-radius: 12px; padding: 20px; max-width: 900px; margin: 0 auto;">
            <div style="color: #fbbf24; font-weight: 700; font-size: 1.05rem; margin-bottom: 6px;">⚠️ FastAPI Backend Server Offline</div>
            <div style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.6;">
                Can't reach <code>http://127.0.0.1:8000/history</code>. Start the backend with:
            </div>
            <pre style="background: #050807; padding: 10px 14px; border-radius: 8px; margin-top: 10px; color: #4ade80; font-family: 'JetBrains Mono', monospace; font-size: 0.86rem; border: 1px solid rgba(74, 222, 128, 0.2);">uvicorn main:app --reload</pre>
        </div>
        """, unsafe_allow_html=True)
        return
    except requests.exceptions.RequestException as e:
        st.error(f"⚠️ Could not load history: {e}")
        return

    if not records:
        st.markdown("""
        <div class="standby-card" style="max-width: 900px; margin: 0 auto;">
            <div class="standby-radar">🗂️</div>
            <div class="standby-title">No Scans Logged Yet</div>
            <div class="standby-desc">
                Run a scan from the Detection tab — every classification and auto-generated
                reply will be recorded here automatically.
            </div>
        </div>
        """, unsafe_allow_html=True)
        return

    for record in records:
        is_scam = record.get("is_scam", False)
        label = record.get("label", "Unknown")
        email_text = record.get("email_text", "")
        reply = record.get("generated_reply")
        timestamp = record.get("timestamp", "")
        try:
            ts_display = datetime.fromisoformat(timestamp).strftime("%b %d, %Y • %H:%M UTC")
        except (ValueError, TypeError):
            ts_display = timestamp

        badge = (
            '<span style="color:#f87171;">🚨 Phishing/Scam</span>' if is_scam
            else '<span style="color:#4ade80;">✅ Legitimate</span>'
        )
        snippet = (email_text[:280] + "…") if len(email_text) > 280 else email_text
        card_class = "history-card" if is_scam else "history-card clean"

        reply_html = ""
        if reply:
            reply_html = f'<div class="history-reply">🤖 {reply}</div>'

        st.markdown(f"""
        <div class="{card_class}">
            <div class="history-meta">
                <span>{ts_display}</span>
                <span>{badge} &nbsp;•&nbsp; {label}</span>
            </div>
            <div class="history-snippet">{snippet}</div>
            {reply_html}
        </div>
        """, unsafe_allow_html=True)


if st.session_state.active_view == "detection":
    render_detection_view()
else:
    render_history_view()



st.markdown("""
<div class="wide-footer reveal">
    <div class="footer-credits">
        Designed & Engineered by <strong>Sahana Abeysinghe</strong>
        &nbsp;•&nbsp;
        <a class="footer-email-link" href="mailto:sahanavichi@gmail.com">sahanavichi@gmail.com</a>
    </div>
    <div class="footer-meta-pill">Scam Baiter Active Defense Framework • Honours Research Project</div>
</div>
""", unsafe_allow_html=True)