import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="State of EvoEvo",
    layout="wide"
)

MASCOT_URL = "https://raw.githubusercontent.com/Junedkhan121/state-of-evoevo/main/mascot.png"

# =========================
# THEME
# =========================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

:root {
    --bg: #0B0E14;
    --panel: #12151D;
    --panel-alt: #161A24;
    --border: #232732;
    --text: #E7E9EE;
    --text-dim: #8A90A0;
    --accent: #C9A227;
    --accent-dim: #8C7420;
    --positive: #3FB984;
    --negative: #E5484D;
}

html, body, .stApp {
    background-color: var(--bg);
    color: var(--text);
    font-family: 'Inter', -apple-system, sans-serif;
}

/* ---- Typography ---- */
h1, h2, h3 {
    font-weight: 600;
    color: var(--text);
    letter-spacing: -0.01em;
}

h1 { font-size: 1.9rem; }
h2 { font-size: 1.3rem; }
h3 { font-size: 1.05rem; }

p, span, label, div {
    color: var(--text);
}

/* ---- Page header block ---- */
.page-header {
    padding-bottom: 14px;
    margin-bottom: 22px;
    border-bottom: 1px solid var(--border);
}

.page-header .eyebrow {
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-size: 0.72rem;
    color: var(--accent);
    font-weight: 600;
    margin-bottom: 4px;
}

.page-header .subtitle {
    color: var(--text-dim);
    font-size: 0.9rem;
    margin-top: 2px;
}

/* ---- Metric cards ---- */
[data-testid="stMetric"] {
    background-color: var(--panel);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 16px 18px;
}

[data-testid="stMetricLabel"] {
    color: var(--text-dim);
    font-size: 0.78rem;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    font-weight: 500;
}

[data-testid="stMetricValue"] {
    color: var(--text);
    font-weight: 600;
    font-size: 1.5rem;
}

[data-testid="stMetricDelta"] {
    font-size: 0.8rem;
}

/* ---- Sidebar ---- */
[data-testid="stSidebar"] {
    background-color: var(--panel);
    border-right: 1px solid var(--border);
}

[data-testid="stSidebar"] h1 {
    color: var(--text);
    font-size: 1.15rem;
    font-weight: 700;
    letter-spacing: 0.02em;
}

[data-testid="stSidebar"] button {
    width: 100%;
    text-align: left;
    border-radius: 6px;
    margin-bottom: 2px;
    font-weight: 500;
    font-size: 0.88rem;
    transition: background-color 0.12s ease, color 0.12s ease, border-color 0.12s ease;
}

[data-testid="stSidebar"] [data-testid="stBaseButton-primary"] {
    background-color: var(--panel-alt);
    color: var(--accent);
    border: 1px solid var(--accent-dim);
}

[data-testid="stSidebar"] [data-testid="stBaseButton-primary"]:hover {
    border-color: var(--accent);
}

[data-testid="stSidebar"] [data-testid="stBaseButton-secondary"] {
    background-color: transparent;
    color: var(--text-dim);
    border: 1px solid transparent;
}

[data-testid="stSidebar"] [data-testid="stBaseButton-secondary"]:hover {
    color: var(--text);
    border-color: var(--border);
}

/* ---- Action buttons in main area ---- */
.main [data-testid="stBaseButton-secondary"] {
    background-color: var(--panel);
    color: var(--text);
    border: 1px solid var(--border);
    font-weight: 500;
}

.main [data-testid="stBaseButton-secondary"]:hover {
    border-color: var(--accent);
    color: var(--accent);
}

/* ---- Tables ---- */
[data-testid="stDataFrame"] {
    border: 1px solid var(--border);
    border-radius: 8px;
    overflow: hidden;
}

/* ---- Expander ---- */
[data-testid="stExpander"] {
    border: 1px solid var(--border);
    border-radius: 8px;
    background-color: var(--panel);
}

/* ---- Dividers ---- */
hr {
    border-color: var(--border);
}

/* ---- Text areas / download buttons ---- */
textarea {
    background-color: var(--panel) !important;
    color: var(--text) !important;
    border: 1px solid var(--border) !important;
}

/* ---- Mascot: header ---- */
.header-row {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 16px;
}

.header-row .mascot-topright img {
    width: 56px;
    border-radius: 10px;
}

/* ---- Mascot: sidebar ---- */
.sidebar-mascot {
    text-align: center;
    margin: 4px 0 14px 0;
}

.sidebar-mascot img {
    width: 64px;
    opacity: 0.95;
}

/* ---- Mascot: floating ---- */
.mascot-floating-wrap {
    position: fixed;
    bottom: 18px;
    right: 18px;
    z-index: 9999;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 8px;
    pointer-events: auto;
    cursor: grab;
    touch-action: none;
    user-select: none;
}

