# Program 2: Block World Using Means-End Analysis

state = {
    "A": "table",
    "B": "table",
    "C": "table"
}

print("Initial State:")
print(state)

steps = []

# Step 1: pickup(B)
steps.append("pickup(B)")

# Step 2: stack(B, A)
state["B"] = "A"
steps.append("stack(B, A)")

# Step 3: pickup(C)
steps.append("pickup(C)")

# Step 4: stack(C, B)
state["C"] = "B"
steps.append("stack(C, B)")

print("\nSteps:")

for i, s in enumerate(steps, start=1):
    print(f"Step {i}: {s}")

print("\nGoal State:")
print(state)