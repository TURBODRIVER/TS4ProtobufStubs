from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer
from enum import IntEnum

from protocolbuffers.SimObjectAttributes_pb2 import *


class CareerOutfit(Message):
    # __init__
    outfit_index: 'int'  # uint32
    mannequin: 'MannequinSimData'


class VetClinicConfiguration(Message):
    class VetClinicOutfitType(IntEnum):
        MALE_EMPLOYEE: 'VetClinicConfiguration.VetClinicOutfitType' = 0
        FEMALE_EMPLOYEE: 'VetClinicConfiguration.VetClinicOutfitType' = 1

    MALE_EMPLOYEE = VetClinicOutfitType.MALE_EMPLOYEE
    FEMALE_EMPLOYEE = VetClinicOutfitType.FEMALE_EMPLOYEE

    # __init__
    outfits: 'RepeatedCompositeFieldContainer[CareerOutfit]'


class UniversityHousingConfiguration(Message):
    # __init__
    university_id: 'int'  # uint64
    gender: 'int'  # uint32
    organization_id: 'int'  # uint64
    roommate_bed_count: 'int'  # uint32
    club_id: 'int'  # uint64


class VenueUpdateRequest(Message):
    # __init__
    venue_key: 'int'  # fixed uint64
    lot_id: 'int'  # uint32
    world_id: 'int'  # uint32


class VenueOwnerUpdateCompleted(Message):
    # __init__
    lot_id: 'int'  # uint32
    previous_owner_id: 'int'  # uint64


class VenueUpdateOwnerRequest(Message):
    # __init__
    zone_id: 'int'  # uint64
    new_owner_id: 'int'  # uint64
