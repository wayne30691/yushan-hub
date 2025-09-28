import streamlit as st
import base64

# -------------------------------
# App Config
# -------------------------------
st.set_page_config(page_title="YuShan Hub", layout="wide")

# -------------------------------
# Whitelist of allowed emails
# -------------------------------
ALLOWED_EMAILS = [
    "",
    # Add more emails here
]

# -------------------------------
# Load Pernod Ricard Logo (base64 inline)
# -------------------------------
with open("assets/logo-white-50.png", "rb") as f:
    data = base64.b64encode(f.read()).decode("utf-8")

logo_url = f"data:image/png;base64,{data}"

# -------------------------------
# Header Section with Logo + Title
# -------------------------------
st.markdown(
    f"""
    <div style="background-color:#002B49;padding:60px 20px;border-radius:10px;margin-bottom:30px;
                text-align:center;">
        <img src="{logo_url}" width="120" style="margin-bottom:20px;">
        <h1 style="color:white;font-family:sans-serif;font-size:50px;font-weight:bold;">
            YuShan Hub
        </h1>
        <p style="color:#FFFFFF;font-size:20px;">
            Pernod Ricard Taiwan • Data & Insights Portal
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# Portal Section
# -------------------------------
st.markdown("### 🚀 Available Tools")

col1, col2 = st.columns(2)

# --- Power BI (always accessible) ---
with col1:
    st.markdown(
        """
        <div style="background-color:#E8E2D6;padding:40px;border-radius:15px;text-align:center;cursor:pointer;"
             onclick="window.open('https://app.powerbi.com/', '_blank')">
            <h2 style="color:#002B49;">📊 Power BI</h2>
            <p style="color:#333333;">Trusted performance dashboards</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- R Shiny (requires login) ---
with col2:
    st.markdown(
        """
        <div style="background-color:#E8E2D6;padding:40px;border-radius:15px;text-align:center;">
            <h2 style="color:#002B49;">📈 R Shiny Apps</h2>
            <p style="color:#333333;">Interactive statistical apps (login required)</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    email = st.text_input("Enter your Pernod Ricard email to access R Shiny")

    if st.button("Login to R Shiny"):
        if email.strip().lower() in [e.lower() for e in ALLOWED_EMAILS]:
            st.success(f"✅ Welcome {email} 👋 Redirecting to R Shiny...")
            st.markdown(
                """
                <meta http-equiv="refresh" content="0; url=http://your-shinyproxy-url/app1">
                """,
                unsafe_allow_html=True
            )
        else:
            st.error("❌ Access denied. You are not in the whitelist.")
