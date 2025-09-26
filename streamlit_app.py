import streamlit as st

# -------------------------------
# App Config
# -------------------------------
st.set_page_config(page_title="Yushan Hub", layout="wide")

# -------------------------------
# Whitelist of allowed emails
# -------------------------------
ALLOWED_EMAILS = [
    "wayne.wang1@pernod-ricard.com",
    # Add more emails here
]

# -------------------------------
# Header Section with Pernod Ricard logo
# -------------------------------
st.markdown(
    """
    <div style="background-color:#002B49;padding:30px;border-radius:10px;margin-bottom:25px;
                text-align:center;">
        <img src="assets/pr_logo.svg" width="100" style="margin-bottom:15px;">
        <h1 style="color:white;font-family:sans-serif;">Yushan Hub 2.0</h1>
        <p style="color:#7AC9E0;font-size:18px;">
            Pernod Ricard Taiwan • Your central access to dashboards and apps
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# Login Section
# -------------------------------
st.markdown(
    """
    <div style="background-color:#E8E2D6;padding:25px;border-radius:15px;
                text-align:center;width:60%;margin:auto;margin-bottom:30px;">
        <h3 style="color:#002B49;">🔒 Login</h3>
    </div>
    """,
    unsafe_allow_html=True
)

email = st.text_input("Enter your Pernod Ricard email")

if st.button("Login"):
    if email.strip().lower() in [e.lower() for e in ALLOWED_EMAILS]:
        st.success(f"✅ Welcome {email} 👋")
        st.subheader("Portal")

        # -------------------------------
        # Portal Cards
        # -------------------------------
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(
                """
                <div style="background-color:#E8E2D6;padding:25px;border-radius:15px;text-align:center;">
                    <h3 style="color:#002B49;">📊 Power BI</h3>
                    <p style="color:#333333;">Trusted performance dashboards</p>
                    <a href="https://app.powerbi.com/" target="_blank">
                        <button style="padding:10px 20px;border:none;border-radius:5px;
                                       background:#009DDC;color:white;cursor:pointer;">Enter</button>
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                """
                <div style="background-color:#E8E2D6;padding:25px;border-radius:15px;text-align:center;">
                    <h3 style="color:#002B49;">📈 R Shiny</h3>
                    <p style="color:#333333;">Interactive statistical apps</p>
                    <a href="http://your-shinyproxy-url/app1" target="_blank">
                        <button style="padding:10px 20px;border:none;border-radius:5px;
                                       background:#7AC9E0;color:#002B49;cursor:pointer;">Enter</button>
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col3:
            st.markdown(
                """
                <div style="background-color:#E8E2D6;padding:25px;border-radius:15px;text-align:center;">
                    <h3 style="color:#002B49;">🔮 Future Tools</h3>
                    <p style="color:#333333;">Coming soon...</p>
                    <button style="padding:10px 20px;border:none;border-radius:5px;
                                   background:#CCCCCC;color:#333333;" disabled>Coming Soon</button>
                </div>
                """,
                unsafe_allow_html=True
            )

        if st.button("Logout"):
            st.experimental_rerun()

    else:
        st.error("❌ Access denied. You are not in the whitelist.")
