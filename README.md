# AI-Powered Automated Code Reviewer 🤖

A lightweight Python CLI tool that inspects local Git changes and runs AI-assisted code reviews to detect security risks, performance bottlenecks, and syntax errors before you commit.

## Features
- **Git Diff Parsing:** Scans staged or unstaged local git diffs automatically.
- **LLM Integration:** Connects to OpenAI/LLM endpoints to generate structured engineering reviews.
- **Rich Terminal UI:** Formats reviews with clean tables, badges, and colored terminal logs.

## Setup & Installation

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/your-username/ai-code-reviewer.git](https://github.com/your-username/ai-code-reviewer.git)
   cd ai-code-reviewer

## Run commands
```bash
   python3 -m reviewer.cli
   python3 -m reviewer.cli --staged
```

## Run test
```bash
   python3 -m pytest
```