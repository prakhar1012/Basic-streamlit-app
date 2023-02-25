import streamlit as st

st.title("Prakhar Agrawal :dove_of_peace:")
st.header("Data Science Intern at Innomatics Research Labs")

st.subheader("Education: ")
st.write('B.Tech CSE-AIML, 2020-2024')
st.write('Oriental Institute of Science & Technology, Bhopal (M.P.)')

st.subheader("Project: ")
st.markdown("**Twitter Sentiment Analysis -**")
st.write("• Classifies tweets into positive and negative.")
st.write("•	Use case of Natural Language Processing.")
st.write("• Trained Naive Bayes Classifier model to perform Classification")
st.write("• Also done Analysis of Amazon echo reviews.")

st.subheader("Skills: ")
st.write("•	Machine Learning     •	Deep Learning    • Natural Language Processing    • Data Analysis")


st.markdown("**Linkedin**- https://www.linkedin.com/in/prakhar-agrawal-078744141/")

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.pexels.com/photos/7130560/pexels-photo-7130560.jpeg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 






