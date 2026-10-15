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

### Completed Algorithms

| # | Problem | Difficulty | Status |
|---|---|---|---|
| 1 | Two Sum | Easy | Completed |
| 2 | Add Two Numbers | Medium | Completed |
| 3 | Longest Substring Without Repeating Characters | Medium | Completed |
| 4 | Median of Two Sorted Arrays | Hard | Completed |
| 5 | Longest Palindromic Substring | Medium | Completed |
| 6 | Zigzag Conversion | Medium | Completed |
| 7 | Reverse Integer | Medium | Completed |
| 8 | String to Integer (atoi) | Medium | Completed |
| 9 | Palindrome Number | Easy | Completed |
| 10 | Regular Expression Matching | Hard | Completed |

### Upcoming Milestones

- [x] Algorithms 1–10
- [ ] Algorithms 11–20
- [ ] Algorithms 21–30
- [ ] Algorithms 31–40
- [ ] Algorithms 41–50
- [ ] Algorithms 51–60
- [ ] Algorithms 61–70
- [ ] Algorithms 71–80
- [ ] Algorithms 81–90
- [ ] Algorithms 91–100

**Target completion date:** 30 November 2026

---

## 🛠️ Tech Stack

### Frontend

- Vue 3
- JavaScript
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
```

## Running the Project Locally

### 1. Start the Backend

Open a terminal from the project root:

```bash
cd backend
.venv\Scripts\activate
uvicorn main:app --reload
```

The backend runs at `http://127.0.0.1:8000`.

### 2. Start the Frontend

Open another terminal from the project root:

```bash
cd frontend
npm install
npm run dev
```

Open the local URL shown in the terminal, usually `http://localhost:5173`.

### 3. Run Automated Tests

From the project root, using the Python environment where Pytest is installed:

```bash
python -m pytest
```

## Development Workflow

Each new algorithm follows this workflow:

1. Implement the Python solution.
2. Verify the solution with manual examples.
3. Write automated tests.
4. Run the full test suite.
5. Add problem metadata to the FastAPI backend.
6. Verify the problem on the Vue.js frontend.
7. Commit and push the changes to GitHub.

## Future Improvements

- Expand the algorithm collection to 100 problems.
- Improve the dashboard and progress overview.
- Add search and more flexible problem filtering.
- Improve the user experience of problem detail pages.
- Explore additional learning and progress-tracking features.

## Author

Developed as a personal portfolio project to practise algorithmic problem-solving, Python development, full-stack engineering, automated testing and Git-based workflows.