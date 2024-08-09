import matplotlib.pyplot as plt
import numpy as np
import random

def generate_housie_ticket():
    # Define the ranges for each column
    column_ranges = [(1, 9), (10, 19), (20, 29), (30, 39), (40, 49),
                     (50, 59), (60, 69), (70, 79), (80, 90)]

    # Initialize the ticket with empty values
    ticket = [[0] * 9 for _ in range(3)]

    # Fill each column with numbers
    for col in range(9):
        nums = random.sample(range(column_ranges[col][0], column_ranges[col][1] + 1), 3)
        nums.sort()  # Sort numbers in ascending order
        for row in range(3):
            if len(nums) > 0:
                ticket[row][col] = nums.pop(0)

    # Ensure each row has exactly 5 numbers
    for row in ticket:
        num_positions = [i for i in range(9) if row[i] != 0]
        empty_positions = [i for i in range(9) if row[i] == 0]

        # If fewer than 5 numbers are present, add more numbers
        while len(num_positions) < 5:
            for col in range(9):
                if len(num_positions) >= 5:
                    break
                if ticket[0][col] == 0:
                    available_numbers = [i for i in range(column_ranges[col][0], column_ranges[col][1] + 1) if i not in [row[i] for row in ticket]]
                    if available_numbers:
                        new_number = random.choice(available_numbers)
                        ticket[random.choice(range(3))][col] = new_number
                        num_positions.append(col)

        # Randomly convert some numbers to empty cells to ensure exactly 5 numbers
        if len(num_positions) > 5:
            num_positions_to_empty = random.sample(num_positions, len(num_positions) - 5)
            for pos in num_positions_to_empty:
                row[pos] = " "

    return ticket

def plot_ticket(ticket):
    fig, ax = plt.subplots(figsize=(10, 4))

    # Create a grid of cells
    table_data = np.array(ticket)

    # Plot the table without row labels
    ax.table(cellText=table_data, loc='center', cellLoc='center', colWidths=[0.1] * 9)
    ax.axis('off')  # Hide the axis

    plt.title('Housie Ticket')
    plt.show()

# Generate a Housie ticket
ticket = generate_housie_ticket()

# Plot the ticket using matplotlib
plot_ticket(ticket)