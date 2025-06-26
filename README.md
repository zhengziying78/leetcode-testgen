# LeetCode Test Case Generator

> "For many times, I found that testing a solution could be equally hard as writing a solution, if not harder."

This repository demonstrates that **generating comprehensive test cases for algorithmic problems can be as challenging as solving the problems themselves**. While most developers focus on implementing solutions, creating robust test cases often requires deep algorithmic thinking and creative problem-solving.

## Project Overview

This project systematically explores test case generation algorithms for LeetCode problems, starting with the first 200-300 problems. For each problem, we develop and implement algorithms that can generate random, comprehensive test cases without simply reimplementing the original solution (which would be a "circular proof").

## Motivation

The inspiration for this project comes from the complexity encountered when trying to generate test cases for seemingly simple problems. For example, generating test cases for a "detect cycle in directed graph" problem requires sophisticated graph construction techniques to ensure proper coverage of both cyclic and acyclic scenarios.

As explored in detail in [this blog post](https://zhengziying.com/2015/03/02/how-to-randomly-generate-test-cases-for-a-hascycle-method/), effective test case generation often involves:

- **Avoiding circular reasoning**: Not reimplementing the solution to verify correctness
- **Ensuring comprehensive coverage**: Generating edge cases and boundary conditions
- **Maintaining algorithmic soundness**: Using mathematically valid approaches to construct test inputs
- **Scaling complexity**: Creating test cases of varying difficulty and size

## Repository Structure

```
leetcode-testgen/
├── problems/           # Individual problem implementations
│   ├── 001-two-sum/
│   ├── 002-add-two-numbers/
│   └── ...
├── generators/         # Reusable test case generation utilities
├── docs/              # Documentation and analysis
└── examples/          # Example outputs and usage
```

## Example: Cycle Detection Test Case Generation

One of the most illustrative examples is generating test cases for cycle detection in directed graphs. The challenge isn't just creating random graphs—it's systematically creating graphs where you can control and verify the presence or absence of cycles without reimplementing cycle detection.

The solution involves:
1. Strategic edge classification (red/blue arcs)
2. Reachability analysis for cycle formation
3. Controlled graph construction to ensure known outcomes

## Goals

- **Educational**: Demonstrate the complexity and importance of thorough test case design
- **Practical**: Provide reusable test case generators for common algorithmic patterns
- **Analytical**: Document the algorithmic thinking required for each problem's test generation
- **Comprehensive**: Cover a wide range of LeetCode problem types and difficulty levels

## Contributing

Each problem implementation should include:
- The test case generation algorithm
- Analysis of why naive approaches fail
- Examples of generated test cases
- Documentation of the underlying mathematical/algorithmic principles

## Getting Started

```bash
git clone https://github.com/yourusername/leetcode-testgen.git
cd leetcode-testgen
# Follow individual problem README files for specific instructions
```

## Philosophy

This project operates on the principle that **good testing requires as much algorithmic sophistication as good solving**. By treating test case generation as a first-class algorithmic challenge, we can build better, more reliable software while deepening our understanding of the underlying problems.

---

*"The best way to understand a problem deeply is to try to generate comprehensive test cases for it."*