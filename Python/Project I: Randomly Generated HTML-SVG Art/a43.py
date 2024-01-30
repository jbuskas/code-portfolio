#!/usr/bin/env python
"""Assignment 4 Part 3 - Jenni Buskas"""
print(__doc__)

from typing import IO
from random import seed
from random import random
from random import randint
from random import uniform

class GenRandom:
    """Random number generation class"""
    def __init__(self, type: int, rangeStart: int, rangeEnd: int):
        """
        Generates a random number in range [rangeStart, rangeEnd]. If the number is a float, generates it between 0 and 1.
        Type: 0 for int, 1 for float

        >>> x: GenRandom = GenRandom(0, 1, 10)
        """
        seed(random())
        if(type==0):
            self.num: int = randint(rangeStart, rangeEnd)
        else:
            self.num: float = round(random(), 2)

class ArtConfig:
    """ArtConfig class"""
    def __init__(self, count: int, canvas: tuple):
        """
        Initializes an ArtConfig object.

        >>> a: ArtConfig = ArtConfig(1, (1000, 1000))
        >>> print(a.cnt)
        1
        """
        self.cnt: int = count
        self.sha: int = GenRandom(0, 0, 3).num
        while self.sha==2:
            # if shape == 2, choose again until you get either 0, 1, or 3
            self.sha: int = GenRandom(0, 0, 3).num
        self.x: int = GenRandom(0, 0, canvas[0]).num
        self.y: int = GenRandom(0, 0, canvas[1]).num
        self.rad: int = GenRandom(0, 0, 100).num
        self.rx: int = GenRandom(0, 10, 30).num
        self.ry: int = GenRandom(0, 10, 30).num
        self.w: int = GenRandom(0, 10, 100).num
        self.h: int = GenRandom(0, 10, 100).num
        self.r: int = GenRandom(0, 0, 255).num
        self.g: int = GenRandom(0, 0, 255).num
        self.b: int = GenRandom(0, 0, 255).num
        self.op: float = GenRandom(1, 0, 0).num

class Circle:
    """Circle class"""
    def __init__(self, cir: tuple, col: tuple) -> None:
        """
        Initializes a circle from a tuple of form (x, y, radius) and colour tuple of form (red, green, blue, opacity).

        >>> xc = Circle((50,50,50), (255,0,0,1.0))
        >>> print(xc.cx)
        50
        """
        self.cx: int = cir[0]
        self.cy: int = cir[1]
        self.rad: int = cir[2]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]

class Rectangle:
    """Rectangle class"""
    def __init__(self, rect: tuple, colour: tuple) -> None:
        """
        Initializes a rectangle from a rectangle tuple of form (x, y, height, width) and colour tuple.

        >>> x = Rectangle((0,350,50,75), (178,9,250,1.0))
        >>> print(x.red)
        178
        """
        self.x: int = rect[0]
        self.y: int = rect[1]
        self.height: int = rect[2]
        self.width: int = rect[3]
        self.red: int = colour[0]
        self.green: int = colour[1]
        self.blue: int = colour[2]
        self.op: float = colour[3]

class Ellipse:
    """Ellipse class"""
    def __init__(self, ell: tuple, colour: tuple) -> None:
        """
        Initializes an ellipse from a tuple of form (x, y, rx, ry, height, width) and colour tuple.

        >>> e = Ellipse((0, 0, 10, 10, 50, 30), (100,200,200,1.0))
        >>> print(e.rx)
        10
        """
        self.x: int = ell[0]
        self.y: int = ell[1]
        self.rx: int = ell[2]
        self.ry: int = ell[3]
        self.height: int = ell[4]
        self.width: int = ell[5]
        self.red: int = colour[0]
        self.green: int = colour[1]
        self.blue: int = colour[2]
        self.op: float = colour[3]

class ProEpilogue:
    """Prints the beginning and end tags for an HTML file"""
    def __init__(self, title: str) -> None:
        """
        Provides the beginning and end tags for an HTML file, as well as the title from an inputted title.

        >>> p = ProEpilogue("Part1")
        >>> print(p.title)
        <head>
           <title>Part1</title>
        </head>
        <body>
        """
        self.prologue: str = "<html>"
        self.title: str = f'<head>\n   <title>{title}</title>\n</head>\n<body>'
        self.epilogue: str = "</body>\n</html>"

