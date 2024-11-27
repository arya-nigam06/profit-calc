import streamlit as st
from backend import load_defaults, save_defaults, calculate_profit

# Load default values
defaults = load_defaults()

# Streamlit App
st.set_page_config(page_title="Shop Calculator", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Plates Count", "Updates"])

# Function to safely convert input to float, or use default value if invalid
def get_float_input(field_label, default_value):
    user_input = st.text_input(field_label, value=str(default_value))
    try:
        return float(user_input)
    except ValueError:
        return default_value

# Page 1: Plates Count
if page == "Plates Count":
    st.title("Plates Count")

    # User inputs for plate counts, use default if empty
    st.subheader("Enter number of plates sold:")
    a = get_float_input("Chicken Momo Plates (a):", defaults["a"])
    b = get_float_input("Paneer Momo Plates (b):", defaults["b"])
    c = get_float_input("Veg Momo Plates (c):", defaults["c"])
    z = get_float_input("Half Veg Plates (z):", defaults["z"])

    # Extras: Input fields at the bottom of the page
    st.subheader("Extras (use default if not provided):")
    m = get_float_input("Chutney (m) (default=100):", defaults["m"])
    l = get_float_input("Disposal (l) (default=50):", defaults["l"])
    o = get_float_input("Miscellaneous (o) (default=100):", defaults["o"])
    j = get_float_input("Rent (j) (default=100):", defaults["j"])
    n = get_float_input("Worker (n) (default=300):", defaults["n"])
    k = get_float_input("Gas (k) (default=100):", defaults["k"])

    # Button to calculate
    if st.button("Calculate"):
        # Calculate with the user's input or default values
        data = {**defaults, "a": a, "b": b, "c": c, "z": z, "m": m, "l": l, "o": o, "j": j, "n": n, "k": k}
        results = calculate_profit(data)

        # Show results
        st.write(f"Chicken Momo Sale (p): ${results['p']:.2f}")
        st.write(f"Paneer Momo Sale (q): ${results['q']:.2f}")
        st.write(f"Veg Momo Sale (r): ${results['r']:.2f}")
        st.write(f"Total Income (t): ${results['t']:.2f}")
        st.write(f"Total Investment (s): ${results['s']:.2f}")

        # Highlight profit
        total_profit = results["total_profit"]
        profit_color = "green" if total_profit >= 0 else "red"
        st.markdown(
            f"<h3 style='color:{profit_color}'>Total Profit: ${total_profit:.2f}</h3>",
            unsafe_allow_html=True,
        )


# Page 2: Updates
elif page == "Updates":
    st.title("Update Values")

    # Editable fields for updates
    st.subheader("Update Default Values:")

    # Exclude keys that should not be updated
    excluded_keys = {"a", "b", "c", "z"}
    for key, value in defaults.items():
        if key not in excluded_keys:
            field_name = {
                "d": "Chicken Momo Price (d)",
                "e": "Paneer Momo Price (e)",
                "f": "Veg Momo Price (f)",
                "x": "Veg Half Plate Price (x)",
                "g": "Cost of 1 Chicken Plate (g)",
                "h": "Cost of 1 Paneer Plate (h)",
                "i": "Cost of 1 Veg Plate (i)",
                "m": "Chutney (m)",
                "l": "Disposal (l)",
                "o": "Miscellaneous (o)",
                "j": "Rent (j)",
                "n": "Worker (n)",
                "k": "Gas (k)",
            }
            field_label = f"{field_name.get(key, key)} (default={value}):"
            defaults[key] = get_float_input(field_label, value)

    # Buttons to save or temporary update
    if st.button("Update"):
        save_defaults(defaults)
        st.success("Default values updated.")
