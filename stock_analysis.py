# -*- coding: UTF-8 -*-     

import os
import sys
import argparse

from hkextools import utiltools
from hkextools import highlight
from hkextools import fAnalysis

def main(argv=None):
    getData = 0
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--data', help='Collect financial data for ratio calculations and analysis', action='store_true', required=False)
    args = parser.parse_args()
    
    folderPath = os.path.dirname(os.path.abspath(__file__))
    print(folderPath)
    allSettings = utiltools.readSettings(os.path.join('Settings', 'settings.txt'))
    print(allSettings)
    fAnalysis.outputPath = highlight.outputPath = allSettings['Output Path']
    print(fAnalysis.outputPath)

    if (args.data): 
        
        getData = 1

    
    
    
    
if __name__ == "__main__":
    sys.exit(main())