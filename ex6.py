import gspread
from google.oauth2.service_account import Credentials
import streamlit as st
import pandas as pd
import json

cd = {
  "type": "service_account",
  "project_id": "web-service-506ef",
  "private_key_id": "d1fc8b30508a0e4dc5a208ff9358058db20735c8",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDQTOk494ymrBcU\n3WiM/HiBwywIbbECcAzZftjRa4Ir8f13XTzMpX2PsbJ4nKRRpnVDS00RIR7MlmRP\n+FLxR32RDgCzvIaybFFLa2jHRIms+cq5BrIjIsHULjI2H1dBrwmI/rt988dGwNO2\njbpuobLz811Zf0+F9evKqgyGhjEkqMWpEiiYlJTHQVOugyxBygFbuYEUCHp2/cJc\n1n41eHGmAFruvcdEqouzhOEoyiSMFG+aLJ4vI97dONcMQUfRuB7azoLm524Qyfzu\nMfTSSXFE9WqDd903D6vknJGgqmlxTlMQfGVFCAnkf0Z/894Lr2vqQ+kx6P4CMbfR\nm5wUjCjzAgMBAAECggEABBT8Kj66D2QZwBg5d2KiAlNh6Z8r4L/Z+8/yc/wqEC4z\niOMw91O0Gul6qJMG3bpbQiCkiuLkXx8AkHHUPxOaRtbu6Mn96I40QG82hCORzR8V\nO9YBQXk2mJYrke4ms0wfIQOlufZAH/qHmGRW1HP8juJK7VLDRLB8JYitxFvp2tPs\nAzQuodDP/DYlJXzqfg+DZfppK1QRSrgMJ94JY/H2705jRsLF0ztSTBPJVm7Gb39U\nSTyfbi4tX4E0V+lkJ0AXDuUKEvfnRrXbSOotgOf/iJXT1jj93C7HfeySL3danXFL\nGLhVm+w74cQR9D0TlRoWvi8UzMnyG963uWmGEkIofQKBgQDuNxbNtcGjRvhQ1AVD\ne8XVbeUEkJG36k5fYpBz4kWebvIN5kkxMbskstOPs0EuEdKDuzIGDONUgPncI2K2\nRVKmexpS8rHyZqyqjAYooBOgwD2+9OvElLv3BvtfQQxnuCzteESTKTixiK/LrpCm\nxYR+bJi5U5U/xJBF6MYZL7WZTwKBgQDf2hK/zrPjNFB5d+kX1w7S8xxGljvGKP38\n1nmx/EJ04LisC0vJPb32cOs9mhwOFXF3B8KWxxjIiPrwZtbchzmdptNPG5TGJsoF\nyVoZM12xTnzIltqJQsezsGOaDsfo4yXLVITvlAR8VnpcmQLGk7aChAXEE5lZiTEG\nFfPusgDFHQKBgCk0TjV24u+jLwCMK/zoQ+gPAjYv64SserH1Epd45CHrfuL4mmBw\nAbbvV7jbgMK/QnKWxqhVQl0zkgSJ+mEczJcPZBZE9JLBP8ygO9B7H+oGVqfZJY7z\nSzAHfSOU1Nh7+wl4bCQoVS4gPog0wcCXGbvkfOZRltdY4Lu2780be4XxAoGAS8ld\nB6tHo+iWRkmelP+ueSTtscgzPIesVemXEfdB2KgsXbMFWYCZy9G3EwgV7367B32N\nF9cYQOx/aNyoackubH2KlQHVgLCpPQRKiLWnRtw3ywGnw0jkq6VQU1wlumcM6KYY\ny7PlQONWUftLwUdJRy7DdPrdtD6KZnEQQQPq1tECgYA6WJQAwdCzk4GZKCe2V+Pb\n64fHRhH1cPNPbOI7sjzIhCPBnBdHbH8tq9KW/u1Ci2nUSVOx6tUsXD3Bsl3gGKhN\nM70TN84nI+lRr9Yr+1yPvFy48XvDsRbid3muYzNleowPl8Oib7i1qt02yqqFiV2g\nzhVH20AulAzw4AV6GW4l/g==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-kgd12@web-service-506ef.iam.gserviceaccount.com",
  "client_id": "118081343232026398180",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-kgd12%40web-service-506ef.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
with open('credentials.json', 'w') as outfile:
    json.dump(cd, outfile)
credentials = Credentials.from_service_account_file('credentials.json', scopes=scope)

credentials = Credentials.from_service_account_file('credentials.json', scopes=["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"])
client = gspread.authorize(credentials)
sheet = client.open_by_key('11bqghL7i8FIGgJVzOl0zFcp5RwJLitAKuitzn3-DZM_g').sheet1

def save_vote(option):
    sheet.append_row([option])

def get_all_votes():
    all_data = sheet.get_all_values()
    if not all_data:
        return pd.DataFrame(columns=["Option"])
    df = pd.DataFrame(all_data[1:], columns=all_data[0])
    return df

st.title("سیستم نظرسنجی/رای‌گیری")

st.header("رای دهی")
selected_option = st.radio("گزینه ها:", ["گزینه 1", "گزینه 2", "گزینه 3"])
vote_button = st.button("ثبت رای")

if vote_button:
    if selected_option:
        save_vote(selected_option)
        st.success("رای شما با موفقیت ثبت شد!")
    else:
        st.error("لطفا یک گزینه را انتخاب کنید.")

st.header("نتایج")
all_votes_df = get_all_votes()
st.write(all_votes_df)
