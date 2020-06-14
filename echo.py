#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "aradcliff"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--upper', '-u', help='convert text to uppercase')
    parser.add_argument('--lower', '-l', help='convert text to lowercase')
    parser.add_argument('--title', '-t', help='convert text to titlecase')
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    ns = parser.parse_args(args)

    if ns.upper:
        print(ns.upper.upper())


if __name__ == '__main__':
    main(sys.argv[1:])
