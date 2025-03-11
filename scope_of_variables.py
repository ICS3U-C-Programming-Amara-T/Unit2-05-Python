#!/usr/bin/env python3

# Created By: Amara Tie

# Date: Month March 7, 2025

# This program shows how local and global variables work.


# global variable
variable_x = 49


def local_variable() -> None:
    """The local_variable() function creates local variables, returns None."""
    variable_x = 29
    variable_y = 0

    variable_x = variable_x + 7
    variable_z = variable_x + variable_y

    print(f"Local variable:  {variable_x} + {variable_y} = {variable_z}")


def global_variable() -> None:
    """The global_variable() function uses a global variable, returns None."""
    global variable_x
    variable_y = 0

    variable_x = variable_x + 7
    variable_z = variable_x + variable_y

    print(f"Global variable: {variable_x} + {variable_y} = {variable_z}")


def main() -> None:
    """The main() function shows local and global variables, returns None."""
    local_variable()
    global_variable()

    print("\nDone.")


if __name__ == "__main__":
    main()
