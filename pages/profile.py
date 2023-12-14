import streamlit as st

def display_profile():
    st.markdown("""
    <style>
        .profile-container {
            max-width: 600px;
            padding: 20px;
            margin: 100px auto;
            background-color: #f9f9f9;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: left;
        }
        h2 {
            margin-bottom: 20px;
            color: #333;
        }
        p {
            margin-bottom: 10px;
            color: #555;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='profile-container'>", unsafe_allow_html=True)
    st.markdown("<h2>Hari Chandra Khatri</h2>", unsafe_allow_html=True)
    
    st.markdown("<p><strong>Age:</strong> 35</p>", unsafe_allow_html=True)
    st.markdown("<p><strong>Occupation:</strong> Software Engineer</p>", unsafe_allow_html=True)
    st.markdown("<p><strong>Location:</strong> Kathmandu, Nepal</p>", unsafe_allow_html=True)
    st.markdown("<p><strong>Email:</strong> harichandra@example.com</p>", unsafe_allow_html=True)
    st.markdown("<p><strong>Interests:</strong> Coding, Hiking, Photography</p>", unsafe_allow_html=True)
    
    st.markdown("<h3>Accessibility Information</h3>", unsafe_allow_html=True)
    st.markdown("<p><strong>Visual Impairment:</strong> No</p>", unsafe_allow_html=True)
    st.markdown("<p><strong>Hearing Impairment:</strong> No</p>", unsafe_allow_html=True)
    st.markdown("<p><strong>Mobility Impairment:</strong> Yes</p>", unsafe_allow_html=True)
    st.markdown("<p><strong>Assistive Device Used:</strong> Wheelchair</p>", unsafe_allow_html=True)
    st.markdown("<p><strong>Accessibility Requirements:</strong> Ramp access, Accessible restroom</p>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    display_profile()