import streamlit as st

def registered_page():
    st.markdown("""
    <style>
        .registered-container {
            max-width: 600px;
            padding: 20px;
            margin: 100px auto;
            background-color: #f9f9f9;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
            font-family: Arial, sans-serif;
        }
        h2 {
            margin-bottom: 30px;
            color: #333;
            font-size: 36px;
            font-weight: bold;
        }
        p {
            margin-bottom: 20px;
            color: #555;
            font-size: 18px;
        }
        .message {
            font-style: italic;
            color: #777;
        }
        .message strong {
            color: #000;
            font-weight: bold;
        }
        .test-link a {
            text-decoration: none;
            color: #c88ea7;
            font-weight: bold;
        }
        .test-link a:hover {
            color: #b3788b;
        }
        .button-container {
            display: flex;
            justify-content: center;
        }
        .btn {
            background-color: #c88ea7;
            color: #fff;
            padding: 12px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
            font-size: 16px;
            margin: 0 10px;
        }
        .btn:hover {
            background-color: #b3788b;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='registered-container'>", unsafe_allow_html=True)
    st.markdown("<h2>You are Registered!</h2>", unsafe_allow_html=True)
    
    st.markdown("""
        <p>Your account has been created successfully. You can now use the platform to access our data and services.</p>
        <p class="message">Click <strong><a href="/test">here</a></strong> to access the test page.</p>
    """, unsafe_allow_html=True)

    st.markdown("<div class='button-container'>", unsafe_allow_html=True)
    if st.button("Go to Dashboard", key="dashboard_btn", class_="btn"):
        # Add functionality to redirect to the dashboard or other functionalities
        pass
    
    if st.button("Logout", key="logout_btn", class_="btn"):
        # Add functionality to logout
        pass
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    registered_page()
