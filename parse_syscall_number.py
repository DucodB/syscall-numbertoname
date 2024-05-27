import re
import json
import sys

def parse_syscall_mapping(filename):
    syscall_map = {}
    with open(filename, 'r') as file:
        for line in file:
            # Match lines with the format: [ number ] = { args, flags, SEN(syscall), "name" },
            match = re.match(r'\[\s*(\d+)\s*\] = \{[^"]*?"([^"]+)"\s*\}', line)
            if match:
                syscall_number = int(match.group(1))
                syscall_name = match.group(2)
                syscall_map[syscall_number] = syscall_name
    return syscall_map

def open_files(filename):
	# Load the syscall mapping
	syscall_map = parse_syscall_mapping('syscallent.h')

	# Load the JSON file containing syscall numbers
	with open(filename, 'r') as file:
	    syscall_numbers = json.load(file)

	# Convert syscall numbers to names
	syscall_names = [syscall_map.get(num, f'unknown_syscall_{num}') for num in syscall_numbers]

	# Print the resulting list of syscall names
	print(syscall_names)

	# Save to a new JSON file called parsed_filename where filename is the provided parameter
	with open(f'parsed_{filename}', 'w') as file:
	    json.dump(syscall_names, file, indent=4)
	    
if __name__ == "__main__":
    filename = sys.argv[1]
    open_files(filename)
