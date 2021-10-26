import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time

st.title('streamlit 入門')
st.write('DataFrame2')

"""
$
    a = f(x)
$
"""

latest_iteration = st.empty()
bar = st.progress(0)

#for i in range(100):
#    latest_iteration.text(f'Iteration {i+1}')
#    bar.progress(i+1)
#    time.sleep(0.1)



left_column, right_column = st.columns(2)

button = left_column.button('right view')

if button:
    right_column.write('Yte')

    
expander = st.expander('query')    
expander.write('write')    
    
text = st.text_input('Input')

'in ', text


#condition = st.sidebar.slider("condition", 0, 100, 40)
#'condition ', condition


option = st.selectbox(
    'select number',
    list(range(1, 11))
)

'test', option, 'is'

f = r"C:\Users\unico\OneDrive\Documents\DOCUMENT\IMAGE\0001\SCN_0017.jpg"

if st.checkbox('sel'):
    img = Image.open(f)
    st.image(img, caption='y', use_column_width=True)


df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(df)