PROBLEMS = {
    "two-sum": {
        "number": 1,
        "title": "Two Sum",
        "difficulty": "Easy",
        "description": (
            "Given an array of integers and a target value, "
            "find the indices of two numbers that add up to the target."
        ),
        "approach": (
            "Use a hash map to store numbers that we have already seen. "
            "For each number, calculate the complement needed to reach "
            "the target and check whether it already exists in the hash map."
        ),
        "patterns": ["Array", "Hash Map"],
        "time_complexity": "O(n)",
        "space_complexity": "O(n)",
        "tests_passed": 3,
        "total_tests": 3,
        "solution_file": "two_sum.py",
    },
    "add-two-numbers": {
        "number": 2,
        "title": "Add Two Numbers",
        "difficulty": "Medium",
        "description": (
            "Add two numbers represented by linked lists "
            "and return the result as a linked list."
        ),
        "approach": (
            "Traverse both linked lists while keeping track of the carry "
            "from the previous digit. Create a new node for each result digit."
        ),
        "patterns": ["Linked List", "Math"],
        "time_complexity": "O(max(n, m))",
        "space_complexity": "O(max(n, m))",
        "tests_passed": 3,
        "total_tests": 3,
        "solution_file": "add_two_numbers.py",
    },
    
    "longest-substring": {
        "number": 3,
        "title": "Longest Substring Without Repeating Characters",
        "difficulty": "Medium",
        "description": (
            "Given a string, find the length of the longest "
            "substring without repeating characters."
        ),
        "approach": (
            "Use a sliding window with two pointers and a set. "
            "Expand the window as you iterate through the string. "
            "When a duplicate character appears, move the left "
            "pointer forward until the window contains unique characters."
        ),
        "patterns": ["String", "Sliding Window", "Hash Set"],
        "time_complexity": "O(n)",
        "space_complexity": "O(min(n, m))",
        "tests_passed": 5,
        "total_tests": 5,
        "solution_file": "longest_substring.py",
    },
    
    "median-two-sorted-arrays": {
        "number": 4,
        "title": "Median of Two Sorted Arrays",
        "difficulty": "Hard",
        "description": (
            "Given two sorted arrays, find the median of the "
            "two sorted arrays."
        ),
        "approach": (
            "Use binary search on the smaller array to find a "
            "partition where all elements on the left are less "
            "than or equal to all elements on the right."
        ),
        "patterns": ["Array", "Binary Search"],
        "time_complexity": "O(log(min(m, n)))",
        "space_complexity": "O(1)",
        "tests_passed": 7,
        "total_tests": 7,
        "solution_file": "median_two_sorted_arrays.py",
    },
    
    "longest-palindromic-substring": {
        "number": 5,
        "title": "Longest Palindromic Substring",
        "difficulty": "Medium",
        "description": (
            "Given a string, find the longest substring "
            "that reads the same forward and backward."
        ),
        "approach": (
            "Expand around every possible center. Check both "
            "odd-length and even-length palindromes, and keep "
            "the longest palindrome found."
        ),
        "patterns": ["String", "Two Pointers", "Expand Around Center"],
        "time_complexity": "O(n^2)",
        "space_complexity": "O(n)",
        "tests_passed": 7,
        "total_tests": 7,
        "solution_file": "longest_palindromic_substring.py",
    },
        "zigzag-conversion": {
        "number": 6,
        "title": "Zigzag Conversion",
        "difficulty": "Medium",
        "description": (
            "Convert a string into a zigzag pattern across a given "
            "number of rows, then read each row from top to bottom."
        ),
        "approach": (
            "Simulate the zigzag traversal by moving down through the "
            "rows and then diagonally upward, storing characters in each "
            "row and joining the rows at the end."
        ),
        "patterns": ["String", "Simulation"],
        "time_complexity": "O(n)",
        "space_complexity": "O(n)",
        "tests_passed": 8,
        "total_tests": 8,
        "solution_file": "zigzag_conversion.py",
    },
    
    "reverse-integer": {
        "number": 7,
        "title": "Reverse Integer",
        "difficulty": "Medium",
        "description": (
            "Given a signed 32-bit integer, reverse its digits. "
            "Return 0 if the reversed integer falls outside the "
            "signed 32-bit integer range."
        ),
        "approach": (
            "Extract the last digit using modulo, append it to the "
            "reversed number, and remove the last digit using "
            "integer division. Preserve the original sign and "
            "check for 32-bit integer overflow."
        ),
        "patterns": ["Math", "Integer Manipulation"],
        "time_complexity": "O(d)",
        "space_complexity": "O(1)",
        "tests_passed": 8,
        "total_tests": 8,
        "solution_file": "reverse_integer.py",
    },

}