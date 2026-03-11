import streamlit as st
import pandas as pd

# ------------------------------
# Sidebar Navigation
# ------------------------------
st.sidebar.title("Home Fitness App")
page = st.sidebar.radio("Go to:", ["Home", "Workout Tracker", "Nutrition", "About"])

# ------------------------------
# HOME PAGE
# ------------------------------
if page == "Home":
    st.title("Home Fitness App")
    st.header("Welcome to Your Fitness Companion")
    st.text("Track workouts, monitor nutrition, and stay motivated!")

    # Inputs
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=10, max_value=100)
    goal = st.selectbox("Choose your fitness goal:", ["Lose Weight", "Build Muscle", "Stay Fit"])
    st.write(f"Hello {name}, your goal is: {goal}")

    # Fun components
    days = st.slider("How many workout days per week?", 1, 7, 3)
    time_pref = st.radio("Preferred workout time:", ["Morning", "Afternoon", "Evening"])
    theme_color = st.color_picker("Pick your favorite home workout color theme")

    # Confirmation button
    if st.button("Confirm Details"):
        if name and age and goal:
            st.session_state["user_goal"] = goal  # Save goal for later use
            st.success(f"✅ Thanks {name}! Your fitness goal '{goal}' has been saved.")
        else:
            st.warning("⚠️ Please fill in all required details before confirming.")

# ------------------------------
# WORKOUT TRACKER PAGE
# ------------------------------
elif page == "Workout Tracker":
    st.title("📋 Home Workout Tracker")

    # Retrieve saved goal
    goal = st.session_state.get("user_goal", None)

    if goal:
        st.subheader(f"Recommended Exercises for {goal}")

        # Difficulty level selection
        difficulty = st.selectbox("Select difficulty level:", ["Easy", "Medium", "Intermediate"])

        if goal == "Lose Weight":
            if difficulty == "Easy":
                exercises = pd.DataFrame({
                    "Exercise": ["March in Place", "Wall Push Ups", "Seated March"],
                    "Sets": [2, 2, 2],
                    "Reps": ["2 min", "10 reps", "2 min"]
                })
                exercises = exercises[["Exercise", "Reps", "Sets"]]
            elif difficulty == "Medium":
                exercises = pd.DataFrame({
                    "Exercise": ["Jumping Jacks", "Burpees", "Mountain Climbers"],
                    "Sets": [3, 3, 3],
                    "Reps": ["30 sec", "15 reps", "30 sec"]
                })
                exercises = exercises[["Exercise", "Reps", "Sets"]]
            elif difficulty == "Intermediate":
                exercises = pd.DataFrame({
                    "Exercise": ["High Knees", "Burpee Box Jumps", "Spiderman Climbs"],
                    "Sets": [3, 3, 3],
                    "Reps": ["45 sec", "20 reps", "45 sec"]
                })
                exercises = exercises[["Exercise", "Reps", "Sets"]]
        elif goal == "Build Muscle":
            if difficulty == "Easy":
                exercises = pd.DataFrame({
                    "Exercise": ["Wall Push Ups", "Chair Squats", "Standing Lunges"],
                    "Sets": [2, 2, 2],
                    "Reps": [8, 8, 8]
                })
                exercises = exercises[["Exercise", "Reps", "Sets"]]
            elif difficulty == "Medium":
                exercises = pd.DataFrame({
                    "Exercise": ["Push Ups", "Squats", "Lunges"],
                    "Sets": [2, 2, 2],
                    "Reps": [15, 12, 12]
                })
                exercises = exercises[["Exercise", "Reps", "Sets"]]
            elif difficulty == "Intermediate":
                exercises = pd.DataFrame({
                    "Exercise": ["Diamond Push Ups", "Jump Squats", "Walking Lunges"],
                    "Sets": [3, 3, 3],
                    "Reps": [12, 15, 16]
                })
                exercises = exercises[["Exercise", "Reps", "Sets"]]
        elif goal == "Stay Fit":
            if difficulty == "Easy":
                exercises = pd.DataFrame({
                    "Exercise": ["Seated Plank", "Gentle Yoga", "Slow Walking"],
                    "Sets": [2, 1, 2],
                    "Reps": ["30 sec", "5 min", "10 min"]
                })
                exercises = exercises[["Exercise", "Reps", "Sets"]]
            elif difficulty == "Medium":
                exercises = pd.DataFrame({
                    "Exercise": ["Plank", "Yoga Stretch", "Walking"],
                    "Sets": [2, 1, 1],
                    "Reps": ["60 sec", "10 min", "20 min"]
                })
                exercises = exercises[["Exercise", "Reps", "Sets"]]
            elif difficulty == "Intermediate":
                exercises = pd.DataFrame({
                    "Exercise": ["Side Plank", "Power Yoga", "Brisk Walking"],
                    "Sets": [2, 1, 1],
                    "Reps": ["45 sec each side", "15 min", "30 min"]
                })
                exercises = exercises[["Exercise", "Reps", "Sets"]]

        exercises.index = range(1, len(exercises) + 1)
        st.dataframe(exercises)
    else:
        st.info("ℹ️ Please confirm your fitness goal on the Home page first.")

    # User input logging
    st.text_area("Log your workout here:")
    st.file_uploader("Upload your home workout plan (PDF/Excel)")
    st.date_input("Select workout date")
    st.time_input("Workout start time")

    # Motivation
    if st.button("Generate Motivation Quote"):
        st.success("💪 Keep pushing, progress takes time!")

