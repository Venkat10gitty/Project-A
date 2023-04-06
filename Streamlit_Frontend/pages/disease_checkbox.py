# import streamlit as st

# # Define the prescribed ingredients for each disease
# prescribed_ingredients = {
#     "Cholesterol": ["Vegetables, legumes, fruit, wholegrains, nuts and seeds.", 
#                      "Legumes or pulses such as chickpeas, lentils, split peas, beans such as haricot beans, kidney beans, baked beans , bean mixes.", 
#                      "Wholegrain breads, cereals, pasta, rice and noodles"],
#     "Triglycerides": ["Soy protein.", 
#                        "Fatty fish like sardines, salmon, mackerel, and herring.", 
#                        "Avocado.", 
#                        "Whole grains like oatmeal, buckwheat, barley, and millet.", 
#                        "Cauliflower, cabbage, broccoli, Brussels sprouts, bok choy, and kale."],
#     "Diabetes": ["Whole grains, such as brown rice, oatmeal, quinoa, millet, or amaranth.", 
#                  "Greens such as kale, spinach, and arugula.", 
#                  "Skimmed milk.", 
#                  "Plant-based proteins such as beans, nuts, seeds, or tofu.", 
#                  "Tomatoes.", 
#                  "Berries.", 
#                  "Citrus fruits like grapefruits, oranges, lemons and limes."],
#     "Osteoporosis": ["Whole grains, like quinoa, barley, oats, and brown rice.", 
#                       "Lean proteins, such as poultry and fish.", 
#                       "Nuts and seeds.", 
#                       "Dairy products such as low-fat and non-fat milk, yogurt and cheese.", 
#                       "Collard greens, turnip greens, kale, okra, Chinese cabbage, dandelion greens, mustard greens and broccoli."],
#     "PCOS": ["Omega-3 rich fish  such as salmon, baked or broiled.", 
#              "Olive oil.", 
#              "Beans and other protein-rich legumes.", 
#              "Non-starchy vegetables such as leafy greens (spinach, kale, escarole, endive, lettuce), tomatoes, mushrooms, peppers, broccoli, cauliflower.", 
#              "Whole grains, such as brown rice, barley."]
# }

# # Create a checkbox list for the diseases
# selected_diseases = st.multiselect(
#     "Select the diseases you have been diagnosed with:",
#     ["Cholesterol", "Triglycerides", "Diabetes", "Osteoporosis", "PCOS"]
# )

# # Display the prescribed ingredients for each selected disease
# for disease in selected_diseases:
#     st.write(f"## {disease}")
#     st.write("Prescribed Ingredients:")
#     for ingredient in prescribed_ingredients[disease]:
#         st.write(f"- {ingredient}")


# import streamlit as st

