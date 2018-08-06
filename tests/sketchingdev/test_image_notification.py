from parameterized import parameterized
from os import path

import os

import click
import unittest
from click.testing import CliRunner
from doodledashboard.notifications import ImageNotification

from sketchingdev.console import ConsoleDisplay
from tests.sketchingdev.terminal.ascii_terminal import AsciiTerminal


def _get_current_directory():
    return os.path.dirname(os.path.realpath(__file__))


def resolve_data_path(filename):
    data_dir = path.join(_get_current_directory(), "data/")
    return path.join(data_dir, filename)


class TestConsoleDisplayWithImages(unittest.TestCase):

    @parameterized.expand([
        (resolve_data_path("cross-without-transparency.png"),
         """
         +----------+
         |   @@@%   
         |   @@%#   
         |   @%##   
         |@@@%##*=-:
         |@@%##*=-::
         |@%##*=-::,
         |%##*=-::,.
         |   =-::   
         |   -::,   
         |   ::,.   
         +----------+
         """)
    ])
    def test_text_centred_in_console(self, input_image, expected_ascii_terminal):
        expected_terminal = AsciiTerminal.parse(expected_ascii_terminal)

        image_notification = ImageNotification()
        image_notification.set_image_path(input_image)
        cmd = create_cmd(lambda: ConsoleDisplay(expected_terminal.get_size()).draw(image_notification))
        result = CliRunner().invoke(cmd, catch_exceptions=False)

        self.assertEqual(expected_terminal.get_text(), result.output)

    #
    # def test_draw_image(self):
    #     data_dir = path.join(TestConsoleDisplayWithImages._get_current_directory(), "data/")
    #     notification_image = path.join(data_dir, "cross-without-transparency.png")
    #
    #     image_notification = ImageNotification()
    #     image_notification.set_image_path(notification_image)
    #     cmd = create_cmd(lambda: ConsoleDisplay((20, 20)).draw(image_notification))
    #     result = CliRunner().invoke(cmd, catch_exceptions=False)
    #
    #     f = open(path.join(data_dir, "image.txt"), 'w')
    #     f.write(result.output)
    #     f.close()
    #
    #     self.maxDiff = None
    #     self.assertEqual("", result.output)




def create_cmd(func):
    @click.command()
    def c(f=func):
        f()

    return c


if __name__ == "__main__":
    unittest.main()
