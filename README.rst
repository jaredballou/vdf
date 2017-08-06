#VDF Parser

Based on https://github.com/ValvePython/vdf

Using this as a tool to process theater files for Insurgency and Day of Infamy

#Requirements

##Must Have

[X] Needs to support deep merging of complex dictionary type object
[X] Some nodes will have multiple values with the same key
[X] Support #base and #include notation to source other files
[X] Maintain ordering of all nodes.
[ ] Arbitrary nodes need to be merged/overwritten when combining bases
[ ] Support "?conditionals" at any level
[ ] Link values to other types or lists, so "allowed_items" would ensure that each item exists.

##Nice to have

[ ] Basic syntax checker to report problems in files

##Long term goals

[ ] Basic conditional processing to allow things like "for each item in theater/weapons, set class_restricted to 0" or "for each item in player_classes with name matching ".*officer.*" Add all grenades and bolt action rifle a to allowed_weapons.


#Data types
[ ] Item: has key and value, default string type, like "ammo_type": "ammo_556x45"
[ ] Section: a group of items or sections

#Notes
* Need to have good way to merge sections, so we can merge lists without duplicates and maintain the ordering of items.
* Create custom value data types on the fly or with module, like "vector" or "ammo"
* Requesting ("theater","weapons","weapon-m16a2","ammo") will look up over structure.



VDF is Valve's KeyValue text file format

https://developer.valvesoftware.com/wiki/KeyValues

The module works just like ``json`` for (de)serialization to and from VDF.

| Supported versions: ``kv1``
| Unsupported: ``kv2`` and ``kv3``



#Problems & solutions

* There are known files that contain duplicate keys. This is supported the format and
  makes mapping to ``dict`` impossible. For this case the module provides ``vdf.VDFDict``
  that can be used as mapper instead of ``dict``. See the example section for details.

* By default de-serialization will return a ``dict``, which doesn't preserve nor guarantee
  key order due to `hash randomization`_. If key order is important then
  I suggest using ``collections.OrderedDict``, or ``vdf.VDFDict``.

#Example usage

For text representation

.. code:: python

    import vdf

    # parsing vdf from file or string
    d = vdf.load(open('file.txt'))
    d = vdf.loads(vdf_text)
    d = vdf.parse(open('file.txt'))
    d = vdf.parse(vdf_text)

    # dumping dict as vdf to string
    vdf_text = vdf.dumps(d)
    indented_vdf = vdf.dumps(d, pretty=True)

    # dumping dict as vdf to file
    vdf.dump(d, open('file2.txt','w'), pretty=True)


For binary representation

.. code:: python

    d = vdf.binary_loads(vdf_bytes)
    b = vdf.binary_dumps(d)

Using an alternative mapper

.. code:: python

  d = vdf.loads(vdf_string, mapper=collections.OrderedDict)
  d = vdf.loads(vdf_string, mapper=vdf.VDFDict)

``VDFDict`` works much like the regular ``dict``, except it handles duplicates and remembers
insert order. Additionally, keys can only be of type ``str``. The most important difference
is that when trying to assigning a key that already exist it will create a duplicate instead
of reassign the value to the existing key.

.. code:: python

  >>> d = vdf.VDFDict()
  >>> d['key'] = 111
  >>> d['key'] = 222
  >>> d
  VDFDict([('key', 111), ('key', 222)])
  >>> d.items()
  [('key', 111), ('key2', 222)]
  >>> d['key']
  111
  >>> d[(0, key)]  # get the first duplicate
  111
  >>> d[(1, key)]  # get the second duplicate
  222
  >>> d.get_all_for('key')
  [111, 222]

  >>> d[(1, 'key')] = 123  # reassign specific duplicate
  >>> d.get_all_for('key')
  [111, 123]

  >>> d['key'] = 333
  >>> d.get_all_for('key')
  [111, 123, 333]
  >>> del d[(1, 'key')]
  >>> d.get_all_for('key')
  [111, 333]
  >>> d[(1, 'key')]
  333

  >>> print vdf.dumps(d)
  "key" "111"
  "key" "333"

  >>> d.has_duplicates()
  True
  >>> d.remove_all_for('key')
  >>> len(d)
  0
  >>> d.has_duplicates()
  False


.. _DuplicateOrderedDict: https://github.com/rossengeorgiev/dota2_notebooks/blob/master/DuplicateOrderedDict_for_VDF.ipynb

.. _hash randomization: https://docs.python.org/2/using/cmdline.html#envvar-PYTHONHASHSEED
