"""Tests for learning system stubs."""


def test_progressive_learning():
    from src.self_learning.progressive_learning import progressive_learn
    assert progressive_learn() is None
