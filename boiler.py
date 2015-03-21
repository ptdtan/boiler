#! /usr/bin/env python3
import sys
import argparse
#import genome
import time
import expand
import compress

from pympler import asizeof

if __name__ == '__main__':
    # Print file's docstring if -h is invoked
    parser = argparse.ArgumentParser(description=__doc__, 
            formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--alignments', type=str, required=True, 
        help='Full path of SAM file containing aligned reads')
    parser.add_argument("--binary", help="Write in binary format",
        action="store_true")
    parser.add_argument("--huffman", help="Use huffman coding to compress coverage vectors",
        action="store_true")
    
    args = parser.parse_args(sys.argv[1:])

    binary = False
    if args.binary:
        binary = True

    huffman = False
    if args.huffman:
        huffman = True

    compressedName = 'compressed/compressed_binary.txt'
    expandedName = 'expanded.sam'

    compressor = compress.Compressor()
    startTime = time.time()
    compressor.compress(args.alignments, compressedName, binary, huffman)
    endTime = time.time()
    #print('Compression time: %0.3f s' % (endTime-startTime))
    #print('Alignments size: %f\n' % (asizeof.asizeof(compressor.aligned)/1000000))

    expander = expand.Expander()
    startTime = time.time()
    expander.expand(compressedName, expandedName, binary, huffman)
    endTime = time.time()
    #print('Decompression time: %0.3f s' % (endTime-startTime))
    #print('Alignments size: %f\n' % (asizeof.asizeof(expander.aligned)/1000000))