/* ==========================================================================
   VigilAI — Application Script
   Modular vanilla JS. Sections:
   1. State & config          5. Widgets: check-in form
   2. Utilities                6. Widgets: simulator
   3. API layer (fetch)        7. Charts
   4. Navigation & shell UI    8. Init
   ========================================================================== */

(() => {
  'use strict';

  /* ------------------------------------------------------------------ *
   * 1. STATE & CONFIG
   * ------------------------------------------------------------------ */
  const API_BASE = '/api';

  const ENDPOINTS = {
    dashboard: `${API_BASE}/dashboard`,
    checkin: `${API_BASE}/checkin`,
    recommendations: `${API_BASE}/recommendations`,
    reports: `${API_BASE}/reports`,
    agents: `${API_BASE}/agents`,
    risk: `${API_BASE}/risk`,
    simulator: `${API_BASE}/simulator`,
    documents: `${API_BASE}/documents`,
    upload: `${API_BASE}/upload`,
    history: `${API_BASE}/history`,
    profile: `${API_BASE}/profile`,
  };  const state = {
    theme: localStorage.getItem('vigilai-theme') || 'light',
    sidebarCollapsed: false,
    checkinDraft: {},
    latestAgents: null,
  };

  /* ------------------------------------------------------------------ *
   * 2. UTILITIES
   * ------------------------------------------------------------------ */
  const $ = (sel, ctx = document) => ctx.querySelector(sel);
  const $$ = (sel, ctx = document) => Array.from(ctx.querySelectorAll(sel));

  function formatCurrency(n) {
    if (n >= 100000) return `₹${(n / 100000).toFixed(1)}L`;
    if (n >= 1000) return `₹${(n / 1000).toFixed(1)}K`;
    return `₹${n}`;
  }

  function showToast(message, duration = 2600) {
    const toast = $('#toast');
    toast.textContent = message;
    toast.hidden = false;
    requestAnimationFrame(() => toast.classList.add('is-visible'));
    clearTimeout(showToast._t);
    showToast._t = setTimeout(() => { toast.hidden = true; }, duration);
  }

  function openModal(title, bodyHtml) {
    $('#modalTitle').textContent = title;
    $('#modalBody').innerHTML = bodyHtml;
    $('#modalBackdrop').hidden = false;
    $('#modalCloseBtn').focus();
  }
  function closeModal() { $('#modalBackdrop').hidden = true; }

  /* ------------------------------------------------------------------ *
   * 3. API LAYER
   * Every call gracefully falls back to bundled sample data if the
   * FastAPI backend is unreachable, so the UI stays fully demoable.
   * ------------------------------------------------------------------ */
  async function apiGet(url, fallback) {
    try {
      const res = await fetch(url, { headers: { Accept: 'application/json' } });
      if (!res.ok) throw new Error(`Request failed: ${res.status}`);
      return await res.json();
    } catch (err) {
      console.warn(`[VigilAI] Falling back to sample data for ${url}`, err.message);
      return fallback;
    }
  }

  async function apiPost(url, payload) {
    try {
      const res = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });
      if (!res.ok) throw new Error(`Request failed: ${res.status}`);
      return await res.json();
    } catch (err) {
      console.warn(`[VigilAI] POST to ${url} failed, treated as offline demo`, err.message);
      return { ok: true, offline: true };
    }
  }

  /* ------------------------------------------------------------------ *
   * SAMPLE / DEMO DATA (stand-in for FastAPI JSON responses)
   * ------------------------------------------------------------------ */
  const SAMPLE = {
    notifications: [
      { id: 1, type: 'risk', icon: '⚠', title: 'Cash flow risk rising', body: 'Distress risk moved from 27% to 31% this week.', time: '12m ago', tone: 'red' },
      { id: 2, type: 'scheme', icon: '🏛', title: 'New scheme available', body: 'MSME Credit Guarantee Scheme match found.', time: '1h ago', tone: 'green' },
      { id: 3, type: 'supplier', icon: '🚚', title: 'Supplier delay flagged', body: 'Vendor "Anand Fabrics" reported a 3-day delay.', time: '3h ago', tone: 'amber' },
      { id: 4, type: 'inventory', icon: '📦', title: 'Inventory warning', body: '2 SKUs projected to stock out within 9 days.', time: 'Yesterday', tone: 'amber' },
    ],
    recommendations: [
      { id: 1, priority: 'High', problem: 'Receivables aging past 45 days', cause: 'Two key clients delayed payment cycles', action: 'Introduce a 2% early-payment discount and automate reminders', improvement: '+₹1.8L liquidity', time: '2 weeks' },
      { id: 2, priority: 'High', problem: 'Inventory concentration risk', cause: '68% of stock value sits in 3 SKUs', action: 'Diversify purchasing across 2 additional suppliers', improvement: '−22% stockout risk', time: '1 month' },
      { id: 3, priority: 'Medium', problem: 'Rising customer acquisition cost', cause: 'Ad spend up 30% with flat conversion', action: 'Reallocate budget toward referral incentives', improvement: '−15% CAC', time: '3 weeks' },
      { id: 4, priority: 'Medium', problem: 'Thin cash buffer', cause: 'Average 9 days of operating expenses on hand', action: 'Set aside 5% of weekly revenue into a reserve account', improvement: '+18 days runway', time: '6 weeks' },
      { id: 5, priority: 'Low', problem: 'Manual attendance tracking', cause: 'Paper registers slow payroll processing', action: 'Adopt a low-cost biometric or app-based tracker', improvement: '4 hrs/week saved', time: '1 week' },
      { id: 6, priority: 'Low', problem: 'Underused loyalty program', cause: 'Only 12% of repeat customers enrolled', action: 'Prompt enrollment at checkout with a small incentive', improvement: '+8% repeat rate', time: '2 weeks' },
    ],
    agents: [
      { name: 'CEO Agent', color: '#2952E3', icon: '◆', status: 'Active', confidence: 88, recommendation: 'Prioritize receivables recovery before new hiring', reasoning: 'Cash runway is the binding constraint this quarter; growth moves should wait 6–8 weeks.', risk: 'Moderate' },
      { name: 'CFO Agent', color: '#1FAE6E', icon: '₹', status: 'Active', confidence: 91, recommendation: 'Delay machinery purchase by one quarter', reasoning: 'Current debt-service ratio leaves limited buffer for new fixed costs.', risk: 'Moderate' },
      { name: 'Marketing Agent', color: '#E68A1C', icon: '◎', status: 'Active', confidence: 74, recommendation: 'Shift 20% of ad spend to referral program', reasoning: 'Referral-driven customers show 1.6x higher lifetime value in your segment.', risk: 'Low' },
      { name: 'Operations Agent', color: '#3DDCEE', icon: '⚙', status: 'Active', confidence: 82, recommendation: 'Diversify supplier base for top 3 SKUs', reasoning: 'Single-supplier dependency has caused 2 delays in the last 30 days.', risk: 'Moderate' },
      { name: 'Risk Agent', color: '#E14B4B', icon: '⚠', status: 'Active', confidence: 95, recommendation: 'Escalate distress risk monitoring to daily', reasoning: 'Risk score crossed the 30% moderate threshold this week.', risk: 'High' },
      { name: 'Compliance Agent', color: '#7C5CE0', icon: '↻', status: 'Active', confidence: 97, recommendation: 'File GST return before the 3-day deadline', reasoning: 'Filing history shows two near-miss late filings this year.', risk: 'Low' },
      { name: 'Strategy Agent', color: '#0EA5A0', icon: '♟', status: 'Active', confidence: 68, recommendation: 'Evaluate entry into the wholesale export segment', reasoning: 'Market opportunity score for exports rose 14 points this month.', risk: 'Low' },
      { name: 'Government Policy Agent', color: '#B45309', icon: '🏛', status: 'Active', confidence: 85, recommendation: 'Apply for the MSME Credit Guarantee Scheme', reasoning: 'Business profile matches 4 of 5 eligibility criteria.', risk: 'Low' },
    ],
    recovery: [
      { title: 'Stabilize receivables', body: 'Recover ₹1.8L in outstanding payments from top 4 clients within 3 weeks.' },
      { title: 'Trim discretionary spend', body: 'Pause non-essential purchases for 30 days to preserve cash buffer.' },
      { title: 'Renegotiate supplier terms', body: 'Extend payment terms from 15 to 30 days with two key suppliers.' },
      { title: 'Build a 30-day reserve', body: 'Allocate 5% of weekly revenue automatically into a reserve account.' },
      { title: 'Re-forecast monthly', body: 'Review recovery progress against target every 30 days with the CFO Agent.' },
    ],
    growth: [
      { id: 1, priority: 'High', problem: 'Untapped export demand', cause: 'Regional buyers sourcing similar goods from overseas', action: 'Pilot a small export shipment via an MSME trade facilitator', improvement: 'Est. +12% revenue', time: '2 months' },
      { id: 2, priority: 'Medium', problem: 'Underused e-commerce channel', cause: 'Only 6% of sales come from online storefronts', action: 'List top 10 SKUs on a regional marketplace', improvement: 'Est. +9% revenue', time: '3 weeks' },
      { id: 3, priority: 'Medium', problem: 'Idle weekday production capacity', cause: 'Machinery utilization at 58% on Tue–Thu', action: 'Offer contract manufacturing slots to nearby businesses', improvement: 'Est. +₹40K/mo', time: '1 month' },
    ],
    schemes: [
      { id: 1, priority: 'High', problem: 'Working capital shortage', cause: 'Eligible under MSME Credit Guarantee Scheme', action: 'Apply for collateral-free credit up to ₹2 Cr', improvement: 'Lower borrowing cost', time: '2–4 weeks' },
      { id: 2, priority: 'Medium', problem: 'Technology upgrade needed', cause: 'Eligible under CLCSS subsidy', action: 'Claim 15% capital subsidy on new machinery', improvement: '15% cost offset', time: '1–2 months' },
      { id: 3, priority: 'Low', problem: 'Export readiness', cause: 'Eligible under MSME export promotion scheme', action: 'Register for subsidized trade fair participation', improvement: 'Market access', time: '3 weeks' },
    ],
    kbRecent: [
      { title: 'Understanding your Business Pulse Score', meta: 'Guide · 4 min read' },
      { title: 'Q2 compliance checklist for MSMEs', meta: 'Checklist · Updated last week' },
    ],
    kbPolicy: [
      { title: 'MSME Credit Guarantee Scheme — overview', meta: 'Government policy' },
      { title: 'GST filing deadlines for FY 2026–27', meta: 'Government policy' },
    ],
    kbGuides: [
      { title: 'How to build a 90-day cash reserve', meta: 'Finance guide' },
      { title: 'Reducing supplier concentration risk', meta: 'Business guide' },
    ],
        faq: [
      { q: 'How often does VigilAI refresh my health score?', a: 'Your Business Health Score recalculates hourly using your latest check-ins, transactions and connected data sources.' },
      { q: 'Can I export data for my accountant?', a: 'Yes — visit Reports and download any report as PDF or Excel.' },
      { q: 'What happens if I miss a daily check-in?', a: 'Nothing breaks — VigilAI simply relies more heavily on connected transaction data until your next check-in.' },
    ],
    reports: [
      { title: 'Monthly Report', desc: 'Full operational and financial summary for the current month.', icon: '▤' },
      { title: 'Quarterly Report', desc: 'Trend analysis and distress indicators across the quarter.', icon: '▦' },
      { title: 'Risk Report', desc: 'Deep dive into financial distress drivers and mitigations.', icon: '⚠' },
      { title: 'Growth Report', desc: 'Opportunities, market signals and expansion readiness.', icon: '↗' },
    ],
  };

  /* ------------------------------------------------------------------ *
   * 4. NAVIGATION & SHELL UI
   * ------------------------------------------------------------------ */
  function navigateTo(pageId) {
    $$('.page').forEach(p => p.classList.toggle('is-active', p.dataset.page === pageId));
    $$('.nav-item[data-page]').forEach(n => n.classList.toggle('is-active', n.dataset.page === pageId));
    $('.app-shell').classList.remove('is-mobile-open');
    $('#sidebarOverlay').hidden = true;
    // NOTE: do NOT call window.scrollTo(0,0) here — it was causing the page
    // to jump to top whenever any [data-page] element was clicked or a page
    // was navigated to, which disrupted input focus mid-typing.
    // Instead, scroll the main-content container (not the window) to top.
    const mainContent = $('.main-content');
    if (mainContent) mainContent.scrollTop = 0;
    if (typeof Chart !== 'undefined') {
      setTimeout(() => {
        renderAllCharts();
        window.dispatchEvent(new Event('resize'));
      }, 120);
    }
  }

  function initNavigation() {
    $$('[data-page]').forEach(el => {
      el.addEventListener('click', (e) => {
        e.preventDefault();
        navigateTo(el.dataset.page);
      });
    });
  }

  function initSidebarCollapse() {
    $('#sidebarCollapseBtn').addEventListener('click', () => {
      state.sidebarCollapsed = !state.sidebarCollapsed;
      $('#app-shell').classList.toggle('is-collapsed', state.sidebarCollapsed);
    });
    $('#mobileMenuBtn').addEventListener('click', () => {
      $('#app-shell').classList.add('is-mobile-open');
      $('#sidebarOverlay').hidden = false;
    });
    $('#sidebarOverlay').addEventListener('click', () => {
      $('#app-shell').classList.remove('is-mobile-open');
      $('#sidebarOverlay').hidden = true;
    });
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    $('#darkModeToggle').setAttribute('aria-pressed', String(theme === 'dark'));
    const settingsToggle = $('#settingsDarkToggle');
    if (settingsToggle) settingsToggle.checked = theme === 'dark';
    localStorage.setItem('vigilai-theme', theme);
    // Re-render charts so Chart.js grid/text colors match the new theme if Chart is available.
    if (typeof Chart !== 'undefined') {
      renderAllCharts();
    }
  }

  function initDarkMode() {
    applyTheme(state.theme);
    $('#darkModeToggle').addEventListener('click', () => {
      state.theme = state.theme === 'dark' ? 'light' : 'dark';
      applyTheme(state.theme);
    });
    $('#settingsDarkToggle')?.addEventListener('change', (e) => {
      state.theme = e.target.checked ? 'dark' : 'light';
      applyTheme(state.theme);
    });
  }

  function initDropdowns() {
    const pairs = [
      ['#notifBtn', '#notifPanel'],
      ['#profileBtn', '#profilePanel'],
    ];
    pairs.forEach(([btnSel, panelSel]) => {
      const btn = $(btnSel), panel = $(panelSel);
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const isOpen = !panel.hidden;
        $$('.dropdown-panel').forEach(p => p.hidden = true);
        panel.hidden = isOpen;
        btn.setAttribute('aria-expanded', String(!isOpen));
      });
    });
    document.addEventListener('click', () => $$('.dropdown-panel').forEach(p => p.hidden = true));
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') { $$('.dropdown-panel').forEach(p => p.hidden = true); closeModal(); } });
  }

  function initModal() {
    $('#modalCloseBtn').addEventListener('click', closeModal);
    $('#modalBackdrop').addEventListener('click', (e) => { if (e.target === $('#modalBackdrop')) closeModal(); });
  }

  function initLogout() {
    ['#logoutBtn', '#logoutBtn2'].forEach(sel => {
      $(sel)?.addEventListener('click', (e) => {
        e.preventDefault();
        showToast('Logged out — redirecting to sign in…');
      });
    });
  }

  function initGlobalSearch() {
    const input = $('#globalSearch');
    document.addEventListener('keydown', (e) => {
      if (e.key === '/' && document.activeElement !== input) { e.preventDefault(); input.focus(); }
    });
    input.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' && input.value.trim()) {
        showToast(`Searching for "${input.value.trim()}"…`);
      }
    });
  }

  /* ------------------------------------------------------------------ *
   * RENDER: notifications
   * ------------------------------------------------------------------ */
  function renderNotifications(list) {
    const html = list.map(n => `
      <li class="notif-item" role="menuitem" tabindex="0">
        <span class="notif-item__icon" style="background:var(--bg-surface-2)">${n.icon}</span>
        <span class="notif-item__body">
          <h4>${n.title}</h4>
          <p>${n.body}</p>
          <time>${n.time}</time>
        </span>
      </li>`).join('');
    $('#notifList').innerHTML = html;
    $('#dashNotifList').innerHTML = list.slice(0, 3).map(n => `
      <li><span class="dot dot--${n.tone}"></span><div><strong>${n.title}</strong><br><span class="meta">${n.time}</span></div></li>
    `).join('');
    $('#notifCount').textContent = list.length;
  }

  /* ------------------------------------------------------------------ *
   * RENDER: dashboard extras
   * ------------------------------------------------------------------ */
  function renderDashboardRecoSummary(recs) {
    $('#dashRecoList').innerHTML = recs.slice(0, 4).map(r => `
      <li><span class="dot dot--${r.priority === 'High' ? 'red' : r.priority === 'Medium' ? 'amber' : 'green'}"></span>
      <div><strong>${r.problem}</strong><br><span class="meta">${r.action}</span></div></li>
    `).join('');
  }

  function renderAiInsights() {
    const insights = [
      'Receivables recovery this week could add up to 18 days of runway.',
      'Inventory for SKU "Cotton Weave 210" projected to stock out in 9 days.',
      'A referral-focused campaign may lower acquisition cost by 15%.',
      'Compliance Agent flags a GST filing due in 3 days.',
    ];
    $('#aiInsightsList').innerHTML = insights.map(i => `<li><span class="dot dot--amber"></span><div>${i}</div></li>`).join('');
  }

  function renderHealthDetail() {
    const metrics = [
      ['Revenue Momentum', 74, 'green'], ['Cash Conversion Cycle', 58, 'amber'],
      ['Debt Service Coverage', 81, 'green'], ['Customer Concentration', 46, 'amber'],
      ['Working Capital Ratio', 69, 'green'], ['Expense Volatility', 33, 'red'],
    ];
    $('#healthDetailGrid').innerHTML = metrics.map(([name, score, tone]) => `
      <article class="card card--metric">
        <header class="card__header"><h3>${name}</h3><span class="badge badge--${tone}">${tone === 'green' ? 'Healthy' : tone === 'amber' ? 'Watch' : 'Action needed'}</span></header>
        <p class="metric-value">${score}<span>/100</span></p>
        <div class="mini-bar"><span style="width:${score}%"></span></div>
      </article>`).join('');
  }

  /* ------------------------------------------------------------------ *
   * RENDER: recommendations / growth / schemes (shared)
   * ------------------------------------------------------------------ */
  function recoCardHtml(r) {
  const tone = r.priority === 'High' ? 'red' : r.priority === 'Medium' ? 'amber' : 'green';
  return `
  <article class="reco-card" style="cursor:pointer;" data-priority="${r.priority}" onclick="openModal('${r.problem.replace(/'/g, "\\'")}', '<p><strong>Root Cause:</strong> ${r.cause.replace(/'/g, "\\'")}</p><p><strong>Action:</strong> ${r.action.replace(/'/g, "\\'")}</p><p><strong>Impact:</strong> ${r.improvement} in ${r.time}</p><br><p style=\\\'color:var(--text-secondary);\\\'>This recommendation was generated by the AI engine based on current market trends and your internal data to mitigate financial distress.</p>')">
        <div class="reco-card__top"><h4>${r.problem}</h4><span class="badge badge--${tone}">${r.priority}</span></div>
        <dl>
          <dt>Root cause</dt><dd>${r.cause}</dd>
          <dt>Action</dt><dd>${r.action}</dd>
        </dl>
        <div class="reco-card__footer"><span>${r.improvement}</span><span>${r.time}</span></div>
      </article>`;
  }

  function renderRecommendations(list, filter = 'all') {
    const filtered = filter === 'all' ? list : list.filter(r => r.priority === filter);
    $('#recoGrid').innerHTML = filtered.map(recoCardHtml).join('') || '<p class="metric-caption">No recommendations at this priority.</p>';
  }

  function initRecoFilters(list) {
    $$('.filter-tab').forEach(tab => {
      tab.addEventListener('click', () => {
        $$('.filter-tab').forEach(t => { t.classList.remove('is-active'); t.setAttribute('aria-selected', 'false'); });
        tab.classList.add('is-active'); tab.setAttribute('aria-selected', 'true');
        renderRecommendations(list, tab.dataset.priority);
      });
    });
  }

  /* ------------------------------------------------------------------ *
   * RENDER: AI Decision Board
   * ------------------------------------------------------------------ */
  function renderAgents(agents) {
  $('#agentGrid').innerHTML = agents.map(a => `
  <article class="agent-card" style="--agent-color:${a.color}; cursor:pointer;" onclick="openModal('${a.name} Analysis', '<p><strong>Status:</strong> ${a.status}</p><p><strong>Confidence:</strong> ${a.confidence}%</p><p><strong>Recommendation:</strong> ${(a.recommendation || '-').replace(/'/g, "\\'")}</p><p><strong>Reasoning:</strong> ${(a.reasoning || '-').replace(/'/g, "\\'")}</p><br><p style=\\\'color:var(--text-secondary);\\\'>This agent continuously monitors specific operational and financial signals to detect early warning signs of distress.</p>')">
        <div class="agent-card__head">
          <span class="agent-card__avatar" style="color: ${a.color}">${a.icon}</span>
          <div><div class="agent-card__name">${a.name}</div><div class="agent-card__status">● ${a.status}</div></div>
        </div>
        <div class="confidence-row"><span>Confidence</span><span class="confidence-track"><span class="confidence-fill" style="width:${a.confidence}%"></span></span><span>${a.confidence}%</span></div>
        <p class="agent-card__reco">${a.recommendation || '-'}</p>
        <p class="agent-card__reason">${a.reasoning || '-'}</p>
        <span class="badge badge--outline">Risk: ${a.risk || 'Low'}</span>
      </article>`).join('');
  }

  async function executeFullAnalysis() {
    const runBtn = $('#agentRunBtn');
    const dashBtn = $('#dashRunAnalysisBtn');
    const statusText = $('#agentStatusText');

    if (runBtn) { runBtn.disabled = true; runBtn.textContent = '⏳ Running Analysis...'; }
    if (dashBtn) { dashBtn.disabled = true; dashBtn.textContent = '⏳ Running...'; }
    if (statusText) statusText.textContent = 'Starting multi-agent analysis...';

    // Reset the board to 'Waiting'
    let currentAgents = JSON.parse(JSON.stringify(SAMPLE.agents));
    currentAgents.forEach(a => {
      a.status = 'Waiting';
      a.recommendation = '-';
      a.reasoning = 'Waiting for task...';
      a.confidence = 0;
    });
    renderAgents(currentAgents);

    try {
      const response = await fetch('/api/agents/run', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_query: 'Analyze the business', business_id: 'default' })
      });
      
      if (!response.ok) throw new Error(`HTTP error ${response.status}`);
      
      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let buffer = '';

      while (true) {
        const { value, done } = await reader.read();
        if (done) break;
        
        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split('\n');
        buffer = lines.pop() || '';

        for (let line of lines) {
          const trimmed = line.trim();
          if (trimmed.startsWith('data:')) {
            const rawJson = trimmed.replace(/^data:\s*/, '');
            if (!rawJson) continue;

            let data;
            try {
              data = JSON.parse(rawJson);
            } catch (parseErr) {
              console.warn('Failed to parse SSE JSON:', parseErr, rawJson);
              continue;
            }
            
            if (data.status === 'completed' && !data.node) {
              if (statusText) statusText.textContent = '✓ Multi-agent analysis complete! All recommendations & graphs updated.';
              break;
            }
            
            if (data.node) {
              const nodeName = data.node.toLowerCase();
              if (statusText) statusText.textContent = `Agent ${data.agent || data.node} executed...`;
              
              const nodeAliases = {
                finance: ['finance', 'cfo'],
                risk: ['risk'],
                competitor: ['competitor', 'marketing'],
                schemes: ['scheme', 'government policy', 'policy'],
                recovery: ['recovery', 'compliance'],
                growth: ['growth', 'strategy'],
                ceo: ['ceo'],
                operations: ['operations']
              };

              const targetKeys = nodeAliases[nodeName] || [nodeName];
              const agentIndex = currentAgents.findIndex(a => {
                const aName = a.name.toLowerCase();
                return targetKeys.some(k => aName.includes(k));
              });

              if (agentIndex !== -1) {
                const out = data.specialist_output || {};
                
                currentAgents[agentIndex].status = 'Completed';
                currentAgents[agentIndex].confidence = out.confidence || Math.floor(Math.random() * 15) + 82;
                
                if (out.recommendations && out.recommendations.length > 0) {
                   currentAgents[agentIndex].recommendation = out.recommendations[0].action || '-';
                   currentAgents[agentIndex].reasoning = out.recommendations[0].problem || out.recommendations[0].cause || '-';
                } else if (out.opportunities && out.opportunities.length > 0) {
                   currentAgents[agentIndex].recommendation = out.opportunities[0].action || '-';
                   currentAgents[agentIndex].reasoning = out.opportunities[0].problem || '-';
                } else if (out.top_factors && out.top_factors.length > 0) {
                   currentAgents[agentIndex].recommendation = `Risk Band: ${out.risk_band || 'Moderate'}`;
                   currentAgents[agentIndex].reasoning = `Key Factor: ${out.top_factors[0][0]}`;
                } else if (data.node === 'ceo' && data.final_recommendation) {
                   currentAgents[agentIndex].recommendation = data.final_recommendation.primary_action || data.final_recommendation.headline;
                   currentAgents[agentIndex].reasoning = data.final_recommendation.narrative || data.final_recommendation.rationale;
                } else if (out.day_30 && out.day_30.length > 0) {
                   currentAgents[agentIndex].recommendation = out.day_30[0].title;
                   currentAgents[agentIndex].reasoning = out.day_30[0].body;
                } else {
                   currentAgents[agentIndex].recommendation = out.summary || 'Analysis complete.';
                   currentAgents[agentIndex].reasoning = 'Processed successfully.';
                }
                
                currentAgents[agentIndex].risk = out.risk_band || 'Low';
                renderAgents(currentAgents);
              }
            }
          }
        }
      }
    } catch (e) {
      console.warn('Backend run failed, running offline simulation fallback:', e);
      // Fallback: simulate agent progress for demo integrity
      for (let i = 0; i < currentAgents.length; i++) {
        currentAgents[i].status = 'Completed';
        currentAgents[i].confidence = Math.floor(Math.random() * 15) + 82;
        renderAgents(currentAgents);
      }
      if (statusText) statusText.textContent = '✓ Multi-agent analysis complete! (Offline mode)';
    } finally {
      if (runBtn) { runBtn.disabled = false; runBtn.textContent = 'Run Analysis'; }
      if (dashBtn) { dashBtn.disabled = false; dashBtn.textContent = '⚡ Run Analysis'; }
      
      const lastTimeEl = $('#lastAnalysisTime');
      if (lastTimeEl) lastTimeEl.textContent = 'Just now';

      updateExecutiveAnalysisSummary(currentAgents);

      // Refresh all graphs with latest state
      if (typeof Chart !== 'undefined') {
        renderAllCharts(currentAgents);
      }
      showToast('✓ Analysis complete! Executive summary & graphs updated.');
    }
  }

  function updateExecutiveAnalysisSummary(agents = null) {
    const summaryCard = $('#analysisSummaryCard');
    if (!summaryCard) return;
    const activeAgents = agents || state.latestAgents || SAMPLE.agents;
    
    const ceoAgent = activeAgents.find(a => a.name.includes('CEO')) || activeAgents[0];
    const cfoAgent = activeAgents.find(a => a.name.includes('CFO') || a.name.includes('Finance'));
    const riskAgent = activeAgents.find(a => a.name.includes('Risk'));
    const schemeAgent = activeAgents.find(a => a.name.includes('Scheme') || a.name.includes('Policy'));

    const headline = ceoAgent ? (ceoAgent.recommendation || 'Prioritize receivables recovery before new hiring') : 'Prioritize receivables recovery before new hiring';
    const narrative = `Executive Multi-Agent Analysis Complete: Risk is rated ${riskAgent ? riskAgent.risk : 'Moderate'} (${riskAgent ? riskAgent.confidence : 95}% confidence). ${cfoAgent ? cfoAgent.recommendation : 'Delay machinery purchase by 1 quarter to preserve liquidity buffer'}. ${schemeAgent ? schemeAgent.recommendation : 'Apply for MSME Credit Guarantee Scheme'}.`;

    $('#analysisSummaryHeadline').textContent = `🎯 ${headline}`;
    $('#analysisSummaryNarrative').textContent = narrative;
    $('#analysisSummaryTime').textContent = 'Updated Just now';

    const pillsEl = $('#analysisSummaryPills');
    if (pillsEl) {
      pillsEl.innerHTML = `
        <span class="pill pill--amber">Overall Risk: ${riskAgent ? riskAgent.risk : 'Moderate'}</span>
        <span class="pill">CFO: ${cfoAgent ? cfoAgent.recommendation : 'Delay Machinery'}</span>
        <span class="pill">Policy: ${schemeAgent ? schemeAgent.recommendation : 'Apply Scheme'}</span>
        <span class="pill">Consensus: 8/8 Agents Synchronized</span>
      `;
    }
    summaryCard.hidden = false;
  }

  function initAgentBoard() {
    const runBtn = $('#agentRunBtn');
    const dashBtn = $('#dashRunAnalysisBtn');

    if (runBtn) runBtn.addEventListener('click', executeFullAnalysis);
    if (dashBtn) dashBtn.addEventListener('click', () => {
      navigateTo('agents');
      executeFullAnalysis();
    });
  }

  /* ------------------------------------------------------------------ *
   * RENDER: recovery, reports, knowledge base
   * ------------------------------------------------------------------ */
  function renderRecovery(steps) {
  $('#recoverySteps').innerHTML = steps.map(s => `<li style="cursor:pointer;" onclick="openModal('${s.title.replace(/'/g, "\\'")}', '<p>${s.body.replace(/'/g, "\\'")}</p><br><p style=\\\'color:var(--text-secondary);\\\'>Detailed execution strategy for this step involves cross-department coordination and regular CFO check-ins to track progress against benchmarks.</p>')"><div><h4>${s.title}</h4><p>${s.body}</p></div></li>`).join('');
  }

  function renderReports(reports) {
    $('#reportsGrid').innerHTML = reports.map(r => `
      <article class="report-card">
        <span class="report-card__icon">${r.icon}</span>
        <h4>${r.title}</h4>
        <p>${r.desc}</p>
        <div class="report-card__actions">
          <button class="btn btn--ghost" data-export="pdf" data-title="${r.title}">PDF</button>
          <button class="btn btn--ghost" data-export="xlsx" data-title="${r.title}">Excel</button>
        </div>
      </article>`).join('');
    $$('#reportsGrid [data-export]').forEach(btn => {
      btn.addEventListener('click', () => showToast(`Preparing "${btn.dataset.title}" as ${btn.dataset.export.toUpperCase()}…`));
    });
  }

  // --- Render Benchmark Intelligence ---
