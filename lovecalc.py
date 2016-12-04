#! .env/bin/python
"""CLI app implemented in docopt, and requests library

Usage:
    lovecalc.py fetch <fname><sname>
    lovecalc.py (-h | --help)
Arguments
    <command>
    <fname> Your name
    <sname> Your partners name
Options:
   -h --help    Show this screen
"""
from docopt import docopt
import unirest
from termcolor import colored



if __name__ == '__main__':
    ARGS = docopt(__doc__, version='1.0')


if ARGS['fetch']:
    # GET specific
    RES = unirest.get("https://love-calculator.p.mashape.com/getPercentage",
                       headers={"X-Mashape-Key": "FnAklDhuR2mshaO0fzxlVxR71NJFp1JPZM2jsnKerQV4YESGRr",
                                "Accept": "application/json"
                                },
                        params={ "fname": ARGS['<fname>'], "sname": ARGS['<sname>'] }
                       )

    print RES
    
