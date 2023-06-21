
import unittest
import fasta

"""
- Run a test to see if the FASTA formatted data properly converts to dictionary.
- data : An iterator that represents each line in a FASTA file.
- expected : the expected dictionary.
"""
def run(data, expected):
    actual = fasta.processLines(data)
    assert actual == expected, actual

class Test(unittest.TestCase):

    def testZeroSizeFile(self):
        run([], {})
    
    def testNoHeader(self):
        run(['abc', 'def'], {})
    
    def testOnlyHeaderFirstLine(self):
        run(['>Header'], {'Header' : ''})
    
    # This is probably an extension of the FASTA format - but we strip lines of whitespace before processing
    def testSpaceBeforeHeader(self):
        run([' >Header'], {'Header' : ''})
        
    def testNonSpaceBeforeHeader(self):
        run([' abc >Header'], {})
    
    def testOnlyHeaderSecondLine(self):
        run(['abc', '>Header'], {'Header' : ''})
    
    def test1Block1DataLine(self):
        run(['>Header', 'data'], {'Header' : 'data'})
    
    def test1Block2DataLines(self):
        run(['>Header', 'data1', 'data2'], {'Header' : 'data1data2'})
    
    def test1Block3DataLines(self):
        run(['>Header', 'data1', 'data2', 'data3'], {'Header' : 'data1data2data3'})
    
    def test1Block1DataLineAnd1HeaderOnly(self):
        run(['>Header1', 'data1', '>Header2'], {'Header1' : 'data1', 'Header2' : ''})
    
    def test2BlocksEach1DataLine(self):
        run(['>Header1', 'data1', '>Header2', 'data2'], {'Header1' : 'data1', 'Header2' : 'data2'})
    
    def testHeaderOnlyAnd1Block(self):
        run(['>Header1', '>Header2', 'data'], {'Header1' : '', 'Header2' : 'data'})
        
    def test2HeadersOnly(self):
        run(['>Header1', '>Header2'], {'Header1' : '', 'Header2' : ''})
        
    def test3HeadersOnly(self):
        run(['>Header1', '>Header2', '>Header3'], {'Header1' : '', 'Header2' : '', 'Header3' : ''})
    
    def test3BlocksEach1DataLine(self):
        run(['>Header1', 'data1', '>Header2', 'data2', '>Header3', 'data3'], {'Header1' : 'data1', 'Header2' : 'data2', 'Header3' : 'data3'})
    
    def test3BlocksEach2DataLines(self):
        run(['>Header1', 'data1', 'data2', '>Header2', 'data3', 'data4', '>Header3', 'data5', 'data6'],
            {'Header1' : 'data1data2', 'Header2' : 'data3data4', 'Header3' : 'data5data6'})

if __name__ == "__main__":
    unittest.main()