#!/usr/bin/env python3

import unittest
from todo_by import todo_by, todo_while

class TodoByTests(unittest.TestCase):
    def test_todo_by_future_date(self):
        @todo_by("2050-01-01")
        def my_function():
            self.assertTrue(True)  # Placeholder assertion

        # The function should execute without raising an error
        my_function()

    def test_todo_by_past_date(self):
        with self.assertRaises(RuntimeError) as cm:
            @todo_by("1970-01-01", "This is a comment")
            def my_function():
                self.assertTrue(True)  # Placeholder assertion

            # The function should raise a RuntimeError with the appropriate error message
            my_function()

        error_message = str(cm.exception)
        expected_error_message = "TODO by Jan 1, 1970 has passed: This is a comment"
        self.assertEqual(error_message, expected_error_message)

    def test_todo_by_no_comment(self):
        with self.assertRaises(RuntimeError) as cm:
            @todo_by("1970-01-01")
            def my_function():
                self.assertTrue(True)  # Placeholder assertion

            # The function should raise a RuntimeError without a comment in the error message
            my_function()

        error_message = str(cm.exception)
        expected_error_message = "TODO by Jan 1, 1970 has passed"
        self.assertEqual(error_message, expected_error_message)

    def test_todo_by_future_version(self):
        @todo_while("999.0.0", "setup.py")
        def my_function():
            self.assertTrue(True)  # Placeholder assertion

        # The function should execute without raising an error
        my_function()

    def test_todo_by_past_version_no_comment(self):

        import sys
        if sys.version_info >= (3, 8):
            from importlib import metadata
        else:
            import importlib_metadata as metadata

        def _get_version():
            try:
                version = metadata.version('todo_by')
            except:
                version = None
            return version

        with self.assertRaises(RuntimeError) as cm:
            @todo_while("1.0.0", "setup.py")
            def my_function():
                self.assertTrue(True)  # Placeholder assertion

            # The function should raise a RuntimeError with the appropriate error message
            my_function()

        error_message = str(cm.exception)
        expected_error_message = f"TODO version requirement '1.0.0' not satisfied by current v{_get_version()}"
        self.assertEqual(error_message, expected_error_message)

if __name__ == '__main__':
    unittest.main()
