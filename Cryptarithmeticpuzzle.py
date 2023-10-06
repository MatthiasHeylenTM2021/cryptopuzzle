from itertools import permutations

# Function to check if a given assignment satisfies the equation
def is_solution(assignment, word1, word2, result):
    val1 = sum(assignment[char] * (10 ** (len(word1) - i - 1)) for i, char in enumerate(word1))
    val2 = sum(assignment[char] * (10 ** (len(word2) - i - 1)) for i, char in enumerate(word2))
    val3 = sum(assignment[char] * (10 ** (len(result) - i - 1)) for i, char in enumerate(result))
    return val1 + val2 == val3

# Function to solve the cryptarithmetic puzzle
def solve_cryptarithmetic(word1, word2, result):
    # Extract unique characters from the words
    unique_chars = set(word1 + word2 + result)
    
    # Check if there are more than 10 unique characters (invalid puzzle)
    if len(unique_chars) > 10:
        return None
    
    # Generate all possible permutations of digits from 0 to 9
    for perm in permutations(range(10), len(unique_chars)):
        assignment = {char: digit for char, digit in zip(unique_chars, perm)}
        
        # Check if the assignment is valid (no leading zeros)
        if '0' not in assignment.values():
            
            # Check if the assignment satisfies the equation
            if is_solution(assignment, word1, word2, result):
                return assignment
    
    # No solution found
    return None

# Input equation from the user
word1 = input("Enter the first word: ").upper()
word2 = input("Enter the second word: ").upper()
result = input("Enter the result word: ").upper()

# Solve the cryptarithmetic puzzle
solution = solve_cryptarithmetic(word1, word2, result)

if solution:
    print("Solution found:")
    for char, digit in solution.items():
        print(f"{char}: {digit}")
else:
    print("No solution found.")
