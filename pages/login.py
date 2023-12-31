import streamlit as st

def login_page():
    st.set_page_config(layout="wide")  # Hides Streamlit's default header and footer
    
    st.markdown(
        """
        <style>
            .login-container {
                max-width: 400px;
                padding: 20px;
                margin: 100px auto;
                background-color: #f9f9f9;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                font-family: Arial, sans-serif;
            }
            h2 {
                text-align: center;
                margin-bottom: 30px;
                color: #333;
                font-size: 32px;
                font-weight: bold;
            }
            label {
                font-weight: bold;
                margin-bottom: 8px;
                display: block;
                color: #555;
            }
            input[type="text"],
            input[type="password"] {
                width: 100%;
                padding: 12px;
                margin-bottom: 20px;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            button {
                background-color: #ff7eb9;
                color: #fff;
                padding: 12px 20px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                width: 100%;
                transition: background-color 0.3s;
                font-size: 18px;
                font-weight: bold;
            }
            button:hover {
                background-color: #c2e0ff; /* Light blue hover color */
            }
        </style>
        """, unsafe_allow_html=True)

    st.markdown("<div class='login-container'>", unsafe_allow_html=True)
    st.markdown("<h2>Login</h2>", unsafe_allow_html=True)
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Check login logic here
        if username == "your_username" and password == "your_password":
            st.success(f"Logged in as {username}")
            # Redirect to another page or perform actions after successful login
        else:
            st.error("Invalid username or password")
    
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    login_page()
