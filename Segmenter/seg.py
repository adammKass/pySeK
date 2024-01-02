import click

from Segmenter import segmenterClass


@click.command()
@click.argument('source', type=click.Path(exists=True), required=1)
@click.argument('goal', type=click.Path(exists=False), required=1)
def segment(source, goal):
    """Segmentuje text zo súboru SOURCE do novovytvoreného súboru GOAL.

    SOURCE je cesta k zdrojovému textovému súboru.

    GOAL je cesta k cielovému textovému súboru.
    """
    if not source.lower().endswith('.txt'):
        click.echo("Zdrojový súbor nie je typu .txt.",err=True)
    else:
        if not goal.lower().endswith('.txt'):
            click.echo("Cielový súbor nie je typu .txt.",err=True)
        else:
            seg = segmenterClass.Segmenter()
            f = open(source, encoding="utf8")
            line = f.readline()
            line2 = seg.replaceSkrat(line)
            fw = open(goal, "w", encoding="utf8")
            fw.write(line2)
            fw.close()
            f.close()
            click.echo("Segmentácia prebehla úspešne.")



