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
test_path = os.path.join(os.getcwd(),"tests")

out_path = os.path.join(test_path,"tmp")
out_files = ["bases", "vdf", "theater"]

theater_path = os.path.join(test_path,"data/insurgency-data/mods/insurgency/2.2.7.3/scripts/theaters")
theater_files = ["default_checkpoint.theater"]

theater_test = os.path.join(theater_path,"default.theater")
theater_missing = "nothere.txt"
theater_instances = [None, theater_missing, theater_test]
#theater_pattern = "*.theater"
#theater_files = glob(os.path.join(theater_path,theater_pattern))
#pprint(theater_files)

class TheaterCase(unittest.TestCase):
	def test_theater_instance(self,filename=None):
		th = Theater(filename=filename)
		th.find_file(filename=filename)
		th.set_filename(filename=filename)
		th.load_file(filename=filename)
		return th

	def test_theater_instances(self):
		for theater_instance in theater_instances:
			self.test_theater_instance(filename=theater_instance)

	def test_theater_directives(self,filename=theater_test):
		th = self.test_theater_instance(filename)
		obj = vdf.VDFDict()
		obj['#include'] = 'test.inc'
		th.process_directives(obj=obj)
		th.load_base(filename=filename,obj=th.theater)
		th.load_base(filename=filename,obj=th.theater)

	def test_theater_files(self):
		for theater_file in theater_files:
			th = Theater(filename=os.path.join(theater_path,theater_file))
			for out_file in out_files:
				data = getattr(th, out_file)
				out_file_path = os.path.join(out_path,os.path.basename(theater_file).replace(".theater",""),"%s.txt" % out_file)
				if not os.path.exists(os.path.dirname(out_file_path)):
					os.makedirs(os.path.dirname(out_file_path))
				vdf.dump(data, open(out_file_path,'w'), pretty=True)

