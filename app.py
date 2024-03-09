import streamlit as st
from src.inference import get_prediction

#Initialise session state variable
if 'input_features' not in st.session_state:
    st.session_state['input_features'] = {}

def app_sidebar():
    st.sidebar.header('Loan Details')
    is_female_options = ['0','1']
    is_married_options = ['0','1']
    colg_edu_options = ['0','1']
    is_female = st.sidebar.selectbox("Is Female", is_female_options)
    is_married = st.sidebar.selectbox("Is Married", is_married_options)
    colg_edu = st.sidebar.selectbox("Colg Education", colg_edu_options)
    yearly_income = st.sidebar.text_input("Yearly Income '000s", placeholder="in '000s")
    months_residence = st.sidebar.slider('Months Residences', 0, 80, 30, 1)
    def get_input_features():
        input_features = {'is_female': is_female,
                          'is_married': is_married,
                          'colg_edu':colg_edu,
                          'yearly_income': int(yearly_income)*1000,
                          'months_residence': months_residence,
                         }
        return input_features
    sdb_col1, sdb_col2 = st.sidebar.columns(2)
    with sdb_col1:
        predict_button = st.sidebar.button("Assess", key="predict")
    with sdb_col2:
        reset_button = st.sidebar.button("Reset", key="clear")
    if predict_button:
        st.session_state['input_features'] = get_input_features()
    if reset_button:
        st.session_state['input_features'] = {}
    return None

def app_body():
    title = '<p style="font-family:arial, sans-serif; color:Black; font-size: 40px;"><b> Welcome to Coupon Subscription Assessment</b></p>'
    st.markdown(title, unsafe_allow_html=True)
    default_msg = '**System assessment says:** {}'
    if st.session_state['input_features']:
        assessment = get_prediction(is_female=st.session_state['input_features']['is_female'],
                                    is_married=st.session_state['input_features']['is_married'],
                                    yearly_income=st.session_state['input_features']['yearly_income'],
                                    colg_edu=st.session_state['input_features']['colg_edu'],
                                    months_residence=st.session_state['input_features']['months_residence'])
        if assessment == '1':
            st.success(default_msg.format('Subscribed'))
        else:
            st.warning(default_msg.format('Not Subscribed'))
    return None

def main():
    app_sidebar()
    app_body()
    return None

if __name__ == "__main__":
    main()