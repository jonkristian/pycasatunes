"""
Class object for CasaTunesSource
Documentation: https://github.com/jonkristian/pycasatunes

Generated by generator/generator.py - 2021-08-03 20:35:05.287334
"""
from .base import CasaBaseClient


class CasaTunesSource(CasaBaseClient):
    @property
    def Hidden(self):
        return self.attributes.get("Hidden", False)

    @property
    def IsShared(self):
        return self.attributes.get("IsShared", False)

    @property
    def Name(self):
        return self.attributes.get("Name", "")

    @property
    def MediaTypesSupported(self):
        return self.attributes.get("MediaTypesSupported", None)

    @property
    def Type(self):
        return self.attributes.get("Type", None)

    @property
    def SourceType(self):
        return self.attributes.get("SourceType", None)

    @property
    def SourceID(self):
        return self.attributes.get("SourceID", None)

    @property
    def ExternalDeviceType(self):
        return self.attributes.get("ExternalDeviceType", None)
