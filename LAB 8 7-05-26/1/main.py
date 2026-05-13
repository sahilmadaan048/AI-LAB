# Program 1: Robot Traversal Using Means-End Analysis

start = (0, 0)
goal = (3, 3)

x, y = start
gx, gy = goal

step = 1

print(f"Initial: {start} Goal: {goal} diff: {gx-x},{gy-y}")

while (x, y) != goal:
    dx = gx - x
    dy = gy - y

    if dx > 0:
        x += 1
        move = "MoveRight"

    elif dx < 0:
        x -= 1
        move = "MoveLeft"

    elif dy > 0:
        y += 1
        move = "MoveUp"

    elif dy < 0:
        y -= 1
        move = "MoveDown"

    print(f"Step {step}: {move} -> ({x},{y}) diff: {gx-x},{gy-y}")

    step += 1

print("GOAL REACHED")
print("Total moves:", step - 1)