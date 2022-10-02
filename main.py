import argparse

parser = argparse.ArgumentParser(prog='myprogram')
parser.add_argument('-c', help='create a sync-node')
parser.add_argument('-m', help='create a main-node')
parser.print_help()
