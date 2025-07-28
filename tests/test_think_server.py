import unittest
from unittest.mock import patch
from q_think_mcp.server import think


class TestThinkServer(unittest.TestCase):
    @patch("builtins.print")
    def test_think_basic(self, mock_print):
        """
        Test the think function to ensure it prints the correct output and returns expected value.
        """
        thought_text = "This is a test thought."
        result = think(thought_text)

        # Verify print was called with correct message
        mock_print.assert_called_once_with(f"Received thought: {thought_text}")

        # Verify return value
        self.assertEqual(result, "Recorded")

    @patch("builtins.print")
    def test_think_empty_string(self, mock_print):
        """
        Test the think function with empty string input.
        """
        thought_text = ""
        result = think(thought_text)

        mock_print.assert_called_once_with(f"Received thought: {thought_text}")
        self.assertEqual(result, "Recorded")

    @patch("builtins.print")
    def test_think_long_text(self, mock_print):
        """
        Test the think function with long text input.
        """
        thought_text = (
            "This is a very long thought that contains multiple sentences and complex reasoning. "
            * 10
        )
        result = think(thought_text)

        mock_print.assert_called_once_with(f"Received thought: {thought_text}")
        self.assertEqual(result, "Recorded")

    @patch("builtins.print")
    def test_think_special_characters(self, mock_print):
        """
        Test the think function with special characters and unicode.
        """
        thought_text = "思考：这是一个包含特殊字符的测试！@#$%^&*()_+-=[]{}|;':\",./<>?"
        result = think(thought_text)

        mock_print.assert_called_once_with(f"Received thought: {thought_text}")
        self.assertEqual(result, "Recorded")

    @patch("builtins.print")
    def test_think_newlines(self, mock_print):
        """
        Test the think function with newlines and formatting.
        """
        thought_text = "Line 1\nLine 2\n\tTabbed line\n  Spaced line"
        result = think(thought_text)

        mock_print.assert_called_once_with(f"Received thought: {thought_text}")
        self.assertEqual(result, "Recorded")


if __name__ == "__main__":
    unittest.main()
