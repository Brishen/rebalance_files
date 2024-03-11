import io
import time
import unittest
from contextlib import redirect_stdout

from rebalance_files import print_progress_bar


class TestPrintProgressBar(unittest.TestCase):
    def test_progress_bar_output(self):
        # Redirect stdout to capture the print output
        f = io.StringIO()
        with redirect_stdout(f):
            # Example parameters
            iteration = 50
            total = 100
            current_size = 25
            total_size = 50
            start_time = time.time() - 60  # simulate 60 seconds elapsed
            print_progress_bar(iteration, total, current_size, total_size, start_time)
        output = f.getvalue().strip()

        print(output)
        # Expected values based on the example parameters
        expected_rate = 25 / 60  # MB/s
        expected_eta = 25 / expected_rate  # seconds
        expected_output = f"|█████████████████████████-------------------------| 50.0%  [50/100 Files, 25.00/50.00 MB, {expected_rate:.2f} MB/s, ETA: {expected_eta:.2f}s]"

        # Verify that the output starts with the expected format
        # Note: This is a simplified check and may need adjustments based on the exact output format and rounding
        self.assertTrue(output.startswith("|"), "Progress bar output format is incorrect")
        self.assertIn("50.0%", output, "Progress percentage is incorrect")
        self.assertEqual(output, expected_output)
