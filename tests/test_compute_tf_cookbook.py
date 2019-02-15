"""Test cases for the comments and entities modules"""

from termfrequency import compute_tf_cookbook

# TODO: Add extra test cases from a previous assignment
# TODO: Explore the use of the parameterized pytest test cases
# TODO: Make sure that you understand by compute_tf_cookbook cannot
# be tested by using parameterized pytest test cases

def test_read_file_populates_data_0():
    """Checks that the singleline comment count works"""
    # pylint: disable=len-as-condition
    assert len(compute_tf_cookbook.data) == 0
    compute_tf_cookbook.read_file("inputs/input.txt")
    assert len(compute_tf_cookbook.data) != 0
