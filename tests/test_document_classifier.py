"""Tests for the document classifier stub."""


def test_document_classifier():
    from src.self_learning.classifiers.document_classifier import classify_document
    assert classify_document("test") == "unknown"
