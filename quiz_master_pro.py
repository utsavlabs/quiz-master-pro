"""
╔══════════════════════════════════════════════════════════════╗
║                    QUIZ MASTER PRO  v2.0                    ║
║         A Python Tkinter GUI Quiz Application               ║
║                                                             ║
║  Author  : [Your Name]                                      ║
║  College : [Your College Name]                              ║
║  Date    : June 2026                                        ║
║  Version : 2.0 (GUI Edition)                                ║
╚══════════════════════════════════════════════════════════════╝

Description:
    Quiz Master Pro is an interactive GUI quiz application built
    with Python's Tkinter library. It features 10 beginner-friendly
    Python programming multiple-choice questions. The app tracks scores,
    assigns grades, and maintains a persistent high-score leaderboard.

Features:
    - 10 beginner Python multiple-choice questions
    - Professional dark-themed Tkinter GUI
    - Welcome screen with name entry
    - One question at a time with A/B/C/D buttons
    - Instant correct/incorrect visual feedback
    - Running score tracker and progress bar
    - Final results dashboard with grade
    - High-score leaderboard (saved to scores.txt)
    - Play-again functionality
    - Full input validation and error handling
"""

# ──────────────────────────────────────────────────────────────
# Standard Library Imports (no external dependencies)
# ──────────────────────────────────────────────────────────────
import tkinter as tk
from tkinter import messagebox
import random
import os
from datetime import datetime


# ══════════════════════════════════════════════════════════════
#                       CONFIGURATION
# ══════════════════════════════════════════════════════════════

SCORES_FILE = "scores.txt"
WINDOW_WIDTH = 920
WINDOW_HEIGHT = 660
APP_TITLE = "Quiz Master Pro"

# ── Color Palette (elegant dark theme) ──
C = {
    "bg":          "#0d1b2a",   # Darkest navy – main background
    "panel":       "#1b2838",   # Panel / card background
    "card":        "#22354a",   # Lighter card / option default
    "card_hover":  "#2c4460",   # Option hover state
    "input_bg":    "#1e3048",   # Entry field background
    "accent":      "#4cc9f0",   # Cyan accent
    "blue":        "#4361ee",   # Primary button blue
    "blue_hover":  "#3a56d4",   # Button hover
    "success":     "#06d6a0",   # Correct – green
    "error":       "#ef476f",   # Incorrect – pink/red
    "gold":        "#ffd166",   # Gold – scores & highlights
    "text":        "#e0e5ec",   # Primary text
    "text_dim":    "#7b8da3",   # Secondary / dimmed text
    "white":       "#ffffff",   # Pure white
    "border":      "#2a3f55",   # Subtle borders
}

# ── Typography ──
FF = "Segoe UI"                       # Font family (ships with Windows)
FONTS = {
    "hero":       (FF, 34, "bold"),    # Welcome title
    "heading":    (FF, 22, "bold"),    # Screen headings
    "subheading": (FF, 16, "bold"),   # Question text
    "body":       (FF, 13),           # General body text
    "body_b":     (FF, 13, "bold"),   # Bold body
    "button":     (FF, 13, "bold"),   # Button labels
    "small":      (FF, 11),           # Captions / footnotes
    "grade":      (FF, 64, "bold"),   # Large grade letter
    "stat_num":   (FF, 26, "bold"),   # Score / percentage numbers
}

# ── Grading Scale ──
GRADE_BOUNDARIES = [
    (90, "A", "Outstanding!"),
    (80, "B", "Great Job!"),
    (70, "C", "Good Effort!"),
    (60, "D", "Needs Improvement"),
    (0,  "F", "Better Luck Next Time"),
]


# ══════════════════════════════════════════════════════════════
#                       QUESTION BANK
# ══════════════════════════════════════════════════════════════
# 10 questions total:
#   • 10 Beginner Python programming
#
# Each question has:
#   "question" – the question string
#   "options"  – list of 4 option strings (A, B, C, D)
#   "answer"   – correct option index (1-based: 1 = A, 2 = B …)
#   "topic"    – category label
# ──────────────────────────────────────────────────────────────

