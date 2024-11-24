def read(filepath):
    """Reads the to-do list from a file."""
    with open(filepath, 'r') as f:
        return f.readlines()


def write(li, filepath):
    """Writes the to-do list to a file."""
    with open(filepath, 'w') as f:
        f.writelines(li)


if __name__ == "__main__":
    print("Welcome to the digital base".upper())
