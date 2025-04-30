import streamlit as st

# Page configuration
st.set_page_config(page_title="AI Drug Analyzer", layout="centered")

# Custom header with styling
st.markdown(
    """
    <div style='background-color:#4B0082; padding: 10px; text-align: center; border-radius: 8px;'>
        <h2 style='color:white;'>DRUG ANALYSER</h2>
    </div>
    """,
    unsafe_allow_html=True
)

# Logo placeholder
st.image("https://via.placeholder.com/200x200.png?text=LOGO", width=200)  # Replace with your logo path or URL

# Subtitle
st.markdown(
    "<p style='text-align: center; font-weight: bold;'>AI ANALYSE EITHER YOUR DRUG WILL BE <br> DESIRED OR NOT BY ITS FEED DATA</p>",
    unsafe_allow_html=True
)

# Inputs
drug_name = st.text_input("Enter Drug Name")
molecular_data = st.text_input("Enter Molecular Data")
compound_id = st.text_input("Enter SMILES or Compound ID")

# Button
if st.button("✅ CHECK NOW"):
    st.success("Processing your inputs...")
    st.write(f"**Drug Name:** {drug_name}")
    st.write(f"**Molecular Data:** {molecular_data}")
    st.write(f"**Compound ID / SMILES:** {compound_id}")


