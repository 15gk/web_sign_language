import streamlit as st

def navbar():
    st.markdown("""
    <style>
        nav {
            background-color: #c88ea7;
            color: #000;
            padding: 10px;
        }

        ul {
            list-style-type: none;
            padding: 0;
            display: flex;
        }

        li {
            margin-right: 20px;
        }

        a {
            text-decoration: none;
            color: #2f2e41;
            font-weight: bold;
            transition: color 0.3s;
        }

        a:hover {
            color: #000;
        }

        .login-link {
            margin-right: 0;
            display: flex;
            justify-content: flex-end;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <nav>
        <ul>
            <li><a href="/">Gesture Sync</a></li>
            <li><a href="/about">About Us</a></li>
            <li><a href="/Contact">Contact</a></li>
            <li><a href="/webcam">Webcam</a></li>
            <li class="login-link"><a href="/login">Login</a></li>
        </ul>
    </nav>
    """, unsafe_allow_html=True)

def contact_form():
   

    navbar()  # Include the navbar

    st.markdown("""
    <style>
        .contact-container {
            text-align: center;
            max-width: 600px;
            margin: 50px auto;
                background-color: #000000;
        }
        .contactimg {
            max-width: 600px;
            height: 360px;
            margin-bottom: 20px;
        }
        form {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 8px;
        }
        textarea {
            width: 100%;
            padding: 8px;
            margin-bottom: 16px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #c88ea7;
            color: #fff;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #c88ea7;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='contact-container'>", unsafe_allow_html=True)
    st.image("./Image/contact.png", width=400, use_column_width=True)
    st.markdown("""
        <form>
            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea>
            <button type="submit">Submit</button>
        </form>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    contact_form()
