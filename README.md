# Gradebook CLI (Python Project)

A command-line gradebook application built in Python.  
This project demonstrates **object-oriented programming, file persistence, CSV handling, and GPA calculation logic** — suitable for showcasing technical skills on a resume or GitHub portfolio.

---
## 🔹 Key Technical Highlights

- **Python (3.8+)** – implemented entirely with the standard library (no external dependencies).  
- **Object-Oriented Design** – `Student` and `Gradebook` classes encapsulate data and behavior.  
- **File Persistence** – automatic saving/loading of grade data to a CSV file.  
- **CLI Application** – interactive text-based menu for usability.  
- **Algorithmic Logic** – GPA scale conversion (A=4, B=3, etc.) from numerical averages.  

---
## 📂 Project Structure
```
gradebook-cli/
- ├── gradebook.py # Main source code (application entry point)
- ├── gradebook.csv # Data file (created automatically after first run)
- └── README.md # Project documentation
```

---
## ⚙️ Installation & Setup
Clone the repository and move into the project folder:

```bash

```
---
🖥️ Usage
On running, a simple interactive menu is displayed:
```markdown
1. Add Student
2. Add Grade
3. Show Gradebook
4. Exit
```
- Add Student → Add a new student by name
- Add Grade → Add a grade (0–100) for a student
- Show Gradebook → Displays all students with averages & GPAs
- Exit → Saves automatically and quits

---
📊 Example Run
```pgsql
1. Add Student
2. Add Grade
3. Show Gradebook
4. Exit
Choose: 1
Student name: Alice

1. Add Student
2. Add Grade
3. Show Gradebook
4. Exit
Choose: 2
Student name: Alice
Grade (0-100): 95

1. Add Student
2. Add Grade
3. Show Gradebook
4. Exit
Choose: 3

--- Gradebook ---
Alice | Avg: 95.00 | GPA: 4.00
```
