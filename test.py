import argparse


def test(first, second , third):
    print(first, second, third)


parser = argparse.ArgumentParser(description='Worker for filling users collection.')
parser.add_argument('-s', '--start_id', required=True, type=int)
parser.add_argument('-e', '--end_id', required=True, type=int)
parser.add_argument('-id', '--ids', required=True, type=int)
args = parser.parse_args()

#print(args.start_id,args.end_id,args.ids)
test(args.start_id, args.end_id, args.ids)
'''
parser.add_argument('integers', metavar='start_id', type=int, nargs='+',
                    help='integer, start id for parse WOT Blitz API')
parser.add_argument('integers', metavar='end_id', type=int, nargs='+',
                    help='integer, end id for parse WOT Blitz API')
parser.add_argument('integers', metavar='ids_per_request', type=int, nargs='+',
                    help='integer, number of getting IDs per request')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
'''
#args = parser.parse_args()
#print(args.accumulate(args.integers))