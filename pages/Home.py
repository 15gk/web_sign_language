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
            <li class="login-link"><a href="/login">Login</a></li>
        </ul>
    </nav>
    """, unsafe_allow_html=True)

def landing_page():
    

    navbar()  # Include the navbar

    # CSS styles
    st.markdown("""
        <style>
            .container {
                text-align: center;
                padding: 20px;
                background-color: #ffffff;
                font-family: "Libre Baskerville", serif;
                animation: fadeIn 2s ease;
            }
            /* Add other styles here */
            
            @keyframes fadeIn {
                from {
                    opacity: 0;
                }
                to {
                    opacity: 1;
                }
            }
            @keyframes slideInDown {
                from {
                    transform: translateY(-100%);
                }
                to {
                    transform: translateY(0);
                }
            }
        </style>
    """, unsafe_allow_html=True)

    # HTML structure
    st.markdown("""
        <style>
            /* Add your CSS styles here */
        </style>
    """, unsafe_allow_html=True)



if __name__ == "__main__":
    landing_page()
