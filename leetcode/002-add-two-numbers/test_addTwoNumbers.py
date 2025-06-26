import pytest
import sys
from pathlib import Path
from solution_addTwoNumbers import Solution, ListNode

# Add the leetcode directory to the path so we can import common modules
sys.path.append(str(Path(__file__).parent.parent))
from common.test_utils import load_test_cases


def list_to_linked_list(arr):
    """Convert list to linked list."""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(node):
    """Convert linked list to list."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# Load test cases at module level
TEST_CASES = load_test_cases(__file__)


@pytest.mark.parametrize("test_case", TEST_CASES, ids=[tc["id"] for tc in TEST_CASES])
def test_add_two_numbers(test_case):
    """Data-driven test for Add Two Numbers problem."""
    solution = Solution()
    
    # Convert input lists to linked lists
    l1 = list_to_linked_list(test_case["input"]["l1"])
    l2 = list_to_linked_list(test_case["input"]["l2"])
    
    # Get the result
    result_node = solution.addTwoNumbers(l1, l2)
    result = linked_list_to_list(result_node)
    
    # Verify result matches expected
    expected = test_case["expected"]
    assert result == expected