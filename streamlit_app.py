import streamlit as st
from test import main
from google.cloud import firestore

st.write('Hello world!')
st.write('this is main page')
st.write('this is a change')


main()



# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("firestore-key.json")
"""
# Create a reference to the Google post.
doc_ref = db.collection("posts").document("Google")

# Then get the data at that reference.
doc = doc_ref.get()

# Let's see what we got!
st.write("The id is: ", doc.id)
st.write("The contents are: ", doc.to_dict())
"""

st.write("testing through dev neqw")

#doc_ref = db.collection("April 2023").document("13 April 2023")
#docs = db.collection("Test").document("DocTest")

docs = db.collection('Test').stream()

      
#st.write(docs)
for doc in docs:
    st.write('{doc.id} => {doc.to_dict()}')




#collections = db.collection("Test").document("DocTest").collections()
collections = db.collection("Test").collections()
#st.write(collections)
for collection in collections:
    #st.write(collection)
    for doc in collection.stream():
        st.write("The id is: ", doc.id)
        st.write("The contents are: ", doc.to_dict())
   



    
