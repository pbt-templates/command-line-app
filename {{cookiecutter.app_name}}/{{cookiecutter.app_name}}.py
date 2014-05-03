import sys
import argparse

APP_VERSION = '0.0.1'
APP_NAME = '{{cookiecutter.app_name}}'
APP_DESCRIPTION = 'Application to ...'
HELP_EPILOG = ''

def make_parser():
    '''creates and returns an argument parser'''
    parser = argparse.ArgumentParser(prog=APP_NAME,
            description=APP_DESCRIPTION, epilog=HELP_EPILOG)

    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                               help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                               const=sum, default=max,
                               help='sum the integers (default: find the max)')
    parser.add_argument('-t', '--true', action='store_const', const=True)
    parser.add_argument('-f', '--false', action='store_const', const=False)
    parser.add_argument('--verbose', '-v', action='count')
    parser.add_argument('age', type=int)
    parser.add_argument('move', choices=['rock', 'paper', 'scissors'])

    parser.add_argument('--version', action='version',
            version='%(prog)s ' + APP_VERSION)


    return parse

def parse_args(args_to_parse=None):
    '''return the arguments passed to the app using the parser defined by
    make_parser'''
    if args_to_parse is None:
        args_to_parse = sys.argv[1:]

    parser = make_parser()
    args = parser.parse_args(args_to_parse)
    return args

def main():
    '''main app entry point'''
    args = parse_args()
    print(args)

if __name__ == '__main__':
    main()

