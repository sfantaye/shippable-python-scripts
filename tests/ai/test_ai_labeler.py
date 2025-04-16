"""
✅ test_ai_labeler.py
Tests the smart_data_labeler module from scripts.ai.
Covers:
- Multiple categories of input
- Mixed-category detection
- Case insensitivity
- No keyword fallback
- Punctuation tolerance
"""

import pytest
from scripts.ai import smart_data_labeler

def test_detect_technical_problem():
    tags = smart_data_labeler.label_data("There's a bug in the system.")
    assert "technical_problem" in tags

    tags = smart_data_labeler.label_data("ERROR on line 400")
    assert "technical_problem" in tags

    tags = smart_data_labeler.label_data("We encountered a serious issue.")
    assert "technical_problem" in tags

def test_detect_feature_request():
    tags = smart_data_labeler.label_data("Can you add this feature?")
    assert "feature_request" in tags

    tags = smart_data_labeler.label_data("This is a feature REQUEST.")
    assert "feature_request" in tags

def test_detect_positive_feedback():
    tags = smart_data_labeler.label_data("Thank you for resolving this.")
    assert "positive_feedback" in tags

    tags = smart_data_labeler.label_data("I just wanted to say THANK YOU.")
    assert "positive_feedback" in tags

def test_mixed_labels():
    tags = smart_data_labeler.label_data("Thank you for fixing the bug and adding the feature.")
    assert "technical_problem" in tags
    assert "positive_feedback" in tags
    assert "feature_request" in tags

def test_case_insensitivity():
    tags = smart_data_labeler.label_data("ThAnK YoU")
    assert "positive_feedback" in tags

    tags = smart_data_labeler.label_data("BUG report")
    assert "technical_problem" in tags

def test_punctuation_and_noise_tolerance():
    tags = smart_data_labeler.label_data("Bug?! Seriously, why again?!")
    assert "technical_problem" in tags

def test_irrelevant_text():
    tags = smart_data_labeler.label_data("Let's meet tomorrow to discuss the roadmap.")
    assert tags == []

def test_empty_input():
    tags = smart_data_labeler.label_data("")
    assert tags == []

def test_whitespace_input():
    tags = smart_data_labeler.label_data("     ")
    assert tags == []

