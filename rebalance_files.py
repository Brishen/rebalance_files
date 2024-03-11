from pathlib import Path
import shutil
import time


def print_progress_bar(iteration, total, current_size, total_size, start_time, prefix='', suffix='', decimals=1,
                       length=50, fill='█', print_end="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        current_size- Required  : current total size processed (Float)
        total_size  - Required  : total size to process (Float)
        start_time  - Required  : start time of the process (Time)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        print_end   - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    current_time = time.time()
    elapsed_time = current_time - start_time
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    rate = current_size / elapsed_time if elapsed_time > 0 else 0
    estimated_total_time = total_size / rate if rate > 0 else 0
    remaining_time = estimated_total_time - elapsed_time if estimated_total_time - elapsed_time > 0 else 0
    progress_message = f'\r{prefix} |{bar}| {percent}% {suffix} [{iteration}/{total} Files, {current_size:.2f}/{total_size:.2f} MB, {rate:.2f} MB/s, ETA: {remaining_time:.2f}s]'
    print(progress_message, end=print_end)
    # print(f'\r{prefix} |{bar}| {percent}% {suffix} [{iteration}/{total} Files, {current_size:.2f}/{total_size:.2f} MB, {rate:.2f} MB/s, ETA: {remaining_time:.2f}s]', end=print_end)
    # Print New Line on Complete
    if iteration == total:
        print()


def rebalance_dir(directory):
    directory_path = Path(directory)
    files = [p for p in directory_path.rglob('*') if p.is_file() and not p.is_symlink()]
    total_files = len(files)
    total_size = sum(f.stat().st_size for f in files) / (1024 * 1024)  # Total size in MB
    processed_size = 0  # Track the size of processed files in MB
    processed_files = 0  # Count of processed files
    start_time = time.time()  # Start time of the rebalance operation

    print(f"Total size to rebalance: {total_size:.2f} MB across {total_files} files.")

    for file_path in files:
        file_size = file_path.stat().st_size / (1024 * 1024)  # Size in MB

        counter = 1
        new_name = file_path.parent / f"{file_path.stem}{counter}{file_path.suffix}"

        while new_name.exists():
            counter += 1
            new_name = file_path.parent / f"{file_path.stem}{counter}{file_path.suffix}"

        shutil.copy(file_path, new_name)
        file_path.unlink()
        new_name.rename(file_path)

        processed_files += 1
        processed_size += file_size
        print_progress_bar(processed_files, total_files, processed_size, total_size, start_time, prefix='Progress:',
                           suffix='Complete', length=50)

    print("Rebalance complete!")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    directory_path = Path(directory)

    if directory_path.is_dir():
        directory_realpath = directory_path.resolve()

        confirm = input(f"Balance the files within [{directory_realpath}] (y/n)? ")
        if confirm.lower() == 'y':
            rebalance_dir(directory_realpath)
            print("Complete!")
        else:
            print("Operation cancelled.")
    else:
        print('Invalid directory given!')
