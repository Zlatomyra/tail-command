import click

__version__ = "0.0.1"

@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option('-n', '--lines', default=10, help='Кількість рядків для виводу')
@click.version_option(__version__, '--version')
def main(filename, lines):
    """Вивід останніх рядків файлу."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            all_lines = f.readlines()
        for line in all_lines[-lines:]:
            click.echo(line.rstrip())
    except Exception:
        click.echo("Помилка при читанні файлу")

if __name__ == "__main__":
    main()
