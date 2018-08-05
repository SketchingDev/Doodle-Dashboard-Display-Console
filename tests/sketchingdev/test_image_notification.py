from os import path

import os

import click
import unittest
from click.testing import CliRunner
from doodledashboard.notifications import ImageNotification

from sketchingdev.console import ConsoleDisplay


class TestConsoleDisplayWithImages(unittest.TestCase):

    def test_draw_image(self):
        data_dir = path.join(TestConsoleDisplayWithImages._get_current_directory(), "data/")
        notification_image = path.join(data_dir, "image.bmp")

        image_notification = ImageNotification()
        image_notification.set_image_path(notification_image)
        cmd = create_cmd(lambda: ConsoleDisplay((100, 100)).draw(image_notification))
        result = CliRunner().invoke(cmd, catch_exceptions=False)

        f = open(path.join(data_dir, "image.txt"), 'w')
        f.write(result.output)
        f.close()

        self.maxDiff = None
        self.assertEqual("", result.output)

    @staticmethod
    def _get_current_directory():
        return os.path.dirname(os.path.realpath(__file__))



def create_cmd(func):
    @click.command()
    def c(f=func):
        f()

    return c


if __name__ == "__main__":
    unittest.main()
