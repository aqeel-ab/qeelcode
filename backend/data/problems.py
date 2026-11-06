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
    
    "string-to-integer-atoi": {
        "number": 8,
        "title": "String to Integer (atoi)",
        "difficulty": "Medium",
        "description": (
            "Convert a string into a 32-bit signed integer, handling "
            "leading whitespace, an optional sign, digits, and overflow."
        ),
        "approach": (
            "Skip leading whitespace, detect the optional sign, and "
            "read digits until a non-digit character appears. Apply "
            "the sign and clamp the result to the 32-bit integer range."
        ),
        "patterns": ["String", "Parsing"],
        "time_complexity": "O(n)",
        "space_complexity": "O(1)",
        "tests_passed": 12,
        "total_tests": 12,
        "solution_file": "string_to_integer.py",
    },
    
    "palindrome-number": {
        "number": 9,
        "title": "Palindrome Number",
        "difficulty": "Easy",
        "description": (
            "Given an integer x, return True if x reads the same "
            "forward and backward, otherwise return False."
        ),
        "approach": (
            "Return False for negative numbers. Reverse the digits "
            "using modulo and integer division, then compare the "
            "reversed number with the original number."
        ),
        "patterns": ["Math", "Integer Manipulation"],
        "time_complexity": "O(d)",
        "space_complexity": "O(1)",
        "tests_passed": 9,
        "total_tests": 9,
        "solution_file": "palindrome_number.py",
    },
    
    "regular-expression-matching": {
        "number": 10,
        "title": "Regular Expression Matching",
        "difficulty": "Hard",
        "description": (
            "Implement regular expression matching with support for "
            "'.' matching any single character and '*' matching zero "
            "or more occurrences of the preceding element."
        ),
        "approach": (
            "Use dynamic programming. Each state represents whether "
            "a prefix of the string matches a prefix of the pattern. "
            "Handle '.' as a single-character match and '*' as either "
            "zero occurrences or one or more matching occurrences."
        ),
        "patterns": ["String", "Dynamic Programming"],
        "time_complexity": "O(m * n)",
        "space_complexity": "O(m * n)",
        "tests_passed": 12,
        "total_tests": 12,
        "solution_file": "regular_expression_matching.py",
    },
    "container-with-most-water": {
        "number": 11,
        "title": "Container With Most Water",
        "difficulty": "Medium",
        "description": (
            "Given an array of heights, find two lines that together "
            "with the x-axis form a container that holds the most water."
        ),
        "approach": (
            "Use two pointers starting at both ends of the array. "
            "Calculate the area formed by the lines at these pointers, "
            "then move the pointer pointing to the shorter line inward. "
            "Repeat until the pointers meet."
        ),
        "patterns": ["Array", "Two Pointers"],
        "time_complexity": "O(n)",
        "space_complexity": "O(1)",
        "tests_passed": 4,
        "total_tests": 4,
        "solution_file": "container_with_most_water.py",
    },
    "integer-to-roman": {
        "number": 12,
        "title": "Integer to Roman",
        "difficulty": "Medium",
        "description": "Convert an integer to its Roman numeral representation.",
        "approach": "Greedy: repeatedly use the largest Roman numeral value that fits.",
        "patterns": ["Math", "Greedy"],
        "time_complexity": "O(1)",
        "space_complexity": "O(1)",
        "tests_passed": 4,
        "total_tests": 4,
        "solution_file": "integer_to_roman.py",
    },
    "roman-to-integer": {
        "number": 13,
        "title": "Roman to Integer",
        "difficulty": "Easy",
        "description": "Convert a Roman numeral string to an integer.",
        "approach": "Scan the symbols; subtract a value when it is smaller than the next symbol, otherwise add it.",
        "patterns": ["Hash Map", "Math"],
        "time_complexity": "O(n)",
        "space_complexity": "O(1)",
        "tests_passed": 5,
        "total_tests": 5,
        "solution_file": "roman_to_integer.py",
    },
    "longest-common-prefix": {
        "number": 14,
        "title": "Longest Common Prefix",
        "difficulty": "Easy",
        "description": "Find the longest common prefix shared by all strings.",
        "approach": "Start with the first string and shorten the prefix until every string starts with it.",
        "patterns": ["String", "Trie"],
        "time_complexity": "O(S)",  # S is the total number of characters checked
        "space_complexity": "O(1)",
        "tests_passed": 5,
        "total_tests": 5,
        "solution_file": "longest_common_prefix.py",
    },
    "3sum": {
        "number": 15,
        "title": "3Sum",
        "difficulty": "Medium",
        "description": (
            "Given an integer array, return all unique triplets "
            "whose values sum to zero."
        ),
        "approach": (
            "Sort the array, then fix one value and use two pointers "
            "to find pairs that complete a sum of zero. Skip duplicate "
            "values to avoid returning duplicate triplets."
        ),
        "patterns": ["Array", "Sorting", "Two Pointers"],
        "time_complexity": "O(n^2)",
        "space_complexity": "O(1) auxiliary space, excluding the output",
        "tests_passed": 4,
        "total_tests": 4,
        "solution_file": "three_sum.py",
    },
    "3sum-closest": {
        "number": 16,
        "title": "3Sum Closest",
        "difficulty": "Medium",
        "description": "Find three integers whose sum is closest to the target.",
        "approach": "Sort the array, then use two pointers for each fixed number.",
        "patterns": ["Array", "Two Pointers", "Sorting"],
        "time_complexity": "O(n²)",
        "space_complexity": "O(1)",
        "tests_passed": 4,
        "total_tests": 4,
        "solution_file": "three_sum_closest.py",
    },
    "letter-combinations": {
        "number": 17,
        "title": "Letter Combinations of a Phone Number",
        "difficulty": "Medium",
        "description": (
            "Given a string containing digits from 2 to 9, return "
            "all possible letter combinations that the digits could represent."
        ),
        "approach": (
            "Build combinations one digit at a time. For each existing "
            "combination, append every letter mapped to the current digit."
        ),
        "patterns": ["String", "Backtracking", "Combinations"],
        "time_complexity": "O(3^n * 4^m), where n digits map to 3 letters and m digits map to 4",
        "space_complexity": "O(3^n * 4^m)",
        "tests_passed": 4,
        "total_tests": 4,
        "solution_file": "letter_combinations.py",
    },
    "4sum": {
        "number": 18,
        "title": "4Sum",
        "difficulty": "Medium",
        "description": "Find all unique quadruplets in the array that sum to the target.",
        "approach": "Sort the array, fix two values, then use two pointers to find the remaining pair while skipping duplicates.",
        "patterns": ["Array", "Two Pointers", "Sorting"],
        "time_complexity": "O(n³)",
        "space_complexity": "O(1) auxiliary, excluding the result",
        "tests_passed": 4,
        "total_tests": 4,
        "solution_file": "four_sum.py",
    },
    "remove-nth-node-from-end": {
        "number": 19,
        "title": "Remove Nth Node From End of List",
        "difficulty": "Medium",
        "description": (
            "Given the head of a linked list, remove the nth node "
            "from the end of the list and return its head."
        ),
        "approach": (
            "Use a dummy node and two pointers. Move the fast pointer "
            "n + 1 steps ahead, then move both pointers until fast "
            "reaches the end. Remove the target node after slow."
        ),
        "patterns": ["Linked List", "Two Pointers"],
        "time_complexity": "O(n)",
        "space_complexity": "O(1)",
        "tests_passed": 4,
        "total_tests": 4,
        "solution_file": "remove_nth_node.py",
    },
    "valid-parentheses": {
        "number": 20,
        "title": "Valid Parentheses",
        "difficulty": "Easy",
        "description": (
            "Given a string containing brackets, determine whether "
            "the brackets are properly opened, closed, and nested."
        ),
        "approach": (
            "Use a stack to track opening brackets. For each closing "
            "bracket, check that the stack's top contains its matching "
            "opening bracket. The string is valid if no mismatch occurs "
            "and the stack is empty at the end."
        ),
        "patterns": ["String", "Stack"],
        "time_complexity": "O(n)",
        "space_complexity": "O(n)",
        "tests_passed": 5,
        "total_tests": 5,
        "solution_file": "valid_parentheses.py",
    },
    "merge-two-sorted-lists": {
        "number": 21,
        "title": "Merge Two Sorted Lists",
        "difficulty": "Easy",
        "description": (
            "Given the heads of two sorted linked lists, merge them "
            "into one sorted linked list and return its head."
        ),
        "approach": (
            "Use a dummy node and a current pointer. Compare the nodes "
            "at the heads of both lists, attach the smaller one, and "
            "advance that list. Finally, attach any remaining nodes."
        ),
        "patterns": ["Linked List", "Two Pointers"],
        "time_complexity": "O(n + m)",
        "space_complexity": "O(1)",
        "tests_passed": 4,
        "total_tests": 4,
        "solution_file": "merge_two_sorted_lists.py",
    },
    "generate-parentheses": {
        "number": 22,
        "title": "Generate Parentheses",
        "difficulty": "Medium",
        "description": "Generate all combinations of well-formed parentheses for n pairs.",
        "approach": "Use backtracking to build valid combinations by tracking the number of opening and closing parentheses.",
        "patterns": ["String", "Dynamic Programming", "Backtracking"],
        "time_complexity": "O(4^n / √n)",
        "space_complexity": "O(4^n / √n)",
        "tests_passed": 5,
        "total_tests": 5,
        "solution_file": "generate_parentheses.py",
    },
}