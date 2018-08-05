import pytest
import unittest

from tests.sketchingdev.terminal.ascii_terminal import ValidationError, AsciiTerminal


class AsciiTerminalTests(unittest.TestCase):

    def test_validation_fails_if_first_line_not_width_indicator(self):
        text_terminal = """

        |A
        +-+
        """

        with pytest.raises(ValidationError) as err_info:
            AsciiTerminal.parse(text_terminal)

        self.assertEqual("First line must be a width indicator", err_info.value.value)

    def test_validation_fails_if_last_line_not_width_indicator(self):
        text_terminal = """
        +-+
        |A
        """

        with pytest.raises(ValidationError) as err_info:
            AsciiTerminal.parse(text_terminal)

        self.assertEqual("Last line must be a width indicator", err_info.value.value)

    def test_validation_fails_if_lines_between_width_indicators_do_not_start_with_pipe(self):
        text_terminal = """
                +-+
                 A
                +-+
                """

        with pytest.raises(ValidationError) as err_info:
            AsciiTerminal.parse(text_terminal)

        self.assertEqual("All lines between width indicators must start with a pipe", err_info.value.value)

    def test_get_text_returns_single_line_text(self):
        text_terminal = """
                +----+
                |   A
                +----+
                """

        terminal = AsciiTerminal.parse(text_terminal)
        self.assertEqual("   A", terminal.get_text())

    def test_get_text_returns_multiline_text(self):
        text_terminal = """
                +----+
                |   A
                |  B 
                +----+
                """

        terminal = AsciiTerminal.parse(text_terminal)
        self.assertEqual("   A\n  B", terminal.get_text())

    def test_get_text_returns_multiline_text_without_trailing_whitespace(self):
        text_terminal = """
                +----+
                |   A
                |  B 
                |
                +----+
                """

        terminal = AsciiTerminal.parse(text_terminal)
        self.assertEqual("   A\n  B", terminal.get_text())

    def test_get_size_returns_expected_size(self):
        text_terminal = """
                +----+
                |   A
                |  B 
                +----+
                """

        terminal = AsciiTerminal.parse(text_terminal)
        self.assertEqual((4, 2), terminal.get_size())
