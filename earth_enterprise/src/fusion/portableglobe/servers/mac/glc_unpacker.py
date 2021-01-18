#!/usr/bin/env python3
#
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.5
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_glc_unpacker', [dirname(__file__)])
        except ImportError:
            import _glc_unpacker
            return _glc_unpacker
        if fp is not None:
            try:
                _mod = imp.load_module('_glc_unpacker', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _glc_unpacker = swig_import_helper()
    del swig_import_helper
else:
    import _glc_unpacker
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class GlcUnpacker(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, GlcUnpacker, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, GlcUnpacker, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _glc_unpacker.new_GlcUnpacker(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _glc_unpacker.delete_GlcUnpacker
    __del__ = lambda self : None;
    def FindDataPacket(self, *args): return _glc_unpacker.GlcUnpacker_FindDataPacket(self, *args)
    def FindMapDataPacket(self, *args): return _glc_unpacker.GlcUnpacker_FindMapDataPacket(self, *args)
    def FindQtpPacket(self, *args): return _glc_unpacker.GlcUnpacker_FindQtpPacket(self, *args)
    def MaxResolutionLod(self, *args): return _glc_unpacker.GlcUnpacker_MaxResolutionLod(self, *args)
    def HasData(self, *args): return _glc_unpacker.GlcUnpacker_HasData(self, *args)
    def FindLayerFile(self, *args): return _glc_unpacker.GlcUnpacker_FindLayerFile(self, *args)
    def FindFile(self, *args): return _glc_unpacker.GlcUnpacker_FindFile(self, *args)
    def FindMetaDbRoot(self, *args): return _glc_unpacker.GlcUnpacker_FindMetaDbRoot(self, *args)
    def IsGee(self): return _glc_unpacker.GlcUnpacker_IsGee(self)
    def Is2d(self): return _glc_unpacker.GlcUnpacker_Is2d(self)
    def Is3d(self): return _glc_unpacker.GlcUnpacker_Is3d(self)
    def Id(self): return _glc_unpacker.GlcUnpacker_Id(self)
    def Info(self): return _glc_unpacker.GlcUnpacker_Info(self)
    def IndexFile(self, *args): return _glc_unpacker.GlcUnpacker_IndexFile(self, *args)
    def IndexSize(self): return _glc_unpacker.GlcUnpacker_IndexSize(self)
    def NumberOfLayers(self): return _glc_unpacker.GlcUnpacker_NumberOfLayers(self)
    def LayerIndex(self, *args): return _glc_unpacker.GlcUnpacker_LayerIndex(self, *args)
    def Index(self): return _glc_unpacker.GlcUnpacker_Index(self)
GlcUnpacker_swigregister = _glc_unpacker.GlcUnpacker_swigregister
GlcUnpacker_swigregister(GlcUnpacker)

class GlcReader(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, GlcReader, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, GlcReader, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    def Read(self, *args): return _glc_unpacker.GlcReader_Read(self, *args)
    def ReadData(self, *args): return _glc_unpacker.GlcReader_ReadData(self, *args)
    def Size(self): return _glc_unpacker.GlcReader_Size(self)
    def Suffix(self): return _glc_unpacker.GlcReader_Suffix(self)
    __swig_destroy__ = _glc_unpacker.delete_GlcReader
    __del__ = lambda self : None;
GlcReader_swigregister = _glc_unpacker.GlcReader_swigregister
GlcReader_swigregister(GlcReader)

class PortableGlcReader(GlcReader):
    __swig_setmethods__ = {}
    for _s in [GlcReader]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, PortableGlcReader, name, value)
    __swig_getmethods__ = {}
    for _s in [GlcReader]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, PortableGlcReader, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _glc_unpacker.new_PortableGlcReader(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _glc_unpacker.delete_PortableGlcReader
    __del__ = lambda self : None;
    def Read(self, *args): return _glc_unpacker.PortableGlcReader_Read(self, *args)
    def ReadData(self, *args): return _glc_unpacker.PortableGlcReader_ReadData(self, *args)
    def Size(self): return _glc_unpacker.PortableGlcReader_Size(self)
    def Suffix(self): return _glc_unpacker.PortableGlcReader_Suffix(self)
PortableGlcReader_swigregister = _glc_unpacker.PortableGlcReader_swigregister
PortableGlcReader_swigregister(PortableGlcReader)

class FileUnpacker(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FileUnpacker, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FileUnpacker, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _glc_unpacker.new_FileUnpacker(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _glc_unpacker.delete_FileUnpacker
    __del__ = lambda self : None;
    def FindDataPacket(self, *args): return _glc_unpacker.FileUnpacker_FindDataPacket(self, *args)
    def FindMapDataPacket(self, *args): return _glc_unpacker.FileUnpacker_FindMapDataPacket(self, *args)
    def FindQtpPacket(self, *args): return _glc_unpacker.FileUnpacker_FindQtpPacket(self, *args)
    def HasData(self, *args): return _glc_unpacker.FileUnpacker_HasData(self, *args)
    def FindFile(self, *args): return _glc_unpacker.FileUnpacker_FindFile(self, *args)
    def IndexFile(self, *args): return _glc_unpacker.FileUnpacker_IndexFile(self, *args)
    def IndexSize(self): return _glc_unpacker.FileUnpacker_IndexSize(self)
    def Index(self): return _glc_unpacker.FileUnpacker_Index(self)
FileUnpacker_swigregister = _glc_unpacker.FileUnpacker_swigregister
FileUnpacker_swigregister(FileUnpacker)

class PackageFileLoc(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PackageFileLoc, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PackageFileLoc, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _glc_unpacker.new_PackageFileLoc(*args)
        try: self.this.append(this)
        except: self.this = this
    def AddBaseToOffset(self, *args): return _glc_unpacker.PackageFileLoc_AddBaseToOffset(self, *args)
    def Set(self, *args): return _glc_unpacker.PackageFileLoc_Set(self, *args)
    def Offset(self): return _glc_unpacker.PackageFileLoc_Offset(self)
    def Size(self): return _glc_unpacker.PackageFileLoc_Size(self)
    def LowOffset(self): return _glc_unpacker.PackageFileLoc_LowOffset(self)
    def HighOffset(self): return _glc_unpacker.PackageFileLoc_HighOffset(self)
    def LowSize(self): return _glc_unpacker.PackageFileLoc_LowSize(self)
    def HighSize(self): return _glc_unpacker.PackageFileLoc_HighSize(self)
    __swig_destroy__ = _glc_unpacker.delete_PackageFileLoc
    __del__ = lambda self : None;
PackageFileLoc_swigregister = _glc_unpacker.PackageFileLoc_swigregister
PackageFileLoc_swigregister(PackageFileLoc)

class PackageIndexEntry(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PackageIndexEntry, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PackageIndexEntry, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _glc_unpacker.new_PackageIndexEntry(*args)
        try: self.this.append(this)
        except: self.this = this
    def Path(self): return _glc_unpacker.PackageIndexEntry_Path(self)
    def FileLoc(self): return _glc_unpacker.PackageIndexEntry_FileLoc(self)
    __swig_destroy__ = _glc_unpacker.delete_PackageIndexEntry
    __del__ = lambda self : None;
PackageIndexEntry_swigregister = _glc_unpacker.PackageIndexEntry_swigregister
PackageIndexEntry_swigregister(PackageIndexEntry)

class Package(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Package, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Package, name)
    __repr__ = _swig_repr
    __swig_getmethods__["CalculateCrc"] = lambda x: _glc_unpacker.Package_CalculateCrc
    if _newclass:CalculateCrc = staticmethod(_glc_unpacker.Package_CalculateCrc)
    __swig_getmethods__["ReadCrc"] = lambda x: _glc_unpacker.Package_ReadCrc
    if _newclass:ReadCrc = staticmethod(_glc_unpacker.Package_ReadCrc)
    __swig_getmethods__["ReadVersion"] = lambda x: _glc_unpacker.Package_ReadVersion
    if _newclass:ReadVersion = staticmethod(_glc_unpacker.Package_ReadVersion)
    __swig_getmethods__["FileSize"] = lambda x: _glc_unpacker.Package_FileSize
    if _newclass:FileSize = staticmethod(_glc_unpacker.Package_FileSize)
    def __init__(self): 
        this = _glc_unpacker.new_Package()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _glc_unpacker.delete_Package
    __del__ = lambda self : None;
Package_swigregister = _glc_unpacker.Package_swigregister
Package_swigregister(Package)
cvar = _glc_unpacker.cvar
Package.kCrcSize = _glc_unpacker.cvar.Package_kCrcSize
Package.kCrcOffset = _glc_unpacker.cvar.Package_kCrcOffset
Package.kVersionSize = _glc_unpacker.cvar.Package_kVersionSize
Package.kVersionOffset = _glc_unpacker.cvar.Package_kVersionOffset
Package.kIndexOffsetSize = _glc_unpacker.cvar.Package_kIndexOffsetSize
Package.kIndexOffsetOffset = _glc_unpacker.cvar.Package_kIndexOffsetOffset

def Package_CalculateCrc(*args):
  return _glc_unpacker.Package_CalculateCrc(*args)
Package_CalculateCrc = _glc_unpacker.Package_CalculateCrc

def Package_ReadCrc(*args):
  return _glc_unpacker.Package_ReadCrc(*args)
Package_ReadCrc = _glc_unpacker.Package_ReadCrc

def Package_ReadVersion(*args):
  return _glc_unpacker.Package_ReadVersion(*args)
Package_ReadVersion = _glc_unpacker.Package_ReadVersion

def Package_FileSize(*args):
  return _glc_unpacker.Package_FileSize(*args)
Package_FileSize = _glc_unpacker.Package_FileSize

kDbRootPacket = _glc_unpacker.kDbRootPacket
kDbRoot2Packet = _glc_unpacker.kDbRoot2Packet
kQtpPacket = _glc_unpacker.kQtpPacket
kQtp2Packet = _glc_unpacker.kQtp2Packet
kImagePacket = _glc_unpacker.kImagePacket
kTerrainPacket = _glc_unpacker.kTerrainPacket
kVectorPacket = _glc_unpacker.kVectorPacket
class IndexItem(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IndexItem, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IndexItem, name)
    __repr__ = _swig_repr
    __swig_setmethods__["btree_high"] = _glc_unpacker.IndexItem_btree_high_set
    __swig_getmethods__["btree_high"] = _glc_unpacker.IndexItem_btree_high_get
    if _newclass:btree_high = _swig_property(_glc_unpacker.IndexItem_btree_high_get, _glc_unpacker.IndexItem_btree_high_set)
    __swig_setmethods__["btree_low"] = _glc_unpacker.IndexItem_btree_low_set
    __swig_getmethods__["btree_low"] = _glc_unpacker.IndexItem_btree_low_get
    if _newclass:btree_low = _swig_property(_glc_unpacker.IndexItem_btree_low_get, _glc_unpacker.IndexItem_btree_low_set)
    __swig_setmethods__["level"] = _glc_unpacker.IndexItem_level_set
    __swig_getmethods__["level"] = _glc_unpacker.IndexItem_level_get
    if _newclass:level = _swig_property(_glc_unpacker.IndexItem_level_get, _glc_unpacker.IndexItem_level_set)
    __swig_setmethods__["packet_type"] = _glc_unpacker.IndexItem_packet_type_set
    __swig_getmethods__["packet_type"] = _glc_unpacker.IndexItem_packet_type_get
    if _newclass:packet_type = _swig_property(_glc_unpacker.IndexItem_packet_type_get, _glc_unpacker.IndexItem_packet_type_set)
    __swig_setmethods__["channel"] = _glc_unpacker.IndexItem_channel_set
    __swig_getmethods__["channel"] = _glc_unpacker.IndexItem_channel_get
    if _newclass:channel = _swig_property(_glc_unpacker.IndexItem_channel_get, _glc_unpacker.IndexItem_channel_set)
    __swig_setmethods__["file_id"] = _glc_unpacker.IndexItem_file_id_set
    __swig_getmethods__["file_id"] = _glc_unpacker.IndexItem_file_id_get
    if _newclass:file_id = _swig_property(_glc_unpacker.IndexItem_file_id_get, _glc_unpacker.IndexItem_file_id_set)
    __swig_setmethods__["packet_size"] = _glc_unpacker.IndexItem_packet_size_set
    __swig_getmethods__["packet_size"] = _glc_unpacker.IndexItem_packet_size_get
    if _newclass:packet_size = _swig_property(_glc_unpacker.IndexItem_packet_size_get, _glc_unpacker.IndexItem_packet_size_set)
    __swig_setmethods__["offset"] = _glc_unpacker.IndexItem_offset_set
    __swig_getmethods__["offset"] = _glc_unpacker.IndexItem_offset_get
    if _newclass:offset = _swig_property(_glc_unpacker.IndexItem_offset_get, _glc_unpacker.IndexItem_offset_set)
    def __eq__(self, *args): return _glc_unpacker.IndexItem___eq__(self, *args)
    def __lt__(self, *args): return _glc_unpacker.IndexItem___lt__(self, *args)
    def SetLookupInfo(self, *args): return _glc_unpacker.IndexItem_SetLookupInfo(self, *args)
    def Fill(self, *args): return _glc_unpacker.IndexItem_Fill(self, *args)
    def __init__(self): 
        this = _glc_unpacker.new_IndexItem()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _glc_unpacker.delete_IndexItem
    __del__ = lambda self : None;
IndexItem_swigregister = _glc_unpacker.IndexItem_swigregister
IndexItem_swigregister(IndexItem)
IndexItem.kIgnoreChannelAndType = _glc_unpacker.cvar.IndexItem_kIgnoreChannelAndType

class PacketBundle(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PacketBundle, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PacketBundle, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _glc_unpacker.delete_PacketBundle
    __del__ = lambda self : None;
PacketBundle_swigregister = _glc_unpacker.PacketBundle_swigregister
PacketBundle_swigregister(PacketBundle)

# This file is compatible with both classic and new-style classes.
