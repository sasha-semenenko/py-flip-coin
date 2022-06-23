import ast
import inspect
from unittest import mock
import pytest

from app.main import flip_coin


def generate_cases(n: int) -> list:
    cases = []
    for i in range(10):
        if i % 2 != 0:
            cases += [[j for j in range(0, 10000, n + i)]]
        else:
            cases += [[j for j in range(1, 10000)]]

    return cases


@pytest.mark.parametrize(
    "n, expected",
    [
        pytest.param(
            10,
            {
                0: 0.01,
                1: 0.0,
                2: 0.28,
                3: 3.85,
                4: 25.97,
                5: 69.8,
                6: 0.04,
                7: 0.01,
                8: 0.03,
                9: 0.01,
                10: 0.0
            }
        ),
        pytest.param(
            7,
            {
                0: 0.06,
                1: 0.78,
                2: 3.45,
                3: 7.59,
                4: 15.24,
                5: 72.79,
                6: 0.03,
                7: 0.02,
                8: 0.02,
                9: 0.02,
                10: 0.0
            }
        ),
    ],
)
@mock.patch('random.choice')
def test_random_choice_when_head_and_tail(choice_mock, n, expected):
    code = inspect.getsource(flip_coin)
    parsed_code = ast.parse(code)

    if "choice" in ast.dump(parsed_code):
        test_case = []

        cases = generate_cases(n)

        for counter in range(10000):
            for i in range(10):
                if i + counter in cases[i]:
                    test_case += ["tail"]
                else:
                    test_case += ["head"]

        choice_mock.side_effect = test_case

        try:
            assert flip_coin() == expected
        except KeyError:
            return


@pytest.mark.parametrize(
    "n, expected",
    [
        pytest.param(
            10,
            {
                0: 0.01,
                1: 0.0,
                2: 0.28,
                3: 3.85,
                4: 25.97,
                5: 69.8,
                6: 0.04,
                7: 0.01,
                8: 0.03,
                9: 0.01,
                10: 0.0
            }
        ),
        pytest.param(
            7,
            {
                0: 0.06,
                1: 0.78,
                2: 3.45,
                3: 7.59,
                4: 15.24,
                5: 72.79,
                6: 0.03,
                7: 0.02,
                8: 0.02,
                9: 0.02,
                10: 0.0
            }
        ),
    ],
)
@mock.patch('random.choice')
def test_random_choice_when_heads_and_tails(choice_mock, n, expected):
    code = inspect.getsource(flip_coin)
    parsed_code = ast.parse(code)

    if "choice" in ast.dump(parsed_code):
        test_case = []

        cases = generate_cases(n)

        for counter in range(10000):
            for i in range(10):
                if i + counter in cases[i]:
                    test_case += ["tails"]
                else:
                    test_case += ["heads"]

        choice_mock.side_effect = test_case

        try:
            assert flip_coin() == expected
        except KeyError:
            return


@pytest.mark.parametrize(
    "n, expected",
    [
        pytest.param(
            10,
            {
                0: 0.01,
                1: 0.0,
                2: 0.28,
                3: 3.85,
                4: 25.97,
                5: 69.8,
                6: 0.04,
                7: 0.01,
                8: 0.03,
                9: 0.01,
                10: 0.0
            }
        ),
        pytest.param(
            7,
            {
                0: 0.06,
                1: 0.78,
                2: 3.45,
                3: 7.59,
                4: 15.24,
                5: 72.79,
                6: 0.03,
                7: 0.02,
                8: 0.02,
                9: 0.02,
                10: 0.0
            }
        ),
    ],
)
@mock.patch('random.choice')
def test_random_choice_when_heads_and_tails(choice_mock, n, expected):
    code = inspect.getsource(flip_coin)
    parsed_code = ast.parse(code)

    if "choice" in ast.dump(parsed_code):
        test_case = []

        cases = generate_cases(n)

        for counter in range(10000):
            for i in range(10):
                if i + counter in cases[i]:
                    test_case += ["tail"]
                else:
                    test_case += ["eagle"]

        choice_mock.side_effect = test_case

        try:
            assert flip_coin() == expected
        except KeyError:
            return


@pytest.mark.parametrize(
    "n, expected",
    [
        pytest.param(
            10,
            {
                0: 0.01,
                1: 0.0,
                2: 0.28,
                3: 3.85,
                4: 25.97,
                5: 69.8,
                6: 0.04,
                7: 0.01,
                8: 0.03,
                9: 0.01,
                10: 0.0
            }
        ),
        pytest.param(
            7,
            {
                0: 0.06,
                1: 0.78,
                2: 3.45,
                3: 7.59,
                4: 15.24,
                5: 72.79,
                6: 0.03,
                7: 0.02,
                8: 0.02,
                9: 0.02,
                10: 0.0
            }
        ),
    ],
)
@mock.patch('random.randint')
def test_random_choice_when_zero_and_one(choice_mock, n, expected):
    code = inspect.getsource(flip_coin)
    parsed_code = ast.parse(code)

    if "randint" in ast.dump(parsed_code):

        test_case = []

        cases = generate_cases(n)

        for counter in range(10000):
            for i in range(10):
                if i + counter in cases[i]:
                    test_case += [0]
                else:
                    test_case += [1]

        choice_mock.side_effect = test_case

        try:
            assert flip_coin() == expected
        except KeyError:
            return


@pytest.mark.parametrize(
    "n, expected",
    [
        pytest.param(
            10,
            {
                0: 0.01,
                1: 0.0,
                2: 0.28,
                3: 3.85,
                4: 25.97,
                5: 69.8,
                6: 0.04,
                7: 0.01,
                8: 0.03,
                9: 0.01,
                10: 0.0
            }
        ),
        pytest.param(
            7,
            {
                0: 0.06,
                1: 0.78,
                2: 3.45,
                3: 7.59,
                4: 15.24,
                5: 72.79,
                6: 0.03,
                7: 0.02,
                8: 0.02,
                9: 0.02,
                10: 0.0
            }
        ),
    ],
)
@mock.patch('random.randint')
def test_random_randint_when_one_and_two(choice_mock, n, expected):
    code = inspect.getsource(flip_coin)
    parsed_code = ast.parse(code)

    if "randint" in ast.dump(parsed_code):
        test_case = []

        cases = generate_cases(n)

        for counter in range(10000):
            for i in range(10):
                if i + counter in cases[i]:
                    test_case += [1]
                else:
                    test_case += [2]

        choice_mock.side_effect = test_case

        try:
            assert flip_coin() == expected
        except KeyError:
            return
