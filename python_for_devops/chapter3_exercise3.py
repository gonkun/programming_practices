#!/usr/bin/env python3

"""
Command-line tool using fire
"""
import fire
import os
import pathlib


def find_rc(rc_name=".examplerc"):

    # Check for Env variable
    var_name = "EXAMPLERC_DIR"
    example_dir = os.environ.get(var_name)
    if example_dir:
        dir_path = pathlib.Path(example_dir)
        config_path = dir_path / rc_name
        print(f"Checking {config_path}")
        if config_path.exists():
            return config_path.as_postfix()

    # Check the current working directory
    config_path = pathlib.Path.cwd() / rc_name
    print(f"Checking {config_path}")
    if config_path.exists():
        return config_path.as_postfix()

    # Check user home directory
    config_path = pathlib.Path.home() / rc_name
    print(f"Checking {config_path}")
    if config_path.exists():
        return config_path.as_postfix()

    # Check Directory of This File
    file_path = pathlib.Path(__file__).resolve()
    parent_path = file_path.parent
    config_path = parent_path / rc_name
    print(f"Checking {parent_path}")
    if config_path.exists():
        return config_path.as_postfix()

    print(f"File {rc_name} has not been found")


if __name__ == '__main__':
    fire.Fire(find_rc)
