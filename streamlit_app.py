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
doc_ref = db.collection("Test").document("DocTest")

# List all subcollections of the document
subcollections = doc_ref.list_collections()

# Iterate over subcollections and print their IDs
for subcollection in subcollections:
    print(f"Subcollection ID: {subcollection.id}")

