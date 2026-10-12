from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from data.problems import PROBLEMS

app = FastAPI(title="QeelCode API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "QeelCode API is running"}


@app.get("/api/problems/{slug}")
@app.get("/api/problems/{slug}")
def get_problem(slug: str):
    problem = PROBLEMS.get(slug)

    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")

    solution_path = (
        Path(__file__).resolve().parent.parent
        / "solutions"
        / problem["solution_file"]
    )

    if not solution_path.exists():
        raise HTTPException(status_code=404, detail="Solution file not found")

    solution = solution_path.read_text(encoding="utf-8")

    return {
        **problem,
        "solution": solution,
    }