# Viva Questions & Answers — Quiz Master Pro v2.0 (GUI) 🎤

Prepared answers for common questions an examiner may ask during a viva/oral examination.

---

## 1. General Project Questions

### Q1: What is Quiz Master Pro?
**A:** Quiz Master Pro is a professional GUI quiz application built using Python's Tkinter library. It presents 10 multiple-choice questions covering beginner Python programming. It features a dark-themed interface with clickable answer buttons, instant visual feedback, score tracking, grade assignment (A–F), and a persistent high-score leaderboard saved to a text file.

---

### Q2: Why did you choose Python and Tkinter for this project?
**A:** Python was chosen for its simplicity and readability. Tkinter was chosen as the GUI framework because it is built into Python's standard library — no external installation is needed. This makes the project easy to run on any system with Python installed, which is ideal for a college submission.

---

### Q3: What are the main features of your application?
**A:** The main features are:
- Professional dark-themed GUI with four screens (Welcome, Quiz, Results, High Scores)
- 10 randomized multiple-choice questions
- Clickable A/B/C/D answer buttons with hover effects
- Instant green/red visual feedback after each answer
- Running score tracker and progress bar
- Final results dashboard with score, percentage, grade, and verdict
- Persistent high-score leaderboard saved in `scores.txt`
- Play-again functionality without restarting the program
- Input validation for the player's name

---

### Q4: What external libraries did you use?
**A:** None. The project uses only Python's standard library: `tkinter` (GUI), `os` (file checks), `random` (shuffling), and `datetime` (timestamps). No `pip install` is required.

---

## 2. Technical / Code Questions

### Q5: Explain the architecture of your application.
**A:** The application follows an OOP (Object-Oriented Programming) design with a single main class `QuizMasterPro`. This class manages four screens (Welcome, Quiz, Results, High Scores) implemented as stacked `tk.Frame` widgets. Screen switching is done using `tkraise()`. The class encapsulates all state (player name, score, current question index, questions list) as instance variables, and all UI-building and event-handling logic as methods.

---

### Q6: How does screen navigation work in your Tkinter app?
**A:** All four screens are `tk.Frame` widgets placed at the same position using `.place(x=0, y=0, relwidth=1, relheight=1)`. They are stacked on top of each other. To "navigate" to a screen, the `tkraise()` method is called on the target frame, which brings it to the front. This approach avoids destroying and recreating widgets and is the standard pattern for multi-screen Tkinter apps.

---

### Q7: How does the grading system work?
**A:** The `calculate_grade()` function uses a list of tuples called `GRADE_BOUNDARIES`. Each tuple contains a minimum percentage threshold, a letter grade, and a verdict message. The function iterates from highest to lowest threshold. The first threshold the player's percentage meets or exceeds determines their grade:

```
90–100% → A    |    80–89% → B    |    70–79% → C
60–69%  → D    |    Below 60% → F
```

---

### Q8: How are scores saved and loaded?
**A:** Scores are saved by appending a pipe-delimited line to `scores.txt` using Python's `open()` in append mode (`"a"`). Each record contains the player's name, score, percentage, grade, and timestamp. When loading scores, the file is read line-by-line, parsed by splitting on `|`, and sorted by percentage in descending order to create the leaderboard. Only the top 10 records are displayed.

---

### Q9: How does the answer feedback system work visually?
**A:** When a player clicks an answer button:
1. All buttons become non-interactive (click events are ignored via the `self.answered` flag).
2. If the selected answer is correct, its background turns **green** (`#06d6a0`).
3. If incorrect, the selected button turns **red** (`#ef476f`) and the correct answer is highlighted in **green**.
4. A text label shows "Correct!" or "Incorrect! Answer: X".
5. A "Next Question" button appears for the player to proceed.

---

### Q10: Explain the data structure used for storing questions.
**A:** Questions are stored as a list of dictionaries. Each dictionary has four keys:
- `"question"` — the question text (string)
- `"options"` — a list of four option strings (A, B, C, D)
- `"answer"` — the correct option number, 1-based (1=A, 2=B, 3=C, 4=D)
- `"topic"` — the category label (string)

This structure makes it easy to iterate, access options by index, and extend the bank.

---

### Q11: What input validation does your program perform?
**A:** The program validates the player's name:
1. It must be non-empty.
2. It must contain only alphabetic characters and spaces.

If validation fails, an error message is displayed below the entry field. The quiz does not start until a valid name is provided.

---

### Q12: How do you handle errors in the program?
**A:** Error handling includes:
- **Name validation**: Checks for empty or invalid characters before starting.
- **Answer lockout**: The `self.answered` flag prevents multiple clicks on the same question.
- **File I/O**: `try/except IOError` blocks around file read/write operations; a `messagebox` or status label reports failures gracefully.
- **Missing scores file**: `os.path.exists()` check before reading; an empty leaderboard is shown if the file doesn't exist.

---

### Q13: What is `tkraise()` and why do you use it?
**A:** `tkraise()` is a Tkinter method that raises a widget to the top of the stacking order among its siblings. In this application, all four screens are frames placed at the same position. Calling `frame.tkraise()` brings that screen to the front, effectively "navigating" to it without destroying other screens. This is efficient because widgets are created once and reused.

---

