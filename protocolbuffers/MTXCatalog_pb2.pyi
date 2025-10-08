from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer
from enum import IntEnum

from protocolbuffers.ResourceKey_pb2 import *


class Product(Message):
    class BundleContainment(IntEnum):
        LOOSE: 'Product.BundleContainment' = 0
        TIGHT: 'Product.BundleContainment' = 1

    LOOSE = BundleContainment.LOOSE
    TIGHT = BundleContainment.TIGHT

    class ProductType(IntEnum):
        CAS: 'Product.ProductType' = 0
        BB: 'Product.ProductType' = 1
        GAMEPLAY: 'Product.ProductType' = 2
        GENERIC_MTX: 'Product.ProductType' = 3
        INVALID_MTX: 'Product.ProductType' = 4

    CAS = ProductType.CAS
    BB = ProductType.BB
    GAMEPLAY = ProductType.GAMEPLAY
    GENERIC_MTX = ProductType.GENERIC_MTX
    INVALID_MTX = ProductType.INVALID_MTX

    # __init__
    id: 'int'  # uint64
    offerid: 'str'
    children: 'RepeatedCompositeFieldContainer[int]'  # uint64
    instances: 'RepeatedCompositeFieldContainer[ResourceKey]'
    name: 'str'
    countries: 'RepeatedCompositeFieldContainer[Country]'
    isBundle: 'bool'
    containmentType: 'Product.BundleContainment'
    childProductIds: 'RepeatedCompositeFieldContainer[int]'  # uint64
    bundlePriority: 'int'  # int32
    keyNameHash: 'int'  # uint32
    keyDescriptionHash: 'int'  # uint32
    keyUpsellDescriptionHash: 'int'  # uint32
    thumbnailResourceInstanceIdHash: 'int'  # uint64
    hiddenInCatalog: 'bool'
    isPurchasable: 'bool'
    celebrationPriority: 'int'  # uint32
    localizedImages: 'bool'
    show_variants: 'bool'
    keyImage: 'int'  # uint64
    productType: 'Product.ProductType'
    productInfoURL: 'str'
    isAvailable: 'bool'
    showInPackDetail: 'bool'
    packId: 'int'  # int32


class OfferList(Message):
    # __init__
    offer_id: 'RepeatedCompositeFieldContainer[str]'


class Catalog(Message):
    # __init__
    timestamp: 'int'  # uint64
    products: 'RepeatedCompositeFieldContainer[Product]'


class Country(Message):
    # __init__
    countryCode: 'str'
    prices: 'RepeatedCompositeFieldContainer[Price]'


class Price(Message):
    # __init__
    price: 'float'  # float32
    currency: 'str'
    currencyType: 'str'
    priceType: 'str'
    startDate: 'int'  # uint64
    endDate: 'int'  # uint64


class ViewedEntitlements(Message):
    # __init__
    viewed_entitlements: 'RepeatedCompositeFieldContainer[EntitlementNotification]'


class EntitlementNotification(Message):
    class ViewedState(IntEnum):
        VIEWED_INVALID: 'EntitlementNotification.ViewedState' = 0
        VIEWED_NEW: 'EntitlementNotification.ViewedState' = 1
        VIEWED_CELEBRATED: 'EntitlementNotification.ViewedState' = 2
        VIEWED_USED: 'EntitlementNotification.ViewedState' = 4
        VIEWED_ALL: 'EntitlementNotification.ViewedState' = 255

    VIEWED_INVALID = ViewedState.VIEWED_INVALID
    VIEWED_NEW = ViewedState.VIEWED_NEW
    VIEWED_CELEBRATED = ViewedState.VIEWED_CELEBRATED
    VIEWED_USED = ViewedState.VIEWED_USED
    VIEWED_ALL = ViewedState.VIEWED_ALL

    class TrialViewedStateMask(IntEnum):
        TRIAL_VIEWED_MASK_EXPIRED_TRIAL_OR_CONVERTED: 'EntitlementNotification.TrialViewedStateMask' = 1
        TRIAL_VIEWED_MASK_TRIALS_NOT_SUPPORTED: 'EntitlementNotification.TrialViewedStateMask' = 2

    TRIAL_VIEWED_MASK_EXPIRED_TRIAL_OR_CONVERTED = TrialViewedStateMask.TRIAL_VIEWED_MASK_EXPIRED_TRIAL_OR_CONVERTED
    TRIAL_VIEWED_MASK_TRIALS_NOT_SUPPORTED = TrialViewedStateMask.TRIAL_VIEWED_MASK_TRIALS_NOT_SUPPORTED

    class TrialViewedState(IntEnum):
        TRIAL_VIEWED_EXPIRED_TRIAL_OR_CONVERTED: 'EntitlementNotification.TrialViewedState' = 1
        TRIAL_VIEWED_TRIALS_NOT_SUPPORTED: 'EntitlementNotification.TrialViewedState' = 2

    TRIAL_VIEWED_EXPIRED_TRIAL_OR_CONVERTED = TrialViewedState.TRIAL_VIEWED_EXPIRED_TRIAL_OR_CONVERTED
    TRIAL_VIEWED_TRIALS_NOT_SUPPORTED = TrialViewedState.TRIAL_VIEWED_TRIALS_NOT_SUPPORTED

    # __init__
    viewed_state: 'int'  # uint32
    product_id: 'int'  # uint64
    trial_viewed_state: 'int'  # uint32
    entitlement_id_at_trial_expiration_or_conversion: 'int'  # uint64
