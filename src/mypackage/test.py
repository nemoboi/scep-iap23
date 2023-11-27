	#!/usr/bin/env python3
# Module containing the data transformation
from datetime import date, datetime
import click

@click.command()
@click.option('--estimate', t help='Estimated runtime of the program in hours')
@click.option('--area', help='Local area code as given in x.file') #default implementation
@click.option('--deadline', help='latest time when the program should be finished in "YYYY-MM-DD hh:mm:ss"')

def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    hello()
