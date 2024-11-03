#!/usr/bin/env python3
# Author ID: Roniel G. Pangan

def read_file_string(file_name):
    """Takes file_name as string for a file name, returns its entire contents as a string."""
    try:
        with open(file_name, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
        return None
    except IOError:
        print(f"Error: An IOError occurred while accessing the file '{file_name}'.")
        return None

def read_file_list(file_name):
    """Takes a file_name as string for a file name, 
    return its entire contents as a list of lines without new-line characters."""
    try:
        with open(file_name, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
        return None
    except IOError:
        print(f"Error: An IOError occurred while accessing the file '{file_name}'.")
        return None

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))

