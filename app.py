import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import streamlit.components.v1 as components # Ads ke liye zaroori

# --- 1. STARTUP CONFIGURATION ---
st.set_page_config(page_title="SMC FLUX PRO | Trade & Earn", layout="wide")

# --- 2. THE REVENUE-FOCUSED UI (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #0b0e11; color: #eaecef; }
    
    /* Ad Slot Styling */
    .ad-slot-horizontal {
        background: #161a1e;
        border: 1px dashed #444;
        color: #707a8a;
        text-align: center;
        padding: 10px;
        margin: 10px 0;
        border-radius: 8px;
        font-size: 12px;
    }
    
    .ad-slot-sidebar {
        background: #1e2329;
        border: 1px solid #2b2f36;
        padding: 60px 10px;
        text-align: center;
        border-radius: 10px;
        color: #555;
        margin-top: 20px;
    }

    /* Professional Elements */
    .header-box { background: #161a1e; padding: 20px; border-radius: 15px; border-bottom: 2px solid #02d39a; }
    .news-card { background: #11151a; padding: 15px; border-radius: 10px; border-left: 4px solid #02d39a; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. TOP AD BANNER (Leaderboard) ---
st.markdown('<div class="ad-slot-horizontal">ADVERTISEMENT: Top Leaderboard (Google AdSense 728x90)</div>', unsafe_allow_html=True)

# --- 4. HEADER ---
with st.container():
    st.markdown("""
    <div class="header-box">
        <h1 style='margin:0; color:#02d39a;'>🏛️ SMC FLUX PRO</h1>
        <p style='color:#707a8a;'>The Institutional Intelligence Terminal</p>
    </div>
    """, unsafe_allow_html=True)

# --- 5. SIDEBAR (With Ad Support) ---
st.sidebar.title("🛠️ TERMINAL")
symbol = st.sidebar.text_input("Search Asset", "BTC-USD").upper()
timeframe = st.sidebar.selectbox("Timeframe", ("15m", "1h", "1d"), index=2)

# Sidebar Affiliate Ad
st.sidebar.markdown("---")
st.sidebar.markdown("### 💎 PREMIUM SPONSOR")
st.sidebar.info("🚀 Open an account with our Partner Broker and get 0% Brokerage! [Click Here]")

# Sidebar Google Ad
st.sidebar.markdown('<div class="ad-slot-sidebar">AD SLOT: Vertical Banner (160x600)</div>', unsafe_allow_html=True)

# --- 6. MAIN CONTENT AREA ---
try:
    ticker = yf.Ticker(symbol)
    df = ticker.history(period="6mo", interval=timeframe)
    
    if not df.empty:
        col_left, col_right = st.columns([3, 1])
        
        with col_left:
            # Main Chart
            fig = go.Figure(data=[go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'],
                                                increasing_line_color='#02d39a', decreasing_line_color='#f6465d')])
            fig.update_layout(template="plotly_dark", height=500, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', xaxis_rangeslider_visible=False)
            st.plotly_chart(fig, use_container_width=True)
            
            # Mid-Page Ad (High CTR)
            st.markdown('<div class="ad-slot-horizontal">ADVERTISEMENT: Mid-Content (In-Feed Ad)</div>', unsafe_allow_html=True)
            
            # News Section
            st.markdown("### 📰 LATEST MARKET INTELLIGENCE")
            for n in ticker.news[:4]:
                st.markdown(f"""
                <div class="news-card">
                    <small>{n['publisher']}</small><br>
                    <a href="{n['link']}" style='color:white; text-decoration:none; font-weight:bold;'>{n['title']}</a>
                </div>
                """, unsafe_allow_html=True)
        
        with col_right:
            # FII/DII Sentiment Card
            st.markdown("### 🐋 BIG BOY MOVES")
            st.success("FII: NET BUYERS")
            st.error("DII: NET SELLERS")
            
            st.markdown("---")
            # Fundamental Stats
            st.markdown("### 📊 FUNDAMENTALS")
            st.metric("LTP", f"{df['Close'].iloc[-1]:,.2f}")
            st.metric("PROFIT MARGIN", f"{ticker.info.get('profitMargins', 0)*100:.2f}%")
            
            # Bottom Right Ad
            st.markdown('<div class="ad-slot-sidebar" style="padding:20px;">AD SLOT: Square (250x250)</div>', unsafe_allow_html=True)

except Exception as e:
    st.error("Asset not found. Please use valid symbols like AAPL or BTC-USD.")

# --- 7. FOOTER AD ---
st.markdown('<div class="ad-slot-horizontal">ADVERTISEMENT: Bottom Banner</div>', unsafe_allow_html=True)
