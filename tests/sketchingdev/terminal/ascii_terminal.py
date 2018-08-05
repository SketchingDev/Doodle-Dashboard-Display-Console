import re


class ValidationError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class AsciiTerminal:
    """
    Provides a convenient way of representing the terminal as text in the tests e.g. a terminal of 5x5 is represented
    as:

    +-----+
    |
    |
    |
    |
    |
    +-----+

    The first line is used to determine the width and left-hand pipes the height.
    """

    _WIDTH_REGEX = re.compile("\s*\+([-]+)\+")

    def __init__(self, size, text):
        self._size = size
        self._text = text

    def get_text(self):
        return self._text

    def get_size(self):
        return self._size

    @staticmethod
    def _strip_chars_outside_terminal_border(target_lines):
        left_stripped = map(lambda x: x.lstrip(), target_lines)
        non_empty = filter(lambda l: len(l) > 0, left_stripped)
        return list(non_empty)

    @staticmethod
    def _validate(lines):
        if len(lines) < 2:
            raise ValidationError("ASCII terminal must contain at width indicator at top and bottom")

        if not AsciiTerminal._WIDTH_REGEX.match(lines[0]):
            raise ValidationError("First line must be a width indicator")

        if not AsciiTerminal._WIDTH_REGEX.match(lines[-1]):
            raise ValidationError("Last line must be a width indicator")

        if len(lines) > 2:
            lines_without_pipe_at_start = filter(lambda line: line[0] != "|", lines[1:-1])

            if len(list(lines_without_pipe_at_start)) is not 0:
                raise ValidationError("All lines between width indicators must start with a pipe")

    @staticmethod
    def _remove_border(lines):
        without_width_indicators = lines[1:-1]
        without_pipes = map(lambda line: line[1:], without_width_indicators)
        without_trailing_whitespace = map(lambda line: line.rstrip(), without_pipes)
        text = "\n".join(list(without_trailing_whitespace))
        return text.rstrip()

    @staticmethod
    def _extract_size(lines):
        match = AsciiTerminal._WIDTH_REGEX.match(lines[0])
        width = len(match.group(1))
        height = len(lines) - 2
        return width, height

    @staticmethod
    def parse(text):
        lines = text.split("\n")
        cleaned = AsciiTerminal._strip_chars_outside_terminal_border(lines)
        AsciiTerminal._validate(cleaned)

        size = AsciiTerminal._extract_size(cleaned)
        text = AsciiTerminal._remove_border(cleaned)
        return AsciiTerminal(size, text)
