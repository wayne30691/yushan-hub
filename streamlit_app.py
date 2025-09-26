import streamlit as st

st.set_page_config(page_title="YuShan Hub", layout="wide")

# --- Whitelist of allowed emails ---
ALLOWED_EMAILS = [
    "wayne.wang1@pernod-ricard.com",
    # Add more emails here
]

# --- Hero Banner (replace with your hosted image URL if needed) ---
banner_url = "https://www.pernod-ricard.com/themes/custom/pernodricard_theme/images/hero-home.jpg"

st.markdown(
    f"""
    <div style="position:relative;text-align:center;color:white;margin-bottom:30px;">
        <img src="{banner_url}" style="width:100%;border-radius:10px;opacity:0.85;">
        <div style="position:absolute;top:50%;left:50%;transform:translate(-50%, -50%);">
            <h1 style="font-size:48px;font-family:sans-serif;font-weight:bold;">
                YuShan Hub
            </h1>
            <p style="font-size:20px;">Pernod Ricard Taiwan • Data & Insights Portal</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

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