.mascot-floating-wrap img {
    width: 68px;
    filter: drop-shadow(0 4px 12px rgba(0,0,0,0.45));
    pointer-events: none;
}

.mascot-ticker {
    position: relative;
    background-color: var(--panel);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 7px 12px;
    font-size: 0.76rem;
    color: var(--text-dim);
    min-width: 210px;
    max-width: 250px;
    height: 18px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.35);
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.4s ease;
}

.mascot-floating-wrap.mascot-awake .mascot-ticker {
    opacity: 1;
    pointer-events: auto;
}

.mascot-ticker span {
    position: absolute;
    left: 12px;
    right: 12px;
    top: 7px;
    opacity: 0;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

</style>
""", unsafe_allow_html=True)

# =========================
# PAGE HEADER HELPER
# =========================

def page_header(title, subtitle=None, eyebrow="State of EvoEvo"):
    st.markdown(f"""
    <div class="page-header">
        <div class="header-row">
            <div>
                <div class="eyebrow">{eyebrow}</div>
                <h1>{title}</h1>
                {f'<div class="subtitle">{subtitle}</div>' if subtitle else ''}
            </div>
            <div class="mascot-topright">
                <img src="{MASCOT_URL}" />
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# SIDEBAR NAVIGATION
# =========================

PAGES = [
    "Network Growth",
    "Reports Center",
    "Network Insights"
]

if "page" not in st.session_state:
    st.session_state.page = PAGES[0]

st.sidebar.title("State of EvoEvo")

st.sidebar.markdown(f"""
<div class="sidebar-mascot">
    <img src="{MASCOT_URL}" />
</div>
""", unsafe_allow_html=True)

for p in PAGES:
    if st.sidebar.button(
        p,
        key=f"nav_{p}",
        use_container_width=True,
        type="primary" if st.session_state.page == p else "secondary"
    ):
        st.session_state.page = p
        st.rerun()

page = st.session_state.page

# =========================
# FLOATING MASCOT
# =========================

MASCOT_MESSAGES = [
    "Tracking the EvoEvo economy...",
    "Scanning agents...",
    "Monitoring network growth...",
    "Watching trending agents...",
    "Analyzing prediction markets...",
    "Calculating weekly growth...",
    "Refreshing platform metrics...",
    "Checking win streaks...",
    "Comparing this week to last...",
    "Watching for new agents..."
]

_n = len(MASCOT_MESSAGES)
_per_message_seconds = 3.2
_total_seconds = _n * _per_message_seconds
_slot_pct = 100 / _n
_fade_pct = _slot_pct * 0.12

# Built without f-string braces to avoid Python formatting ambiguity, and
# as single-line strings (no leading indentation) so Streamlit's
# markdown-to-HTML conversion never mistakes an indented line for a
# CommonMark indented code block.
_mascot_keyframes_css = (
    "<style>@keyframes mascotMsgFade{0%{opacity:0}"
    + format(_fade_pct, ".2f") + "%{opacity:1}"
    + format(_slot_pct - _fade_pct, ".2f") + "%{opacity:1}"
    + format(_slot_pct, ".2f") + "%{opacity:0}"
    + "100%{opacity:0}}</style>"
)

_ticker_spans = "".join(
    '<span style="animation:mascotMsgFade ' + str(_total_seconds) + 's infinite;'
    + 'animation-delay:-' + str(i * _per_message_seconds) + 's;">' + msg + '</span>'
    for i, msg in enumerate(MASCOT_MESSAGES)
)

# JS lives on the <img onload="..."> attribute (not a <script> tag) because
# Streamlit inserts markdown HTML via innerHTML, and browsers never execute
# <script> tags inserted that way. Built as a plain string (no f-string) so
# none of the JS braces need escaping, then flattened to one line and
# quotes swapped so it survives sitting inside an HTML attribute untouched.
_mascot_drag_js = """
(function(){
    var wrap = document.getElementById('evoevo-mascot-wrap');
    if (!wrap) return;
    if (wrap.getAttribute('data-mascot-bound') === '1') return;
    wrap.setAttribute('data-mascot-bound', '1');

    var dragging = false;
    var startX, startY, origX, origY;
    var lastX, lastY, lastT;
    var vx = 0, vy = 0;
    var animId = null;

    function getPos(e){
        if (e.touches && e.touches.length) {
            return {x: e.touches[0].clientX, y: e.touches[0].clientY};
        }
        return {x: e.clientX, y: e.clientY};
    }

    function cancelAnim(){
        if (animId) { cancelAnimationFrame(animId); animId = null; }
    }

    function onDown(e){
        cancelAnim();
        dragging = true;
        wrap.style.cursor = 'grabbing';
        var p = getPos(e);
        var rect = wrap.getBoundingClientRect();
        origX = rect.left;
        origY = rect.top;
        startX = p.x;
        startY = p.y;
        lastX = p.x;
        lastY = p.y;
        lastT = Date.now();
        wrap.style.left = origX + 'px';
        wrap.style.top = origY + 'px';
        wrap.style.right = 'auto';
        wrap.style.bottom = 'auto';
        e.preventDefault();
    }

    function onMove(e){
        if (!dragging) return;
        var p = getPos(e);
        var dx = p.x - startX;
        var dy = p.y - startY;
        wrap.style.left = (origX + dx) + 'px';
        wrap.style.top = (origY + dy) + 'px';

        var now = Date.now();
        var dt = now - lastT;
        if (dt > 0) {
            vx = (p.x - lastX) / dt;
            vy = (p.y - lastY) / dt;
        }
        lastX = p.x;
        lastY = p.y;
        lastT = now;
        e.preventDefault();
    }

    function onUp(e){
        if (!dragging) return;
        dragging = false;
        wrap.style.cursor = 'grab';
        var movedDist = Math.hypot(lastX - startX, lastY - startY);
        if (movedDist < 6) {
            wrap.classList.add('mascot-awake');
        } else {
            throwIt();
        }
    }

    function throwIt(){
        var friction = 0.95;
        function step(){
            vx *= friction;
            vy *= friction;

            var rect = wrap.getBoundingClientRect();
            var left = rect.left + vx * 16;
            var top = rect.top + vy * 16;

            var maxLeft = window.innerWidth - rect.width;
            var maxTop = window.innerHeight - rect.height;

            if (left < 0) { left = 0; vx *= -0.6; }
            if (left > maxLeft) { left = maxLeft; vx *= -0.6; }
            if (top < 0) { top = 0; vy *= -0.6; }
            if (top > maxTop) { top = maxTop; vy *= -0.6; }

            wrap.style.left = left + 'px';
            wrap.style.top = top + 'px';

            if (Math.abs(vx) > 0.02 || Math.abs(vy) > 0.02) {
                animId = requestAnimationFrame(step);
            }
        }
        animId = requestAnimationFrame(step);
    }

    wrap.addEventListener('mousedown', onDown);
    wrap.addEventListener('touchstart', onDown, {passive: false});
    document.addEventListener('mousemove', onMove);
    document.addEventListener('touchmove', onMove, {passive: false});
    document.addEventListener('mouseup', onUp);
    document.addEventListener('touchend', onUp);

    setTimeout(function(){
        wrap.classList.add('mascot-awake');
    }, 10000);
})();
""".replace("\n", " ").replace('"', "&quot;")

_mascot_html = (
    '<div id="evoevo-mascot-wrap" class="mascot-floating-wrap">'
    + '<div class="mascot-ticker">' + _ticker_spans + '</div>'
    + '<img src="' + MASCOT_URL + '" '
    + 'style="width:68px !important;height:auto !important;max-width:68px !important;" '
    + 'onload="' + _mascot_drag_js + '" />'
    + '</div>'
)

st.markdown(_mascot_keyframes_css + _mascot_html, unsafe_allow_html=True)

# =========================================
# PAGE 1 - NETWORK GROWTH (resets weekly)
# =========================================

if page == "Network Growth":

    HISTORY_URL = "https://raw.githubusercontent.com/Junedkhan121/state-of-evoevo/main/history.csv"

    history = pd.read_csv(HISTORY_URL)

    history["timestamp"] = pd.to_datetime(history["timestamp"])

    history = history.sort_values("timestamp").reset_index(drop=True)

    latest_ts = history["timestamp"].max()

    # Week runs Monday 00:00 through Sunday 23:59, anchored to the most
    # recent snapshot in the data. weekday(): Monday=0 ... Sunday=6.
    this_week_start = (
        latest_ts - pd.Timedelta(days=latest_ts.weekday())
    ).normalize()

    this_week_end = this_week_start + pd.Timedelta(days=7)

    last_week_start = this_week_start - pd.Timedelta(days=7)
    last_week_end = this_week_start

    week_df = (
        history[
            (history["timestamp"] >= this_week_start) &
            (history["timestamp"] < this_week_end)
        ]
        .sort_values("timestamp")
        .reset_index(drop=True)
    )

    last_week_df = (
        history[
            (history["timestamp"] >= last_week_start) &
            (history["timestamp"] < last_week_end)
        ]
        .sort_values("timestamp")
        .reset_index(drop=True)
    )

    week_label = (
        f"{this_week_start.strftime('%b %d')} \u2013 "
        f"{(this_week_end - pd.Timedelta(days=1)).strftime('%b %d, %Y')}"
    )

    page_header(
        "Network Growth",
        subtitle=f"Week of {week_label} \u00b7 resets every Monday"
    )

    if week_df.empty:

        st.info("No data recorded yet for this week.")

    else:

        first = week_df.iloc[0]
        latest = week_df.iloc[-1]

        elapsed_hours = (
            latest["timestamp"] - first["timestamp"]
        ).total_seconds() / 3600

        new_agents = (
            latest["agents"]
            - first["agents"]
        )

        new_memories = (
            latest["memories"]
            - first["memories"]
        )

        new_topics = (
            latest["markets"]
            - first["markets"]
        )

        new_predictions = (
            latest["opinions"]
            - first["opinions"]
        )

        st.caption(
            f"This week's growth measured over the last {elapsed_hours:.1f} hours "
            f"({first['timestamp'].strftime('%a %b %d, %I:%M %p')} \u2192 "
            f"{latest['timestamp'].strftime('%a %b %d, %I:%M %p')})"
        )

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "New Agents",
            f"{new_agents:,}"
        )

        c2.metric(
            "New Memories",
            f"{new_memories:,}"
        )

        c3.metric(
            "New Topics",
            f"{new_topics:,}"
        )

        c4.metric(
            "New Predictions",
            f"{new_predictions:,}"
        )

        st.subheader("Network Growth This Week")

        growth_df = week_df.set_index("timestamp")[
            [
                "agents",
                "memories",
                "markets",
                "opinions"
            ]
        ]

        st.line_chart(growth_df)

        # =========================
        # DAILY BREAKDOWN (this week only)
        # =========================

        st.subheader("Daily Breakdown")

        week_df["date"] = week_df["timestamp"].dt.date

        daily_last = (
            week_df
            .groupby("date")
            .last()
            .reset_index()
            .sort_values("date")
        )

        daily_last["New Agents"] = daily_last["agents"].diff()
        daily_last["New Memories"] = daily_last["memories"].diff()
        daily_last["New Topics"] = daily_last["markets"].diff()
        daily_last["New Predictions"] = daily_last["opinions"].diff()

        daily_table = daily_last[
            [
                "date",
                "agents",
                "New Agents",
                "New Memories",
                "New Topics",
                "New Predictions"
            ]
        ].rename(
            columns={
                "date": "Date",
                "agents": "Total Agents"
            }
        )

        st.dataframe(
            daily_table,
            use_container_width=True,
            hide_index=True
        )

        st.caption(
            "New * columns show growth versus the previous day's final "
            "snapshot within this week. Monday's row has no prior day in "
            "this week to compare against, so it shows blank."
        )

        st.subheader("Latest Snapshot")

        latest_df = pd.DataFrame({
            "Metric": [
                "Agents",
                "Memories",
                "Topics",
                "Predictions"
            ],
            "Value": [
                latest["agents"],
                latest["memories"],
                latest["markets"],
                latest["opinions"]
            ]
        })

        st.dataframe(
            latest_df,
            use_container_width=True,
            hide_index=True
        )

    # =========================
    # LAST WEEK'S PROGRESS
    # =========================

    st.markdown("---")

    st.subheader("Last Week's Progress")

    if last_week_df.empty:

        st.info("No data available yet for last week.")

    else:

        lw_first = last_week_df.iloc[0]
        lw_latest = last_week_df.iloc[-1]

        lw_new_agents = (
            lw_latest["agents"]
            - lw_first["agents"]
        )

        lw_new_memories = (
            lw_latest["memories"]
            - lw_first["memories"]
        )

        lw_new_topics = (
            lw_latest["markets"]
            - lw_first["markets"]
        )

        lw_new_predictions = (
            lw_latest["opinions"]
            - lw_first["opinions"]
        )

        last_week_label = (
            f"{last_week_start.strftime('%b %d')} \u2013 "
            f"{(last_week_end - pd.Timedelta(days=1)).strftime('%b %d, %Y')}"
        )

        st.caption(f"Snapshot for the week of {last_week_label}")

        l1, l2, l3, l4 = st.columns(4)

        l1.metric(
            "New Agents",
            f"{lw_new_agents:,}"
        )

        l2.metric(
            "New Memories",
            f"{lw_new_memories:,}"
        )

        l3.metric(
            "New Topics",
            f"{lw_new_topics:,}"
        )

        l4.metric(
            "New Predictions",
            f"{lw_new_predictions:,}"
        )

        st.dataframe(
            pd.DataFrame({
                "Metric": [
                    "Ending Agents",
                    "Ending Memories",
                    "Ending Topics",
                    "Ending Predictions"
                ],
                "Value": [
                    lw_latest["agents"],
                    lw_latest["memories"],
                    lw_latest["markets"],
                    lw_latest["opinions"]
                ]
            }),
            use_container_width=True,
            hide_index=True
        )

