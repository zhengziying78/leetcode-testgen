import pytest
import json
import yaml
from pathlib import Path
from solution_twoSum import Solution


def load_test_cases():
    """Load all test case files (JSON and YAML) and combine them."""
    testgen_output_dir = Path(__file__).parent / "testgen_output"
    all_cases = []
    
    # Load YAML files
    for yaml_file in testgen_output_dir.glob("*.yaml") or testgen_output_dir.glob("*.yml"):
        with open(yaml_file, 'r') as f:
            data = yaml.safe_load(f)
            all_cases.extend(data["test_cases"])
    
    # Load JSON files
    for json_file in testgen_output_dir.glob("*.json"):
        with open(json_file, 'r') as f:
            data = json.load(f)
            all_cases.extend(data["test_cases"])
    
    return all_cases


# Load test cases at module level
TEST_CASES = load_test_cases()


@pytest.mark.parametrize("test_case", TEST_CASES, ids=[tc["id"] for tc in TEST_CASES])
def test_two_sum_data_driven(test_case):
    """Data-driven test for Two Sum problem."""
    solution = Solution()
    result = solution.twoSum(test_case["input"]["nums"], test_case["input"]["target"])
    
    # Verify result matches expected (handle multiple valid solutions)
    expected = test_case["expected"]
    assert result == expected or sorted(result) == sorted(expected)
    
