# Testing and Debugging (15 minutes):

- Importance of testing in software development.
- Overview of testing frameworks (e.g., unittest).
- Debugging techniques and tools.

## Introduction to TDD

Test-driven development (TDD) is a software development approach that emphasizes writing tests before writing the actual code. In Python, you can follow these basic steps to practice test-driven development:

1. Define the Test: Start by defining a test case for a specific functionality or behavior you want to implement. A test case typically involves specifying the expected behavior of a function or class.

2. Write the Test: Write the test code using a testing framework like `unittest` or `pytest`. The test code should call the function or utilize the class and verify that the actual output matches the expected output.

3. Run the Test: Run the test to ensure that it fails. This step is important because you're testing code that hasn't been implemented yet, so the test should fail at this stage.

4. Write the Code: Write the code that is being tested. Focus on implementing the minimum amount of code required to pass the test.

5. Run the Test Again: Run the test suite again to check if the newly implemented code passes the test. If it passes, you can proceed to the next step. If it fails, revise the code until the test passes.

6. Refactor: Once the test passes, you can refactor your code to improve its design, efficiency, or readability while ensuring that the tests still pass. Refactoring helps maintain clean and maintainable code.

7. Repeat: Repeat this process for each new functionality or behavior you want to implement, gradually building up your codebase with tests and reliable code.

## Benefits of Writing Unit Tests:

1. Verification: Unit tests provide a way to verify that the code behaves as expected. They act as a safety net, catching bugs or regressions before they make their way into production.

2. Documentation: Tests serve as living documentation for your code. They describe the expected behavior and serve as a reference for future developers working on the codebase.

3. Confidence: Having a comprehensive test suite gives confidence that the code is functioning correctly, even when modifications or enhancements are made.

4. Refactoring: Unit tests enable refactoring by ensuring that existing functionality remains intact during code changes. You can refactor with confidence, knowing that the tests will catch any unintended side effects.

5. Collaboration: Tests facilitate collaboration among team members. They provide a common understanding of how the code should work and help identify and resolve issues early in the development process.

6. Continuous Integration: Unit tests are essential for continuous integration and continuous delivery (CI/CD) pipelines. They ensure that new changes don't break existing functionality and allow for automated testing and deployment.

By following the test-driven development approach and writing unit tests, you can improve code quality, reduce bugs, and enhance the overall maintainability of your Python projects.

## Example using pytest

Here's an example of how to use `pytest` for testing a simple Python method. Let's say we have a module called `calculator.py` with a method called `add()` that adds two numbers:

**calculator.py:**
```python
def add(a, b):
    return a + b
```

To write tests for the `add()` method using `pytest`, follow these steps:

1. Install `pytest` by running the command `pip install pytest` in your terminal or command prompt.

2. Create a new file named `test_calculator.py` in the same directory as `calculator.py`.

3. In `test_calculator.py`, import the `pytest` library and the method you want to test.

**test_calculator.py:**
```python
import pytest
from calculator import add
```

4. Write test functions using the `pytest` framework. Test functions should have names starting with `test_` to be automatically discovered by `pytest`. Use the `assert` statement to check if the actual output matches the expected output.

**test_calculator.py:**
```python
def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-5, -7) == -12

def test_add_zero():
    assert add(10, 0) == 10
```

5. To run the tests, simply execute `pytest` in the terminal or command prompt in the same directory as `test_calculator.py`. `pytest` will automatically discover and execute all the test functions in the file.

```
$ pytest
```

The output will show the status of each test, indicating if they passed or failed:

```
============================= test session starts ==============================
platform linux -- Python 3.8.10, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /path/to/your/directory
collected 3 items

test_calculator.py ...                                                [100%]

============================== 3 passed in 0.01s ===============================
```

In this example, we wrote three test functions to verify the behavior of the `add()` method. Each test asserts that the actual result of the `add()` method matches the expected result for different scenarios.

By running the `pytest` command, the tests will be executed, and you will see the results. If all tests pass, it means that the `add()` method is functioning as expected. If any test fails, `pytest` will provide details about the failure, helping you identify and fix the issue.

Note: It's good practice to organize your tests into separate files or directories, especially as your test suite grows larger. `pytest` follows a set of conventions to discover and run tests automatically, making it easy to scale your testing efforts.

## Example using unittest

Here's the same example of testing the `add()` method, but this time using the built-in `unittest` module in Python:

**calculator.py:**
```python
def add(a, b):
    return a + b
```

To write tests for the `add()` method using `unittest`, follow these steps:

1. Import the `unittest` module and the method you want to test.

**test_calculator.py:**
```python
import unittest
from calculator import add
```

2. Create a subclass of `unittest.TestCase` to define your test case.

**test_calculator.py:**
```python
class CalculatorTest(unittest.TestCase):
    def test_add_positive_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        result = add(-5, -7)
        self.assertEqual(result, -12)

    def test_add_zero(self):
        result = add(10, 0)
        self.assertEqual(result, 10)
```

3. To run the tests, you can execute the `unittest` module directly by adding the following code at the bottom of your test file:

**test_calculator.py:**
```python
if __name__ == '__main__':
    unittest.main()
```

4. Run the `test_calculator.py` file. The `unittest` module will discover and execute the test methods within the `CalculatorTest` class.

