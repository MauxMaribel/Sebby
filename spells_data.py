import sys
import codecs
sys.stdout = codecs.getwriter('UTF-8')(sys.stdout.buffer, 'strict')