function renderBenchmarkAI() {
  const container = $('#benchmarkAiContent');
  if (!container) return;

  const benchmarkDetails = [
    {
      title: "1. Bridging the 18% Revenue Gap",
      body: "Top MSMEs achieve this by optimizing their price-to-volume ratio. <strong>Action:</strong> Run the what-if simulator to see the impact of a +5% price adjustment combined with introducing a new product line. Your current margins allow for this slight increase without triggering significant customer churn."
    },
    {
      title: "2. Improving Inventory Turnover by 22%",
      body: "Your capital is tied up in slow-moving stock. <strong>Action:</strong> Adopt a just-in-time (JIT) procurement model for your top 3 SKU categories. Similar businesses reduced warehouse holding times from 45 days to 28 days by ordering smaller, weekly batches instead of monthly."
    },
    {
      title: "3. Reducing Procurement Costs by 11% in Hyderabad",
      body: "Local competitors are utilizing bulk-purchasing consortiums and renegotiating vendor contracts annually. <strong>Action:</strong> Leverage your consistent payment history to renegotiate terms with your primary supplier, asking for a 5% volume discount or extending payment terms to 45 days."
    },
    {
      title: "4. Optimizing Team Size (3 Fewer Employees)",
      body: "Similar sized operations rely heavily on automation for back-office tasks. <strong>Action:</strong> Consolidate your bookkeeping and attendance tracking into an automated software suite. This eliminates the need for manual data entry, saving approximately 40 hours of administrative work per week."
    }
  ];

  container.innerHTML = benchmarkDetails.map(item => `
    <div style="margin-bottom: 20px;">
      <h4 style="color: var(--text-primary); margin-bottom: 6px;">${item.title}</h4>
      <p style="color: var(--text-secondary);">${item.body}</p>
    </div>
  `).join('');
}

  function renderKnowledgeBase() {
    const docItem = (d) => `<li class="kb-doc-item" tabindex="0" data-title="${d.title}"><span class="kb-doc-item__icon">📄</span><div><h5>${d.title}</h5><span>${d.meta}</span></div></li>`;
    $('#kbRecentList').innerHTML = SAMPLE.kbRecent.map(docItem).join('');
    $('#kbPolicyList').innerHTML = SAMPLE.kbPolicy.map(docItem).join('');
    $('#kbGuideList').innerHTML = SAMPLE.kbGuides.map(docItem).join('');
    $('#faqList').innerHTML = SAMPLE.faq.map(f => `<details class="faq-item" name="faq"><summary>${f.q}</summary><p style="line-height: 1.6; margin-top: 4px;">${f.a}</p></details>`).join('');

    $$('.kb-doc-item').forEach(item => {
      const open = () => {
        $('#kbPreview').innerHTML = `<h3>${item.dataset.title}</h3><p style="margin-top:10px;color:var(--text-secondary);font-size:.85rem;line-height:1.6;">Preview content for “${item.dataset.title}” would load here from <code>/api/documents</code>.</p>`;
      };
      item.addEventListener('click', open);
      item.addEventListener('keydown', (e) => { if (e.key === 'Enter') open(); });
    });

    $('#kbSearch').addEventListener('input', (e) => {
      const q = e.target.value.toLowerCase();
      $$('.kb-doc-item').forEach(item => {
        item.style.display = item.dataset.title.toLowerCase().includes(q) ? '' : 'none';
      });
    });
  }

  /* ------------------------------------------------------------------ *
   * 5. DAILY CHECK-IN FORM
   * ------------------------------------------------------------------ */
  function initCheckinForm() {
    const form = $('#checkinForm');
    if (!form) return;

    const fields = $$('input, select, textarea', form);
    const requiredFields = fields.filter(f => f.hasAttribute('required'));
    const saveBtn = $('#checkinSaveBtn');
    const submitBtn = $('#checkinSubmitBtn');
    const statusEl = $('#checkinStatus');

    function updateProgress() {
      const filled = requiredFields.filter(f => f.value && f.value.trim() !== '').length;
      if ($('#checkinProgressText')) $('#checkinProgressText').textContent = filled;
      if ($('#checkinTotal')) $('#checkinTotal').textContent = requiredFields.length;
      if ($('#checkinProgressFill')) $('#checkinProgressFill').style.width = `${(filled / requiredFields.length) * 100}%`;
    }

    fields.forEach(f => {
      f.addEventListener('input', updateProgress);
      f.addEventListener('change', updateProgress);
    });
    updateProgress();

    function preparePayload(status = 'submitted') {
      const raw = Object.fromEntries(new FormData(form).entries());
      return {
        sales: parseFloat(raw.sales) || 0,
        complaints: parseInt(raw.complaints, 10) || 0,
        delays: raw.delays || 'None',
        inventory: raw.inventory || 'None',
        attendance: parseFloat(raw.attendance) || 100,
        expenses: parseFloat(raw.expenses) || 0,
        competitors: raw.competitors || 'No',
        marketchange: raw.marketchange || '',
        feedback: raw.feedback || '',
        notes: raw.notes || '',
        status: status,
      };
    }

    if (saveBtn) {
      saveBtn.addEventListener('click', async (e) => {
        e.preventDefault();
        saveBtn.disabled = true;
        statusEl.textContent = 'Saving draft...';
        statusEl.style.color = 'var(--text-secondary)';

        try {
          const payload = preparePayload('draft');
          await apiPost(ENDPOINTS.checkin, payload);
          statusEl.textContent = '✓ Draft saved.';
          statusEl.style.color = 'var(--green-500)';
          showToast('Draft saved successfully');
        } catch (err) {
          statusEl.textContent = 'Draft save complete.';
          showToast('Draft saved');
        } finally {
          saveBtn.disabled = false;
        }
      });
    }

    async function handleSubmit(e) {
      if (e) e.preventDefault();

      const missing = requiredFields.filter(f => !f.value || f.value.trim() === '');
      if (missing.length > 0) {
        statusEl.textContent = `⚠️ Please fill in all required fields (${missing.length} remaining).`;
        statusEl.style.color = 'var(--red-500)';
        missing[0].focus();
        showToast(`Please complete required fields (${missing.length} missing)`);
        return;
      }

      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = '⏳ Submitting...';
      }
      statusEl.textContent = 'Submitting check-in...';
      statusEl.style.color = 'var(--text-secondary)';

      try {
        const payload = preparePayload('submitted');
        const res = await apiPost(ENDPOINTS.checkin, payload);

        statusEl.textContent = '✓ Daily Check-in submitted successfully!';
        statusEl.style.color = 'var(--green-500)';
        showToast('✓ Check-in submitted! Business health signals updated.');

        form.reset();
        updateProgress();
      } catch (err) {
        console.error('Checkin submit error:', err);
        statusEl.textContent = '✓ Check-in recorded!';
        statusEl.style.color = 'var(--green-500)';
        showToast('Check-in submitted');
        form.reset();
        updateProgress();
      } finally {
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.textContent = 'Submit check-in';
        }
      }
    }

    form.addEventListener('submit', handleSubmit);
    if (submitBtn) {
      submitBtn.addEventListener('click', (e) => {
        if (form.checkValidity && !form.checkValidity()) {
          // Trigger form submit validation flow
          return;
        }
        handleSubmit(e);
      });
    }
  }

  /* ------------------------------------------------------------------ *
   * 6. WHAT-IF SIMULATOR
   * ------------------------------------------------------------------ */
  let simulatorChart;

  function initSimulator() {
    const revInput = $('#sim-rev'), expInput = $('#sim-exp'), cashInput = $('#sim-cash');
    const hire    = $('#sim-hire');
    const machinery = $('#sim-machinery'), loan = $('#sim-loan');
    const price   = $('#sim-price');
    const newProd = $('#sim-newproduct'), newBranch = $('#sim-newbranch');
        const runBtn  = $('#simRunBtn');

    if (!runBtn) return;

    // ---- CRITICAL: Prevent any form submit from reloading/scrolling the page ----
    const simForm = $('#simForm');
    if (simForm) {
      simForm.addEventListener('submit', e => { e.preventDefault(); e.stopPropagation(); });
      // Also prevent href="#" bubbling from scrolling to top
      simForm.addEventListener('click', e => {
        if (e.target.tagName === 'A') e.preventDefault();
      });
    }

    // --- Helper: format INR value to lakh string ---
    const toLakh = v => {
      const n = Number(v);
      if (n >= 100000) return `₹${(n / 100000).toFixed(2)}L`;
      if (n >= 1000)   return `₹${(n / 1000).toFixed(1)}K`;
      return `₹${n}`;
    };

    // --- Live hint updates for currency inputs ---
    const updateHints = () => {
      const revHint = $('#sim-rev-hint');
      const expHint = $('#sim-exp-hint');
      const cashHint = $('#sim-cash-hint');
      if (revHint  && revInput)  revHint.textContent  = `${toLakh(revInput.value)} / month`;
      if (expHint  && expInput)  expHint.textContent  = `${toLakh(expInput.value)} / month`;
      if (cashHint && cashInput) cashHint.textContent = `${toLakh(cashInput.value)} available`;
    };

    // Prevent Enter key in number inputs from triggering form submit / scroll-to-top
    [revInput, expInput, cashInput].filter(Boolean).forEach(inp => {
      inp.addEventListener('keydown', e => {
        if (e.key === 'Enter') {
          e.preventDefault();
          e.stopPropagation();
          inp.blur(); // dismiss keyboard on mobile
        }
      });
    });

    // --- Stepper buttons (▲▼) for currency inputs ---
    document.querySelectorAll('.stepper-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const target = $(`#${btn.dataset.target}`);
        if (!target) return;
        const step = Number(btn.dataset.step || 1);
        const dir  = Number(btn.dataset.dir  || 1);
        const min  = Number(target.min || 0);
        const newVal = Math.max(min, Number(target.value || 0) + dir * step);
        target.value = newVal;
        target.dispatchEvent(new Event('input', { bubbles: true }));
      });
    });

    if (revInput)  revInput.addEventListener('input', updateHints);
    if (expInput)  expInput.addEventListener('input', updateHints);
    if (cashInput) cashInput.addEventListener('input', updateHints);
    updateHints();

    // --- Pill selectors (Hire Employees, Price Adjustment) ---
    document.querySelectorAll('.pill-selector').forEach(group => {
      const targetId = group.dataset.target;
      const hiddenInput = $(`#${targetId}`);
      const outputEl = $(`#${targetId}-out`);
      group.querySelectorAll('.pill-opt').forEach(btn => {
        btn.addEventListener('click', () => {
          group.querySelectorAll('.pill-opt').forEach(b => b.classList.remove('is-active'));
          btn.classList.add('is-active');
          const val = btn.dataset.val;
          if (hiddenInput) hiddenInput.value = val;
          if (outputEl) {
            if (targetId === 'sim-hire') {
              outputEl.textContent = `${val} ${Number(val) === 1 ? 'person' : 'people'}`;
            } else if (targetId === 'sim-price') {
              outputEl.textContent = `${Number(val) > 0 ? '+' : ''}${val}%`;
            }
          }
        });
      });
    });

    // --- Toggle pill groups (Check-in: delays, inventory, competitors) ---
    document.querySelectorAll('.toggle-pill-group').forEach(group => {
      const targetId = group.dataset.target;
      const hiddenInput = $(`#${targetId}`);
      group.querySelectorAll('.tpill').forEach(btn => {
        btn.addEventListener('click', () => {
          group.querySelectorAll('.tpill').forEach(b => b.classList.remove('is-active'));
          btn.classList.add('is-active');
          if (hiddenInput) hiddenInput.value = btn.dataset.val;
        });
      });
    });

    // --- Count pill selectors (complaints: 0,1,2,3,5+) ---
    document.querySelectorAll('.count-pill-selector').forEach(group => {
      const targetId = group.dataset.target;
      const hiddenInput = $(`#${targetId}`);
      group.querySelectorAll('.count-pill').forEach(btn => {
        btn.addEventListener('click', () => {
          group.querySelectorAll('.count-pill').forEach(b => b.classList.remove('is-active'));
          btn.classList.add('is-active');
          if (hiddenInput) hiddenInput.value = btn.dataset.val;
        });
      });
    });

    // --- Styled range sliders (machinery, loan, attendance) ---
    const syncSliders = () => {
      if (machinery) {
        const mOut = $('#sim-machinery-out');
        if (mOut) mOut.textContent = toLakh(machinery.value);
      }
      if (loan) {
        const lOut = $('#sim-loan-out');
        if (lOut) lOut.textContent = toLakh(loan.value);
      }
      const att = $('#ci-attendance');
      const attOut = $('#ci-attendance-out');
      if (att && attOut) attOut.textContent = `${att.value}%`;
    };

    if (machinery) machinery.addEventListener('input', syncSliders);
    if (loan)      loan.addEventListener('input', syncSliders);
    const att = $('#ci-attendance');
    if (att) att.addEventListener('input', syncSliders);
    syncSliders();

    // --- Simulation trigger ---
    const triggerSimulation = async () => {
      runBtn.disabled = true;
      runBtn.textContent = '⏳ Simulating...';

      const payload = {
        monthly_revenue:   Number(revInput?.value || 180000),
        monthly_expenses:  Number(expInput?.value || 140000),
        cash_balance:      Number(cashInput?.value || 250000),
        hire:              Number(hire?.value || 0),
        machinery:         Number(machinery?.value || 0),
        loan:              Number(loan?.value || 0),
        price_increase:    Number(price?.value || 0),
        new_product:       newProd ? newProd.checked : false,
        new_branch:        newBranch ? newBranch.checked : false,
      };

      try {
        const result = await apiPost('/api/simulator/run', payload);
        if (result && !result.offline) {
          renderSimResult(result);
        } else {
          renderSimResult(computeSampleSimulation(payload));
        }
      } catch (err) {
        console.error('Simulator API error:', err);
        renderSimResult(computeSampleSimulation(payload));
      } finally {
        runBtn.disabled = false;
        runBtn.innerHTML = '&#9881; Run AI Simulation';
      }
    };

    runBtn.addEventListener('click', triggerSimulation);
    triggerSimulation();
  }

  function computeSampleSimulation(payload) {
    const { monthly_revenue, monthly_expenses, cash_balance, hire, machinery, loan, price_increase, new_product, new_branch } = payload;
    const revLift = monthly_revenue * (price_increase / 100) + (new_product ? 22000 : 0) + (new_branch ? 60000 : 0);
    const expAdd = (hire * 22000) + (machinery * 0.01) + (loan * 0.02) + (new_product ? 9000 : 0) + (new_branch ? 95000 : 0);

    const projected_monthly_revenue = monthly_revenue + revLift;
    const projected_monthly_expenses = monthly_expenses + expAdd;
    const monthly_profit = projected_monthly_revenue - projected_monthly_expenses;

    const margin = (projected_monthly_revenue - projected_monthly_expenses) / (projected_monthly_revenue || 1);
    const risk_score = Math.min(95, Math.max(5, Math.round(50 - margin * 100 + (loan / 50000) + (machinery / 100000))));
    const risk_band = risk_score >= 65 ? 'High' : risk_score >= 35 ? 'Moderate' : 'Low';

    const ending_balance = Math.round(cash_balance + loan - machinery + (monthly_profit * 6));
    const months = ['Month 1', 'Month 2', 'Month 3', 'Month 4', 'Month 5', 'Month 6'];
    const cash_trajectory = months.map((_, i) => Math.round(cash_balance + loan - machinery + (monthly_profit * (i + 1))));

    let rec = 'Simulation complete.';
    if (risk_band === 'High') rec = `HIGH RISK (${risk_score}/100): High lever costs leave a tight cash buffer. Phase machinery and hiring.`;
    else if (monthly_profit < 0) rec = `NET BURN (-${formatCurrency(Math.abs(monthly_profit))}/mo): Operating expenses exceed projected revenue.`;
    else rec = `FINANCIALLY SOUND (${risk_score}/100): Projected net profit is +${formatCurrency(monthly_profit)}/month. Cash reaches ${formatCurrency(ending_balance)}.`;

    return {
      projected_monthly_revenue,
      projected_monthly_expenses,
      projected_monthly_profit: monthly_profit,
      profit: monthly_profit,
      riskScore: risk_score,
      risk: risk_band,
      ending_cash: ending_balance,
      probability_of_recovery: Math.max(10, Math.min(95, 90 - risk_score * 0.6)),
      business_health_score: Math.round(100 - risk_score),
      recommendation: rec,
      cost_breakdown: {
        payroll: hire * 22000,
        machinery_maintenance: machinery * 0.01,
        loan_emi: loan * 0.02,
        product_cost: new_product ? 9000 : 0,
        branch_cost: new_branch ? 95000 : 0,
      },
      months,
      cash_trajectory,
    };
  }

  function renderSimResult(result) {
    const profit = result.projected_monthly_profit ?? result.profit ?? 0;
    const rev = result.projected_monthly_revenue ?? 0;
    const exp = result.projected_monthly_expenses ?? 0;

    let riskBand = 'Low';
    let riskScore = 20;

    if (typeof result.risk === 'object' && result.risk !== null) {
      riskBand = result.risk.band || 'Moderate';
      riskScore = result.risk.score || 50;
    } else if (typeof result.risk === 'string') {
      riskBand = result.risk;
      riskScore = result.riskScore ?? 50;
    }

    const endingCash = result.ending_cash ?? result.cashflow?.ending_balance ?? 0;
    const breachWeek = result.cashflow?.runway_breach_week;
    const recovery = result.probability_of_recovery ?? 80;
    const health = result.business_health_score ?? 70;
    const recommendation = result.recommendation || 'No recommendation available.';

    // Update KPI Scorecards
    $('#simProfit').textContent = formatCurrency(profit);
    const profitBadge = $('#simProfitBadge');
    if (profitBadge) {
      profitBadge.textContent = profit >= 0 ? 'Positive' : 'Net Loss';
      profitBadge.className = `badge badge--${profit >= 0 ? 'green' : 'red'}`;
    }
    $('#simRevExpMeta').textContent = `Rev: ${formatCurrency(rev)} · Exp: ${formatCurrency(exp)}`;

    $('#simRisk').innerHTML = `${riskScore}<span>/100</span>`;
    const riskBadge = $('#simRiskBadge');
    if (riskBadge) {
      riskBadge.textContent = riskBand;
      riskBadge.className = `badge badge--${riskBand === 'High' ? 'red' : riskBand === 'Moderate' ? 'amber' : 'green'}`;
    }
    $('#simRiskSource').textContent = result.risk_details?.source ? `Model: ${result.risk_details.source}` : 'AI Distress Classifier';

    $('#simCashflow').textContent = formatCurrency(endingCash);
    $('#simRunwayStatus').textContent = breachWeek !== undefined && breachWeek !== null
      ? `🚨 Cash breach in Month ${breachWeek + 1}`
      : '✓ No cash breach predicted';

    $('#simRecovery').innerHTML = `${recovery}<span>%</span>`;
    $('#simHealthMeta').textContent = `Health Index: ${health}/100`;

    // AI Advisor Card
    $('#simRecoText').textContent = recommendation;

    // Cost Breakdown Tags
    const cb = result.cost_breakdown || {};
    const cbItems = [];
    if (cb.payroll > 0) cbItems.push(`👥 Payroll: +${formatCurrency(cb.payroll)}/mo`);
    if (cb.machinery_maintenance > 0) cbItems.push(`⚙ Machinery Upkeep: +${formatCurrency(cb.machinery_maintenance)}/mo`);
    if (cb.loan_emi > 0) cbItems.push(`💳 Loan EMI: +${formatCurrency(cb.loan_emi)}/mo`);
    if (cb.product_cost > 0) cbItems.push(`📦 New Product: +${formatCurrency(cb.product_cost)}/mo`);
    if (cb.branch_cost > 0) cbItems.push(`🏢 Branch Overhead: +${formatCurrency(cb.branch_cost)}/mo`);

    const breakdownEl = $('#simCostBreakdown');
    if (breakdownEl) {
      if (cbItems.length > 0) {
        breakdownEl.innerHTML = `<strong>Cost Impact:</strong> ${cbItems.map(item => `<span class="pill pill--amber">${item}</span>`).join(' ')}`;
      } else {
        breakdownEl.innerHTML = '<span class="pill">No additional recurring costs selected</span>';
      }
    }

    // Simulator Chart — premium animated area with breakeven line
    const months = result.months || result.graph?.months || ['Month 1', 'Month 2', 'Month 3', 'Month 4', 'Month 5', 'Month 6'];
    const trajectory = result.cash_trajectory || result.graph?.cash_trajectory || [250000, 260000, 270000, 280000, 290000, 300000];

    const simCanvas = $('#chartSimulator');
    if (simCanvas) {
      const styles = getChartStyles();
      const simWrap = simCanvas.parentElement;
      if (simWrap) {
        simWrap.style.height = '220px';
        simWrap.style.minHeight = '220px';
      }
      simCanvas.removeAttribute('height');
      simCanvas.removeAttribute('width');
      simCanvas.style.width = '100%';
      simCanvas.style.height = '100%';

      if (typeof Chart === 'undefined') return;
      if (simulatorChart) simulatorChart.destroy();
      const isPositive = trajectory[trajectory.length - 1] >= trajectory[0];
      const lineColor = isPositive ? styles.green : styles.red;
      const ctx = simCanvas.getContext('2d');
      const grad = ctx.createLinearGradient(0, 0, 0, 220);
      grad.addColorStop(0, hexToRgba(lineColor, 0.35));
      grad.addColorStop(1, hexToRgba(lineColor, 0.0));

      // Monthly profit overlay (net per month)
      const startCash = trajectory[0];
      const profitData = trajectory.map((v, i) => i === 0 ? null : Math.round(v - trajectory[i - 1]));

      simulatorChart = new Chart(simCanvas, {
        type: 'line',
        data: {
          labels: months,
          datasets: [
            {
              label: 'Projected Cash Balance (₹)',
              data: trajectory,
              borderColor: lineColor,
              backgroundColor: grad,
              tension: 0.4,
              fill: true,
              pointRadius: 5,
              pointHoverRadius: 8,
              pointBackgroundColor: lineColor,
              pointBorderColor: '#fff',
              pointBorderWidth: 2,
              borderWidth: 2.5,
              order: 1,
            },
            {
              label: 'Monthly Net (₹)',
              data: profitData,
              type: 'bar',
              backgroundColor: profitData.map(v => v === null ? 'transparent' : v >= 0 ? hexToRgba(styles.green, 0.5) : hexToRgba(styles.red, 0.5)),
              borderColor: profitData.map(v => v === null ? 'transparent' : v >= 0 ? styles.green : styles.red),
              borderWidth: 1,
              borderRadius: 4,
              maxBarThickness: 22,
              order: 2,
              yAxisID: 'y2',
            }
          ],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          animation: { duration: 800, easing: 'easeOutQuart' },
          interaction: { mode: 'index', intersect: false },
          plugins: {
            legend: {
              display: true,
              position: 'top',
              align: 'end',
              labels: { color: styles.text, font: { size: 10, family: 'Inter' }, boxWidth: 10, padding: 12 }
            },
            tooltip: {
              backgroundColor: '#10192B',
              titleColor: '#fff',
              bodyColor: '#B7C4DA',
              padding: 12,
              cornerRadius: 8,
              callbacks: {
                label: (ctx) => {
                  if (ctx.raw === null) return '';
                  if (ctx.datasetIndex === 0) return ` Cash Balance: ${formatCurrency(ctx.raw)}`;
                  return ` Monthly Net: ${formatCurrency(ctx.raw)}`;
                }
              }
            }
          },
          scales: {
            x: { grid: { display: false }, ticks: { color: styles.text, font: { size: 10, family: 'Inter' } } },
            y: {
              grid: { color: styles.grid },
              ticks: { color: styles.text, font: { size: 10, family: 'JetBrains Mono' }, callback: v => `₹${(v/100000).toFixed(1)}L` }
            },
            y2: {
              position: 'right',
              grid: { display: false },
              ticks: { color: styles.text, font: { size: 9, family: 'JetBrains Mono' }, callback: v => `₹${(v/1000).toFixed(0)}K` }
            }
          }
        },
      });
    }
  }

  /* ------------------------------------------------------------------ *
   * 7. CHARTS (Chart.js) — Premium Production Implementation
   * ------------------------------------------------------------------ */
  let charts = {};

  // ---- Utility: create a vertical linear gradient on a canvas ----
  function createGradient(ctx, height, colorTop, colorBottom) {
    const g = ctx.createLinearGradient(0, 0, 0, height);
    g.addColorStop(0, colorTop);
    g.addColorStop(1, colorBottom);
    return g;
  }

  // ---- Utility: animate a numeric value (count-up) ----
  function animateValue(el, from, to, duration = 900, format = v => Math.round(v).toLocaleString('en-IN')) {
    if (!el) return;
    const start = performance.now();
    el.classList.add('metric-value--animating');
    const tick = (now) => {
      const p = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - p, 3);
      el.childNodes[0] && (el.childNodes[0].nodeType === Node.TEXT_NODE
        ? el.childNodes[0].textContent = format(from + (to - from) * eased)
        : null);
      if (p < 1) requestAnimationFrame(tick);
      else el.classList.remove('metric-value--animating');
    };
    requestAnimationFrame(tick);
  }

  // ---- Utility: inject a skeleton loader inside a chart-wrap ----
  function showChartSkeleton(wrapEl, heights = [40, 60, 75, 50, 85, 55, 70, 45]) {
    if (!wrapEl) return;
    const existing = wrapEl.querySelector('.chart-skeleton');
    if (existing) return;
    const bars = heights.map(h => `<span style="height:${h}%"></span>`).join('');
    const sk = document.createElement('div');
    sk.className = 'chart-skeleton';
    sk.innerHTML = `<div class="chart-skeleton__bar">${bars}</div><span class="chart-skeleton__label">Loading analytics…</span>`;
    wrapEl.appendChild(sk);
  }

  function hideChartSkeleton(wrapEl) {
    if (!wrapEl) return;
    const sk = wrapEl.querySelector('.chart-skeleton');
    if (sk) sk.remove();
  }

  function getChartStyles() {
    const cs = getComputedStyle(document.documentElement);
    const get = (v, fallback) => {
      const val = cs.getPropertyValue(v).trim();
      return val || fallback;
    };
    return {
      text:       get('--text-secondary', '#6B7B9A'),
      grid:       get('--border-subtle',  '#1E3352'),
      accent:     get('--blue-600',       '#2952E3'),
      accentCyan: get('--cyan-400',       '#3DDCEE'),
      green:      get('--green-500',      '#1FAE6E'),
      red:        get('--red-500',        '#E14B4B'),
    };
  }

  function hexToRgba(color, alpha) {
    if (!color) return `rgba(41,82,227,${alpha})`;
    color = color.trim();
    // Handle rgb(...) and rgba(...) — extract r, g, b
    const rgbMatch = color.match(/rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)/i);
    if (rgbMatch) {
      return `rgba(${rgbMatch[1]},${rgbMatch[2]},${rgbMatch[3]},${alpha})`;
    }
    // Handle hex shorthand #ABC → #AABBCC
    let hex = color.replace('#', '');
    if (hex.length === 3) hex = hex.split('').map(c => c + c).join('');
    if (hex.length !== 6 || /[^0-9a-fA-F]/.test(hex)) {
      // Unknown format — return a safe default
      return `rgba(41,82,227,${alpha})`;
    }
    const bigint = parseInt(hex, 16);
    const r = (bigint >> 16) & 255, g = (bigint >> 8) & 255, b = bigint & 255;
    return `rgba(${r},${g},${b},${alpha})`;
  }

  function baseChartOptions(styles) {
    return {
      responsive: true,
      maintainAspectRatio: false,
      plugins: { legend: { display: false }, tooltip: { backgroundColor: styles.text, titleFont: { family: 'Inter' }, bodyFont: { family: 'JetBrains Mono' } } },
      scales: {
        x: { grid: { display: false }, ticks: { color: styles.text, font: { size: 10, family: 'Inter' } } },
        y: { grid: { color: styles.grid }, ticks: { color: styles.text, font: { size: 10, family: 'JetBrains Mono' } } },
      },
    };
  }

  function prepareCanvas(el, chartHeight = 220) {
    if (!el) return null;
    const parent = el.parentElement;
    if (!parent) return null;
    // Remove any HTML height attribute that conflicts with Chart.js responsive sizing
    el.removeAttribute('height');
    el.removeAttribute('width');
    // Set the height on the parent so Chart.js gets correct dimensions
    parent.style.height = chartHeight + 'px';
    parent.style.minHeight = chartHeight + 'px';
    el.style.width = '100%';
    el.style.height = '100%';
    el.style.display = 'block';
    return el;
  }

  function renderAllCharts(agentData = null) {
    if (typeof Chart === 'undefined') return;
    if (agentData) state.latestAgents = agentData;
    const styles = getChartStyles();

    // Destroy all existing charts cleanly
    Object.values(charts).forEach(c => { try { c && c.destroy(); } catch(e) {} });
    charts = {};

    // Common tooltip config
    const tipStyle = {
      backgroundColor: state.theme === 'dark' ? '#0F2138' : '#10192B',
      titleColor: '#E8F0FE',
      bodyColor: '#8FA0BC',
      padding: 12,
      cornerRadius: 8,
      borderColor: 'rgba(61,220,238,0.2)',
      borderWidth: 1,
      titleFont: { family: 'Inter', size: 11, weight: '600' },
      bodyFont: { family: 'JetBrains Mono', size: 10.5 },
    };

    // =========================================================
    // 1. REVENUE TREND — Dual-line (Revenue + Expenses) + Forecast
    // =========================================================
    const revenueEl = prepareCanvas($('#chartRevenue'), 210);
    if (revenueEl) {
      const ctx1 = revenueEl.getContext('2d');
      const gradRev = createGradient(ctx1, 210, hexToRgba(styles.accent, 0.4), hexToRgba(styles.accent, 0.0));
      const gradExp = createGradient(ctx1, 210, hexToRgba(styles.green, 0.2), hexToRgba(styles.green, 0.0));

      const revenueData = [412000, 398000, 445000, 431000, 467000, 452000, 489000, null];
      const expenseData = [340000, 355000, 368000, 360000, 375000, 370000, 382000, null];

      charts.revenue = new Chart(revenueEl, {
        type: 'line',
        data: {
          labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'],
          datasets: [
            {
              label: 'Revenue',
              data: revenueData,
              borderColor: styles.accent,
              backgroundColor: gradRev,
              tension: 0.4, fill: true,
              pointRadius: revenueData.map((v, i) => i < 7 ? 4 : 0),
              pointHoverRadius: 8,
              pointBackgroundColor: styles.accent,
              pointBorderColor: '#fff',
              pointBorderWidth: 2,
              borderWidth: 2.5,
              order: 1,
            },
            {
              label: 'Expenses',
              data: expenseData,
              borderColor: styles.green,
              backgroundColor: gradExp,
              tension: 0.4, fill: true,
              pointRadius: expenseData.map((v, i) => i < 7 ? 3 : 0),
              pointHoverRadius: 7,
              pointBackgroundColor: styles.green,
              pointBorderColor: '#fff',
              pointBorderWidth: 2,
              borderWidth: 2,
              order: 2,
            },
            {
              label: 'Forecast',
              data: [null, null, null, null, null, null, 489000, 514000],
              borderColor: hexToRgba(styles.accent, 0.55),
              backgroundColor: 'transparent',
              tension: 0.4, fill: false,
              borderWidth: 2,
              borderDash: [7, 4],
              pointRadius: [0,0,0,0,0,0,0,6],
              pointHoverRadius: 9,
              pointBackgroundColor: styles.accent,
              pointBorderColor: '#fff',
              pointBorderWidth: 2,
              order: 3,
            }
          ],
        },
        options: {
          responsive: true, maintainAspectRatio: false,
          animation: { duration: 1000, easing: 'easeOutQuart' },
          interaction: { mode: 'index', intersect: false },
          plugins: {
            legend: {
              display: true, position: 'top', align: 'end',
              labels: { color: styles.text, font: { size: 10, family: 'Inter' }, boxWidth: 10, padding: 14,
                filter: item => item.datasetIndex < 2 }
            },
            tooltip: { ...tipStyle, callbacks: {
              title: (items) => items[0]?.label || '',
              label: ctx => {
                if (ctx.raw === null) return '';
                const prefix = ctx.datasetIndex === 2 ? ' Forecast: ' : ` ${ctx.dataset.label}: `;
                return prefix + formatCurrency(ctx.raw);
              },
              afterBody: (items) => {
                const rev = items.find(i => i.datasetIndex === 0)?.raw;
                const exp = items.find(i => i.datasetIndex === 1)?.raw;
                if (rev && exp) return [``, ` Net Profit: ${formatCurrency(rev - exp)}`];
                return [];
              }
            }}
          },
          scales: {
            x: { grid: { display: false, drawBorder: false }, ticks: { color: styles.text, font: { size: 10, family: 'Inter' } } },
            y: { grid: { color: styles.grid, drawBorder: false }, ticks: { color: styles.text, font: { size: 10, family: 'JetBrains Mono' }, callback: v => `₹${(v/1000).toFixed(0)}K` } }
          }
        }
      });
      hideChartSkeleton(revenueEl.parentElement);
    }

    // =========================================================
    // 2. CASH FLOW TREND — Bars (green/red) + Cumulative line
    // =========================================================
    const cashflowEl = prepareCanvas($('#chartCashflow'), 210);
    if (cashflowEl) {
      const cashData = [42000, -8000, 31000, 15000, -12000, 26000, 35000, 18000];
      const cashLabels = ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8'];
      let cum = 0;
      const cumulativeData = cashData.map(v => { cum += v; return cum; });

      charts.cashflow = new Chart(cashflowEl, {
        type: 'bar',
        data: {
          labels: cashLabels,
          datasets: [
            {
              label: 'Weekly Net Cash',
              data: cashData,
              backgroundColor: cashData.map(v => v >= 0 ? hexToRgba(styles.green, 0.82) : hexToRgba(styles.red, 0.82)),
              borderColor: cashData.map(v => v >= 0 ? styles.green : styles.red),
              borderWidth: 1.5,
              borderRadius: 6,
              maxBarThickness: 30,
              order: 2,
            },
            {
              label: 'Cumulative Balance',
              data: cumulativeData,
              type: 'line',
              borderColor: styles.accentCyan,
              backgroundColor: 'transparent',
              borderWidth: 2.5,
              tension: 0.4,
              pointRadius: 4,
              pointHoverRadius: 7,
              pointBackgroundColor: styles.accentCyan,
              pointBorderColor: '#fff',
              pointBorderWidth: 2,
              order: 1,
              yAxisID: 'y2',
            }
          ],
        },
        options: {
          responsive: true, maintainAspectRatio: false,
          animation: { duration: 900, easing: 'easeOutQuart' },
          interaction: { mode: 'index', intersect: false },
          plugins: {
            legend: {
              display: true, position: 'top', align: 'end',
              labels: { color: styles.text, font: { size: 10, family: 'Inter' }, boxWidth: 10, padding: 14 }
            },
            tooltip: { ...tipStyle, callbacks: {
              label: ctx => ` ${ctx.dataset.label}: ${formatCurrency(ctx.raw)}`
            }}
          },
          scales: {
            x: { grid: { display: false, drawBorder: false }, ticks: { color: styles.text, font: { size: 10 } } },
            y: { grid: { color: styles.grid, drawBorder: false }, ticks: { color: styles.text, font: { size: 10, family: 'JetBrains Mono' }, callback: v => `₹${(v/1000).toFixed(0)}K` } },
            y2: { position: 'right', grid: { display: false }, ticks: { color: styles.accentCyan, font: { size: 9, family: 'JetBrains Mono' }, callback: v => `₹${(v/1000).toFixed(0)}K` } }
          }
        }
      });
      hideChartSkeleton(cashflowEl.parentElement);
    }

    // =========================================================
    // 3. BUSINESS HEALTH RADAR — Current vs Industry Benchmark
    // =========================================================
    const healthRadarEl = prepareCanvas($('#chartHealthRadar'), 270);
    if (healthRadarEl) {
      charts.healthRadar = new Chart(healthRadarEl, {
        type: 'radar',
        data: {
          labels: ['Revenue\nMomentum', 'Cash\nConversion', 'Debt\nService', 'Customer\nConc.', 'Working\nCapital', 'Expense\nVolatility'],
          datasets: [
            {
              label: 'Your Score',
              data: [74, 58, 81, 46, 69, 33],
              borderColor: styles.accent,
              backgroundColor: hexToRgba(styles.accent, 0.22),
              borderWidth: 2.5,
              pointRadius: 5,
              pointHoverRadius: 8,
              pointBackgroundColor: styles.accent,
              pointBorderColor: '#fff',
              pointBorderWidth: 2,
            },
            {
              label: 'Industry Benchmark',
              data: [80, 75, 85, 70, 75, 75],
              borderColor: styles.accentCyan,
              backgroundColor: hexToRgba(styles.accentCyan, 0.06),
              borderWidth: 1.5,
              borderDash: [5, 4],
              pointRadius: 3,
              pointHoverRadius: 6,
              pointBackgroundColor: styles.accentCyan,
            }
          ]
        },
        options: {
          responsive: true, maintainAspectRatio: false,
          animation: { duration: 1200, easing: 'easeOutQuart' },
          plugins: {
            legend: {
              display: true, position: 'bottom',
              labels: { color: styles.text, font: { size: 10, family: 'Inter' }, boxWidth: 10, padding: 16 }
            },
            tooltip: { ...tipStyle, callbacks: {
              label: ctx => ` ${ctx.dataset.label}: ${ctx.raw}/100`
            }}
          },
          scales: {
            r: {
              angleLines: { color: styles.grid },
              grid: { color: styles.grid },
              pointLabels: { color: styles.text, font: { size: 9.5, family: 'Inter' } },
              ticks: { display: false, backdropColor: 'transparent' },
              suggestedMin: 0, suggestedMax: 100,
            }
          }
        }
      });
      hideChartSkeleton(healthRadarEl.parentElement);
    }

    // =========================================================
    // 4. HEALTH & DISTRESS TREND — Dual area + Forecast bands
    // =========================================================
    const healthTrendEl = prepareCanvas($('#chartHealthTrend'), 270);
    if (healthTrendEl) {
      const ctx4 = healthTrendEl.getContext('2d');
      const gradH = createGradient(ctx4, 270, hexToRgba(styles.green, 0.3), hexToRgba(styles.green, 0.0));
      const gradD = createGradient(ctx4, 270, hexToRgba(styles.red, 0.2), hexToRgba(styles.red, 0.0));

      charts.healthTrend = new Chart(healthTrendEl, {
        type: 'line',
        data: {
          labels: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'],
          datasets: [
            {
              label: 'Health Score',
              data: [68, 70, 72, 75, 76, 78, null],
              borderColor: styles.green,
              backgroundColor: gradH,
              tension: 0.4, fill: true, borderWidth: 2.5,
              pointRadius: [4,4,4,4,4,5,0],
              pointHoverRadius: 8,
              pointBackgroundColor: styles.green,
              pointBorderColor: '#fff', pointBorderWidth: 2,
            },
            {
              label: 'Distress Risk %',
              data: [45, 41, 38, 35, 33, 31, null],
              borderColor: styles.red,
              backgroundColor: gradD,
              tension: 0.4, fill: true, borderWidth: 2.5,
              borderDash: [5, 3],
              pointRadius: [4,4,4,4,4,5,0],
              pointHoverRadius: 8,
              pointBackgroundColor: styles.red,
              pointBorderColor: '#fff', pointBorderWidth: 2,
            },
            {
              label: 'Health Forecast',
              data: [null,null,null,null,null,78,82],
              borderColor: hexToRgba(styles.green, 0.5),
              backgroundColor: 'transparent',
              tension: 0.4, fill: false, borderWidth: 2,
              borderDash: [7, 4],
              pointRadius: [0,0,0,0,0,0,6],
              pointHoverRadius: 9,
              pointBackgroundColor: styles.green,
              pointBorderColor: '#fff', pointBorderWidth: 2,
            },
            {
              label: 'Risk Forecast',
              data: [null,null,null,null,null,31,28],
              borderColor: hexToRgba(styles.red, 0.5),
              backgroundColor: 'transparent',
              tension: 0.4, fill: false, borderWidth: 2,
              borderDash: [7, 4],
              pointRadius: [0,0,0,0,0,0,6],
              pointHoverRadius: 9,
              pointBackgroundColor: styles.red,
              pointBorderColor: '#fff', pointBorderWidth: 2,
            }
          ]
        },
        options: {
          responsive: true, maintainAspectRatio: false,
          animation: { duration: 1100, easing: 'easeOutQuart' },
          interaction: { mode: 'index', intersect: false },
          plugins: {
            legend: {
              display: true, position: 'top', align: 'end',
              labels: { color: styles.text, font: { size: 10, family: 'Inter' }, boxWidth: 10, padding: 14,
                filter: item => item.datasetIndex < 2 }
            },
            tooltip: { ...tipStyle, callbacks: {
              label: ctx => {
                if (ctx.raw === null) return '';
                const isForecast = ctx.datasetIndex >= 2;
                const label = isForecast ? `Forecast ${ctx.datasetIndex === 2 ? 'Health' : 'Risk'}` : ctx.dataset.label;
                return ` ${label}: ${ctx.raw}${ctx.datasetIndex % 2 === 1 ? '%' : '/100'}`;
              }
            }}
          },
          scales: {
            x: { grid: { display: false, drawBorder: false }, ticks: { color: styles.text, font: { size: 10 } } },
            y: { grid: { color: styles.grid, drawBorder: false }, suggestedMin: 0, suggestedMax: 100,
              ticks: { color: styles.text, font: { size: 10, family: 'JetBrains Mono' } } }
          }
        }
      });
      hideChartSkeleton(healthTrendEl.parentElement);
    }

    // =========================================================
    // 5. AGENT CONFIDENCE — Horizontal bar, risk-colored
    // =========================================================
    const agentConfidenceEl = prepareCanvas($('#chartAgentConfidence'), 260);
    if (agentConfidenceEl) {
      const activeAgents = state.latestAgents || agentData || SAMPLE.agents;
      const agentNames = activeAgents.map(a => a.name.replace(' Agent', ''));
      const confScores = activeAgents.map(a => a.confidence || 80);
      const barColors = activeAgents.map(a =>
        a.risk === 'High' ? hexToRgba(styles.red, 0.82)
        : a.risk === 'Moderate' ? hexToRgba('#E68A1C', 0.82)
        : hexToRgba(styles.green, 0.82)
      );
      const borderColors = activeAgents.map(a =>
        a.risk === 'High' ? styles.red : a.risk === 'Moderate' ? '#E68A1C' : styles.green
      );

      try {
        charts.agentConfidence = new Chart(agentConfidenceEl, {
          type: 'bar',
          data: {
            labels: agentNames,
            datasets: [{
              label: 'Confidence %',
              data: confScores,
              backgroundColor: barColors,
              borderColor: borderColors,
              borderWidth: 1.5,
              borderRadius: 5,
              maxBarThickness: 28,
            }]
          },
          options: {
            indexAxis: 'y',
            responsive: true, maintainAspectRatio: false,
            animation: { duration: 1000, easing: 'easeOutQuart' },
            plugins: {
              legend: { display: false },
              tooltip: { ...tipStyle, callbacks: {
                label: ctx => ` Confidence: ${ctx.raw}%   Risk Level: ${activeAgents[ctx.dataIndex]?.risk || 'Low'}`
              }}
            },
            scales: {
              x: { min: 0, max: 100, grid: { color: styles.grid, drawBorder: false },
                ticks: { color: styles.text, font: { size: 10, family: 'JetBrains Mono' }, callback: v => `${v}%` } },
              y: { grid: { display: false },
                ticks: { color: styles.text, font: { size: 10.5, family: 'Inter', weight: '600' } } }
            }
          }
        });
      } catch(e) { console.warn('Agent confidence chart error:', e); }

      // Supplementary progress bar rows below chart
      const chartCard = agentConfidenceEl.parentElement?.parentElement;
      if (chartCard) {
        let barsEl = chartCard.querySelector('#agentConfidenceHTMLFallback');
        if (!barsEl) {
          barsEl = document.createElement('div');
          barsEl.id = 'agentConfidenceHTMLFallback';
          barsEl.className = 'agent-confidence-bars';
          chartCard.appendChild(barsEl);
        }
        barsEl.innerHTML = activeAgents.map(a => {
          const score = a.confidence || 85;
          const tone = a.risk === 'High' ? 'red' : a.risk === 'Moderate' ? 'amber' : 'green';
          const barColor = tone === 'red' ? 'var(--red-500)' : tone === 'amber' ? 'var(--orange-500)' : 'var(--green-500)';
          return `<div class="agent-conf-row">
            <span class="agent-conf-row__name">${a.name}</span>
            <div class="agent-conf-row__track"><div class="agent-conf-row__fill" style="width:${score}%;background:${barColor}"></div></div>
            <span class="agent-conf-row__pct">${score}%</span>
            <span class="badge badge--${tone}" style="font-size:.6rem;padding:2px 7px">${a.risk || 'Low'}</span>
          </div>`;
        }).join('');
      }
      hideChartSkeleton(agentConfidenceEl.parentElement);
    }

    // =========================================================
    // 6. RECOVERY TRAJECTORY — Area + confidence band + target
    // =========================================================
    const recoveryEl = prepareCanvas($('#chartRecoveryTrend'), 230);
    if (recoveryEl) {
      const ctx6 = recoveryEl.getContext('2d');
      const gradRec = createGradient(ctx6, 230, hexToRgba(styles.green, 0.38), hexToRgba(styles.green, 0.0));

      const recLabels = ['Day 1', 'Day 10', 'Day 21', 'Day 30', 'Day 45', 'Day 60', 'Day 75', 'Day 90'];
      const recData   = [120000, 148000, 182000, 214000, 248000, 278000, 305000, 320000];
      const upperBand = recData.map(v => Math.round(v * 1.1));
      const lowerBand = recData.map(v => Math.round(v * 0.9));

      try {
        charts.recovery = new Chart(recoveryEl, {
          type: 'line',
          data: {
            labels: recLabels,
            datasets: [
              {
                label: 'Projected Buffer',
                data: recData,
                borderColor: styles.green,
                backgroundColor: gradRec,
                tension: 0.4, fill: true, borderWidth: 2.5,
                pointRadius: 5,
                pointHoverRadius: 8,
                pointBackgroundColor: styles.green,
                pointBorderColor: '#fff', pointBorderWidth: 2,
                order: 1,
              },
              {
                label: 'Upper Band',
                data: upperBand,
                borderColor: hexToRgba(styles.green, 0.25),
                backgroundColor: hexToRgba(styles.green, 0.08),
                tension: 0.4, fill: '+1',
                borderWidth: 1, borderDash: [4, 3],
                pointRadius: 0, pointHoverRadius: 0,
                order: 2,
              },
              {
                label: 'Lower Band',
                data: lowerBand,
                borderColor: hexToRgba(styles.green, 0.25),
                backgroundColor: 'transparent',
                tension: 0.4, fill: false,
                borderWidth: 1, borderDash: [4, 3],
                pointRadius: 0, pointHoverRadius: 0,
                order: 3,
              },
              {
                label: 'Target ₹3.2L',
                data: Array(8).fill(320000),
                borderColor: hexToRgba(styles.accentCyan, 0.65),
                backgroundColor: 'transparent',
                tension: 0, fill: false,
                borderWidth: 1.5, borderDash: [9, 4],
                pointRadius: 0, pointHoverRadius: 0,
                order: 4,
              }
            ],
          },
          options: {
            responsive: true, maintainAspectRatio: false,
            animation: { duration: 1100, easing: 'easeOutQuart' },
            interaction: { mode: 'index', intersect: false },
            plugins: {
              legend: {
                display: true, position: 'top', align: 'end',
                labels: { color: styles.text, font: { size: 10, family: 'Inter' }, boxWidth: 10, padding: 14,
                  filter: item => item.datasetIndex === 0 || item.datasetIndex === 3 }
              },
              tooltip: { ...tipStyle, callbacks: {
                label: ctx => {
                  if (ctx.datasetIndex === 1 || ctx.datasetIndex === 2) return '';
                  return ` ${ctx.dataset.label}: ${formatCurrency(ctx.raw)}`;
                }
              }}
            },
            scales: {
              x: { grid: { display: false, drawBorder: false }, ticks: { color: styles.text, font: { size: 10 } } },
              y: { grid: { color: styles.grid, drawBorder: false },
                ticks: { color: styles.text, font: { size: 10, family: 'JetBrains Mono' }, callback: v => `₹${(v/100000).toFixed(1)}L` } }
            }
          }
        });
      } catch(e) { console.warn('Recovery chart error:', e); }

      // Milestone chips below the chart
      const recCard = recoveryEl.parentElement?.parentElement;
      if (recCard) {
        let milestonesEl = recCard.querySelector('#recoveryHTMLFallback');
        if (!milestonesEl) {
          milestonesEl = document.createElement('div');
          milestonesEl.id = 'recoveryHTMLFallback';
          milestonesEl.className = 'recovery-milestones';
          recCard.appendChild(milestonesEl);
        }
        const milestones = [
          { week: 'W1–W3', val: '₹1.8L', desc: 'Receivables recovery', pct: 38 },
          { week: 'W4–W6', val: '₹2.4L', desc: 'Discretionary trim', pct: 62 },
          { week: 'W7–W9', val: '₹2.8L', desc: 'Supplier renegotiation', pct: 80 },
          { week: 'W10–W12', val: '₹3.2L', desc: 'Target reserve reached', pct: 100 },
        ];
        milestonesEl.innerHTML = milestones.map(m => `
          <div class="recovery-milestone">
            <div class="recovery-milestone__week">${m.week}</div>
            <div class="recovery-milestone__val">${m.val}</div>
            <p class="recovery-milestone__desc">${m.desc}</p>
            <div class="recovery-milestone__bar"><div class="recovery-milestone__bar-fill" style="width:${m.pct}%"></div></div>
          </div>`).join('');
      }
      hideChartSkeleton(recoveryEl.parentElement);
    }

    // =========================================================
    // 7. GROWTH MATRIX — Horizontal bar, score-coded colors
    // =========================================================
    const growthEl = prepareCanvas($('#chartGrowthMatrix'), 230);
    if (growthEl) {
      const growthLabels = ['Wholesale Export', 'E-Commerce Store', 'Equipment Leasing', 'B2B Subsidies', 'Local Franchise'];
      const growthScores = [88, 72, 65, 54, 47];
      const growthColors = growthScores.map(s =>
        s >= 80 ? hexToRgba(styles.green, 0.85)
        : s >= 65 ? hexToRgba('#E68A1C', 0.82)
        : hexToRgba(styles.accent, 0.75)
      );
      const growthBorders = growthScores.map(s =>
        s >= 80 ? styles.green : s >= 65 ? '#E68A1C' : styles.accent
      );

      try {
        charts.growth = new Chart(growthEl, {
          type: 'bar',
          data: {
            labels: growthLabels,
            datasets: [{
              label: 'Opportunity Score',
              data: growthScores,
              backgroundColor: growthColors,
              borderColor: growthBorders,
              borderWidth: 1.5,
              borderRadius: 5,
              maxBarThickness: 26,
            }]
          },
          options: {
            indexAxis: 'y',
            responsive: true, maintainAspectRatio: false,
            animation: { duration: 1000, easing: 'easeOutQuart' },
            plugins: {
              legend: { display: false },
              tooltip: { ...tipStyle, callbacks: {
                label: ctx => ` Opportunity Score: ${ctx.raw} / 100`
              }}
            },
            scales: {
              x: { min: 0, max: 100, grid: { color: styles.grid, drawBorder: false },
                ticks: { color: styles.text, font: { size: 10, family: 'JetBrains Mono' } } },
              y: { grid: { display: false },
                ticks: { color: styles.text, font: { size: 10.5, family: 'Inter', weight: '600' } } }
            }
          }
        });
      } catch(e) { console.warn('Growth chart error:', e); }

      // Path chips below growth chart
      const growthCard = growthEl.parentElement?.parentElement;
      if (growthCard) {
        let pathsEl = growthCard.querySelector('#growthHTMLFallback');
        if (!pathsEl) {
          pathsEl = document.createElement('div');
          pathsEl.id = 'growthHTMLFallback';
          pathsEl.className = 'growth-paths';
          growthCard.appendChild(pathsEl);
        }
        const paths = [
          { name: 'Wholesale Export Pilot', score: 88, tag: 'High Opportunity', tone: 'green' },
          { name: 'E-Commerce Marketplace', score: 72, tag: 'Medium', tone: 'amber' },
          { name: 'Idle Equipment Leasing', score: 65, tag: 'Medium', tone: 'amber' },
          { name: 'B2B Trade Subsidies', score: 54, tag: 'Low Risk Entry', tone: 'outline' },
        ];
        pathsEl.innerHTML = paths.map(p => `
          <div class="growth-path">
            <div>
              <strong style="font-size:.8rem;display:block;margin-bottom:3px">${p.name}</strong>
              <span class="badge badge--${p.tone}" style="font-size:.6rem;padding:2px 7px">${p.tag}</span>
            </div>
            <div class="growth-path__score">${p.score}<small style="font-size:.6rem;color:var(--text-secondary)">/100</small></div>
          </div>`).join('');
      }
      hideChartSkeleton(growthEl.parentElement);
    }

    // =========================================================
    // 8. SIMULATOR — Re-render if simulator page is active
    // =========================================================
    const simCtx = $('#chartSimulator');
    if (simCtx) {
      const simPage = $('#page-simulator');
      const isSimActive = simPage && simPage.classList.contains('is-active');
      if (simulatorChart) {
        try { simulatorChart.destroy(); } catch(e) {}
        simulatorChart = null;
      }
      if (isSimActive) {
        const defaultPayload = {
          monthly_revenue: Number($('#sim-rev')?.value || 180000),
          monthly_expenses: Number($('#sim-exp')?.value || 140000),
          cash_balance: Number($('#sim-cash')?.value || 250000),
          hire: Number($('#sim-hire')?.value || 0),
          machinery: Number($('#sim-machinery')?.value || 0),
          loan: Number($('#sim-loan')?.value || 0),
          price_increase: Number($('#sim-price')?.value || 0),
          new_product: false,
          new_branch: false,
        };
        renderSimResult(computeSampleSimulation(defaultPayload));
      }
    }

    // =========================================================
    // Animate KPI metric values on dashboard (count-up)
    // =========================================================
    const kpiTargets = [
      { sel: '[data-metric="risk"] .metric-value', to: 31, suffix: '%' },
      { sel: '[data-metric="pulse"] .metric-value', to: 72, suffix: '/100' },
      { sel: '[data-metric="csat"] .metric-value', to: 4.4, suffix: '/5', decimals: 1 },
      { sel: '[data-metric="inventory"] .metric-value', to: 63, suffix: '/100' },
      { sel: '[data-metric="supplier"] .metric-value', to: 91, suffix: '/100' },
      { sel: '[data-metric="employee"] .metric-value', to: 85, suffix: '/100' },
    ];
    kpiTargets.forEach(({ sel, to, suffix, decimals = 0 }) => {
      const el = $(sel);
      if (!el) return;
      const spanHTML = el.querySelector('span') ? el.querySelector('span').outerHTML : '';
      el.innerHTML = `0${spanHTML}`;
      animateValue(el, 0, to, 1000, v => (decimals ? v.toFixed(decimals) : Math.round(v)));
    });
  }

  function initGauge(score) {
    const circumference = 2 * Math.PI * 68;
    const fill = $('#gaugeFill');
    fill.style.strokeDasharray = String(circumference);
    requestAnimationFrame(() => {
      fill.style.strokeDashoffset = String(circumference * (1 - score / 100));
    });
    $('#gaugeScore').textContent = score;
  }

  /* ------------------------------------------------------------------ *
   * 8. INIT
   * ------------------------------------------------------------------ */
  async function init() {
    // --- Global Input Behavior Fixes ---
    // 1. Prevent mouse wheel from accidentally changing number input values
    document.addEventListener('wheel', (e) => {
      if (document.activeElement && document.activeElement.type === 'number') {
        document.activeElement.blur();
      }
    }, { passive: true });
    
    // 2. Ensure clicking anywhere in a currency wrapper focuses the input
    document.addEventListener('click', (e) => {
      const wrap = e.target.closest('.currency-input-wrap');
      if (wrap) {
        const inp = wrap.querySelector('input');
        if (inp && document.activeElement !== inp) inp.focus();
      }
    });
    initNavigation();
    initSidebarCollapse();
    initDarkMode();
    initDropdowns();
    initModal();
    initLogout();
    initGlobalSearch();
    initCheckinForm();
    initSimulator();
    initAgentBoard();

    renderNotifications(await apiGet(`${ENDPOINTS.history}/notifications`, SAMPLE.notifications));

    const recos = (await apiGet(ENDPOINTS.recommendations, { items: SAMPLE.recommendations })).items || SAMPLE.recommendations;
    renderRecommendations(recos);
    initRecoFilters(recos);
    renderDashboardRecoSummary(recos);
    renderAiInsights();
    renderHealthDetail();

    const agents = (await apiGet(ENDPOINTS.agents, { items: SAMPLE.agents })).items || SAMPLE.agents;
    renderAgents(agents);
    updateExecutiveAnalysisSummary(agents);

    renderRecovery(SAMPLE.recovery);
    $('#growthGrid').innerHTML = SAMPLE.growth.map(recoCardHtml).join('');
    // $('#schemesGrid').innerHTML = SAMPLE.schemes.map(recoCardHtml).join('');
    renderReports(SAMPLE.reports);
    renderKnowledgeBase();
    if (typeof renderBenchmarkAI === 'function') renderBenchmarkAI();

    initGauge(78);
    // Delay chart rendering slightly to ensure Chart.js is loaded and DOM layout is complete
    if (typeof Chart !== 'undefined') {
      requestAnimationFrame(() => setTimeout(renderAllCharts, 100));
    } else {
      // Wait for Chart.js CDN to load
      const checkChart = setInterval(() => {
        if (typeof Chart !== 'undefined') {
          clearInterval(checkChart);
          renderAllCharts();
        }
      }, 100);
    }

    $('#markAllReadBtn').addEventListener('click', () => {
      $('#notifCount').textContent = '0';
      showToast('All notifications marked as read');
    });
  }

  document.addEventListener('DOMContentLoaded', init);
})();