QUESTION_BANK = [
    {
        "question": "What is the output of:  print(type(10))",
        "options": [
            "<class 'float'>",
            "<class 'int'>",
            "<class 'str'>",
            "<class 'number'>",
        ],
        "answer": 2,
        "topic": "Python – Data Types",
    },
    {
        "question": "Which of the following is a valid Python variable name?",
        "options": ["2name", "my-var", "_count", "class"],
        "answer": 3,
        "topic": "Python – Variables",
    },
    {
        "question": "What built-in function is used to read user input in Python 3?",
        "options": ["scan()", "get()", "input()", "read()"],
        "answer": 3,
        "topic": "Python – Input/Output",
    },
    {
        "question": "What is the output of:  print('Hello' + ' ' + 'World')",
        "options": ["Hello World", "HelloWorld", "Hello + World", "Error"],
        "answer": 1,
        "topic": "Python – Strings",
    },
    {
        "question": "What will this code print?\n\nx = 15\nif x > 10:\n    print('Big')\nelse:\n    print('Small')",
        "options": ["Small", "Big", "Error", "None"],
        "answer": 2,
        "topic": "Python – If-Else",
    },
    {
        "question": "How many times does this loop execute?\n\nfor i in range(5):\n    print(i)",
        "options": ["4 times", "5 times", "6 times", "1 time"],
        "answer": 2,
        "topic": "Python – For Loops",
    },
    {
        "question": "What does the 'break' statement do inside a loop?",
        "options": [
            "Skips the current iteration",
            "Exits the loop immediately",
            "Restarts the loop from the beginning",
            "Pauses the loop for one second",
        ],
        "answer": 2,
        "topic": "Python – Break & Continue",
    },
    {
        "question": "What is the output of:  print(len('Python'))",
        "options": ["5", "6", "7", "Error"],
        "answer": 2,
        "topic": "Python – Strings",
    },
    {
        "question": "How do you add an element to the end of a list in Python?",
        "options": [
            "list.add(x)",
            "list.insert(x)",
            "list.append(x)",
            "list.push(x)",
        ],
        "answer": 3,
        "topic": "Python – Lists",
    },
    {
        "question": "Which loop continues executing as long as its condition is True?",
        "options": ["for loop", "do loop", "repeat loop", "while loop"],
        "answer": 4,
        "topic": "Python – While Loops",
    },
]


# ══════════════════════════════════════════════════════════════
#                   HELPER – GRADE CALCULATOR
# ══════════════════════════════════════════════════════════════

def calculate_grade(percentage):
    """Return (letter, message) for the given percentage."""
    for threshold, grade, message in GRADE_BOUNDARIES:
        if percentage >= threshold:
            return grade, message
    return "F", "Keep Trying!"


# ══════════════════════════════════════════════════════════════
#                   HELPER – SCORE FILE I/O
# ══════════════════════════════════════════════════════════════

