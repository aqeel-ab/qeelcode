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
}