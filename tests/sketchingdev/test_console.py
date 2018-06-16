import click
import unittest
from click.testing import CliRunner

from sketchingdev.console import ConsoleDisplay


class TestConsoleDisplay(unittest.TestCase):

    def test_id(self):
        self.assertEqual("console", ConsoleDisplay().get_id())

    def test_write_text(self):
        input_text = "Abc"
        output_text = "Abc\n"

        cmd = create_cmd(lambda: ConsoleDisplay().write_text(input_text))
        result = CliRunner().invoke(cmd, catch_exceptions=False)

        self.assertEqual(output_text, result.output)

    def test_draw_image(self):
        image_path = "/path/to/image"
        console_output = "One day I'll draw an ASCII version of /path/to/image\n"

        cmd = create_cmd(lambda: ConsoleDisplay().draw_image(image_path))
        result = CliRunner().invoke(cmd, catch_exceptions=False)

        self.assertEqual(console_output, result.output)


def create_cmd(func):
    @click.command()
    def c(f=func):
        f()

    return c


if __name__ == "__main__":
    unittest.main()
