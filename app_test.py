"""Run some trivial tests"""
from app import health


def test_health():
    assert health() == "All is well"


# def test_catch_all():
#     """Method catch_all should return a known message, including route."""
#     assert catch_all("bogus") == "Hello, World! You requested path bogus\n"
