import click

from Segmenter import segmenter


@click.command()
@click.argument('source', type=click.Path(exists=True), required=1)
@click.argument('target', type=click.Path(exists=False), required=1)
def segment(source, target):
    """Segmentuje text zo súboru SOURCE do novovytvoreného súboru TARGET.

    SOURCE je cesta k zdrojovému textovému súboru.

    TARGET je cesta k cielovému textovému súboru.
    """
    if not source.lower().endswith('.txt'):
        click.echo("Zdrojový súbor nie je typu .txt.",err=True)
    else:
        if not target.lower().endswith('.txt'):
            click.echo("Cielový súbor nie je typu .txt.",err=True)
        else:
            seg = segmenter.Segmenter()
            f = open(source, encoding="utf8")
            line = f.readline()
            line2 = seg.replaceSkrat(line)
            fw = open(target, "w", encoding="utf8")
            fw.write(line2)
            fw.close()
            f.close()
            click.echo("Segmentácia prebehla úspešne.")



