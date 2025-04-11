import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo
import time

# ---------- Page config ----------
st.set_page_config(
    page_title="Brigid Countdown",
    page_icon="⏳",
    layout="centered",
)

# ---------- Custom CSS ----------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        background: radial-gradient(circle at top left, #ffecd2 0%, #fcb69f 100%);
    }
    .title {
        font-size: 3rem;
        font-weight: 600;
        color: #fff;
        text-align: center;
        margin-bottom: 0.25rem;
    }
    .subtitle {
        font-size: 1.1rem;
        text-align: center;
        margin-bottom: 2rem;
        color: #fff;
    }
    /* countdown boxes */
    .countbox {
        display: flex;
        justify-content: center;
        gap: 1.5rem;
        flex-wrap: wrap;
    }
    .countunit {
        background: rgba(255,255,255,0.20);
        backdrop-filter: blur(12px);
        border-radius: 12px;
        padding: 1.1rem 1.6rem;
        min-width: 95px;
        text-align: center;
        color: #fff;
    }
    .countunit h1 {
        margin: 0;
        font-size: 2.8rem;
        line-height: 1;
    }
    .countunit span {
        font-size: 0.9rem;
        letter-spacing: 1px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Header ----------
st.markdown('<div class="title">⏳ BRIGID COUNTDOWN ⏳</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Time left until Friday, April 11 at 12:00 PM EST</div>',
    unsafe_allow_html=True,
)

# ---------- Helper ----------
def next_april_11_noon_eastern() -> datetime:
    eastern = ZoneInfo("America/New_York")
    now = datetime.now(eastern)
    target = datetime(now.year, 4, 11, 10, 30, 0, tzinfo=eastern)
    if now >= target:  # if we’ve passed it this year, jump to next year
        target = target.replace(year=now.year + 1)
    return target

target_dt = next_april_11_noon_eastern()
placeholder = st.empty()

# ---------- Live countdown loop ----------
while True:
    now = datetime.now(ZoneInfo("America/New_York"))
    remaining = target_dt - now

    if remaining.total_seconds() <= 0:
        st.balloons()
        st.markdown('<div class="title">🎉 It’s time! 🎉</div>', unsafe_allow_html=True)
        break

    # break down the delta
    days, rem = divmod(int(remaining.total_seconds()), 86_400)
    hours, rem = divmod(rem, 3_600)
    minutes, seconds = divmod(rem, 60)

    with placeholder.container():
        st.markdown(
            f'''
            <div class="countbox">
                <div class="countunit"><h1>{days}</h1><span>Days</span></div>
                <div class="countunit"><h1>{hours:02d}</h1><span>Hours</span></div>
                <div class="countunit"><h1>{minutes:02d}</h1><span>Minutes</span></div>
                <div class="countunit"><h1>{seconds:02d}</h1><span>Seconds</span></div>
            </div>
            ''',
            unsafe_allow_html=True,
        )

    time.sleep(1)
