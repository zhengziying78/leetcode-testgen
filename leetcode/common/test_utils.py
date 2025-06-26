"""
Common utilities for test case loading and management.

This module provides shared functionality for loading test cases from 
data files across different LeetCode problem implementations.
"""

import json
import yaml
from pathlib import Path
from typing import List, Dict, Any


def load_test_cases(test_file_path: str) -> List[Dict[str, Any]]:
    """
    Load all test case files (JSON and YAML) from testgen_output directory.
    
    Args:
        test_file_path: Path to the test file (used to locate testgen_output directory)
        
    Returns:
        List of test case dictionaries with 'id', 'description', 'input', and 'expected' keys
    """
    testgen_output_dir = Path(test_file_path).parent / "testgen_output"
    all_cases = []
    
    # Load YAML files
    for yaml_file in testgen_output_dir.glob("*.yaml"):
        with open(yaml_file, 'r') as f:
            data = yaml.safe_load(f)
            all_cases.extend(data["test_cases"])
    
    for yml_file in testgen_output_dir.glob("*.yml"):
        with open(yml_file, 'r') as f:
            data = yaml.safe_load(f)
            all_cases.extend(data["test_cases"])
    
    # Load JSON files
    for json_file in testgen_output_dir.glob("*.json"):
        with open(json_file, 'r') as f:
            data = json.load(f)
            all_cases.extend(data["test_cases"])
    
    return all_cases