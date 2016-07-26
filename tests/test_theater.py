import vdf
import sys
import os
#from glob import glob
from pprint import pprint
from vdf.theater import Theater
import unittest
from collections import OrderedDict

#TODO: Actually make this a real test case

#u = str if sys.version_info >= (3,) else unicode

class TheaterCase(unittest.TestCase):
	def test_load_file(self):
		theater_path = "../insurgency-tools/data/mods/insurgency/2.2.7.3/scripts/theaters"
		#theater_pattern = "*.theater"
		#theater_files = glob(os.path.join(theater_path,theater_pattern))
		#pprint(theater_files)
		th = Theater(filename=os.path.join(theater_path,"default_checkpoint.theater"))
		print(vdf.dumps(th.bases, pretty=True))
		print(vdf.dumps(th.vdf, pretty=True))
		print(vdf.dumps(th.theater, pretty=True))
