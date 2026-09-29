# PocketLog — Master Project Plan

> A personal expense and income tracker built step-by-step with Python.
>
> **Project philosophy:** Build a real working tool while learning the skills needed to improve it. Do not jump ahead just to make the project look advanced.

---

## 🎯 Project Vision

PocketLog is a personal finance tracker that will gradually grow from a simple Python CLI program into a useful, portfolio-ready application.

### Main goals

- Track daily expenses
- Track income
- Calculate balance
- Organize transactions
- Store data permanently
- Analyze spending
- Generate useful reports
- Improve the application through multiple versions

---

# 🗺️ Development Roadmap

```text
                         POCKETLOG
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
         V1                 V2                 V3
     Basic Tracker      Better Tracker     Permanent Data
          │                  │                  │
          └──────────────────┼──────────────────┘
                             │
                            V4
                       Analytics
                             │
                            V5
                    Polished Application
```

---

# 🚀 V1 — Basic Working Tracker

**Goal:** Create a simple but properly working command-line expense/income tracker.

**Current version:** `PocketLogV1`

**Main file:** `PLG_v1.py`

### Project Setup

- [x] Create PocketLog project folder
- [x] Create V1 folder
- [x] Create `PLG_v1.py`
- [x] Initialize Git repository
- [x] Create GitHub repository
- [x] Connect local repository to GitHub
- [x] Push V1 to GitHub

### Menu

- [x] Create main menu
- [x] Add Expense option
- [x] Add Income option
- [x] Check Balance option
- [x] Exit option
- [x] Use a `while` loop for the application

### Expense System

- [x] Take expense amount
- [x] Take expense description
- [x] Create expense dictionary
- [x] Store expenses in a list
- [ ] Display expenses clearly
- [ ] Calculate total expenses

### Income System

- [ ] Take income amount
- [ ] Take income description
- [ ] Create income record
- [ ] Store income records
- [ ] Calculate total income

### Balance System

- [ ] Calculate total income
- [ ] Calculate total expenses
- [ ] Calculate current balance
- [ ] Display balance clearly

### Input Validation

- [ ] Handle invalid menu choices
- [ ] Handle invalid amount input
- [ ] Prevent inappropriate negative values where needed
- [ ] Handle empty descriptions

### Testing

- [ ] Test adding one expense
- [ ] Test adding multiple expenses
- [ ] Test adding income
- [ ] Test balance calculation
- [ ] Test invalid inputs
- [ ] Test exit option
- [ ] Test the complete application from start to finish

### Code Quality

- [ ] Improve variable naming
- [ ] Add functions where appropriate
- [ ] Remove unnecessary code
- [ ] Add useful comments/docstrings
- [ ] Keep the code beginner-friendly and readable

### V1 Release

- [ ] Complete all V1 features
- [ ] Final testing
- [ ] Update README
- [ ] Commit final V1
- [ ] Push final V1 to GitHub
- [ ] Mark V1 as complete

---

# 🛠️ V2 — Better Tracker

**Goal:** Make PocketLog easier and more useful for daily use.

### Transactions

- [ ] Add transaction ID
- [ ] Add date
- [ ] Add category
- [ ] Improve transaction structure
- [ ] View all transactions
- [ ] Search transactions
- [ ] Filter transactions

### Expense Features

- [ ] Edit expense
- [ ] Delete expense
- [ ] View total expenses
- [ ] View expenses by category

### Income Features

- [ ] Edit income
- [ ] Delete income
- [ ] View total income
- [ ] Support multiple income sources

### Code Structure

- [ ] Separate major operations into functions
- [ ] Improve program flow
- [ ] Improve error handling
- [ ] Refactor repeated code

### V2 Release

- [ ] Test all features
- [ ] Update documentation
- [ ] Commit V2
- [ ] Push V2 to GitHub
- [ ] Mark V2 as complete

---

# 💾 V3 — Permanent Data

**Goal:** Make data survive after closing the program.

### File Handling

- [ ] Learn Python file handling
- [ ] Decide on initial storage format
- [ ] Save transactions to a file
- [ ] Load transactions when PocketLog starts
- [ ] Update stored data
- [ ] Handle missing data files
- [ ] Handle corrupted/invalid data

### Modules

- [ ] Learn Python modules
- [ ] Split PocketLog into multiple files
- [ ] Create reusable functions/classes
- [ ] Create a cleaner project structure

### Database

- [ ] Understand databases
- [ ] Learn basic SQL
- [ ] Learn SQLite
- [ ] Design PocketLog database
- [ ] Create transaction table
- [ ] Insert transactions
- [ ] Read transactions
- [ ] Update transactions
- [ ] Delete transactions

### V3 Release

- [ ] Test data persistence
- [ ] Test restarting the application
- [ ] Test database operations
- [ ] Update README
- [ ] Commit V3
- [ ] Push V3 to GitHub
- [ ] Mark V3 as complete

---

# 📊 V4 — Analytics & Reports

**Goal:** Turn PocketLog data into useful information.

### Data Analysis

- [ ] Learn Pandas basics
- [ ] Load PocketLog data into Pandas
- [ ] Calculate monthly spending
- [ ] Calculate category-wise spending
- [ ] Calculate income vs expenses
- [ ] Find highest spending categories
- [ ] Find spending patterns

