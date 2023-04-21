import streamlit as st
from test import main
from google.cloud import firestore

st.write('Hello world!')
st.write('this is main page')
st.write('this is a change')


main()



# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("firestore-key.json")
'''
# Create a reference to the Google post.
doc_ref = db.collection("posts").document("Google")

# Then get the data at that reference.
doc = doc_ref.get()

# Let's see what we got!
st.write("The id is: ", doc.id)
st.write("The contents are: ", doc.to_dict())
'''



# Define function to print all data in a collection and its subcollections
def print_collection(collection_ref, indent=0):
    # Iterate over documents in the collection
    for doc in collection_ref.stream():
        # Print document ID and data
        st.write(" " * indent + f"Document ID: {doc.id}")
        st.write(" " * indent + f"Document data: {doc.to_dict()}")

        # Iterate over subcollections in the document
        for subcollection in doc.collections():
            # Print subcollection ID
            st.write(" " * indent + f"Subcollection ID: {subcollection.id}")

            # Recursively print all data in the subcollection
            print_collection(subcollection, indent + 4)

# Print all data in the "posts" collection
collection_ref = db.collection("April 2023")
print_collection(collection_ref)
