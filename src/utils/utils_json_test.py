import unittest
import tempfile
import os
import json
from io import StringIO
from unittest.mock import patch

from src.utils.utils_json import read_json, print_json, write_json


class TestJSONFunctions(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the temporary directory and its contents
        for root, dirs, files in os.walk(self.temp_dir, topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        os.rmdir(self.temp_dir)

    def test_read_json(self):
        # Create a sample JSON file in the temporary directory
        sample_data = {"key": "value"}
        json_file = os.path.join(self.temp_dir, "test.json")
        with open(json_file, "w") as f:
            f.write(json.dumps(sample_data))

        # Test reading the JSON file
        result = read_json(json_file)
        self.assertEqual(result, sample_data)

    def test_write_json(self):
        # Create sample JSON data
        sample_data = {"key": "value"}
        json_file = os.path.join(self.temp_dir, "test.json")

        # Write JSON data to the temporary file
        write_json(json_file, sample_data)

        # Read the written JSON file and compare its contents
        with open(json_file, "r") as f:
            result = json.load(f)
        self.assertEqual(result, sample_data)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_json(self, mock_stdout):
        # Create sample JSON data
        sample_data = {"key": "value"}

        # Call the print_json function
        print_json(sample_data, tag="Test Tag")

        # Get the captured output
        printed_text = mock_stdout.getvalue()

        # Check if the printed output contains the tag and JSON data
        expected_output = 'Test Tag {\n  "key": "value"\n}\n'
        self.assertEqual(printed_text, expected_output)


if __name__ == '__main__':
    unittest.main()