### Q14: What is the purpose of the `if __name__ == "__main__":` block?
**A:** This is a Python convention that ensures `main()` runs only when the script is executed directly (e.g., `python quiz_master_pro.py`). If the file were imported as a module by another script, the GUI would not auto-launch, allowing selective reuse of functions and classes.

---

## 3. Conceptual / Theory Questions

### Q15: What is Tkinter?
**A:** Tkinter is Python's standard GUI (Graphical User Interface) toolkit. It is a thin object-oriented wrapper around Tcl/Tk, a cross-platform GUI framework. Tkinter comes bundled with Python's standard installation, so no additional packages need to be installed. It provides widgets like `Label`, `Button`, `Entry`, `Frame`, `Canvas`, and layout managers like `pack`, `grid`, and `place`.

---

### Q16: What is OOP? How is it used in this project?
**A:** OOP (Object-Oriented Programming) is a paradigm that organizes code around objects — instances of classes that encapsulate data (attributes) and behavior (methods). In this project, the `QuizMasterPro` class encapsulates:
- **Attributes**: `player_name`, `score`, `current_idx`, `questions`, `answered`, and widget references.
- **Methods**: `_build_welcome()`, `_on_start()`, `_load_question()`, `_on_answer()`, `_show_results()`, etc.

This keeps the code organized, maintainable, and extendable.

---

### Q17: What is the difference between `pack()`, `grid()`, and `place()` in Tkinter?
**A:**
- **`pack()`** — Arranges widgets in blocks (top, bottom, left, right). Simple and automatic.
- **`grid()`** — Arranges widgets in a table-like grid (rows and columns). Good for forms.
- **`place()`** — Positions widgets at exact pixel coordinates or relative positions. Used in this project to stack frames on top of each other.

This project uses `place()` for screen stacking and `pack()` for internal layout.

---

### Q18: What is event binding in Tkinter?
**A:** Event binding connects user actions (events) to Python functions (handlers). For example:
```python
widget.bind("<Button-1>", handler)   # Left mouse click
widget.bind("<Enter>", handler)      # Mouse enters widget
widget.bind("<Return>", handler)     # Enter key pressed
```
In this project, `<Button-1>` is bound to option cards for click detection, `<Enter>` and `<Leave>` for hover effects, and `<Return>` on the name entry to start the quiz.

---

### Q19: What is the difference between a list and a tuple in Python?
**A:**
- **List** (`[]`) — mutable (can be modified), used for the question bank since we shuffle it.
- **Tuple** (`()`) — immutable (cannot be modified), used for grade boundaries and font definitions since they are constants.

---

### Q20: What is file handling? What modes are used in your project?
**A:** File handling refers to reading from and writing to files on disk. This project uses:
- **`"a"` (append mode)** — to add new score records to `scores.txt` without overwriting.
- **`"r"` (read mode)** — to load previous scores for the leaderboard.

Both use `encoding="utf-8"` for proper character handling.

---

## 4. Enhancement / Improvement Questions

### Q21: How would you add a timer to each question?
**A:** Using Tkinter's `after()` method:
1. Start a countdown (e.g., 30 seconds) when a question is displayed.
2. Update a timer label every second using `self.root.after(1000, update_timer)`.
3. If time runs out, automatically mark the question as incorrect and move to the next one.
4. Cancel the timer using `self.root.after_cancel(timer_id)` when the player answers early.

---

### Q22: How would you load questions from an external file?
**A:** Store questions in a JSON file:
```python
import json
with open("questions.json", "r") as f:
    QUESTION_BANK = json.load(f)
```
This separates content from code, making it easy to add, remove, or modify questions without touching the source code.

---

### Q23: How would you add animations/transitions between screens?
**A:** Tkinter doesn't have built-in animation support, but we can simulate it:
1. Use `after()` to schedule incremental position changes.
2. Slide a frame in from the right by changing its `x` position over multiple steps.
3. Fade effects can be simulated by changing widget colors gradually.
4. For advanced animations, use the `Canvas` widget to draw and redraw elements.

---

### Q24: How would you implement a database instead of a text file?
**A:** Use Python's built-in `sqlite3` module:
```python
import sqlite3
conn = sqlite3.connect("scores.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, score INTEGER, total INTEGER,
        percentage REAL, grade TEXT, timestamp TEXT
    )
""")
```
SQL queries would replace the file read/write operations, providing better querying and data integrity.

---

### Q25: How would you add multiplayer support?
**A:** For local multiplayer:
1. Add a "Number of Players" input on the welcome screen.
2. Each player takes the quiz in turn (same shuffled questions or different).
3. Store each player's results in a list of dictionaries.
4. After all players finish, display a comparative scoreboard on the results screen.

---

### Q26: What is the MVC pattern and how could it apply here?
**A:** MVC (Model-View-Controller) separates:
- **Model**: Question bank, score data, grade logic.
- **View**: All Tkinter widgets and display code.
- **Controller**: Event handlers, quiz flow logic.

Currently, the `QuizMasterPro` class mixes all three. Refactoring into separate `QuizModel`, `QuizView`, and `QuizController` classes would improve testability and maintainability.

---

### Q27: What is the time complexity of your application?
**A:** The quiz runs in **O(n)** time where n = 10 (number of questions). Each question involves constant-time operations (UI update, click check). Shuffling is O(n). Loading high scores is O(m log m) where m = number of saved records (due to sorting). Overall, the application is very efficient.

---

*End of Viva Questions — 27 Q&A total*
