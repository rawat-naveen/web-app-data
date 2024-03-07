
#Imports
import pandas as pd
import seaborn as sns
import streamlit as st

#1. Title and Subheader
st.title("Data Analysis")
st.subheader("Data Analysis Using Python & Streamlit")

#2. Upload Dataset
upload = st.file_uploader("Upload Your Dataset (In CSV Format)")
if upload is not None:
    data=pd.read_csv(upload)

#3. Show Dataset
if upload is not None:
    button_style = """
        <style>
            .stButton>button {
                background-color: Blue;
                color: white;
            }
        </style>
    """

    # Write the custom CSS
    st.markdown(button_style, unsafe_allow_html=True)
    
    if st.checkbox("Preview Dataset"):
        if st.button("Show the First Five Rows of DataSet",type='secondary'):
            st.write(data.head())
        if st.button("Show the Last Five Rows of DataSet"):
            st.write(data.tail())
            
#4.Check DataTypes Of Each Columns
if upload is not None:
    if st.checkbox("Show the DataType of Each Column"):
        st.text("DataTypes")
        st.write(data.dtypes)


#5. Find The shape of the Dataset(Number of Rows And number of Columns)

if upload is not None:
    data_shape = st.radio("What Dimension do you check ?",('Rows','Columns'))
    if data_shape =='Rows':
        st.text("Number of Rows")
        st.write(data.shape[0])
    if data_shape == 'Columns':
        st.text("Number of Columns")
        st.write(data.shape[1])

#6. Find Null Values in the Dataset
if upload is not None:
    test=data.isnull().values.any()
    if test == True:
        if st.checkbox("Null Values in the Datset"):
            sns.heatmap(data.isnull())
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()
    else:
        st.success("Congrulations !!!, No missing Values")
#7. Find Duplicate Values in the Dataset
if upload is not None:
    test = data.duplicated().any()
    if test == True:
        st.warning("This Dataset Contains Some Duplicate Values")
        dup = st.selectbox("Do you want to remove Duplicate Values?",("Select One","Yes","No"))
        if dup =="Yes":
            data=data.drop_duplicates()
            st.text("Duplicate Values are Removed")
        if dup =="No":
            st.text("Ok,No Problem")
        
#8. Get Overall Statistics
if upload is not None:
    if st.checkbox("Summary of The Dataset"):
        st.write(data.describe(include='all'))

#9. About Section
if st.button("About App"):
    st.text("Build With Streamlit")
    st.text("Thanks To Streamlit")
#10. By
if st.checkbox("By"):
    st.success("Naveen Rawat")
        