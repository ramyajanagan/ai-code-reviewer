import pytest
from unittest.mock import patch, MagicMock
from reviewer.git_utils import get_git_diff
from reviewer.review_engine import analyze_diff

def test_get_git_diff_empty():
    """Test that get_git_diff handles empty output correctly."""
    with patch("subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(stdout="")
        diff = get_git_diff()
        assert diff == ""

def test_analyze_diff_no_diff():
    """Test analyze_diff output when diff is empty."""
    result = analyze_diff("", api_key="fake-key")
    assert result == "No code changes detected in Git repository."

@patch("httpx.Client.post")
def test_analyze_diff_success(mock_post):
    """Test analyze_diff with a mocked successful API response."""
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "choices": [{"message": {"content": "- Code looks good!"}}]
    }
    mock_response.raise_for_status = MagicMock()
    mock_post.return_value = mock_response

    output = analyze_diff("diff --git a/file.py", api_key="fake-key")
    assert "- Code looks good!" in output
