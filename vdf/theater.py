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

import json
import logging
import os
import sys
import vdf
import yaml

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TheaterFile(object):
	def __init__(self, filename=None, path=None, vdf=None):
		self.filename = filename
		self.path = path
		self.vdf = vdf

class Theater(object):
	"""Theater file support for Insurgency and Day of Infamy. A lot of this functionality should really be merged into the core vdf module.
		Attributes:
			path (str): Path to use for #base and #include directives
			filename (str): Filename to load. Should be fully qualified.
			files (dict): List of theater files
			theater_conditions (dict): List of theater conditions, like "?nightmap"
			vdf (VDFDict): KeyValues data from this single theater, without #bases merged in
			processed (VDFDict): Merged VDFDict that includes all #base and #include files
	"""

	def __init__(self, filename=None, path=None, paths=None, data=None):
		self.filename = filename
		self.files = vdf.VDFDict()
		self.processed = vdf.VDFDict()
		self.bases = {}
		self.paths = []
		self.theater_conditions = {}
		if paths is None:
			paths = [os.getcwd()]
		if not path is None:
			paths.append(path)
		for path in paths:
			self.add_path(path)
		self.set_filename(filename=filename)
		if not data is None:
			# TODO: Support loading string or dict as data, rather than a file.
			pass

	def add_path(self, path=None):
		"""Add new search path for files
		"""
		if path in self.paths:
			return False
		if path is None:
			return False
		if os.path.exists(path):
			self.paths.append(path)

	def set_filename(self, filename):
		"""Locate the filename and process it
			Args:
				filename (str): Filename to load.
		"""
		filename = self.find_file(filename=filename)
		if filename is None:
			logger.info("Cannot find '{}'".format(filename))
			return
		self.filename = filename
		self.load_file(filename)
		self.basename = os.path.basename(filename)
		self.processed = self.process_directives(obj=self.files[self.basename])

	def find_file(self, filename):
		"""Locate a file inside the hierarchy.
			TODO: Support lists of paths to search, i.e. mod files and version dirs
		"""
		if filename is None:
			return filename
		if os.path.exists(filename):
			return filename
		logger.info("find_file({})".format(filename))
		for path in self.paths:
			for file in [filename, os.path.basename(filename)]:
				fp = os.path.join(path,file)
				if os.path.exists(fp):
					return fp
		logger.warning("Unable to find {}".format(filename))
		logger.warning("Paths:")
		logger.warning(self.paths)
		return None

	def load_file(self, filename=None):
		"""Load file into VDFDict
			Args:
				filename (str): Filename to load. Should be fully qualified.
			Returns:
				VDFDict of data				
		"""
		if filename is None:
			filename = self.filename
		filename = self.find_file(filename=filename)
		logger.debug("load_file({})".format(filename))
		if not os.path.exists(filename):
			return False
		bn = os.path.basename(filename)
		if filename in self.files.keys():
			return self.files[filename]
		if bn in self.files.keys():
			return self.files[bn]
		self.add_path(os.path.dirname(filename))
		self.files[bn] = vdf.parse(open(filename), mapper=vdf.VDFDict)
		return self.files[bn]

	def copy(self, obj=None):
		"""Create a copy of a VDFDict object."""
		if obj is None:
			obj = self.get_data()
		return vdf.loads(vdf.dumps(obj, pretty=True), mapper=vdf.VDFDict)

	def dump(self, data=None, type=None):
		"""Dump VDFDict as specified type"""
		if data is None:
			data = self.get_data()
		if type == "yaml":
			data = yaml.safe_dump(json.loads(self.dump(data=data, type="json")), default_flow_style=False)
		elif type == "json":
			data = json.dumps(data, indent=4)
		else:
			data = vdf.dumps(data, pretty=True)
		return data

	def get_data(self, data=None, type=None):
		"""Return processed tree"""
		if data is None:
			if not self.processed is None:
				data = self.processed
			elif not self.theater is None:
				data = self.theater
			elif not self.vdf is None:
				data = self.vdf
			else:
				return None
		return data

	def process_directives(self, obj):
		"""Process a VDFDict object for #base and #include directives"""
		logger.debug("process_directives")
		#TODO: Make this recurse through the entire tree for #include support
		for key,val in obj.iteritems():
			logger.debug("key {}".format(key))
			logger.debug("val {}".format(val))
			if key == '#base':
				self.load_base(filename=val, obj=obj)
			if key == '#include':
				logger.warning("TODO: Implement #include functionality")
		return obj

	def load_base(self, obj, filename):
		"""Load base file, and merge it into the object.
			Args:
				obj (VDFDict): Object to be merged. This will be merged onto the base file data, and then the entire structure will be put into this variable.
				filename (str): Filename to load. Should be fully qualified.
		"""
		logger.debug("load_base({})".format(filename))
		filename = self.find_file(filename=filename)
		basename = os.path.basename(filename)
		if basename in self.bases.keys():
			logger.warning("Already processed {}".format(basename))
			return
		self.bases[basename] = filename
		vdf = self.load_file(filename)
		base = self.process_directives(vdf)
		self.merge_theaters(base=base, obj=obj)

	def merge_theaters(self, base, obj, level=0):
		"""Merge theater objects
			Args:
				base (VDFDict): Base dict to be merged in. This will be corrupted by the merge process.
				obj (VDFDict): Object to be merged. This will be merged onto the base file data, and then the entire structure will be put into this variable.
				level (int): Depth of recursion
		"""
		if obj is None:
			return base
		if base is None:
			return obj
		for key,val in base.iteritems():
			if key == "#base":
				continue
			if key == "#include":
				continue
			if not key in obj.keys():
				obj[key] = base[key]
			else:
				if getattr(val, "iteritems", None):
					self.merge_theaters(base=base[key], obj=obj[key], level=level+1)
				else:
					obj[key] = base[key]
		return obj