# =========================================
# PAGE 2 - REPORTS CENTER
# =========================================

elif page == "Reports Center":

    page_header(
        "Reports Center",
        subtitle="Weekly and monthly summaries, ready to share or download"
    )

    HISTORY_URL = "https://raw.githubusercontent.com/Junedkhan121/state-of-evoevo/main/history.csv"

    TREND_URL = "https://raw.githubusercontent.com/Junedkhan121/state-of-evoevo/main/trending_agents.csv"

    history = pd.read_csv(HISTORY_URL)
    trend = pd.read_csv(TREND_URL)

    history["timestamp"] = pd.to_datetime(history["timestamp"])

    history = history.sort_values("timestamp").reset_index(drop=True)

    latest_ts = history["timestamp"].max()

    leaderboard = (
        trend.groupby("name")
        .size()
        .reset_index(name="appearances")
        .sort_values(
            "appearances",
            ascending=False
        )
    )

    king = leaderboard.iloc[0]

    def growth_stats(df):

        if df.empty:
            return None

        f = df.iloc[0]
        l = df.iloc[-1]

        return {
            "first": f,
            "latest": l,
            "new_agents": l["agents"] - f["agents"],
            "new_memories": l["memories"] - f["memories"],
            "new_topics": l["markets"] - f["markets"],
            "new_predictions": l["opinions"] - f["opinions"]
        }

    def render_totals_block(stats, show_pct):

        if stats is None:
            st.info("No data available yet.")
            return

        latest = stats["latest"]
        first = stats["first"]

        if show_pct:

            agent_pct = (
                (stats["new_agents"] / first["agents"]) * 100
                if first["agents"] else 0
            )

            memory_pct = (
                (stats["new_memories"] / first["memories"]) * 100
                if first["memories"] else 0
            )

            topic_pct = (
                (stats["new_topics"] / first["markets"]) * 100
                if first["markets"] else 0
            )

            prediction_pct = (
                (stats["new_predictions"] / first["opinions"]) * 100
                if first["opinions"] else 0
            )

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Total Agents",
            f"{latest['agents']:,}",
            delta=f"{agent_pct:.2f}%" if show_pct else None
        )

        c2.metric(
            "Total Memories",
            f"{latest['memories']:,}",
            delta=f"{memory_pct:.2f}%" if show_pct else None
        )

        c3.metric(
            "Total Topics",
            f"{latest['markets']:,}",
            delta=f"{topic_pct:.2f}%" if show_pct else None
        )

        c4.metric(
            "Total Predictions",
            f"{latest['opinions']:,}",
            delta=f"{prediction_pct:.2f}%" if show_pct else None
        )

    # =========================
    # WEEK BOUNDARIES
    # =========================

    this_week_start = (
        latest_ts - pd.Timedelta(days=latest_ts.weekday())
    ).normalize()

    this_week_end = this_week_start + pd.Timedelta(days=7)

    last_week_start = this_week_start - pd.Timedelta(days=7)
    last_week_end = this_week_start

    week_df = (
        history[
            (history["timestamp"] >= this_week_start) &
            (history["timestamp"] < this_week_end)
        ]
        .sort_values("timestamp")
        .reset_index(drop=True)
    )

    last_week_df = (
        history[
            (history["timestamp"] >= last_week_start) &
            (history["timestamp"] < last_week_end)
        ]
        .sort_values("timestamp")
        .reset_index(drop=True)
    )

    week_stats = growth_stats(week_df)
    last_week_stats = growth_stats(last_week_df)

    # =========================
    # MONTH BOUNDARIES
    # =========================

    this_month_start = latest_ts.replace(
        day=1, hour=0, minute=0, second=0, microsecond=0
    )

    if this_month_start.month == 12:
        next_month_start = this_month_start.replace(
            year=this_month_start.year + 1, month=1
        )
    else:
        next_month_start = this_month_start.replace(
            month=this_month_start.month + 1
        )

    last_month_end = this_month_start

    if this_month_start.month == 1:
        last_month_start = this_month_start.replace(
            year=this_month_start.year - 1, month=12
        )
    else:
        last_month_start = this_month_start.replace(
            month=this_month_start.month - 1
        )

    month_df = (
        history[
            (history["timestamp"] >= this_month_start) &
            (history["timestamp"] < next_month_start)
        ]
        .sort_values("timestamp")
        .reset_index(drop=True)
    )

    last_month_df = (
        history[
            (history["timestamp"] >= last_month_start) &
            (history["timestamp"] < last_month_end)
        ]
        .sort_values("timestamp")
        .reset_index(drop=True)
    )

    month_stats = growth_stats(month_df)
    last_month_stats = growth_stats(last_month_df)

    # =========================
    # OVERALL PLATFORM TOTALS (all-time, no percentage)
    # =========================

    all_time_stats = growth_stats(history)

    st.subheader("Overall Platform Totals")

    st.caption("All-time totals as of the latest snapshot, across all tracked history.")

    render_totals_block(all_time_stats, show_pct=False)

    st.markdown("---")

    tab_weekly, tab_monthly = st.tabs(["Weekly", "Monthly"])

    # =========================================
    # PART 1 - WEEKLY (resets every Monday)
    # =========================================

    with tab_weekly:

        week_label = (
            f"{this_week_start.strftime('%b %d')} \u2013 "
            f"{(this_week_end - pd.Timedelta(days=1)).strftime('%b %d, %Y')}"
        )

        st.subheader("Overall Platform Totals")

        st.caption(
            f"Week of {week_label} \u00b7 totals and growth % reset every Monday"
        )

        render_totals_block(week_stats, show_pct=True)

        st.markdown("---")

        st.subheader("This Week")

        st.caption(f"Week of {week_label} \u00b7 resets every Monday")

        if week_stats is None:

            st.info("No data recorded yet for this week.")

        else:

            c1, c2, c3, c4 = st.columns(4)

            c1.metric("New Agents", f"{week_stats['new_agents']:,}")
            c2.metric("New Memories", f"{week_stats['new_memories']:,}")
            c3.metric("New Topics", f"{week_stats['new_topics']:,}")
            c4.metric("New Predictions", f"{week_stats['new_predictions']:,}")

            weekly_report = f"""
STATE OF EVOEVO - WEEKLY REPORT
Week of {week_label}

New Agents: {week_stats['new_agents']:,}
New Memories: {week_stats['new_memories']:,}
New Topics: {week_stats['new_topics']:,}
New Predictions: {week_stats['new_predictions']:,}

Top Trending Agent: {king['name']}
Appearances: {king['appearances']}
"""

            st.text_area(
                "This Week's Report",
                weekly_report,
                height=220,
                key="weekly_report_current"
            )

            st.download_button(
                "Download This Week's Report",
                weekly_report,
                file_name=f"evoevo_week_{this_week_start.date()}.txt",
                key="dl_week_current"
            )

        st.markdown("---")

        st.subheader("Last Week's Snapshot")

        if last_week_stats is None:

            st.info("No data available yet for last week.")

        else:

            last_week_label = (
                f"{last_week_start.strftime('%b %d')} \u2013 "
                f"{(last_week_end - pd.Timedelta(days=1)).strftime('%b %d, %Y')}"
            )

            st.caption(f"Snapshot taken for the week of {last_week_label}")

            l1, l2, l3, l4 = st.columns(4)

            l1.metric("New Agents", f"{last_week_stats['new_agents']:,}")
            l2.metric("New Memories", f"{last_week_stats['new_memories']:,}")
            l3.metric("New Topics", f"{last_week_stats['new_topics']:,}")
            l4.metric(
                "New Predictions",
                f"{last_week_stats['new_predictions']:,}"
            )

            last_week_report = f"""
STATE OF EVOEVO - WEEKLY SNAPSHOT
Week of {last_week_label}

New Agents: {last_week_stats['new_agents']:,}
New Memories: {last_week_stats['new_memories']:,}
New Topics: {last_week_stats['new_topics']:,}
New Predictions: {last_week_stats['new_predictions']:,}

Ending Totals:
Agents: {last_week_stats['latest']['agents']:,}
Memories: {last_week_stats['latest']['memories']:,}
Topics: {last_week_stats['latest']['markets']:,}
Predictions: {last_week_stats['latest']['opinions']:,}
"""

            st.download_button(
                "Download Last Week's Snapshot",
                last_week_report,
                file_name=f"evoevo_week_{last_week_start.date()}.txt",
                key="dl_week_last"
            )

    # =========================================
    # PART 2 - MONTHLY (accumulates until month change)
    # =========================================

    with tab_monthly:

        month_label = this_month_start.strftime("%B %Y")

        st.subheader("Overall Platform Totals")

        st.caption(
            f"{month_label} \u00b7 totals and growth % accumulate through "
            "the month and reset when the month changes"
        )

        render_totals_block(month_stats, show_pct=True)

        st.markdown("---")

        st.subheader("This Month (Month-to-Date)")

        st.caption(
            f"{month_label} \u00b7 keeps accumulating and does not reset "
            "until the month changes"
        )

        if month_stats is None:

            st.info("No data recorded yet for this month.")

        else:

            c1, c2, c3, c4 = st.columns(4)

            c1.metric("New Agents", f"{month_stats['new_agents']:,}")
            c2.metric("New Memories", f"{month_stats['new_memories']:,}")
            c3.metric("New Topics", f"{month_stats['new_topics']:,}")
            c4.metric("New Predictions", f"{month_stats['new_predictions']:,}")

            monthly_report = f"""
STATE OF EVOEVO - MONTHLY REPORT
{month_label} (month-to-date)

Agents Added: {month_stats['new_agents']:,}
Memories Added: {month_stats['new_memories']:,}
Topics Added: {month_stats['new_topics']:,}
Predictions Added: {month_stats['new_predictions']:,}

Top Trending Agent: {king['name']}
Appearances: {king['appearances']}
"""

            st.text_area(
                "Monthly Report (Month-to-Date)",
                monthly_report,
                height=250,
                key="monthly_report_current"
            )

            st.download_button(
                "Download This Month's Report",
                monthly_report,
                file_name=f"evoevo_month_{this_month_start.strftime('%Y-%m')}.txt",
                key="dl_month_current"
            )

        st.markdown("---")

        st.subheader("Monthly Breakdown")

        history_m = history.copy()

        history_m["month"] = history_m["timestamp"].dt.to_period("M")

        monthly_last = (
            history_m
            .groupby("month")
            .last()
            .reset_index()
            .sort_values("month")
        )

        monthly_last["New Agents"] = monthly_last["agents"].diff()
        monthly_last["New Memories"] = monthly_last["memories"].diff()
        monthly_last["New Topics"] = monthly_last["markets"].diff()
        monthly_last["New Predictions"] = monthly_last["opinions"].diff()

        monthly_table = monthly_last[
            [
                "month",
                "agents",
                "New Agents",
                "New Memories",
                "New Topics",
                "New Predictions"
            ]
        ].rename(
            columns={
                "month": "Month",
                "agents": "Total Agents"
            }
        )

        monthly_table["Month"] = monthly_table["Month"].astype(str)

        st.dataframe(
            monthly_table,
            use_container_width=True,
            hide_index=True
        )

        st.caption(
            "New * columns show growth versus the previous month's final "
            "snapshot. The first tracked month has no prior month to "
            "compare against, so it shows blank."
        )

        st.markdown("---")

        st.subheader("Last Month's Snapshot")

        if last_month_stats is None:

            st.info("No data available yet for last month.")

        else:

            last_month_label = last_month_start.strftime("%B %Y")

            st.caption(f"Snapshot stored for {last_month_label}")

            m1, m2, m3, m4 = st.columns(4)

            m1.metric("New Agents", f"{last_month_stats['new_agents']:,}")
            m2.metric("New Memories", f"{last_month_stats['new_memories']:,}")
            m3.metric("New Topics", f"{last_month_stats['new_topics']:,}")
            m4.metric(
                "New Predictions",
                f"{last_month_stats['new_predictions']:,}"
            )

            last_month_report = f"""
STATE OF EVOEVO - MONTHLY SNAPSHOT
{last_month_label}

Agents Added: {last_month_stats['new_agents']:,}
Memories Added: {last_month_stats['new_memories']:,}
Topics Added: {last_month_stats['new_topics']:,}
Predictions Added: {last_month_stats['new_predictions']:,}

Ending Totals:
Agents: {last_month_stats['latest']['agents']:,}
Memories: {last_month_stats['latest']['memories']:,}
Topics: {last_month_stats['latest']['markets']:,}
Predictions: {last_month_stats['latest']['opinions']:,}
"""

            st.download_button(
                "Download Last Month's Snapshot",
                last_month_report,
                file_name=f"evoevo_month_{last_month_start.strftime('%Y-%m')}.txt",
                key="dl_month_last"
            )

