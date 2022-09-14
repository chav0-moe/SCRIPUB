class ToVector:
    """"This object stores bitmap layers with their original color

    Parameters
    ----------
    data : bytes
        Decoded PNG image data derived from bitmap layers

    color: string
        The HTML representation of the color value of a bitmap layer

    """
    def __init__(self, data, color):
        self.data = data
        self.color = color