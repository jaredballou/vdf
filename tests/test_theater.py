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
		test_path = os.path.join(os.getcwd(),"tests")

		theater_path = os.path.join(test_path,"data/insurgency-data/mods/insurgency/2.2.7.3/scripts/theaters")
		theater_files = ["default_checkpoint.theater"]

		out_path = os.path.join(test_path,"tmp")
		out_files = ["bases", "vdf", "theater"]

		#theater_pattern = "*.theater"
		#theater_files = glob(os.path.join(theater_path,theater_pattern))
		#pprint(theater_files)
		for theater_file in theater_files:
			th = Theater(filename=os.path.join(theater_path,theater_file))
			for out_file in out_files:
				data = getattr(th, out_file)
				out_file_path = os.path.join(out_path,os.path.basename(theater_file).replace(".theater",""),"%s.txt" % out_file)
				if not os.path.exists(os.path.dirname(out_file_path)):
					os.makedirs(os.path.dirname(out_file_path))
				vdf.dump(data, open(out_file_path,'w'), pretty=True)

