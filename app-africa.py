import streamlit as st

'''
# This is the simple way to strength
## This is a mealplanner for prepping
'''
from PIL import Image
image = Image.open('arnold.jpg')

#st.sidebar.markdown("# Hello World!")
st.sidebar.image(image, caption='Arnold Motivation',use_column_width=False)
'''
First, let's define the basics
## Targets
'''
kcal_target = st.number_input('Kcal target: ', 2000, 5000, 2400, 50)
protein_target = st.number_input('Protein (g) target: ', 0, 250, 50, 5)

st.write(str(kcal_target) + ' and ' + str(protein_target))
grocery_list = st.sidebar.multiselect("Export: ", options=["grocery list", "mealplanner", "prepping recipe"])
# or select page : options= ['targets', 'mealplan (per day?)', 'groceries', 'prepping', 'progression']
plan = st.sidebar.button("Download")
if plan:
    # export pdf
    None
