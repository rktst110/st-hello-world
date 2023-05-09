import streamlit as st


def main():
    st.title("My Streamlit App")
    
    # Using object notation
    add_selectbox = st.sidebar.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone")
    )

    # Using "with" notation
    with st.sidebar:
        add_radio = st.radio(
            "Choose a shipping method",
            ("Standard (5-15 days)", "Express (2-5 days)")
        )
        
if __name__ == "__main__":
    main()
