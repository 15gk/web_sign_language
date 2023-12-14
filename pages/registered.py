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
        }
        h2 {
            margin-bottom: 30px;
            color: #333;
        }
        p {
            margin-bottom: 20px;
            color: #555;
        }
        .message {
            font-style: italic;
            color: #777;
        }
        .message strong {
            color: #000;
            font-weight: bold;
        }
        button {
            background-color: #c88ea7;
            color: #fff;
            padding: 12px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #b3788b;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='registered-container'>", unsafe_allow_html=True)
    st.markdown("<h2>You are Registered!</h2>", unsafe_allow_html=True)
    
    st.markdown("""
        Your account has been created successfully. You can now use the platform to access our data and services.<br/><br/>
      <li class="test-link"><a href="/test">Test</a></li>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    registered_page()
