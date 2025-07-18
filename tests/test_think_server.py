import unittest
from unittest.mock import patch
from think_server import think


class TestThinkServer(unittest.TestCase):
    @patch("builtins.print")
    def test_think(self, mock_print):
        """
        Test the think function to ensure it prints the correct output.
        """
        thought_text = "This is a test thought."
        think(thought_text)
        mock_print.assert_called_once_with(f"Received thought: {thought_text}")


if __name__ == "__main__":
    unittest.main()
