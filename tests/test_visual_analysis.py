"""Tests for visual analysis stubs."""


def test_gemini_vision():
    from src.visual_analysis.core.gemini_vision import GeminiVision
    assert isinstance(GeminiVision(), GeminiVision)
