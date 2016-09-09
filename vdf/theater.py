"""
Module for handling theater files for Insurgency
TODO:
[X] Support for "#base" directive
[ ] Support for "#include" directive
[ ] Support for "?conditional" statements
[ ] Support for "[conditional]" statements
[ ] Schema for data
"""
__version__ = "0.0.1"
__author__ = "Jared Ballou"

import logging
import os
import sys
import vdf

class Theater(object):
	"""Theater file support for Insurgency and Day of Infamy. A lot of this functionality should really be merged into the core vdf module.
		Attributes:
			path (str): Path to use for #base and #include directives
			filename (str): Filename to load. Should be fully qualified.
			bases (dict): List of included #base files. Used to avoid circular #base directives.
			theater_conditions (dict): List of theater conditions, like "?nightmap"
			vdf (VDFDict): KeyValues data from this single theater, without #bases merged in
			theater (VDFDict): Merged VDFDict that includes all #base and #include files
	"""

	def __init__(self, filename=None, path=None, data=None):
		if path is None:
			self.path = os.getcwd()
		else:
			self.path = path
		self.vdf = None
		self.processed = None
		self.theater = None
		self.bases = {}
		self.theater_conditions = {}
		self.set_filename(filename=filename, path=path)
		if not data is None:
			# TODO: Support loading string or dict as data, rather than a file.
			pass

	def set_path(self, path=None):
		"""Set the path of the object.
			TODO: Support multiple paths in a list
		"""
		if path is None:
			if self.path is not None:
				return
			path = os.getcwd()
		if os.path.exists(path):
			self.path = path
		else:
			self.path = None

	def set_filename(self, filename, path=None):
		"""Locate the filename and process it
			Args:
				filename (str): Filename to load.
				path (str): Path to use for including files. Defaults to path of filename.
		"""
		self.filename = filename
		if filename is not None:
			if self.find_file(filename=filename):
				self.filename = self.find_file(filename=filename)
				self.path = os.path.dirname(filename)
				self.load_file(filename)
			else:
				self.filename = None
				if path is None:
					self.set_path(path=os.path.dirname(filename))
				self.bases[os.path.basename(filename)] = filename
				self.vdf = self.load_file(filename, process=False)
				self.theater = self.load_file(filename, process=True)

	def dump(self,data=None):
		"""Dump VDFDict as string"""
		if data is None:
			data = self.theater
		return(vdf.dumps(data, pretty=True))

	def find_file(self,filename):
		"""Locate a file inside the hierarchy.
			TODO: Support lists of paths to search, i.e. mod files and version dirs
		"""
		if filename is None:
			return filename
		if os.path.exists(filename):
			return filename
		if self.path is not None and os.path.exists(os.path.join(self.path,filename)):
			return os.path.join(self.path,filename)
		return ""

	def load_file(self, filename=None, process=True):
		"""Load file into VDFDict
			Args:
				filename (str): Filename to load. Should be fully qualified.
				process (bool): Process things like #base and #include
			Returns:
				VDFDict of data				
		"""
		if filename is None:
			filename = self.find_file(filename=self.filename)
		obj = vdf.parse(open(filename), mapper=vdf.VDFDict)
		self.bases[os.path.basename(filename)] = filename
		if self.vdf is None:
			self.vdf = obj.copy()
		if process:
			processed = self.process_directives(obj=obj)
			if self.processed is None:
				self.processed = processed
			return processed
		else:
			return obj

	def get_data(self, type=None):
		return self.processed

	def process_directives(self, obj):
		"""Process a VDFDict object for #base and #include directives"""
		#TODO: Make this recurse through the entire tree for #include support
		for key,val in obj.iteritems():
			if key == '#base':
				self.load_base(filename=val, obj=obj)
			if key == '#include':
				print("TODO: Implement #include functionality")
		return obj

	def load_base(self, obj, filename):
		"""Load base file, and merge it into the object.
			Args:
				obj (VDFDict): Object to be merged. This will be merged onto the base file data, and then the entire structure will be put into this variable.
				filename (str): Filename to load. Should be fully qualified.
		"""
		filename = self.find_file(filename=filename)
		if os.path.basename(filename) in self.bases.keys():
			logging.debug("Not loading %s - already in bases" % filename)
			return
		base = self.load_file(filename=filename, process=True)
		self.bases[os.path.basename(filename)] = filename
		self.merge_theaters(base=base,obj=obj)

	def merge_theaters(self, base, obj, level=0):
		"""Merge theater objects
			Args:
				base (VDFDict): Base dict to be merged in. This will be corrupted by the merge process.
				obj (VDFDict): Object to be merged. This will be merged onto the base file data, and then the entire structure will be put into this variable.
				level (int): Depth of recursion
		"""
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
