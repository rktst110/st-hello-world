import streamlit as st

def main():
    st.title("My Streamlit App")
    
    menu = ["Home", "Page 1", "Page 2"]
    choice = st.sidebar.selectbox("Select a page", menu)
    
    if choice == "Home":
        st.write("Welcome to the Home page!")
        
    elif choice == "Page 1":
        st.write("Welcome to Page 1!")
        
    elif choice == "Page 2":
        st.write("Welcome to Page 2!")
        
if __name__ == "__main__":
    main()
