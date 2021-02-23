# Assert that a certain exception is raised
import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    # Assert that a code block/function call raises ``expected_exception``
    # or raise a failure exception otherwise.
    with pytest.raises(SystemExit):
        f()
