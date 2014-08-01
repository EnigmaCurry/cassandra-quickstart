#!python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'cassandra-quickstart==0.1','console_scripts','cqs'
__requires__ = 'cassandra-quickstart==0.1'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('cassandra-quickstart==0.1', 'console_scripts', 'cqs')()
    )
