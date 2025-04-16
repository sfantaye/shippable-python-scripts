# tests/test_summarize_text.py

import pytest
from unittest import mock
from scripts.ai.summarize_text import summarize_text

@pytest.fixture
def mock_openai_response():
    # Mock the OpenAI response object to simulate the summarization result.
    mock_response = mock.MagicMock()
    mock_response.choices[0].text.strip.return_value = "This is a summary of the input text."
    return mock_response

def test_summarize_text(mock_openai_response):
    # Patch the openai.Completion.create method to use the mocked response
    with mock.patch('openai.Completion.create', return_value=mock_openai_response):
        input_text = "This is a long piece of text that needs summarization."
        summary = summarize_text(input_text)
        
        # Assert that the summary is as expected
        assert summary == "This is a summary of the input text."