# ------------------------------
# NUTRITION PAGE
# ------------------------------
elif page == "Nutrition":
    st.title("🥗 Nutrition Tracker")

    # Retrieve saved goal
    goal = st.session_state.get("user_goal", None)

    if goal:
        st.subheader(f"Recommended Foods for {goal}")

        if goal == "Lose Weight":
            foods_df = pd.DataFrame({"Food": ["Salad", "Grilled Chicken", "Broccoli", "Berries", "Green Tea"]})
        elif goal == "Build Muscle":
            foods_df = pd.DataFrame({"Food": ["Eggs", "Salmon", "Sweet Potatoes", "Greek Yogurt", "Nuts"]})
        elif goal == "Stay Fit":
            foods_df = pd.DataFrame({"Food": ["Oats", "Bananas", "Avocados", "Spinach", "Whole Grain Bread"]})

        foods_df.index = range(1, len(foods_df) + 1)
        st.dataframe(foods_df)
    else:
        st.info("ℹ️ Please confirm your fitness goal on the Home page first.")

    # Water intake tracker
    water_glasses = st.slider("Glasses of water consumed today:", 0, 12, 0)
    st.write(f"Water intake: {water_glasses} glasses (recommended: 8 glasses/day)")
    st.progress(water_glasses / 8 if water_glasses <= 8 else 1.0)

    # Meal logging
    st.subheader("Today's Meals")
    breakfast = st.text_input("Breakfast:")
    lunch = st.text_input("Lunch:")
    dinner = st.text_input("Dinner:")
    snacks = st.text_input("Snacks:")

    if st.button("Log Meals"):
        if any([breakfast, lunch, dinner, snacks]):
            st.success("✅ Meals logged successfully!")
        else:
            st.warning("⚠️ Please enter at least one meal.")

    

# ------------------------------
# ABOUT PAGE
# ------------------------------
elif page == "About":
    st.title("ℹ️ About This App")
    st.write("""
    **What it does:**  
    A simple home fitness app for tracking workouts and nutrition. Pick your goal (lose weight, build muscle, or stay fit) and get personalized exercises and food suggestions.

    **Who it's for:**  
    Anyone who wants to exercise at home beginners, busy people, or those without gym equipment.

    **Inputs collected:**  
    - Your name and age  
    - Your fitness goal (lose weight, build muscle, or stay fit)  
    - How many days a week you want to work out, what time of day you prefer, and even your favorite color for the theme  
    - Difficulty level for exercises (easy, medium, or intermediate)  
    - How many glasses of water you've had today, and what you ate for breakfast, lunch, dinner, and snacks  
    
    **Outputs displayed:**  
    - A greeting with your name and goal  
    - Messages saying your info was saved or meals were logged  
    - Lists of exercises with sets and reps that match your goal and skill level  
    - Food suggestions based on what you're trying to achieve  
    - A progress bar showing how much water you've drunk compared to the daily goal of 8 glasses  
    - Success or warning messages depending on what you do  
    - Just general helpful feedback to keep you motivated  
    """)