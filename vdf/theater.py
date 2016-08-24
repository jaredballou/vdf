"""
Module for handling theater files for Insurgency
TODO:
[X] Support for "#base" directive
[ ] Support for "include" directive
[ ] Support for "?conditional" statements
[ ] Schema for data
"""
__version__ = "0.0.1"
__author__ = "Jared Ballou"

import vdf
import sys
import os

class Theater(object):
	def __init__(self,filename=None,path=None,data=None):
		if path is None:
			self.path = os.getcwd()
		else:
			self.path = path
		self.bases = vdf.VDFDict()
		self.theater_conditions = {}
		self.set_filename(filename=filename, path=path)
		#if not filename is None:
		#	self.vdf = self.load_file(filename, process=False)
		if not data is None:
			pass

	def set_filename(self, filename, path=None):
		self.filename = filename
		if filename is not None:
			if self.find_file(filename=filename):
				self.filename = self.find_file(filename=filename)
				if path is None:
					self.path = os.path.dirname(filename)
				self.bases[os.path.basename(filename)] = filename
				self.vdf = self.load_file(filename, process=False)
				self.theater = self.load_file(filename, process=True)["theater"]
			else:
				self.filename = None

	def dump(self,data=None):
		if data is None or data == self.theater:
			data = {"theater": self.theater}
		return(vdf.dumps(data, pretty=True))

	def find_file(self,filename):
		if filename is None:
			return filename
		if os.path.exists(filename):
			return filename
		if os.path.exists(os.path.join(self.path,filename)):
			return os.path.join(self.path,filename)
		return ""

	def load_file(self,filename=None, process=False):
		if filename is None:
			filename = self.find_file(filename=self.filename)
		try:
			obj = vdf.parse(open(filename), mapper=vdf.VDFDict)
		except:
			obj = {}
		if process:
			return self.process_directives(obj=obj)
		return obj

	def process_directives(self, obj):
		#TODO: Make this recurse through the entire tree for #include support
		for key,val in obj.iteritems():
			if key == '#base':
				self.load_base(filename=val, obj=obj)
			if key == '#include':
				print("TODO: Implement #include functionality")
		return obj

	def load_base(self,obj,filename):
		filename = self.find_file(filename=filename)
		if os.path.basename(filename) in self.bases.keys():
			print("Not loading %s - already in bases" % filename)
			return
		base = self.load_file(filename=filename, process=True)
		self.bases[os.path.basename(filename)] = filename
		self.merge_theaters(base=base,obj=obj)

	def merge_theaters(self,base,obj,level=0):
		for key,val in base.iteritems():
			if key == "#base":
				continue
			if not key in obj.keys():
				obj[key] = base[key]
			else:
				if getattr(val, "iteritems", None):
					self.merge_theaters(base=base[key],obj=obj[key],level=level+1)
				else:
					obj[key] = base[key]
