# Python -Learning Path: Bundle 2 (Projects 6-10)

This repository contains the second phase of my Python programming journey as part of the Boot.dev back-end developer path. 

While the first bundle focused on basic logic and introductory OOP, this bundle represents a massive leap forward into **Functional Programming (FP)**, **State Management**, **Data Persistence**, and **Modular Software Architecture**. 

**NOTE:** Like the first bundle, these projects were built independently from the Boot.dev course material to reinforce the skills learned during the course and solidify core concepts by building original projects from scratch.

## 🛠️ General Requirements
* **Python:** 3.x
* **Libraries:** Built-in libraries (`json`, `os`)
* **Virtual Environments:** Recommended to use `.venv`-folder for dependency control.

## 📂 Projects and learned concepts

### 6. Recursive DFS Explorer
A tool that utilizes Depth-First Search to navigate and process nested data structures (like file systems or complex dictionaries).

* **Concepts solidified:** Recursion, Depth-First Search (DFS) algorithms, defining base cases, and tree traversal logic.

### 7. Functional Data Pipeline
Data processing utility that transforms strings through a custom recursive pipeline. Instead of loops, this project uses functions as "first-class citizens," passing them as variables to process data sequentially.

* **Concepts solidified:** Decorators (@wrapper), Currying (functions generating other functions), Recursion, and avoiding side effects through Pure Functions.

### 8. Functional Markdown Parser
A text parsing engine designed to convert Markdown syntax into HTML. Instead of relying on complex object-oriented state machines, it utilizes strict functional rules, an AST-like node structure, and data pipelines to process text blocks.

* **Concepts solidified:** Concepts solidified: Advanced string manipulation, pure functions, Abstract Syntax Tree (AST) concepts, and functional data transformation.

### 9. CLI Task Engine
A command-line task management tool with a fully separated architecture and permanent data storage.

* **Concepts solidified:** Separation of concerns (CLI vs. Router vs. DB Engine), saving and loading state using JSON, error handling, and dependency injection.

### 10. Mini Database Engine (Multi-Table)
A robust, custom-built CRUD database engine. Features an interactive CLI, dynamic routing, and persistent storage capable of handling multiple distinct data tables simultaneously.

* **Concepts solidified:** * Full CRUD operations (Create, Read, Update, Delete)
  * Auto-incrementing Primary Keys
  * Advanced string parsing for CLI inputs
  * Complex JSON state persistence 
  * Modular architectural design utilizing functional closures

## 🚀 How to run the programs?
1. Clone the repository: `git clone [personal-repo-url]`
2. Navigate to the project folder: `cd [project-name]`
3. Create and activate a virtual environment (optional but recommended).
4. Run the program: `python3 main.py` (or the specific file name for earlier projects).

## 📈 What's coming up next?
Following this bundle, I have unlocked the "Build an AI Agent" course. I will be diving into network requests, API integrations (specifically LLMs), Asynchronous programming, and connecting my backend logic to the outside world!

*This portfolio bundle was composed by Jere Kukkohovi in April 2026.*