def writeHTMLcomment(f: IO[str], t: int, com: str) -> None:
    """writeHTMLcomment method"""
    ts: str = "   " * t
    f.write(f"{ts}<!--{com}-->\n")
        
def drawCircleLine(f: IO[str], t: int, c: Circle) -> None:
    """drawCircle method"""
    ts: str = "   " * t
    line1: str = f'<circle cx="{c.cx}" cy="{c.cy}" r="{c.rad}" '
    line2: str = f'fill="rgb({c.red}, {c.green}, {c.blue})" fill-opacity="{c.op}"></circle>'
    f.write(f"{ts}{line1+line2}\n")

def drawRectangle(f: IO[str], t: int, r: Rectangle) -> None:
    """drawRectangle method"""
    ts: str = "   " * t
    line1: str = f'<rect x="{r.x}" y="{r.y}" height="{r.height}" width="{r.width}" '
    line2: str = f'fill="rgb({r.red}, {r.green}, {r.blue})" fill-opacity="{r.op}"></rect>'
    f.write(f"{ts}{line1+line2}\n")

def drawEllipse(f: IO[str], t: int, e: Ellipse) -> None:
    """drawEllipse method"""
    ts: str = "   " * t
    line1: str = f'<rect x="{e.x}" y="{e.y}" rx="{e.rx}" ry="{e.ry}" height="{e.height}" width="{e.width}" '
    line2: str = f'fill="rgb({e.red}, {e.green}, {e.blue})" fill-opacity="{e.op}"></rect>'
    f.write(f"{ts}{line1+line2}\n")

def genArt(f: IO[str], t: int, canvasSize: tuple) -> None:
   """genART method"""
   num_shapes: int = GenRandom(0, 0, 10000).num
   for i in range(num_shapes):
        a = ArtConfig(i, canvasSize)
        if(a.sha==0):
            shape: Circle = Circle((a.x, a.y, a.rad), (a.r, a.g, a.b, a.op))
            drawCircleLine(f, t, shape)
        elif (a.sha==1):
            shape: Rectangle = Rectangle((a.x, a.y, a.h, a.w), (a.r, a.g, a.b, a.op))
            drawRectangle(f, t, shape)
        else:
            shape: Ellipse = Ellipse((a.x, a.y, a.rx, a.ry, a.h, a.w), (a.r, a.g, a.b, a.op))
            drawEllipse(f, t, shape)
        
def openSVGcanvas(f: IO[str], t: int, canvas: tuple) -> None:
     """openSVGcanvas method"""
     ts: str = "   " * t
     writeHTMLcomment(f, t, "Define SVG drawing box")
     f.write(f'{ts}<svg width="{canvas[0]}" height="{canvas[1]}">\n')

def closeSVGcanvas(f: IO[str], t: int, epil: ProEpilogue) -> None:
    """closeSVGcanvas method"""
    ts: str = "   " * t
    f.write(f"{ts}</svg>\n")
    f.write(epil.epilogue)

def writeHTMLline(f: IO[str], t: int, line: str) -> None:
     """writeLineHTML method"""
     ts = "   " * t
     f.write(f"{ts}{line}\n")

def writeHTMLHeader(f: IO[str], winTitle: str, prol: ProEpilogue) -> None:
    """writeHeadHTML method"""
    writeHTMLline(f, 0, prol.prologue)
    writeHTMLline(f, 0, prol.title)

def writeHTMLfile() -> None:
    """writeHTMLfile method"""
    fnam: str = "a43.html"
    winTitle: str = "My Art"
    f: IO[str] = open(fnam, "w")
    tags: ProEpilogue = ProEpilogue(winTitle)
    canvasSize: tuple(int) = (800, 400)
    writeHTMLHeader(f, winTitle, tags)
    openSVGcanvas(f, 1, canvasSize)
    genArt(f, 2, canvasSize)
    closeSVGcanvas(f, 1, tags)
    f.close()

def main() -> None:
    """main method"""
    writeHTMLfile()

if __name__ == "__main__":
    main()