def save_score_to_file(name, score, total, percentage, grade):
    """
    Append one score record to SCORES_FILE.
    Format: Name | Score | Percentage | Grade | Timestamp
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    record = (
        f"{name} | {score}/{total} | {percentage:.1f}% "
        f"| Grade: {grade} | {timestamp}\n"
    )
    try:
        with open(SCORES_FILE, "a", encoding="utf-8") as fh:
            fh.write(record)
        return True
    except IOError:
        return False


def load_high_scores(top_n=10):
    """
    Read SCORES_FILE, parse records, sort by percentage
    descending, and return the top N as a list of tuples:
        (name, score_str, pct_str, grade, timestamp)
    """
    if not os.path.exists(SCORES_FILE):
        return []

    records = []
    try:
        with open(SCORES_FILE, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                parts = [p.strip() for p in line.split("|")]
                if len(parts) == 5:
                    name, score_str, pct_str, grade, timestamp = parts
                    try:
                        pct_val = float(pct_str.replace("%", ""))
                    except ValueError:
                        pct_val = 0.0
                    records.append(
                        (name, score_str, pct_str, grade, timestamp, pct_val)
                    )
    except IOError:
        return []

    records.sort(key=lambda r: r[5], reverse=True)
    return [(r[0], r[1], r[2], r[3], r[4]) for r in records[:top_n]]


# ══════════════════════════════════════════════════════════════
#                   MAIN APPLICATION CLASS
# ══════════════════════════════════════════════════════════════

class QuizMasterPro:
    """
    Main application class.
    Manages four screens: Welcome, Quiz, Results, High Scores.
    Screens are stacked tk.Frames; switching is done via tkraise().
    """

    # ──────────────────────────────────────────────────────
    #  Initialisation
    # ──────────────────────────────────────────────────────

    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.configure(bg=C["bg"])
        self.root.resizable(False, False)

        # Centre the window on screen
        x = (self.root.winfo_screenwidth()  - WINDOW_WIDTH)  // 2
        y = (self.root.winfo_screenheight() - WINDOW_HEIGHT) // 2
        self.root.geometry(
            f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}"
        )

        # ── Quiz state ──
        self.player_name  = ""
        self.score        = 0
        self.current_idx  = 0
        self.questions    = []
        self.answered     = False         # True after an option is clicked

        # ── Build all screens ──
        self.screens = {}
        self._build_welcome()
        self._build_quiz()
        self._build_results()
        self._build_highscores()

        # Show the welcome screen
        self._show("welcome")

    # ──────────────────────────────────────────────────────
    #  Screen switching
    # ──────────────────────────────────────────────────────

    def _show(self, name):
        """Raise the named screen to the front."""
        self.screens[name].tkraise()

    # ──────────────────────────────────────────────────────
    #  WELCOME SCREEN
    # ──────────────────────────────────────────────────────

    def _build_welcome(self):
        f = tk.Frame(self.root, bg=C["bg"])
        f.place(x=0, y=0, relwidth=1, relheight=1)
        self.screens["welcome"] = f

        # ── Decorative top accent line ──
        tk.Frame(f, bg=C["accent"], height=3).pack(fill="x")

        # ── Spacer ──
        tk.Frame(f, bg=C["bg"], height=55).pack()

        # ── Icon + Title ──
        tk.Label(
            f, text="QUIZ MASTER PRO",
            font=FONTS["hero"], bg=C["bg"], fg=C["white"],
        ).pack()
        tk.Label(
            f, text="Test Your Python Programming Knowledge",
            font=FONTS["body"], bg=C["bg"], fg=C["text_dim"],
        ).pack(pady=(4, 0))

        # ── Thin divider ──
        tk.Frame(f, bg=C["border"], height=1, width=360).pack(pady=25)

        # ── Name entry card ──
        card = tk.Frame(f, bg=C["panel"], padx=35, pady=28)
        card.pack()

        tk.Label(
            card, text="Enter Your Name",
            font=FONTS["body_b"], bg=C["panel"], fg=C["text"],
        ).pack(anchor="w", pady=(0, 8))

        self.name_entry = tk.Entry(
            card, font=FONTS["body"], width=32,
            bg=C["input_bg"], fg=C["text"],
            insertbackground=C["accent"],
            relief="flat", bd=0,
            highlightthickness=2,
            highlightcolor=C["accent"],
            highlightbackground=C["border"],
        )
        self.name_entry.pack(ipady=9, fill="x")
        self.name_entry.bind("<Return>", lambda _: self._on_start())

        # Error label (hidden until needed)
        self.name_err = tk.Label(
            card, text="", font=FONTS["small"],
            bg=C["panel"], fg=C["error"],
        )
        self.name_err.pack(anchor="w", pady=(6, 0))

        # ── Buttons ──
        btn_row = tk.Frame(f, bg=C["bg"])
        btn_row.pack(pady=28)

        self._make_btn(
            btn_row, "Start Quiz", C["blue"], C["white"],
            self._on_start,
        ).pack(side="left", padx=8)

        self._make_btn(
            btn_row, "High Scores", C["card"], C["text"],
            lambda: self._open_highscores("welcome"),
        ).pack(side="left", padx=8)

        self._make_btn(
            btn_row, "Exit", C["card"], C["text"],
            self.root.quit,
        ).pack(side="left", padx=8)

        # ── Footer ──
        tk.Label(
            f,
            text="10 Questions  •  Multiple Choice  •  Instant Feedback",
            font=FONTS["small"], bg=C["bg"], fg=C["text_dim"],
        ).pack(side="bottom", pady=24)

        # Focus the entry
        self.name_entry.focus_set()

    # ──────────────────────────────────────────────────────
    #  Start quiz (validation + shuffle)
    # ──────────────────────────────────────────────────────

    def _on_start(self):
        """Validate name, initialise quiz state, show first question."""
        name = self.name_entry.get().strip()

        # Validate
        if not name:
            self.name_err.config(text="Please enter your name.")
            return
        if not all(ch.isalpha() or ch.isspace() for ch in name):
            self.name_err.config(
                text="Name should contain only letters and spaces."
            )
            return

        self.name_err.config(text="")
        self.player_name = name.title()
        self.score       = 0
        self.current_idx = 0
        self.questions   = QUESTION_BANK.copy()
        random.shuffle(self.questions)

        self._load_question()
        self._show("quiz")

    # ──────────────────────────────────────────────────────
    #  QUIZ SCREEN
    # ──────────────────────────────────────────────────────

    def _build_quiz(self):
        f = tk.Frame(self.root, bg=C["bg"])
        f.place(x=0, y=0, relwidth=1, relheight=1)
        self.screens["quiz"] = f

        # ── Top bar ──
        top = tk.Frame(f, bg=C["panel"], height=48)
        top.pack(fill="x")
        top.pack_propagate(False)

        self.lbl_progress = tk.Label(
            top, text="", font=FONTS["body_b"],
            bg=C["panel"], fg=C["text"],
        )
        self.lbl_progress.pack(side="left", padx=20)

        self.lbl_score = tk.Label(
            top, text="", font=FONTS["body_b"],
            bg=C["panel"], fg=C["gold"],
        )
        self.lbl_score.pack(side="right", padx=20)

        self.lbl_topic = tk.Label(
            top, text="", font=FONTS["small"],
            bg=C["panel"], fg=C["accent"],
        )
        self.lbl_topic.pack(side="right", padx=6)

        # ── Progress bar canvas ──
        self.progress_cv = tk.Canvas(
            f, height=4, bg=C["bg"], highlightthickness=0,
        )
        self.progress_cv.pack(fill="x")

        # ── Question area ──
        body = tk.Frame(f, bg=C["bg"], padx=55)
        body.pack(fill="both", expand=True, pady=(18, 0))

        self.lbl_question = tk.Label(
            body, text="", font=FONTS["subheading"],
            bg=C["bg"], fg=C["white"],
            wraplength=780, justify="left", anchor="nw",
        )
        self.lbl_question.pack(fill="x", pady=(0, 18))

        # ── Four option "cards" ──
        self.opt_widgets = []           # list of dicts
        for i in range(4):
            row = tk.Frame(body, bg=C["card"], padx=16, pady=13, cursor="hand2")
            row.pack(fill="x", pady=4)

            prefix_lbl = tk.Label(
                row, text=chr(65 + i),       # A / B / C / D
                font=FONTS["body_b"], width=3,
                bg=C["card"], fg=C["accent"],
            )
            prefix_lbl.pack(side="left")

            text_lbl = tk.Label(
                row, text="", font=FONTS["body"],
                bg=C["card"], fg=C["text"],
                anchor="w", wraplength=660, justify="left",
            )
            text_lbl.pack(side="left", fill="x", expand=True)

            info = {"frame": row, "prefix": prefix_lbl, "text": text_lbl}
            self.opt_widgets.append(info)

            # Click bindings (frame + children)
            for widget in (row, prefix_lbl, text_lbl):
                widget.bind("<Button-1>", lambda e, idx=i: self._on_answer(idx))

            # Hover bindings
            for widget in (row, prefix_lbl, text_lbl):
                widget.bind("<Enter>", lambda e, w=info: self._opt_enter(w))
                widget.bind("<Leave>", lambda e, w=info: self._opt_leave(w))

        # ── Feedback + Next button row ──
        bottom = tk.Frame(f, bg=C["bg"], height=64, padx=55)
        bottom.pack(fill="x", pady=(0, 18))
        bottom.pack_propagate(False)

        self.lbl_feedback = tk.Label(
            bottom, text="", font=FONTS["body_b"],
            bg=C["bg"], fg=C["text"],
        )
        self.lbl_feedback.pack(side="left")

        self.btn_next = tk.Button(
            bottom, text="Next Question  ▶", font=FONTS["button"],
            bg=C["blue"], fg=C["white"],
            activebackground=C["blue_hover"],
            activeforeground=C["white"],
            relief="flat", cursor="hand2",
            padx=22, pady=8,
            command=self._on_next,
        )
        # (not packed yet – shown after answering)

    # ── Option hover helpers ──

    def _opt_enter(self, w):
        if not self.answered:
            for part in ("frame", "prefix", "text"):
                w[part].config(bg=C["card_hover"])

    def _opt_leave(self, w):
        if not self.answered:
            for part in ("frame", "prefix", "text"):
                w[part].config(bg=C["card"])

    # ── Load a question into the UI ──

    def _load_question(self):
        """Populate the quiz screen with the current question."""
        self.answered = False
        q     = self.questions[self.current_idx]
        total = len(self.questions)

        # Header labels
        self.lbl_progress.config(
            text=f"Question {self.current_idx + 1} / {total}"
        )
        self.lbl_score.config(text=f"Score: {self.score}")
        self.lbl_topic.config(text=q["topic"])

        # Progress bar
        self.progress_cv.delete("all")
        frac = self.current_idx / total
        bar_w = WINDOW_WIDTH * frac
        self.progress_cv.create_rectangle(
            0, 0, bar_w, 4, fill=C["accent"], outline="",
        )

        # Question text
        self.lbl_question.config(text=q["question"])

        # Reset option cards
        for i, w in enumerate(self.opt_widgets):
            w["text"].config(text=q["options"][i])
            for part in ("frame", "prefix", "text"):
                w[part].config(bg=C["card"])
            w["prefix"].config(fg=C["accent"])
            w["text"].config(fg=C["text"])
            w["frame"].config(cursor="hand2")

        # Hide feedback & next button
        self.lbl_feedback.config(text="")
        self.btn_next.pack_forget()

    # ── Answer checking ──

    def _on_answer(self, selected):
        """Called when the player clicks an option."""
        if self.answered:
            return
        self.answered = True

        q = self.questions[self.current_idx]
        correct = q["answer"] - 1          # Convert to 0-based

        if selected == correct:
            self.score += 1
            self.lbl_score.config(text=f"Score: {self.score}")
            self.lbl_feedback.config(
                text="  Correct! Well done!", fg=C["success"],
            )
            self._highlight_opt(selected, C["success"])
        else:
            correct_text = f"{chr(65 + correct)}. {q['options'][correct]}"
            self.lbl_feedback.config(
                text=f"  Incorrect!  Answer: {correct_text}",
                fg=C["error"],
            )
            self._highlight_opt(selected, C["error"])
            self._highlight_opt(correct,  C["success"])

        # Disable hover cursor
        for w in self.opt_widgets:
            w["frame"].config(cursor="")

        # Show Next / View Results button
        is_last = self.current_idx >= len(self.questions) - 1
        self.btn_next.config(
            text="View Results  ▶" if is_last else "Next Question  ▶"
        )
        self.btn_next.pack(side="right")

    def _highlight_opt(self, idx, colour):
        """Set background of an option card to the given colour."""
        w = self.opt_widgets[idx]
        for part in ("frame", "prefix", "text"):
            w[part].config(bg=colour)
        w["prefix"].config(fg=C["white"])
        w["text"].config(fg=C["white"])

    # ── Next question ──

    def _on_next(self):
        self.current_idx += 1
        if self.current_idx < len(self.questions):
            self._load_question()
        else:
            self._show_results()

    # ──────────────────────────────────────────────────────
    #  RESULTS SCREEN
    # ──────────────────────────────────────────────────────

    def _build_results(self):
        f = tk.Frame(self.root, bg=C["bg"])
        f.place(x=0, y=0, relwidth=1, relheight=1)
        self.screens["results"] = f

        # Container that gets rebuilt each time
        self.results_box = tk.Frame(f, bg=C["bg"])
        self.results_box.pack(fill="both", expand=True, padx=60, pady=25)

    def _show_results(self):
        """Calculate results, save score, populate the results screen."""
        # Clear previous widgets
        for w in self.results_box.winfo_children():
            w.destroy()

        total      = len(self.questions)
        pct        = (self.score / total) * 100 if total else 0
        grade, msg = calculate_grade(pct)

        # Save to file
        saved = save_score_to_file(
            self.player_name, self.score, total, pct, grade,
        )

        # ── Header ──
        tk.Label(
            self.results_box, text="Quiz Complete!",
            font=FONTS["heading"], bg=C["bg"], fg=C["white"],
        ).pack(pady=(8, 2))
        tk.Label(
            self.results_box,
            text=f"Well played, {self.player_name}!",
            font=FONTS["body"], bg=C["bg"], fg=C["text_dim"],
        ).pack(pady=(0, 18))

        # ── Stats card ──
        card = tk.Frame(self.results_box, bg=C["panel"], padx=30, pady=22)
        card.pack(fill="x")

        cols = tk.Frame(card, bg=C["panel"])
        cols.pack(fill="x")

        # Score column
        col1 = tk.Frame(cols, bg=C["panel"])
        col1.pack(side="left", expand=True)
        tk.Label(col1, text="SCORE", font=FONTS["small"],
                 bg=C["panel"], fg=C["text_dim"]).pack()
        tk.Label(col1, text=f"{self.score} / {total}",
                 font=FONTS["stat_num"], bg=C["panel"],
                 fg=C["white"]).pack()

        # Grade column
        col2 = tk.Frame(cols, bg=C["panel"])
        col2.pack(side="left", expand=True)
        tk.Label(col2, text="GRADE", font=FONTS["small"],
                 bg=C["panel"], fg=C["text_dim"]).pack()
        g_colour = (
            C["success"] if grade in ("A", "B")
            else C["gold"]   if grade == "C"
            else C["error"]
        )
        tk.Label(col2, text=grade, font=FONTS["grade"],
                 bg=C["panel"], fg=g_colour).pack()

        # Percentage column
        col3 = tk.Frame(cols, bg=C["panel"])
        col3.pack(side="left", expand=True)
        tk.Label(col3, text="PERCENTAGE", font=FONTS["small"],
                 bg=C["panel"], fg=C["text_dim"]).pack()
        tk.Label(col3, text=f"{pct:.1f}%",
                 font=FONTS["stat_num"], bg=C["panel"],
                 fg=C["white"]).pack()

        # Verdict
        tk.Label(card, text=msg, font=FONTS["subheading"],
                 bg=C["panel"], fg=C["gold"]).pack(pady=(14, 0))

        # ── Visual progress bar ──
        bar_frame = tk.Frame(self.results_box, bg=C["bg"])
        bar_frame.pack(fill="x", pady=(14, 4))

        bar_cv = tk.Canvas(
            bar_frame, height=18, bg=C["card"], highlightthickness=0,
        )
        bar_cv.pack(fill="x")

        # Draw filled portion after layout
        def _draw_bar(_=None):
            bar_cv.delete("all")
            w = bar_cv.winfo_width()
            if w > 1:
                filled = int(w * pct / 100)
                bar_cv.create_rectangle(
                    0, 0, filled, 18, fill=g_colour, outline="",
                )
        bar_cv.bind("<Configure>", _draw_bar)

        # ── Saved confirmation ──
        save_txt = (
            "Score saved to scores.txt"
            if saved else "Could not save score"
        )
        tk.Label(
            self.results_box, text=save_txt,
            font=FONTS["small"], bg=C["bg"], fg=C["text_dim"],
        ).pack(pady=(8, 16))

        # ── Buttons ──
        btn_row = tk.Frame(self.results_box, bg=C["bg"])
        btn_row.pack()

        self._make_btn(
            btn_row, "Play Again", C["blue"], C["white"],
            self._play_again,
        ).pack(side="left", padx=8)

        self._make_btn(
            btn_row, "High Scores", C["card"], C["text"],
            lambda: self._open_highscores("results"),
        ).pack(side="left", padx=8)

        self._make_btn(
            btn_row, "Exit", C["card"], C["text"],
            self.root.quit,
        ).pack(side="left", padx=8)

        self._show("results")

    # ──────────────────────────────────────────────────────
    #  PLAY AGAIN
    # ──────────────────────────────────────────────────────

    def _play_again(self):
        """Reset state and return to welcome screen."""
        self.name_entry.delete(0, "end")
        self.name_err.config(text="")
        self._show("welcome")
        self.name_entry.focus_set()

    # ──────────────────────────────────────────────────────
    #  HIGH SCORES SCREEN
    # ──────────────────────────────────────────────────────

    def _build_highscores(self):
        f = tk.Frame(self.root, bg=C["bg"])
        f.place(x=0, y=0, relwidth=1, relheight=1)
        self.screens["highscores"] = f

        self.hs_box = tk.Frame(f, bg=C["bg"])
        self.hs_box.pack(fill="both", expand=True, padx=50, pady=25)

    def _open_highscores(self, return_to):
        """Populate and show the high-scores screen."""
        for w in self.hs_box.winfo_children():
            w.destroy()

        # ── Header ──
        tk.Label(
            self.hs_box, text="High Score Leaderboard",
            font=FONTS["heading"], bg=C["bg"], fg=C["white"],
        ).pack(pady=(6, 18))

        records = load_high_scores()

        if not records:
            tk.Label(
                self.hs_box,
                text="No scores recorded yet.\nBe the first to play!",
                font=FONTS["body"], bg=C["bg"], fg=C["text_dim"],
                justify="center",
            ).pack(pady=50)
        else:
            # ── Table header ──
            hdr = tk.Frame(self.hs_box, bg=C["panel"], padx=14, pady=9)
            hdr.pack(fill="x")

            col_defs = [
                ("Rank", 6), ("Name", 16), ("Score", 10),
                ("Pct", 10), ("Grade", 12), ("Date", 0),
            ]
            for label, w in col_defs:
                kw = {"width": w} if w else {}
                tk.Label(
                    hdr, text=label, font=FONTS["body_b"],
                    bg=C["panel"], fg=C["accent"],
                    anchor="w", **kw,
                ).pack(side="left")

            # ── Scrollable rows ──
            canvas = tk.Canvas(
                self.hs_box, bg=C["bg"], highlightthickness=0, height=340,
            )
            sb = tk.Scrollbar(
                self.hs_box, orient="vertical", command=canvas.yview,
            )
            inner = tk.Frame(canvas, bg=C["bg"])
            inner.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all")),
            )
            canvas.create_window((0, 0), window=inner, anchor="nw",
                                 width=WINDOW_WIDTH - 120)
            canvas.configure(yscrollcommand=sb.set)
            canvas.pack(side="left", fill="both", expand=True)
            sb.pack(side="right", fill="y")

            medals = ["1st", "2nd", "3rd"]

            for idx, (name, sc, pct, grade, ts) in enumerate(records):
                row_bg = C["card"] if idx % 2 == 0 else C["bg"]
                row = tk.Frame(inner, bg=row_bg, padx=14, pady=8)
                row.pack(fill="x")

                rank = medals[idx] if idx < 3 else f"{idx + 1}th"
                rank_fg = C["gold"] if idx < 3 else C["text"]

                vals = [
                    (rank,      6,  rank_fg),
                    (name[:14], 16, C["text"]),
                    (sc,        10, C["text"]),
                    (pct,       10, C["text"]),
                    (grade,     12, C["gold"]),
                    (ts,        0,  C["text_dim"]),
                ]
                for txt, w, fg in vals:
                    kw = {"width": w} if w else {}
                    tk.Label(
                        row, text=txt, font=FONTS["body"],
                        bg=row_bg, fg=fg, anchor="w", **kw,
                    ).pack(side="left")

        # ── Back button ──
        self._make_btn(
            self.hs_box, "Back", C["card"], C["text"],
            lambda: self._show(return_to),
        ).pack(pady=18)

        self._show("highscores")

    # ──────────────────────────────────────────────────────
    #  UI HELPER – styled button factory
    # ──────────────────────────────────────────────────────

    def _make_btn(self, parent, text, bg, fg, command):
        """Create and return a flat, styled button."""
        btn = tk.Button(
            parent, text=text,
            font=FONTS["button"],
            bg=bg, fg=fg,
            activebackground=C["blue_hover"],
            activeforeground=C["white"],
            relief="flat", cursor="hand2",
            padx=24, pady=9, bd=0,
            command=command,
        )
        return btn


# ══════════════════════════════════════════════════════════════
#                       ENTRY POINT
# ══════════════════════════════════════════════════════════════

def main():
    """Create the Tk root window and launch the application."""
    root = tk.Tk()

    # Set window icon (suppress errors if unavailable)
    try:
        root.iconbitmap(default="")
    except tk.TclError:
        pass

    app = QuizMasterPro(root)
    root.mainloop()


if __name__ == "__main__":
    main()
