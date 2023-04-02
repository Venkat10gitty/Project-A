import streamlit as st

# Define the prescribed ingredients for each disease
prescribed_ingredients = {
    "Cholesterol": ["Vegetables, legumes, fruit, wholegrains, nuts and seeds.", 
                     "Legumes or pulses such as chickpeas, lentils, split peas, beans such as haricot beans, kidney beans, baked beans , bean mixes.", 
                     "Wholegrain breads, cereals, pasta, rice and noodles"],
    "Triglycerides": ["Soy protein.", 
                       "Fatty fish like sardines, salmon, mackerel, and herring.", 
                       "Avocado.", 
                       "Whole grains like oatmeal, buckwheat, barley, and millet.", 
                       "Cauliflower, cabbage, broccoli, Brussels sprouts, bok choy, and kale."],
    "Diabetes": ["Whole grains, such as brown rice, oatmeal, quinoa, millet, or amaranth.", 
                 "Greens such as kale, spinach, and arugula.", 
                 "Skimmed milk.", 
                 "Plant-based proteins such as beans, nuts, seeds, or tofu.", 
                 "Tomatoes.", 
                 "Berries.", 
                 "Citrus fruits like grapefruits, oranges, lemons and limes."],
    "Osteoporosis": ["Whole grains, like quinoa, barley, oats, and brown rice.", 
                      "Lean proteins, such as poultry and fish.", 
                      "Nuts and seeds.", 
                      "Dairy products such as low-fat and non-fat milk, yogurt and cheese.", 
                      "Collard greens, turnip greens, kale, okra, Chinese cabbage, dandelion greens, mustard greens and broccoli."],
    "PCOS": ["Omega-3 rich fish  such as salmon, baked or broiled.", 
             "Olive oil.", 
             "Beans and other protein-rich legumes.", 
             "Non-starchy vegetables such as leafy greens (spinach, kale, escarole, endive, lettuce), tomatoes, mushrooms, peppers, broccoli, cauliflower.", 
             "Whole grains, such as brown rice, barley."]
}

# Create a checkbox list for the diseases
selected_diseases = st.multiselect(
    "Select the diseases you have been diagnosed with:",
    ["Cholesterol", "Triglycerides", "Diabetes", "Osteoporosis", "PCOS"]
)

# Display the prescribed ingredients for each selected disease
for disease in selected_diseases:
    st.write(f"## {disease}")
    st.write("Prescribed Ingredients:")
    for ingredient in prescribed_ingredients[disease]:
        st.write(f"- {ingredient}")
