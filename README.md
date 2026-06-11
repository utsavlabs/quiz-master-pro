# Quiz Master Pro v2.0 — GUI Edition 📝

## A Python Tkinter GUI Quiz Application

**Version:** 2.0 (GUI Edition)  
**Language:** Python 3.x (Pure Python — Tkinter only, no external libraries)  
**Type:** College Mini-Project  
**Date:** June 2026  

---

## 📖 Project Description

**Quiz Master Pro** is a professional GUI quiz application built using Python's built-in **Tkinter** library. It tests users on **beginner Python programming** through 10 multiple-choice questions spanning topics such as Variables, Loops, Lists, Strings, Data Types, and more.

The application features a polished dark-themed interface with:
- A welcome screen with name entry
- One question displayed at a time with clickable A/B/C/D answer buttons
- Instant visual feedback (green for correct, red for incorrect)
- A final results dashboard showing score, percentage, grade, and a progress bar
- A persistent high-score leaderboard saved in `scores.txt`
- Play-again functionality

It demonstrates core programming concepts including **OOP (class-based design)**, **GUI programming**, **file I/O**, **input validation**, **error handling**, **control flow**, and **data structures** — making it an ideal submission for a college-level mini-project.

---

## 📁 Folder Structure

```
miniproject-1/
│
├── quiz_master_pro.py      # Main GUI application source code
├── README.md               # Project documentation (this file)
├── viva_questions.md        # Viva Q&A for exam preparation
│
└── scores.txt              # (Auto-generated) High score records
```

---

## ⚙️ How to Run

### Prerequisites

- **Python 3.6 or higher** installed on your system.
- **Tkinter** must be available (it ships with standard Python on Windows and macOS; on Linux, install with `sudo apt install python3-tk`).
- **No external libraries** are required.

### Step-by-Step Instructions

1. **Open a terminal / command prompt.**

2. **Navigate to the project folder:**
   ```bash
   cd path\to\miniproject-1
   ```

3. **Run the application:**
   ```bash
   python quiz_master_pro.py
   ```

4. **The GUI window will open:**
   - Enter your name on the welcome screen.
   - Click **"Start Quiz"** to begin.
   - Click one of the four answer buttons (A, B, C, D) for each question.
   - View instant feedback (green = correct, red = incorrect).
   - Click **"Next Question"** to proceed.
   - After all 10 questions, view your **final results** (score, percentage, grade).
   - Click **"Play Again"** to retake the quiz, **"High Scores"** to view the leaderboard, or **"Exit"** to close.

---

## ✨ Features List

| #  | Feature                          | Description                                              |
|----|----------------------------------|----------------------------------------------------------|
| 1  | Professional Tkinter GUI         | Dark-themed, polished interface with styled widgets       |
| 2  | Welcome Screen                   | Name entry field with validation and start button         |
| 3  | 10 Multiple-Choice Questions     | 10 beginner Python questions                              |
| 4  | Randomized Question Order        | Questions are shuffled each playthrough                   |
| 5  | Clickable Answer Buttons         | Four A/B/C/D option buttons per question                  |
| 6  | Instant Visual Feedback          | Green highlight for correct, red for incorrect             |
| 7  | Running Score Display            | Live score counter in the top bar                         |
| 8  | Progress Bar                     | Visual progress indicator during the quiz                 |
| 9  | Topic Tags                       | Each question displays its category                       |
| 10 | Final Results Dashboard          | Score, percentage, grade, verdict, and progress bar       |
| 11 | Grade Assignment                 | A/B/C/D/F grading based on percentage thresholds          |
| 12 | High Score Leaderboard           | Top 10 scores with rank indicators                        |
| 13 | Persistent Score Storage         | All scores saved to `scores.txt`                          |
| 14 | Play Again Option                | Replay without restarting the program                     |
| 15 | Input Validation                 | Name must be non-empty, letters and spaces only           |
| 16 | Error Handling                   | Graceful handling of file I/O and edge cases              |
| 17 | OOP Architecture                 | Clean class-based code structure                          |
| 18 | Cross-Platform Compatible        | Works on Windows, macOS, and Linux                        |

---

## 🎓 Grading Scale

| Percentage   | Grade | Verdict              |
|--------------|-------|----------------------|
| 90 – 100%   | A     | Outstanding!          |
| 80 – 89%    | B     | Great Job!            |
| 70 – 79%    | C     | Good Effort!          |
| 60 – 69%    | D     | Needs Improvement     |
| Below 60%   | F     | Better Luck Next Time |

---

## 📚 Question Topics

### Beginner Python Programming (10 questions)
- Variables & Data Types
- Input and Output
- Strings & String Methods
- If-Else Statements
- For Loops & While Loops
- Lists & List Methods
- Break & Continue Statements

---

## 🔮 Future Enhancements

1. **Difficulty Levels** — Add Easy, Medium, and Hard modes with varying question complexity.
2. **Timed Questions** — Introduce a countdown timer for each question using `after()`.
3. **Category Selection** — Allow users to choose specific topics before starting.
4. **Multiplayer Mode** — Support two or more players competing in the same session.
5. **Question Bank Expansion** — Load questions from an external JSON file.
6. **Hint System** — Provide optional hints that reduce the score reward.
7. **Statistics Dashboard** — Show analytics like average score and most-missed questions.
8. **Animations** — Add smooth transition effects between screens.
9. **Sound Effects** — Play audio feedback for correct/incorrect answers.
10. **Export Results** — Generate a PDF certificate for completed quizzes.

---

## 🛠️ Technologies Used

| Technology   | Purpose                                  |
|-------------|------------------------------------------|
| Python 3    | Core programming language                |
| `tkinter`   | GUI framework (built into Python)        |
| `os`        | File existence checks                    |
| `random`    | Shuffling question order                 |
| `datetime`  | Timestamping score records               |

---

## 👤 Author

- **Name:** Utsav Panduranga
- **Roll No:** 25SUUBECS1559
- **College:** Sapthagiri NPS University
- **Course:** B.E.CSE
- **Semester:** Second

---

## 📜 License

This project is created for educational purposes as a college mini-project submission.
