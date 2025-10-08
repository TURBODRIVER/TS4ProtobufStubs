from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer


class ListOfEntitlements(Message):
    class Entitlement():
        # __init__
        Id: 'int'  # uint64
        UseCount: 'int'  # uint32
        entitlementId: 'int'  # uint64
        entitlementVersion: 'int'  # uint32

    # __init__
    Entitlements: 'RepeatedCompositeFieldContainer[ListOfEntitlements.Entitlement]'
    Id: 'int'  # uint64
    UseCount: 'int'  # uint32
    entitlementId: 'int'  # uint64
    entitlementVersion: 'int'  # uint32