elif page == "Network Insights":

    HISTORY_URL = "https://raw.githubusercontent.com/Junedkhan121/state-of-evoevo/main/history.csv"

    history = pd.read_csv(HISTORY_URL)

    history["timestamp"] = pd.to_datetime(history["timestamp"])

    history = history.sort_values("timestamp").reset_index(drop=True)

    latest = history.iloc[-1]

    page_header(
        "Network Insights",
        subtitle="Token efficiency trends and all-time growth records"
    )

    # =========================================
    # PART 1 - TOKEN & EFFICIENCY INSIGHTS
    # =========================================

    st.subheader("Token & Efficiency Insights")

    tokens_per_agent = (
        latest["tokens"] / latest["agents"]
        if latest["agents"] else 0
    )

    tokens_per_prediction = (
        latest["tokens"] / latest["opinions"]
        if latest["opinions"] else 0
    )

    memories_per_agent = (
        latest["memories"] / latest["agents"]
        if latest["agents"] else 0
    )

    predictions_per_market = (
        latest["opinions"] / latest["markets"]
        if latest["markets"] else 0
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Total LLM Tokens",
        f"{latest['tokens']:,}"
    )

    c2.metric(
        "Tokens per Agent",
        f"{tokens_per_agent:,.0f}"
    )

    c3.metric(
        "Tokens per Prediction",
        f"{tokens_per_prediction:,.0f}"
    )

    c4.metric(
        "Memories per Agent",
        f"{memories_per_agent:,.2f}"
    )

    st.caption(
        "Efficiency ratios based on the latest snapshot \u2014 how much "
        "token and memory activity each agent or prediction represents "
        "right now."
    )

    st.subheader("Token Consumption Over Time")

    st.line_chart(
        history.set_index("timestamp")["tokens"]
    )

    st.subheader("Efficiency Trend: Tokens per Prediction")

    eff_df = history.copy()

    eff_df["tokens_per_prediction"] = (
        eff_df["tokens"] / eff_df["opinions"].replace(0, pd.NA)
    )

    st.line_chart(
        eff_df.set_index("timestamp")["tokens_per_prediction"]
    )

    st.caption(
        "A falling line means predictions are getting cheaper, in tokens, "
        "to produce as the network scales. A rising line means the "
        "opposite \u2014 each prediction is costing more tokens over time."
    )

    # =========================================
    # PART 2 - GROWTH RECORDS / MILESTONES
    # =========================================

    st.markdown("---")

    st.subheader("Growth Records")

    st.caption(
        "The single biggest jumps ever recorded in one day, pulled from "
        "every daily snapshot in tracked history."
    )

    daily = history.copy()

    daily["date"] = daily["timestamp"].dt.date

    daily_last = (
        daily
        .groupby("date")
        .last()
        .reset_index()
        .sort_values("date")
    )

    daily_last["agents_diff"] = daily_last["agents"].diff()
    daily_last["memories_diff"] = daily_last["memories"].diff()
    daily_last["opinions_diff"] = daily_last["opinions"].diff()

    if daily_last["agents_diff"].notna().any():

        best_agent_day = daily_last.loc[daily_last["agents_diff"].idxmax()]
        best_memory_day = daily_last.loc[daily_last["memories_diff"].idxmax()]
        best_prediction_day = daily_last.loc[daily_last["opinions_diff"].idxmax()]

        r1, r2, r3 = st.columns(3)

        r1.metric(
            "Biggest Single-Day Agent Growth",
            f"{int(best_agent_day['agents_diff']):,}",
            best_agent_day["date"].strftime("%b %d, %Y")
        )

        r2.metric(
            "Biggest Single-Day Memory Growth",
            f"{int(best_memory_day['memories_diff']):,}",
            best_memory_day["date"].strftime("%b %d, %Y")
        )

        r3.metric(
            "Biggest Single-Day Prediction Growth",
            f"{int(best_prediction_day['opinions_diff']):,}",
            best_prediction_day["date"].strftime("%b %d, %Y")
        )

    else:

        st.info(
            "Not enough daily history yet to identify single-day records. "
            "Check back after a few days of tracking."
        )

    st.markdown("---")

    st.subheader("Milestone Timeline")

    st.caption(
        "Moments the network crossed a new round-number threshold for "
        "each metric."
    )

    def pick_step(value):

        if value <= 0:
            return 1

        digits = len(str(int(value)))

        return 10 ** max(digits - 2, 0)

    def milestone_crossings(df, column, label):

        step = pick_step(df[column].max())

        crossed = []
        last_hit = 0

        for _, row in df.iterrows():

            val = row[column]
            threshold = (val // step) * step

            if threshold > last_hit and threshold > 0:

                crossed.append({
                    "Metric": label,
                    "Threshold": int(threshold),
                    "Reached On": row["timestamp"]
                })

                last_hit = threshold

        return crossed

    all_milestones = []
    all_milestones += milestone_crossings(history, "agents", "Agents")
    all_milestones += milestone_crossings(history, "memories", "Memories")
    all_milestones += milestone_crossings(history, "opinions", "Predictions")
    all_milestones += milestone_crossings(history, "markets", "Markets")

    milestone_df = pd.DataFrame(all_milestones)

    if milestone_df.empty:

        st.info("No milestone crossings recorded yet.")

    else:

        milestone_df = milestone_df.sort_values(
            "Reached On",
            ascending=False
        )

        milestone_df["Reached On"] = milestone_df["Reached On"].dt.strftime(
            "%b %d, %Y %I:%M %p"
        )

        milestone_df["Threshold"] = milestone_df["Threshold"].apply(
            lambda x: f"{x:,}"
        )

        st.dataframe(
            milestone_df,
            use_container_width=True,
            hide_index=True
        )
