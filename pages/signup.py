import streamlit as st

def signup_page():
    st.markdown("""
    <style>
        .signup-container {
            max-width: 400px;
            padding: 20px;
            margin: 100px auto;
            background-color: #f9f9f9;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h2 {
            text-align: center;
            margin-bottom: 30px;
            color: #333;
        }
        label {
            font-weight: bold;
            margin-bottom: 8px;
            display: block;
            color: #555;
        }
        input[type="text"],
        input[type="email"],
        input[type="password"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #c88ea7;
            color: #fff;
            padding: 12px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #b3788b;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='signup-container'>", unsafe_allow_html=True)
    st.markdown("<h2>Sign Up</h2>", unsafe_allow_html=True)
    
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):
        # Check signup logic here
        if password == confirm_password:
            st.success("Account created for {}".format(username))
            # Perform actions after successful signup, e.g., database entry
        else:
            st.error("Passwords do not match")
    
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    signup_page()
