# Palindrome Number - Usage Guide

This directory contains the solution and test generator for the **Palindrome Number** LeetCode problem.

## How To Use

### 1. Generate Test Cases

First, run the test case generator to create comprehensive test cases:

```bash
python testgen_isPalindrome.py
```

This will generate test case files (JSON/YAML format) in the `testgen_output/` directory.

### 2. Inspect Generated Test Cases (Optional)

The generated test cases are human-readable and stored in `testgen_output/`:
- **YAML files**: `*.yaml` or `*.yml` 
- **JSON files**: `*.json`

You can open these files to review the test cases before running them.

### 3. Run the Tests

You have two options to run the data-driven tests:

#### Option A: Command Line
```bash
# Run all tests
python -m pytest test_isPalindrome.py -v

# Run with detailed output
python -m pytest test_isPalindrome.py -v -s
```

#### Option B: VS Code GUI
1. Open `test_isPalindrome.py` in VS Code
2. Click the test icons in the gutter next to `test_isPalindrome`
3. Or use the Test Explorer panel to run individual test cases

## Files Overview

- **`solution_isPalindrome.py`** - The Palindrome Number solution implementation
- **`testgen_isPalindrome.py`** - Test case generator (generates comprehensive test scenarios)  
- **`test_isPalindrome.py`** - Data-driven pytest test that loads and runs generated test cases
- **`testgen_output/`** - Directory containing generated test case files
- **`testgen_output/samples.yaml`** - Sample test cases (kept in version control as reference)

## Key Features

- **Data-Driven Testing**: Each generated test case runs as a separate pytest result
- **Multiple Formats**: Supports both JSON and YAML test case files
- **Clean Repository**: Generated test files are ignored by git (except samples.yaml)
- **Flexible Execution**: Run tests via command line or VS Code GUI
- **Human Readable**: Test cases are in readable JSON/YAML format for easy inspection

## Workflow

1. **Generate** → Run `testgen_isPalindrome.py` to create test cases
2. **Inspect** → (Optional) Review generated test cases in `testgen_output/`
3. **Test** → Run `test_isPalindrome.py` via pytest or VS Code
4. **Iterate** → Modify generator and re-run as needed

The generated test case files won't pollute your git repository thanks to `.gitignore` rules that exclude all `testgen_output/*` files except reference samples.