class PhoneScreen:
    def __init__(self,
                 width,
                 height,
                 colors
                 ):
        self._width = width
        self._height = height
        self._colors = colors

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def colors(self):
        return self._colors