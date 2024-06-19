# Syscall Number to Name

This Python script is designed to convert a JSON file containing syscall numbers to a JSON file containing syscall names. It achieves this by parsing the list of syscalls from the C header file `syscallent.h` (https://gitlab.com/strace/strace/-/blob/master/src/linux/x86_64/syscallent.h) to create a mapping from syscall numbers to names.

## Usage
To use Syscall Number to Name, follow these steps:
1. **Install Python:** Ensure you have Python installed on your system.
2. **Run the Program:** Run the script using the following command:
   ```
   python3 parse_syscall_numbers.py <input_file>
   ```
   - `<input_file>`: Name of the JSON file containg syscall numbers.
4. **View Results**: The parsed content will be printed in the console and written to the file named `parsed_<input_file>`.


## Example
Suppose you have `syscallent.h` and `diff.json` files in your directory. To run the script and parse syscall names from `diff.json`, execute the following command:
```
python parse_syscall_numbers.py diff.json
```
This will print the list of syscall names and save them to a file named `parsed_diff.json`.

## Note
- Ensure that `syscallent.h` is in the same directory as the script. It can be found on the github provided.
