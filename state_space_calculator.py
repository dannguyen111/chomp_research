import math

def calculate_chomp_states(rows, cols):
    """
    Calculates the total number of game states for an
    m x n Chomp board using the binomial coefficient (n+m) C m.
    
    Args:
        rows (int): The number of rows (m).
        cols (int): The number of columns (n).
        
    Returns:
        int: The total number of possible game states.
    """
    if rows <= 0 or cols <= 0:
        return 0
        
    # Total steps in the grid path
    total_steps = rows + cols
    
    # Calculate (rows + cols) CHOOSE (rows)
    # This is equivalent to (rows + cols) CHOOSE (cols)
    num_states = math.comb(total_steps, rows)
    
    return num_states

def main():
    """
    Main function to get user input and print the result.
    """
    try:
        m_rows = int(input("Enter the number of rows (m): "))
        n_cols = int(input("Enter the number of columns (n): "))

        if m_rows <= 0 or n_cols <= 0:
            print("Rows and columns must be positive integers.")
            return

        total_states = calculate_chomp_states(m_rows, n_cols)
        
        print(f"\nFor an {m_rows} x {n_cols} Chomp board:")
        print(f"Total number of game states = {total_states:,}")

    except ValueError:
        print("Invalid input. Please enter integers for rows and columns.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()