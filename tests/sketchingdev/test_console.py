import click
import unittest
from click.testing import CliRunner
from doodledashboard.notifications import TextNotification, ImageNotification

from sketchingdev.console import ConsoleDisplay


class TestConsoleDisplay(unittest.TestCase):

    def test_id(self):
        self.assertEqual("console", ConsoleDisplay().get_id())

    def test_write_text(self):
        input_text = "Abc"
        output_text = "Abc\n"

        text_notification = TextNotification()
        text_notification.set_text(input_text)
        cmd = create_cmd(lambda: ConsoleDisplay().draw(text_notification))
        result = CliRunner().invoke(cmd, catch_exceptions=False)

        self.assertEqual(output_text, result.output)

    def test_draw_image(self):
        image_path = "/path/to/image"
        console_output = "Image: /path/to/image\n"

        image_notification = ImageNotification()
        image_notification.set_image_path(image_path)
        cmd = create_cmd(lambda: ConsoleDisplay().draw(image_notification))
        result = CliRunner().invoke(cmd, catch_exceptions=False)

        self.assertEqual(console_output, result.output)

def create_cmd(func):
    @click.command()
    def c(f=func):
        f()

    return c


if __name__ == "__main__":
    unittest.main()
