#! /usr/bin/env python

class PairedRead:
    def __init__(self, chromA, exonsA, chromB, exonsB, xs=None, NH=1):
        ''' exon is a list of (start,end) tuples marking each exonic region of this read.
            xs indicates the strand on which this gene lies, as described in the SAM file format.
        '''
        self.chromA = chromA
        self.chromB = chromB
        self.exonsA = exonsA
        self.exonsB = exonsB
        self.xs = xs

        self.NH = NH
        #if self.NH > 1:
        #    print 'NH: ' + str(self.NH)
        #else:
        #    print '>>NH: ' + str(self.NH)