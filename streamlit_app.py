import streamlit as st

# Set the title and page icon
st.set_page_config(page_title="TeleHealth-Ease App", page_icon="🌡️")

# Add custom CSS to change the background color to blue
st.markdown(
    """
    <style>
    body {
        background-color: #0074e4; /* Blue color */
    }
    .divider {
        border-left: 1px solid black; /* Black vertical line */
        height: auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add a title
st.title("Welcome to TeleHealth-Ease")

# Add an introduction for patients
st.write("Empowering You with Easy Access to Quality Healthcare Services")

# Create a sidebar for buttons with a divider
with st.sidebar:
    st.subheader("Select a Feature:")
    selected_feature = st.selectbox("", [
        "User Registration & Login",
        "Profile Management",
        "Appointment Scheduling",
        "Medical Records Access",
        "Symptom Checker",
    ])
    if selected_feature == "User Registration & Login":
        st.subheader("User Registration / Login Area:")
        username = st.text_input("Username", "")
        password = st.text_input("Password", "", type="password")
        registration_button = st.button("Register")
        login_button = st.button("Login")
        if registration_button:
            st.success("Registration Successful!")
        if login_button:
            st.success("Login Successful!")

# Add an empty space with a black vertical line
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Display feature details or registration/login area
if selected_feature:
    st.write(f"This is where the {selected_feature} details will appear.")

