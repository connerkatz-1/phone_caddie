import streamlit as st

st.title("Phone Caddie")

st.write("Improve your golf practice by tracking your shots and getting instant feedback on your consistency.")

#Input 1: Select Club Type

club = st.selectbox(
    "Select the club you used:",
    ["Driver", "3-Wood", "5-Wood", "3-Hybrid", "5-Hybrid",
   "7-Wood", "1-Iron", "2-Iron", "3-Iron", "4-Iron", "5-Iron",
     "6- Iron", "7-Iron", "8-Iron", "9-Iron", "Pitching Wedge",
       "Approach Wedge", "52", "54", "56", "58", "60"  ]
)

# Input 2: Select shot result
shot_result = st.radio(
    "Where did your shot go?",
    ["Left", "Straight", "Right"]
)

# Input 3: Number of shots
shots = st.number_input(
    "How many shots did you take?",
    min_value=1,
    max_value=15
)
   

# Output (changes based on input)
st.subheader("Your Feedback:")

if shot_result == "Left":
    st.write(f"You tend to pull your {club.lower()} shots.")
    st.write("👉 Try adjusting your grip and aim slightly right.")
elif shot_result == "Right":
    st.write(f"You tend to push your {club.lower()} shots.")
    st.write("👉 Focus on closing the clubface and aligning properly.")
else:
    st.write(f"Great job! Your {club.lower()} shots are going straight.")
    st.write("👉 Keep practicing for consistency!")

st.write(f"Session Summary: You hit {shots} shots with your {club}.")