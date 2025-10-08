from protocolbuffers._ProtobufTypes import Message

from protocolbuffers.ResourceKey_pb2 import *


class SoundStart(Message):
    # __init__
    object_id: 'int'  # uint64
    channel: 'int'  # uint32
    sound_id: 'int'  # uint64
    is_vox: 'bool'
    joint_name_hash: 'int'  # uint32
    play_on_active_sim_only: 'bool'
    sound_name: 'str'


class SoundStop(Message):
    # __init__
    object_id: 'int'  # uint64
    channel: 'int'  # uint32


class SoundSkipToNext(Message):
    # __init__
    object_id: 'int'  # uint64
    channel: 'int'  # uint32


class SoundResource(Message):
    # __init__
    sound: 'ResourceKey'
    music_track_snippet: 'ResourceKey'