```
$ python test_calculator.py
```

The output will show the status of each test, indicating if they passed or failed:

```
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

In this example, we created a subclass of `unittest.TestCase` named `CalculatorTest`, which contains three test methods. Each test method calls the `add()` function with different inputs and asserts that the actual result matches the expected result using the `self.assertEqual()` method provided by `unittest.TestCase`.

By running the test file, `unittest` will execute the test methods and display the results. If all tests pass, it means that the `add()` method is functioning as expected. If any test fails, `unittest` will provide details about the failure, helping you identify and fix the issue.

The `unittest` module offers additional features for test setup and teardown, test discovery, and more. It's a comprehensive testing framework that comes built-in with Python, making it a powerful choice for unit testing in Python projects.

## Ooh.. Too many choices, how to decide unittest vs pytest!

The `pytest` and `unittest` frameworks are both popular choices for writing unit tests in Python, but they have some key differences in terms of syntax, features, and philosophy. Here are the key differences between `pytest` and `unittest`:

1. Syntax: `pytest` offers a more concise and expressive syntax compared to `unittest`. It allows you to write tests using plain functions rather than defining test classes and methods like in `unittest`. `pytest` leverages Python's assert statement for assertions, making the test code more readable and natural.

2. Test Discovery: `pytest` has powerful test discovery capabilities. It automatically discovers and runs all test functions in files that match a certain naming pattern (e.g., files starting with `test_` or ending with `_test.py`). In contrast, `unittest` requires explicit definition of test classes and methods and relies on a test runner to execute them.

3. Fixtures: `pytest` provides a flexible and powerful fixture mechanism that allows you to set up and tear down resources needed for tests. Fixtures help with test setup and can be reused across multiple tests. `unittest` also has similar functionality, but `pytest` offers a more streamlined and intuitive approach.

4. Assertions: Both frameworks provide a range of assertions for verifying expected outcomes. `unittest` has a wide variety of assertions built-in, while `pytest` provides a smaller set of core assertions. However, `pytest` can be extended with additional assertion libraries like `pytest-codestyle`, `pytest-approx`, or `pytest-mock`.

5. Plugins and Ecosystem: `pytest` has a rich ecosystem of plugins that extend its functionality. These plugins cover a wide range of areas such as test coverage, code analysis, mocking, parallel testing, and more. `unittest` has a more limited ecosystem of extensions and plugins.

When to Use `pytest` or `unittest`:

- Use `pytest` when you prefer a more concise and expressive syntax, powerful test discovery, and a rich ecosystem of plugins. `pytest` is especially useful for complex test setups, fixtures, and parameterized testing.

- Use `unittest` when you prefer a more traditional and structured approach to writing tests. `unittest` is well-suited for larger projects with more extensive test suites that require a hierarchical test organization.

- If you're starting a new project or have the freedom to choose, it's worth considering the benefits of `pytest`, such as its ease of use, readability, and powerful features.

- If you're working with an existing codebase that already uses `unittest`, it may be more convenient to continue using `unittest` to maintain consistency and avoid rewriting existing tests.

Ultimately, the choice between `pytest` and `unittest` depends on personal preference, the needs of your project, and the existing test infrastructure. Both frameworks are capable of writing effective unit tests, so it's essential to evaluate their features and decide which aligns better with your testing goals and style.

Don't compromise writing good tests, pick one!

## Why is TDD so important for your career capital?

"If I were given an hour to solve a problem, I would spend 55 minutes pondering over the problem and only 5 minutes contemplating solutions." 
― Albert Einstein

When it comes to developing software, it is crucial to dedicate ample time to thinking about test scenarios. The depth of your test scenarios provides valuable insights into your understanding of the problem you are attempting to solve.

Always keep the following points in mind:

- If you find it challenging to outline test scenarios for the method you have just written, it indicates a potential lack of understanding of the problem. Take this as a hint to delve deeper into grasping the intricacies of the task at hand.

- Embrace the practice of red/green/refactor from the very start of your career. This approach holds immense value because, by the time your code is complete, you will have already addressed the testing phase. 

- The beauty of the red/green/refactor cycle lies in the fact that, when you finish writing your code, you will have no tests left to create. This systematic process allows you to evolve your code with confidence.

- Consider the maintainability of your code by investing time in writing comprehensive and effective tests. Adequate test coverage ensures that your code remains robust and facilitates easier maintenance in the future.

- Adopt a pragmatic approach to testing. Writing tests solely for the purpose of achieving 100% test coverage on simple getter/setter methods may not be the best use of your time. Instead, focus on writing tests for complex business logic methods that aim to solve real-world problems. By doing so, you lay a solid foundation of feedback that instills confidence in future contributors. They will greatly appreciate the safety net you've created, which helps detect any unintended impact their changes may have on the existing behavior.

- Therefore, Test-Driven Development (TDD) is an investment in time that benefits all future contributors. By paying it forward and prioritizing testing, you contribute to a culture of confidence, enabling future modifications with ease. Embrace the mindset of leaving behind a legacy of trust and empowerment for those who follow in your footsteps!

Remember, the time invested in writing tests is a small price to pay for the long-term benefits they bring. So, seize the opportunity to establish a robust testing practice early on and let it guide your journey as a software developer.
