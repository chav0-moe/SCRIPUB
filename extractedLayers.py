class ExtractedLayers:
    
    def __init__(self, background_raster, contours, title, grid, border, axes, numbers, beams, labels):
        self.background_raster = background_raster
        self.contours = contours
        self.title = title
        self.grid = grid
        self.border = border
        self.axes = axes
        self.numbers = numbers
        self.beams = beams
        self.labels = labels

    #TODO get and set methods to obtain layers in byte form