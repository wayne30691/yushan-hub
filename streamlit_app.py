import streamlit as st

st.set_page_config(page_title="Yushan Hub 2.0", layout="wide")

# --- Whitelist of allowed emails ---
ALLOWED_EMAILS = [
    "wayne.wang1@pernod-ricard.com",
    # Add more emails here
]

# --- Header Banner ---
st.markdown(
    """
    <div style="background-color:#0E1117;padding:20px;border-radius:10px;margin-bottom:20px;">
        <h1 style="color:white;text-align:center;">🌐 Yushan Hub 2.0</h1>
        <p style="color:lightgray;text-align:center;">Your central portal for dashboards and apps</p>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Login Box ---
email = st.text_input("Enter your Pernod Ricard email")

if st.button("Login"):
    if email.strip().lower() in [e.lower() for e in ALLOWED_EMAILS]:
        st.success(f"✅ Welcome {email} 👋")

        # --- Portal Section ---
        st.markdown("### 🚀 Available Tools")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(
                """
                <div style="background-color:#1E1E1E;padding:20px;border-radius:15px;text-align:center;">
                    <h3 style="color:#4CAF50;">📊 Power BI</h3>
                    <p style="color:gray;">Trusted performance dashboards</p>
                    <a href="https://app.powerbi.com/" target="_blank">
                        <button style="padding:10px 20px;border:none;border-radius:5px;background:#4CAF50;color:white;cursor:pointer;">Enter</button>
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                """
                <div style="background-color:#1E1E1E;padding:20px;border-radius:15px;text-align:center;">
                    <h3 style="color:#2196F3;">📈 R Shiny</h3>
                    <p style="color:gray;">Interactive statistical apps</p>
                    <a href="http://your-shinyproxy-url/app1" target="_blank">
                        <button style="padding:10px 20px;border:none;border-radius:5px;background:#2196F3;color:white;cursor:pointer;">Enter</button>
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col3:
            st.markdown(
                """
                <div style="background-color:#1E1E1E;padding:20px;border-radius:15px;text-align:center;">
                    <h3 style="color:#FF9800;">🔮 Future Tools</h3>
                    <p style="color:gray;">Coming soon...</p>
                    <button style="padding:10px 20px;border:none;border-radius:5px;background:#FF9800;color:white;cursor:pointer;" disabled>Coming Soon</button>
                </div>
                """,
                unsafe_allow_html=True
            )

        if st.button("Logout"):
            st.experimental_rerun()

    else:
        st.error("❌ Access denied. You are not in the whitelist.")
