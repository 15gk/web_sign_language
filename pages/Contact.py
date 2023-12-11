import streamlit as st

def contact_form():
    st.title('Contact Us')
    st.markdown("""
    <style>
        .contact-container {
            text-align: center;
            max-width: 600px;
            margin: 50px auto;
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
    st.image("./Image/contact.png",width=400, use_column_width=True)
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
