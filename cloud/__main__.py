from cloud.utils import *
import cloud.xyz as xyz
import argparse
import sys


def formatter(prog): return argparse.HelpFormatter(prog, max_help_position=60)


parser = argparse.ArgumentParser('cloud', formatter_class=formatter)

parser.add_argument('-c', '--count',
                    action='store_true',
                    help='count points in the cloud')
parser.add_argument('-H', '--hist',
                    nargs='?', const=42, metavar='BINS', type=int,
                    help='plot a histogram')
parser.add_argument('-r', '--remove',
                    nargs=2, metavar=('LO', 'HI'), type=float,
                    help='remove points with Z in range [LO, HI]')
parser.add_argument('-o', '--output', nargs=1, metavar='OUTPUT',
                    help='place [modified] cloud into OUTPUT in .xyz format')
parser.add_argument('FILE',
                    help='.xyz file')

args = parser.parse_args()

with open(args.FILE) as inp:
    cloud = xyz.read(inp)

if args.remove is not None:
    cloud = erase(cloud, *args.remove)

if args.count:
    print(count(cloud))

if args.hist is not None:
    hist(cloud, args.hist)

if args.output is not None:
    with open(*args.output, 'w') as out:
        xyz.write(cloud, out)