### Visualization

- [ ] Learn Matplotlib basics
- [ ] Create expense charts
- [ ] Create income vs expense chart
- [ ] Create category spending chart
- [ ] Create monthly spending trend

### Reports

- [ ] Daily summary
- [ ] Weekly summary
- [ ] Monthly summary
- [ ] Category report
- [ ] Income report
- [ ] Expense report
- [ ] Balance report

### V4 Release

- [ ] Test analytics
- [ ] Verify calculations
- [ ] Verify charts
- [ ] Update documentation
- [ ] Commit V4
- [ ] Push V4 to GitHub
- [ ] Mark V4 as complete

---

# 🖥️ V5 — Polished Application

**Goal:** Turn PocketLog into a complete portfolio-ready application.

### User Experience

- [ ] Improve interface
- [ ] Improve navigation
- [ ] Improve messages
- [ ] Improve error handling
- [ ] Add help/about section

### Dashboard

- [ ] Current balance
- [ ] Total income
- [ ] Total expenses
- [ ] Recent transactions
- [ ] Spending summary
- [ ] Charts

### Data Management

- [ ] Export data
- [ ] Import data
- [ ] Backup data
- [ ] Restore data
- [ ] Data validation

### Documentation

- [ ] Complete README
- [ ] Add installation instructions
- [ ] Add usage instructions
- [ ] Add screenshots
- [ ] Document project structure
- [ ] Document major features
- [ ] Document technologies used

### Portfolio

- [ ] Clean GitHub repository
- [ ] Meaningful commit history
- [ ] Add project description
- [ ] Add screenshots/demo
- [ ] Add future improvements
- [ ] Prepare project for résumé/portfolio

---

# 📚 Learning Tree

PocketLog is also a learning project.

## Python

- [x] Variables and data types
- [x] Input/output
- [x] Conditions
- [x] Loops
- [x] Lists
- [x] Dictionaries
- [x] Functions
- [x] Basic OOP
- [ ] File handling
- [ ] Modules
- [ ] Exception handling
- [ ] Advanced OOP only when needed
- [ ] Useful Python standard-library modules

## Git & GitHub

- [x] Repository
- [x] `git init`
- [x] `git add`
- [x] `git commit`
- [x] `git push`
- [x] Remote repository
- [x] Basic branches
- [ ] Pull requests in real projects
- [ ] Tags/releases
- [ ] Better commit practices

## SQL / SQLite

- [ ] Database fundamentals
- [ ] Tables
- [ ] Primary keys
- [ ] `INSERT`
- [ ] `SELECT`
- [ ] `UPDATE`
- [ ] `DELETE`
- [ ] `WHERE`
- [ ] `ORDER BY`
- [ ] Aggregations
- [ ] Basic joins

## Data Analytics

- [ ] Pandas
- [ ] Data cleaning
- [ ] Data aggregation
- [ ] Matplotlib
- [ ] Basic data visualization
- [ ] Interpreting spending patterns

---

# 🌿 GitHub Workflow

For each feature:

```text
PLAN
  ↓
LEARN WHAT IS NEEDED
  ↓
CODE
  ↓
TEST
  ↓
FIX
  ↓
COMMIT
  ↓
PUSH TO GITHUB
  ↓
UPDATE THIS PLAN
```

### Commit principle

Use commits that describe what actually changed.

Examples:

```text
Add income tracking
Fix balance calculation
Add transaction categories
Implement file storage
Add monthly spending analysis
```

---

# 🔄 Daily PocketLog Workflow

Before starting:

- [ ] Check this plan
- [ ] Find the current version
- [ ] Choose one small task
- [ ] Identify what needs to be learned

While working:

- [ ] Learn only what the current task requires
- [ ] Build the feature
- [ ] Test it
- [ ] Fix problems
- [ ] Avoid jumping randomly to future features

After working:

- [ ] Confirm the feature works
- [ ] Update checkboxes
- [ ] Commit changes
- [ ] Push to GitHub
- [ ] Write down the next task

---

# 📌 Current Status

**Current version:** V1 — Basic Working Tracker

**Current focus:**

1. Finish Income system
2. Calculate total expenses
3. Calculate total income
4. Calculate balance
5. Improve transaction display
6. Add validation
7. Test the complete V1
8. Release V1

**Rule:** Do not move to V2 until V1 is a properly working application.

---

# 💡 Future Ideas

Ideas can be added here without committing to them yet.

- [ ] Budget limits
- [ ] Savings goals
- [ ] Recurring transactions
- [ ] Monthly budget
- [ ] Notifications/reminders
- [ ] Export to CSV
- [ ] Export to Excel
- [ ] More advanced analytics
- [ ] Web interface
- [ ] Desktop interface
- [ ] Mobile version

---

# 🏁 Long-Term Goal

PocketLog should eventually become more than a Python exercise.

The goal is to have a project that demonstrates:

- Python programming
- OOP
- File/database handling
- SQL
- Data analysis
- Data visualization
- Git/GitHub
- Software development workflow
- Problem solving
- Ability to build and improve a real-world tool

> **Build → Learn → Test → Improve → Release**

---

## Project Repository

GitHub: https://github.com/iamsreeraj/PocketLog
