import streamlit as st

# -------------------------------
# App Config
# -------------------------------
st.set_page_config(page_title="YuShan Hub", layout="wide")

# -------------------------------
# Whitelist of allowed emails
# -------------------------------
ALLOWED_EMAILS = [
    "wayne.wang1@pernod-ricard.com",
    # Add more emails here
]

# -------------------------------
# Load Pernod Ricard Logo (inline SVG)
# -------------------------------
with open("assets/pr_logo.svg", "r", encoding="utf-8") as f:
    logo_svg = f.read()

# -------------------------------
# Header Section with Logo Centered
# -------------------------------
st.markdown(
    f"""
    <div style="background-color:#002B49;padding:30px;border-radius:10px;margin-bottom:25px;
                text-align:center;">
        <div style="margin-bottom:15px;">{logo_svg}</div>
        <h1 style="color:white;font-family:sans-serif;">YuShan Hub</h1>
        <p style="color:#7AC9E0;font-size:18px;">
            Pernod Ricard Taiwan • Your central access to dashboards and apps
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

# --- Power BI Card (no login) ---
with col1:
    st.markdown(
        """
        <div style="background-color:#E8E2D6;padding:25px;border-radius:15px;text-align:center;cursor:pointer;"
             onclick="window.open('https://app.powerbi.com/', '_blank')">
            <h3 style="color:#002B49;">📊 Power BI</h3>
            <p style="color:#333333;">Trusted performance dashboards</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- R Shiny Card (login required) ---
with col2:
    st.markdown("### 📈 R Shiny Apps")
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
