from typing import TextIO, NewType, NamedTuple
import re

XYZ = NamedTuple('XYZ', [('x', float), ('y', float), ('z', float)])
Cloud = NewType('Cloud', list[XYZ])


def read(inp: TextIO) -> Cloud:
    cloud = []
    for xyz in inp:
        if xyz and xyz[0] != '#':
            xyz = xyz.replace(',', ' ')
            x, y, z = map(float, xyz.split())
            cloud.append(XYZ(x, y, z))
    return cloud


def write(cloud: Cloud, out: TextIO):
    for point in cloud:
        out.write(f'{point.x} {point.y} {point.z}\n')
