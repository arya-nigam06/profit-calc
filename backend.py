import json

# Load default values from a JSON file
def load_defaults():
    with open("defaults.json", "r") as file:
        return json.load(file)

# Save updated values to the JSON file
def save_defaults(updated_values):
    with open("defaults.json", "w") as file:
        json.dump(updated_values, file)

# Perform calculations
def calculate_profit(data):
    # Extract values
    a, b, c, z = data["a"], data["b"], data["c"], data["z"]
    d, e, f, x = data["d"], data["e"], data["f"], data["x"]
    g, h, i = data["g"], data["h"], data["i"]
    m, l, o, j, n, k = data["m"], data["l"], data["o"], data["j"], data["n"], data["k"]

    # # Hidden calculation
    # y = x - (f / 2)

    # Income calculations
    p = a * d
    q = b * e
    r = c * f + x*z
    t = a * d + b * e + c * f + x* z

    # Investment calculations
    s = a * g + b * h + c * i + j + k + l + m + n + o

    # Profit
    total_profit = t - s

    return {
        "p": p,
        "q": q,
        "r": r,
        "t": t,
        "s": s,
        "total_profit": total_profit,
    }
