import vdf
import sys
import os
#from glob import glob
from pprint import pprint
from vdf.theater import Theater
import unittest
from collections import OrderedDict

#TODO: Actually make this a real test case

base_path = os.path.join("tests", "data", "insurgency-data", "mods", "doi", "2.4.7.2")

def do_map(path = None, filename = None):
	pprint(path)
	pprint(filename)
	if filename is None:
		filename = os.path.join(base_path, "maps", "src", "comacchio_d.vmf")
	d = vdf.parse(open(filename), mapper=vdf.VDFDict)
	print(d)
	print(vdf.dumps(d, pretty=True))

def do_theater(path = None, filename=None):
	if path is None:
		path = os.path.join(base_path, "scripts", "theaters")
	if filename is None:
		filename = os.path.join("tests", "data", "test_doi_coop.theater")
	t = Theater(filename=filename, path=path)
	"""
	suffix = "_vnf"
	for team, teamdata in t.theater["theater"]["teams"].iteritems():
		for conditional, conditionaldata in teamdata.iteritems():
			for squad, squaddata in conditionaldata["squads"].iteritems():
				for classname, classcount in squaddata["classes"].iteritems():
					pprint(t.theater["theater"]["teams"][team][conditional][squad]["classes"][classname])
					del t.theater["theater"]["teams"][team][conditional][squad]["classes"][classname]
					classname = "{}{}".format(classname, suffix)
					t.theater["theater"]["teams"][team][conditional][squad]["classes"][classname] = classcount
	for classname, classdata in t.theater["theater"]["player_templates"].iteritems():
		if not classname.endswith(suffix):
			del t.theater["theater"]["player_templates"][classname]
			classname = "{}{}".format(classname, suffix)
			t.theater["theater"]["player_templates"][classname] = classdata
		t.theater["theater"]["player_templates"][classname]["import"] = classname.replace(suffix,"")
	"""
	#pprint(t.bases)
	print(t.dump())

	#pprint(vars(t))
	#pprint(t.theater)
	#pprint(t.vdf)
	#print(t.dump(data=t.vdf))
	#print(t)

do_theater(path="/home/insserver/insurgency-tools/data/mods/doi/2.4.7.2/scripts/theaters")

#filename="/home/doiserver/serverfiles/doi/scripts/theaters/vnf_doi.theater", 

"""
th = Theater(filename=os.path.join(theater_path,theater_file))
                        for out_file in out_files:
                                data = getattr(th, out_file)
                                out_file_path = os.path.join(out_path,os.path.basename(theater_file).replace(".theater",""),"%s.txt" % out_file)
                                if not os.path.exists(os.path.dirname(out_file_path)):
                                        os.makedirs(os.path.dirname(out_file_path))
                                vdf.dump(data, open(out_file_path,'w'), pretty=True)
#tf = ["default_entrenchment.theater", "default_patrol.theater", "default_stronghold.theater"]
#data = "\n".join([('"#base" "%s"' % f) for f in tf])
#print(data)
#"default.theater", 
#"default_weapon_german.theater", 
#"default_weapon_american.theater", 
#"default_weapon_upgrades.theater", 
#"default_ammo.theater", 
#"default_gear.theater", 
#"default_weapon_commonwealth.theater", 

#u = str if sys.version_info >= (3,) else unicode
test_path = os.path.join(os.getcwd(),"tests")

out_path = os.path.join(test_path,"tmp")
out_files = ["bases", "vdf", "theater"]

theater_path = os.path.join(base_path, "scripts", "theaters")
theater_files = ["default_checkpoint.theater"]

theater_instances = [None, "nothere.txt", os.path.join(theater_path, "default.theater")]

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
"""
