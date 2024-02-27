import streamlit as st
from msal import PublicClientApplication
from dotenv import load_dotenv
import os

load_dotenv()

st.title("Hello World")
app = PublicClientApplication(
        client_id=os.environ['MS_APP_SERVICE_CLIENT_ID'], 
        authority='https://login.microsoftonline.com/common'
        # client_secret="sMi8Q~VYZKjw323~fCr5uVyWhcGMBnVv3ljC.cnQ"
    )


# flow = app.initiate_device_flow(scopes=["User.Read"])
# st.write(f"\n1) Copy the Access Code: :red[{flow['user_code']}] \n2) Go to : {flow['verification_uri']}\n 3) Verify Identity with NTU Email\n 4) Accept App Access Permission.")
# result = app.acquire_token_by_device_flow(flow)

result = app.acquire_token_interactive(scopes=["User.Read"])
user = result['id_token_claims']['name']
email = result['id_token_claims']['preferred_username']
st.write(user)
st.write(email)