import streamlit as st
st.set_page_config(page_title='ISKCON',page_icon='http://iskconbhuvaikuntha.com/wp-content/uploads/2023/06/iskcon-pandharpur.jpeg')
mymenu=st.sidebar.selectbox('My menu',('Home','FillForm','Downloads'))
st.image('http://iskconbhuvaikuntha.com/wp-content/uploads/2023/06/iskcon-pandharpur.jpeg')
st.title('ISKCON PANDHARPUR')
st.header('By ANANT VITTHAL DAS')
st.text('This is a tutorial on streamlit library')
if(mymenu=='Home'):
	st.markdown('<center><h1>WELCOME</h2></center>',unsafe_allow_html=True)
	st.video('https://www.youtube.com/watch?v=tvj1y9UaK8A')
elif(mymenu=='FillForm'):
	with st.form('My Form'):
		name=st.text_input('Enter Name')
		dob=st.date_input("Choose Date of Birth")
		marks=st.slider('Choose Marks')
		k=st.form_submit_button("Submit Form")
		if k:
			st.write('Name:',name,'DOB:',dob,'Marks:',marks)
elif(mymenu=='Downloads'):
     st.header("Downloads")
     st.download_button('Download Now','https:st.image(//i.ytimg.com/vi/tvj1y9UaK8A/maxresdefault.jpg)','onlei.txt')