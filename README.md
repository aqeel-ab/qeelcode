# QeelCode

QeelCode is a full-stack personal algorithm learning and practice platform built to improve problem-solving, algorithm knowledge, and software engineering skills.

The project combines a Vue.js frontend with a Python FastAPI backend to provide an interactive platform for exploring algorithm problems, solutions, patterns, complexity, and progress.

## 🚧 Project Status

QeelCode is currently **in development**.

The current version includes a dynamic Problems page, difficulty filters, problem detail pages, and FastAPI integration.

More algorithms and learning features will be added as the project develops.

---

## ✨ Features

- Browse algorithm problems
- Filter problems by difficulty
- View problem descriptions
- View algorithm approaches
- View algorithm patterns
- View time and space complexity
- View Python solutions
- View test results
- Dynamic problem data through FastAPI
- Dynamic problem detail pages
- Personal notes section
- Progress tracking foundation

---

## 🧩 Algorithms

The initial QeelCode learning roadmap includes 10 algorithm problems:

| # | Problem | Difficulty |
|---|---|---|
| 1 | Two Sum | Easy |
| 2 | Add Two Numbers | Medium |
| 3 | Longest Substring Without Repeating Characters | Medium |
| 4 | Median of Two Sorted Arrays | Hard |
| 5 | Longest Palindromic Substring | Medium |
| 6 | Zigzag Conversion | Medium |
| 7 | Reverse Integer | Medium |
| 8 | String to Integer (atoi) | Medium |
| 9 | Palindrome Number | Easy |
| 10 | Regular Expression Matching | Hard |

Currently implemented:

- ✅ Two Sum
- ✅ Add Two Numbers
- ⏳ Longest Substring Without Repeating Characters
- ⏳ Median of Two Sorted Arrays
- ⏳ Longest Palindromic Substring
- ⏳ Zigzag Conversion
- ⏳ Reverse Integer
- ⏳ String to Integer (atoi)
- ⏳ Palindrome Number
- ⏳ Regular Expression Matching

---

## 🛠️ Tech Stack

### Frontend

- Vue 3
- TypeScript
- Vite
- Vue Router
- HTML / CSS

### Backend

- Python
- FastAPI
- Uvicorn

### Testing

- Pytest
- Vitest

### Development Tools

- Git
- GitHub
- Visual Studio Code

---

## 📁 Project Structure

```text
qeelcode/
│
├── backend/
│   ├── data/
│   │   └── problems.py
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   └── src/
│       ├── router/
│       └── views/
│           ├── DashboardView.vue
│           ├── ProblemsView.vue
│           └── ProblemDetailView.vue
│
├── solutions/
│   ├── __init__.py
│   ├── two_sum.py
│   └── add_two_numbers.py
│
├── tests/
│   ├── test_two_sum.py
│   └── test_add_two_numbers.py
│
├── .gitignore
└── README.md