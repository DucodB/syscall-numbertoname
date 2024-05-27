# syscall-number-to-name

## Description
This Python script is designed to parse syscall numbers from the C header file `syscallent.h` (https://gitlab.com/strace/strace/-/blob/master/src/linux/x86_64/syscallent.h) and then map them to their corresponding syscall names. It takes a JSON file containing syscall numbers as input, converts those numbers to syscall names using the mapping extracted from `syscallent.h`, and prints the resulting list of syscall names. Additionally, it saves the list of syscall names to a new JSON file with a name combining the prefix 'parsed_' and the name of the input file provided as a parameter.

## Usage
1. Ensure you have Python installed on your system.
2. Run the script using the following command:
   ```
   python3 parse_syscall_numbers.py filename
   ```
   Replace `filename` with the name of the input file containing syscall numbers.


## Example
Suppose you have `syscallent.h` and `diff.json` files in your directory. To run the script and parse syscall names from `diff.json`, execute the following command:
```
python parse_syscall_numbers.py diff.json
```
This will print the list of syscall names and save them to a file named `parsed_diff.json`.

## Note
- Ensure that `syscallent.h` is in the same directory as the script. It can be found on the github provided.
- Make sure to provide the correct file name as a parameter when executing the script.
