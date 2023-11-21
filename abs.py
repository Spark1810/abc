import streamlit as st
import subprocess

def open_application(app_name):
    try:
        # Use subprocess to run the specified app_name command
        subprocess.run([app_name], check=True)
    except subprocess.CalledProcessError as e:
        st.error(f"Error opening {app_name}: {e}")

def main():
    st.title("Application Opener App")

    # Get the application name from the user
    app_name = st.text_input("Enter the application name:")

    if st.button("Open Application"):
        if app_name:
            open_application(app_name)
            st.success(f"{app_name} opened successfully!")
        else:
            st.warning("Please enter an application name.")

if __name__ == "__main__":
    main()
