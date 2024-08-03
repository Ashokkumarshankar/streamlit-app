import streamlit as st
import joblib
import numpy as np
import pandas as pd


# Load the combined model
with open('hybrid_model.pkl', 'rb') as file:
    hybrid_model = joblib.load(file)

# Streamlit app
st.title("Hybrid Model Deployment")

# Input fields for the user
inputs = {
    'dt': st.number_input('dt', value=0),
    'switch': st.number_input('switch', value=1),
    'src': st.text_input('src', value='10.0.0.1'),
    'dst': st.text_input('dst', value='10.0.0.8'),
    'pktcount': st.number_input('pktcount', value=100),
    'bytecount': st.number_input('bytecount', value=2000),
    'dur': st.number_input('dur', value=30),
    'dur_nsec': st.number_input('dur_nsec', value=10),
    'tot_dur': st.number_input('tot_dur', value=40),
    'flows': st.number_input('flows', value=5),
    'packetins': st.number_input('packetins', value=50),
    'pktperflow': st.number_input('pktperflow', value=10),
    'byteperflow': st.number_input('byteperflow', value=400),
    'pktrate': st.number_input('pktrate', value=20),
    'Pairflow': st.number_input('Pairflow', value=1),
    'port_no': st.number_input('port_no', value=3),
    'tx_bytes': st.number_input('tx_bytes', value=500),
    'rx_bytes': st.number_input('rx_bytes', value=400),
    'tx_kbps': st.number_input('tx_kbps', value=100),
    'rx_kbps': st.number_input('rx_kbps', value=200),
    'tot_kbps': st.number_input('tot_kbps', value=300),
    'Protocol': st.text_input('Protocol', value='UDP')
}

# Create DataFrame from inputs
input_df = pd.DataFrame([inputs])

# Predict button
if st.button("Predict"):
    try:
        # Ensure Protocol is encoded if necessary
        if 'Protocol' in hybrid_model.encoders:
            input_df['Protocol'] = hybrid_model.encoders['Protocol'].transform(input_df['Protocol'])
        
        # Preprocess and predict
        predictions = hybrid_model.predict(input_df)
        predicted_class = np.argmax(predictions, axis=1)[0]
        st.write(f"The predicted attack category is: {predicted_class}")
    
    except Exception as e:
        st.error(f"An error occurred: {e}")
