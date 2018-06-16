import click
from doodledashboarddisplay import Display
from doodledashboarddisplay.display import CanWriteText, CanDrawImage


class ConsoleDisplay(Display, CanWriteText, CanDrawImage):

    def __init__(self, size=click.get_terminal_size()):
        self._size = size

    def clear(self):
        click.clear()

    def write_text(self, text):
        click.echo(text)

    def draw_image(self, image_path):
        click.echo("One day I'll draw an ASCII version of %s" % image_path)

    @staticmethod
    def get_id():
        return "console"

    def __str__(self):
        return "Console display"
