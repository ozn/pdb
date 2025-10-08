"""Tests for learner stubs."""


def test_base_learner():
    from src.self_learning.learners.base_learner import BaseLearner
    learner = BaseLearner()
    assert hasattr(learner, 'learn')
