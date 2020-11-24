#!/usr/bin/env python3

"""
Command-line tool using click
"""
import click


@click.command()
@click.option('--argument', default='wololo', help='Only prints arguments that starts with "p"')
def check_argument(argument):
    if argument[0] == 'p':
        print(f"argument: {argument}")


if __name__ == '__main__':
    check_argument()
