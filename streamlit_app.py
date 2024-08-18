import streamlit as st
import pandas as pd
import requests

WEBHOOK_URL = st.secrets["WEBHOOK_URL"]

def post_to_webhook(**data):
    response = requests.post(WEBHOOK_URL, json=data)
    return response


st.title("🤖 Email Mautic Helper for Marketing")

st.markdown(
    """
Got a great email for a campaign and need a copy paste helper? Fill a form and helper will help you shape the content in all Mautic apps.
"""
)

with st.form(key="idea_form"):
    name = st.text_input("Internal name", placeholder="2030 - 05- CLIENTS - email")
    subject = st.text_input("Subject", placeholder="Easy Redmine subject!")
    html = st.text_area("Insert HTML template", placeholder="insert everything after <!-- BEGIN BODY // --> comment to <!-- // END BODY -->, it should start with <table> html.")
    utmsource = st.text_input("Campaign source", placeholder="newsletter")
    utmmedium = st.text_input("Campaign medium", placeholder="email")
    utmcampaign = st.text_input("Campaign name", placeholder="Scrum_Boards")
    #st.write("Choose where to create Mautic email:")
    #mauticoption_EPcom = st.checkbox("EP.com")
    #mauticoption_EPcz = st.checkbox("EP.cz")
    #mauticoption_EPhu = st.checkbox("EP.hu")
    submit_button = st.form_submit_button(label="Submit Email Template 🚀")

    if submit_button:
        if not html.strip():
            st.error("Please enter an email info 💡")
            st.stop()
            
        data = {"name": name, "subject": subject, "customHtml": html, "utmSource": utmsource, "utmMedium": utmmedium, "utmCampaign": utmcampaign}
        #"mauticoption_EPcom": mauticoption_EPcom, "mauticoption_EPcz": mauticoption_EPcz, "mauticoption_EPhu": mauticoption_EPhu
        response = post_to_webhook(**data)
        if response.status_code == 200:
            st.success("Thanks for your submission! 🌟")
        else:
            st.error("There was an error. Please try again. 🛠️")
