from typing import TypeVar, Generic, List

T = TypeVar('T')


class Message():
    def __deepcopy__(self, memo=None) -> 'Message':
        pass

    def __eq__(self, other_msg) -> 'bool':
        pass

    def __ne__(self, other_msg) -> 'bool':
        pass

    def __str__(self) -> 'str':
        pass

    def __unicode__(self) -> 'str':
        pass

    def MergeFrom(self, other_msg):
        pass

    def CopyFrom(self, other_msg):
        pass

    def Clear(self):
        pass

    def SetInParent(self):
        pass

    def IsInitialized(self) -> 'bool':
        pass

    def MergeFromString(self, serialized) -> 'int':
        pass

    def ParseFromString(self, serialized):
        pass

    def SerializeToString(self) -> 'str':
        pass

    def SerializePartialToString(self) -> 'str':
        pass

    def ListFields(self) -> 'list':
        pass

    def HasField(self, field_name) -> 'bool':
        pass

    def ClearField(self, field_name):
        pass

    def HasExtension(self, extension_handle) -> 'bool':
        pass

    def ClearExtension(self, extension_handle):
        pass

    def ByteSize(self) -> 'int':
        pass

    def _SetListener(self, message_listener):
        pass


class RepeatedCompositeFieldContainer(Generic[T]):
    def __init__(self, message_listener, type_checker) -> 'None':
        self._message_listener = message_listener
        self._values: 'list'
        self._type_checker = type_checker

    def __getitem__(self, key) -> 'T':
        pass

    def __delitem__(self, key) -> 'None':
        pass

    def __getslice__(self, start, stop) -> 'List[T]':
        pass

    def __delslice__(self, start, stop) -> 'None':
        pass

    def __eq__(self, other) -> bool:
        pass

    def __len__(self) -> 'int':
        pass

    def __ne__(self, other) -> 'bool':
        pass

    def __hash__(self):
        pass

    def __repr__(self) -> 'str':
        pass

    def sort(self, *args, **kwargs) -> 'None':
        pass

    def add(self, **kwargs) -> 'T':
        pass

    def extend(self, elem_seq) -> 'None':
        pass

    def MergeFrom(self, other) -> 'None':
        pass

    def remove(self, elem) -> 'None':
        pass