# # Define the dictionary of diseases and their respective restricted and prescribed food items
# diseases = {
#     "Cholesterol": {
#         "Restricted": ["beef", "lamb", "pork", "butter", "cream", "coconut oil", "palm oil", "biscuits", "cakes", "pastries", "brownies", "French Fries", "doughnuts", "sausages", "ham", "bacon", "salami"],
#         "Prescribed": ["Vegetables", "legumes", "fruit", "wholegrains", "nuts", "seeds", "chickpeas", "lentils", "split peas", "haricot beans", "kidney beans", "baked beans", "bean mixes", "Wholegrain breads", "cereals", "pasta", "rice", "noodles"]
#     },
#     "Triglycerides": {
#         "Restricted": ["corn", "lamb", "CannedFish", "pasta", "potatoes", "cereals", "sweet iced tea", "regular soda", "fruit juice","beans" "syrupy coffee drink", "Baked goods", "fried foods", "red meat", "chicken skin", "egg yolks", "high-fat-dairy", "butter"],
#         "Prescribed": ["Soy protein", "sardines", "salmon", "mackerel", "herring", "Avocado", "oatmeal", "buckwheat", "barley", "millet", "Cauliflower", "cabbage", "broccoli", "Brussels sprouts", "bok choy", "kale"]
#     },
#     "Diabetes": {
#         "Restricted": ["white rice", "white flour", "Canned vegetables with sodium", "Regular jam", "lamb", "preserves", "Fried meats", "Whole milk", "Regular yogurt", "Regular cottage cheese", "Energy drinks", "Sweetened tea", "Saturated fats"],
#         "Prescribed": ["brown rice", "oatmeal", "quinoa", "millet", "amaranth", "kale", "spinach", "arugula", "Skimmed milk", "beans", "nuts", "seeds", "tofu", "Tomatoes", "Berries", "grapefruits", "oranges", "lemons", "limes"]
#     },
#     "Hepatitis": {
#         "Restricted" : ["butter", "cream", "cooking margarine", "coconut oil", "palm oil", "biscuits", "cakes", "pastries", "processed meats", "pizza", "fried food", "potato chips", "crisps", "snacks", "food and drinks with salt and sugar alcohol"],
#         "Prescribed" : ["vegetables", "fruits", "whole grains like oats, brown rice, barley, quinoa", "fish", "skinless chicken", "egg whites", "beans", "low-fat or non-dairy products", "nuts", "avocadoes", "olive oil", "foods rich in Iron", "Vitamin A", "Vitamin B3 (niacin)", "Vitamin C", "Vitamin D"]
#     },
#     "Stroke": {
#         "Restricted" : ["butter", "cream", "cooking margarine", "coconut oil", "palm oil", "biscuits", "cakes", "pastries", "processed meats", "pizza", "fried food", "potato chips", "crisps", "snacks", "food and drinks with salt and sugar alcohol"],
#         "Prescribed" : ["vegetables", "fruits", "low-fat", "fat-free dairy products", "salmon", "flaxseeds", "nuts & seeds", "avocados", "eggs", "olive oil", "quinoa", "greek yoghurt", "green tea", "legumes", "blueberries", "pomegranate", "citrus fruits", "apples", "tomatoes"]
#     },
#     "Gall Bladder Removal":{
#         "Restricted" : ["butter", "cream", "cooking margarine", "coconut oil", "palm oil", "biscuits", "cakes", "pastries", "processed meats", "pizza", "fried food", "potato chips", "crisps", "snacks", "food and drinks with salt and sugar alcohol"],
#         "Prescribed" : ["vegetables", "fruits", "low-fat", "fat-free dairy products", "salmon", "flaxseeds", "nuts & seeds", "avocados", "eggs", "olive oil", "quinoa", "greek yoghurt", "green tea", "legumes", "blueberries", "pomegranate", "citrus fruits", "apples", "tomatoes"]
#     },
#     "FattyLiver":{
#         "Restricted" : ["butter", "cream", "cooking margarine", "coconut oil", "palm oil", "biscuits", "cakes", "pastries", "processed meats", "pizza", "fried food", "potato chips", "crisps", "snacks", "food and drinks with salt and sugar alcohol"],
#         "Prescribed" : ["vegetables", "fruits", "low-fat", "fat-free dairy products", "salmon", "flaxseeds", "nuts & seeds", "avocados", "eggs", "olive oil", "quinoa", "greek yoghurt", "green tea", "legumes", "blueberries", "pomegranate", "citrus fruits", "apples", "tomatoes"]
#     }
# }

# # Define empty lists to hold the overall restricted and prescribed foods
# overall_restricted_foods = []
# overall_prescribed_foods = []

# # Create a checkbox list for the diseases
# selected_diseases = st.multiselect("Select the diseases you have:", list(diseases.keys()))

# # Loop through the selected diseases and add their restricted and prescribed foods to the overall lists
# for disease in selected_diseases:
#     overall_restricted_foods += diseases[disease]["Restricted"]
#     overall_prescribed_foods += diseases[disease]["Prescribed"]

# # Remove duplicates from the overall lists
# overall_restricted_foods = list(set(overall_restricted_foods))
# overall_prescribed_foods = list(set(overall_prescribed_foods))

# # Display the overall restricted and prescribed foods
# st.write("Overall Restricted Foods:")
# st.write(", ".join(overall_restricted_foods))

# st.write("Overall Prescribed Foods:")
# st.write(", ".join(overall_prescribed_foods))



# import streamlit as st


# st.write("# Do you have personal Nutritionist")

# # Ask user how they are feeling today
# if st.button("Yes"):
#     feeling_today = st.error("Are you feeling good today?")
#     response = feeling_today.button("Yes") or not feeling_today.button("No")
#     if response:
#         st.write("Great! Please provide your information below.")
#         name = st.text_input("Name")
#         age = st.number_input("Age", min_value=0, max_value=150, value=25)
#         gender = st.radio("Gender", options=["Male", "Female", "Other"])
#         height = st.slider("Height (in cm)", min_value=100, max_value=250, value=170)
#         weight = st.slider("Weight (in kg)", min_value=20, max_value=500, value=70)

import streamlit as st

# Create a list of options for the user to choose from
options = ["Yes", "No"]

# Ask the user how they're feeling today and give them the option to choose
feeling_today = st.selectbox("How are you feeling today?", options)

# If the user chooses "Yes", display the rest of the form
if feeling_today == "No":
    st.write("Please fill out the following information:")
    name = st.text_input("Name")
    age = st.number_input("Age")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    height = st.number_input("Height (in cm)")
    weight = st.number_input("Weight (in kg)")
else:
    # If the user chooses "No", don't display anything
    pass


