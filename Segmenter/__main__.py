import click

from Segmenter import *

@click.group()
def cli():
    pass

cli.add_command(seg.segment)


if __name__ == "__main__":
    cli()

#D:\text_ref_final.txt
#D:\goal.txt