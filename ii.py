#!/usr/bin/env python3

import click
from lib.uptime import get_uptime, format_uptime, get_load_average, get_users

@click.group()
def cli():
    """A simple CLI example"""
    pass

@click.command()
@click.argument('filename', type=click.Path(exists=True))
def read_file(filename):
    """Read and print the contents of a file"""
    with open(filename, 'r') as file:
        content = file.read()
    click.echo(content)

@click.command()
def uptime():
    """Get the system uptime"""
    uptime_in_seconds = get_uptime()
    uptime_message = format_uptime(uptime_in_seconds)
    load_avg = get_load_average()
    users = get_users()
    click.echo(f"Uptime: {uptime_message}, Users: {users}, Load Averages: {load_avg[0]:.2f} {load_avg[1]:.2f} {load_avg[2]:.2f}")


cli.add_command(read_file)
cli.add_command(uptime)

def main():
    cli()

if __name__ == '__main__':
    main()
