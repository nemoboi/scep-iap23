#!usr/bin/env python3
# Module containing the data transformation
from datetime import date, datetime
import click

@click.command()
@click.option('--estimate', type=float, help='Estimated runtime of the program in hours')
@click.option('--deadline', type=str, help='latest date when the program should be finished in "YYYY-MM-DD"') #maybe allow for time later... date works for now
@click.option('--area', type=str, help='Local ara code as given in x.file') #default implementation
@click.option('--path', type=str, help='Path to your application')
@click.option('--cond', type=str, default=None, help='conditions for execution')

def hello(estimate, deadline, area, path, cond):
    print(f"Input: estimate {estimate}, deadline {deadline}, area {area}, path {path}, conditions {cond}")
    print("Joke's on you this doesn't do anything.")
    #deadline still needs to be converted into date.fromisoformat(deadline)

if __name__ == '__main__':
    hello()
