#!/usr/bin/python3
import sys
import signal

# Initialize counters and metrics
total_file_size = 0
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0


def print_stats():
    """Print the accumulated statistics."""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print("{}: {}".format(code, status_code_counts[code]))


def handle_interrupt(signum, frame):
    """Handle the keyboard interruption (CTRL + C) and print statistics."""
    print_stats()
    sys.exit(0)


# Register signal handler for keyboard interruption
signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        line = line.strip()
        if len(line) == 0:
            continue

        # Split the line into components
        parts = line.split()
        if len(parts) < 7:
            continue

        # Extract and validate components
        ip_address = parts[0]
        status_code = parts[-2]
        try:
            file_size = int(parts[-1])
        except ValueError:
            continue

        # Update metrics
        total_file_size += file_size
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        line_count += 1

        # Print stats after every 10 lines
        if line_count % 10 == 0:
            print_stats()

except Exception as e:
    print(e)

# Print any remaining stats if the input ends
print_stats()
