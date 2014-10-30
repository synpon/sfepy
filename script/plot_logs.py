#!/usr/bin/env python
"""
Plot logs of variables saved in a text file by sfepy.base.log.Log class.

The plot should be almost the same as the plot that would be generated by the
Log directly.
"""
import sys
sys.path.append('.')
from optparse import OptionParser

import matplotlib.pyplot as plt

from sfepy.base.log import read_log, plot_log

usage = '%prog [options] filename\n' + __doc__.rstrip()

def parse_rc(option, opt, value, parser):
    pars = {}
    for pair in value.split(','):
        key, val = pair.split('=')
        pars[key] = eval(val)

    setattr(parser.values, option.dest, pars)

helps = {
    'output_filename' :
    'save the figure using the given file name',
    'rc' : 'matplotlib resources',
    'no_show' :
    'do not show the figure',
}

def main():
    parser = OptionParser(usage=usage)
    parser.add_option('-o', '--output', metavar='filename',
                      action='store', dest='output_filename',
                      default=None, help=helps['output_filename'])
    parser.add_option('--rc', type='str', metavar='key=val,...',
                      action='callback', dest='rc',
                      callback=parse_rc, default={}, help=helps['rc'])
    parser.add_option('-n', '--no-show',
                      action='store_true', dest='no_show',
                      default=False, help=helps['no_show'])
    options, args = parser.parse_args()

    if len(args) == 1:
        filename = args[0]

    else:
        parser.print_help()
        return

    log, info = read_log(filename)

    plt.rcParams.update(options.rc)

    plot_log(1, log, info)

    if options.output_filename:
        plt.savefig(options.output_filename)

    if not options.no_show:
        plt.show()

if __name__ == '__main__':
    main()
