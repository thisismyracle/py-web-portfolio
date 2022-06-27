from PIL import Image
from streamlit_lottie import st_lottie

import requests
import streamlit as st


# functions
def load_css(path):
    with open(path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()




# page config
st.set_page_config(page_title='Myracle - あいさつ', page_icon=':sparkles:', layout='centered')
load_css('style/style.css')

# assets
lottie_code = load_lottie('https://assets4.lottiefiles.com/packages/lf20_4kx2q32n.json')
img_ui_rexirus = Image.open('images/img_ui_rexirus.png')
img_ui_suluhsuar = Image.open('images/img_ui_suluhsuar.png')
img_ui_sponsorku = Image.open('images/img_ui_sponsorku.png')
img_logo_sanctuary = Image.open('images/img_logo_sanctuary.png')
img_logo_hmif = Image.open('images/img_logo_hmif.png')
img_logo_focusassist = Image.open('images/img_logo_focusassist.png')

# header
with st.container():
    st.subheader('Hi, I am Myracle :wave:')
    st.title('A Software Developer from Indonesia')
    st.write('If my work is beatifully works, its Myracle.')
    st.write('[Learn More >](https://www.myracle.id)')

# what i do
with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)

    with left_column:
        st.header('What I do')
        st.write('##')
        st.write(
            """
            I just follow my creativity such as:
            - programming
            - do music cover/remix/composing
            - do song cover
            - make an art

            Sounds interesting? check out my social media to find out more!
            """
        )
        st.write("""
        [YouTube](https://www.youtube.com/channel/UCL9uYQIXwckRA5QzJRC88SQ)  &#183;  [Instagram](https://www.instagram.com/thisismyracle)  &#183;  [GitHub](https://github.com/thisismyracle)  &#183;  [Trakteer](https://trakteer.id/myracle)
        """)

    with right_column:
        st_lottie(lottie_code, height=300, key='coding')


# projects
with st.container():
    st.write('---')
    st.header('My previous works')

    st.write('##')
    st.subheader('UI Designs')
    ui_column1, ui_column2, ui_column3 = st.columns(3)
    with ui_column1:
        st.image(img_ui_rexirus)
    with ui_column2:
        st.image(img_ui_suluhsuar)
    with ui_column3:
        st.image(img_ui_sponsorku)

    st.write('##')
    st.subheader('Logos')
    logo_column1, logo_column2, logo_column3 = st.columns(3)
    with logo_column1:
        st.image(img_logo_sanctuary)
    with logo_column2:
        st.image(img_logo_hmif)
    with logo_column3:
        st.image(img_logo_focusassist)

    st.write('##')
    st.subheader('Music')
    st.write('#')
    music_column1, music_column2 = st.columns(2)
    with music_column1:
        st.video('https://www.youtube.com/embed/wJi0dxISuU4')
        st.video('https://www.youtube.com/embed/sMVN4pgMSCc')
    with music_column2:
        st.video('https://www.youtube.com/embed/99IAmzJstig')
        st.video('https://www.youtube.com/embed/bhZQ6tcqQ1M')
    
    st.write('##')
    st.subheader('Covers')
    st.write('#')
    cover_column1, cover_column2 = st.columns(2)
    with cover_column1:
        st.video('https://www.youtube.com/embed/kvzsM3upI50')
        st.video('https://www.youtube.com/embed/lgNeMKUBdgo')
    with cover_column2:
        st.video('https://www.youtube.com/embed/JYHBTWKj3BU')
        st.video('https://www.youtube.com/embed/8ZrRP8hHmrM')
        
# get in touch
with st.container():
    st.write('---')
    st.header('Get in touch!')
    st.write('##')

    left_column, right_column = st.columns((2,1))
    with left_column:
        contact_form = """
        <form action="https://formsubmit.co/thisismyracle@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
