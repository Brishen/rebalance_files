# File Rebalancer

The File Rebalancer project consists of a Python script designed to rebalance files within a specified directory. This rebalancing process involves copying each file to a new location and then deleting the original, ensuring data blocks are rewritten across all drives. This operation can be particularly useful in environments where filesystem performance or data distribution across physical media is a concern, such as in RAID setups or distributed filesystems.

## Features

- **Directory Traversal**: Recursively processes all files within the given directory, excluding symlinks to prevent potential issues.
- **Progress Monitoring**: Displays a progress bar with detailed metrics, including percentage complete, number of files processed, total data volume processed, data processing rate, and estimated time to completion.
- **Force Mode**: Allows the operation to proceed without user confirmation, suitable for automated scripts or environments where manual input is not feasible.

## Requirements

- Python 3.6 or higher
- No external Python packages are required for the main script, ensuring compatibility with environments where installing additional dependencies may not be possible.

## Usage

To use the File Rebalancer, navigate to the directory containing `rebalance_files.py` and execute the script from the command line, specifying the target directory as an argument. Optionally, you can use the `--force` flag to bypass the confirmation prompt.

### Example

    python rebalance_files.py /path/to/my/directory --force

This command will start the rebalancing operation on `/path/to/my/directory` without user confirmation.

## Testing

A test suite for the File Rebalancer is provided in `test_rebalance_files.py`. To run the tests, ensure you have Python's `unittest` framework available in your environment (included with standard Python installations) and execute the following command:

    python -m unittest test_rebalance_files.py


## Contributing

Contributions to the File Rebalancer project are welcome! Please feel free to submit pull requests with bug fixes, improvements, or additional features.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
