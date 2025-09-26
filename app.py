import streamlit as st

st.set_page_config(page_title="Yushan Hub 2.0", layout="wide")

# --- Whitelist of allowed emails ---
ALLOWED_EMAILS = [
    "wayne.wang1@pernod-ricard.com",
    # You can add more emails here, e.g.:
    # "alice.chen@pernod-ricard.com",
    # "bob.lin@pernod-ricard.com",
]

# --- Simple login page ---
st.title("Yushan Hub 2.0")
st.markdown("### 🔒 Please enter your email to login")

email = st.text_input("Email")

if st.button("Login"):
    if email.strip().lower() in ALLOWED_EMAILS:
        st.success(f"✅ Welcome {email} 👋")
        st.subheader("Portal")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("### 📊 Power BI Dashboards")
            st.link_button("Enter", "https://app.powerbi.com/")

        with col2:
            st.markdown("### 📈 R Shiny Apps")
            st.link_button("Enter", "http://your-shinyproxy-url/app1")

        with col3:
            st.markdown("### 🚀 Future Tools")
            st.link_button("Coming Soon", "#")

        if st.button("Logout"):
            st.experimental_rerun()

    else:
        st.error("❌ Access denied. You are not in the whitelist.")
