from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer
from enum import IntEnum

from protocolbuffers.Localization_pb2 import *
from protocolbuffers.SituationPersistence_pb2 import *
from protocolbuffers.SimsCustomOptions_pb2 import *
from protocolbuffers.Outfits_pb2 import *
from protocolbuffers.Animation_pb2 import *
from protocolbuffers.Audio_pb2 import *
from protocolbuffers.ResourceKey_pb2 import *


class RelationshipIndex(IntEnum):
    RELATIONSHIP_MOTHER: 'RelationshipIndex' = 0
    RELATIONSHIP_FATHER: 'RelationshipIndex' = 1
    RELATIONSHIP_MOTHERS_MOM: 'RelationshipIndex' = 2
    RELATIONSHIP_MOTHERS_FATHER: 'RelationshipIndex' = 3
    RELATIONSHIP_FATHERS_MOM: 'RelationshipIndex' = 4
    RELATIONSHIP_FATHERS_FATHER: 'RelationshipIndex' = 5
    RELATIONSHIP_NONE: 'RelationshipIndex' = 6
    RELATIONSHIP_PARENT: 'RelationshipIndex' = 7
    RELATIONSHIP_SIBLING: 'RelationshipIndex' = 8
    RELATIONSHIP_SPOUSE: 'RelationshipIndex' = 9
    RELATIONSHIP_FIANCE: 'RelationshipIndex' = 10
    RELATIONSHIP_STEADY: 'RelationshipIndex' = 11
    RELATIONSHIP_DESCENDANT: 'RelationshipIndex' = 12
    RELATIONSHIP_GRANDPARENT: 'RelationshipIndex' = 13
    RELATIONSHIP_GRANDCHILD: 'RelationshipIndex' = 14
    RELATIONSHIP_SIBLINGS_CHILDREN: 'RelationshipIndex' = 15
    RELATIONSHIP_PARENTS_SIBLING: 'RelationshipIndex' = 16
    RELATIONSHIP_COUSIN: 'RelationshipIndex' = 17
    RELATIONSHIP_DISTANT_RELATIVE: 'RelationshipIndex' = 18
    RELATIONSHIP_GREAT_GRANDPARENT: 'RelationshipIndex' = 19
    RELATIONSHIP_GREAT_GRANDCHILD: 'RelationshipIndex' = 20
    RELATIONSHIP_GRANDPARENT_SIBLING: 'RelationshipIndex' = 21
    RELATIONSHIP_FIRST_COUSIN_ONCE_REMOVED: 'RelationshipIndex' = 22
    RELATIONSHIP_SIBLINGS_GRANDCHILD: 'RelationshipIndex' = 23
    RELATIONSHIP_SIBLINGS_GREAT_GRANDCHILD: 'RelationshipIndex' = 24
    RELATIONSHIP_GREAT_GRANDPARENT_SIBLING: 'RelationshipIndex' = 25
    RELATIONSHIP_HALF_SIBLING: 'RelationshipIndex' = 26


RELATIONSHIP_MOTHER = RelationshipIndex.RELATIONSHIP_MOTHER
RELATIONSHIP_FATHER = RelationshipIndex.RELATIONSHIP_FATHER
RELATIONSHIP_MOTHERS_MOM = RelationshipIndex.RELATIONSHIP_MOTHERS_MOM
RELATIONSHIP_MOTHERS_FATHER = RelationshipIndex.RELATIONSHIP_MOTHERS_FATHER
RELATIONSHIP_FATHERS_MOM = RelationshipIndex.RELATIONSHIP_FATHERS_MOM
RELATIONSHIP_FATHERS_FATHER = RelationshipIndex.RELATIONSHIP_FATHERS_FATHER
RELATIONSHIP_NONE = RelationshipIndex.RELATIONSHIP_NONE
RELATIONSHIP_PARENT = RelationshipIndex.RELATIONSHIP_PARENT
RELATIONSHIP_SIBLING = RelationshipIndex.RELATIONSHIP_SIBLING
RELATIONSHIP_SPOUSE = RelationshipIndex.RELATIONSHIP_SPOUSE
RELATIONSHIP_FIANCE = RelationshipIndex.RELATIONSHIP_FIANCE
RELATIONSHIP_STEADY = RelationshipIndex.RELATIONSHIP_STEADY
RELATIONSHIP_DESCENDANT = RelationshipIndex.RELATIONSHIP_DESCENDANT
RELATIONSHIP_GRANDPARENT = RelationshipIndex.RELATIONSHIP_GRANDPARENT
RELATIONSHIP_GRANDCHILD = RelationshipIndex.RELATIONSHIP_GRANDCHILD
RELATIONSHIP_SIBLINGS_CHILDREN = RelationshipIndex.RELATIONSHIP_SIBLINGS_CHILDREN
RELATIONSHIP_PARENTS_SIBLING = RelationshipIndex.RELATIONSHIP_PARENTS_SIBLING
RELATIONSHIP_COUSIN = RelationshipIndex.RELATIONSHIP_COUSIN
RELATIONSHIP_DISTANT_RELATIVE = RelationshipIndex.RELATIONSHIP_DISTANT_RELATIVE
RELATIONSHIP_GREAT_GRANDPARENT = RelationshipIndex.RELATIONSHIP_GREAT_GRANDPARENT
RELATIONSHIP_GREAT_GRANDCHILD = RelationshipIndex.RELATIONSHIP_GREAT_GRANDCHILD
RELATIONSHIP_GRANDPARENT_SIBLING = RelationshipIndex.RELATIONSHIP_GRANDPARENT_SIBLING
RELATIONSHIP_FIRST_COUSIN_ONCE_REMOVED = RelationshipIndex.RELATIONSHIP_FIRST_COUSIN_ONCE_REMOVED
RELATIONSHIP_SIBLINGS_GRANDCHILD = RelationshipIndex.RELATIONSHIP_SIBLINGS_GRANDCHILD
RELATIONSHIP_SIBLINGS_GREAT_GRANDCHILD = RelationshipIndex.RELATIONSHIP_SIBLINGS_GREAT_GRANDCHILD
RELATIONSHIP_GREAT_GRANDPARENT_SIBLING = RelationshipIndex.RELATIONSHIP_GREAT_GRANDPARENT_SIBLING
RELATIONSHIP_HALF_SIBLING = RelationshipIndex.RELATIONSHIP_HALF_SIBLING


class PersistenceMaster(Message):
    class DATA_TYPE(IntEnum):
        SimInfoAttribute: 'PersistenceMaster.DATA_TYPE' = 1
        StateComponent: 'PersistenceMaster.DATA_TYPE' = 2
        RelationshipTracker: 'PersistenceMaster.DATA_TYPE' = 3
        Relationship: 'PersistenceMaster.DATA_TYPE' = 4
        CommodityTracker: 'PersistenceMaster.DATA_TYPE' = 5
        StatisticsTracker: 'PersistenceMaster.DATA_TYPE' = 6
        ObjectPreferences: 'PersistenceMaster.DATA_TYPE' = 7
        CraftingComponent: 'PersistenceMaster.DATA_TYPE' = 8
        ObjectOwnership: 'PersistenceMaster.DATA_TYPE' = 9
        Stereo: 'PersistenceMaster.DATA_TYPE' = 10
        InventoryItemComponent: 'PersistenceMaster.DATA_TYPE' = 11
        LightingComponent: 'PersistenceMaster.DATA_TYPE' = 12
        EventDataTracker: 'PersistenceMaster.DATA_TYPE' = 13
        NameComponent: 'PersistenceMaster.DATA_TYPE' = 14
        StoredSimInfoComponent: 'PersistenceMaster.DATA_TYPE' = 15
        PregnancyTracker: 'PersistenceMaster.DATA_TYPE' = 16
        SimPermissions: 'PersistenceMaster.DATA_TYPE' = 17
        TraitTracker: 'PersistenceMaster.DATA_TYPE' = 18
        CanvasComponent: 'PersistenceMaster.DATA_TYPE' = 19
        DeathTracker: 'PersistenceMaster.DATA_TYPE' = 20
        OwnableComponent: 'PersistenceMaster.DATA_TYPE' = 21
        FlowingPuddleComponent: 'PersistenceMaster.DATA_TYPE' = 22
        AdventureTracker: 'PersistenceMaster.DATA_TYPE' = 23
        StatisticComponent: 'PersistenceMaster.DATA_TYPE' = 24
        GenealogyTracker: 'PersistenceMaster.DATA_TYPE' = 25
        ObjectRelationshipComponent: 'PersistenceMaster.DATA_TYPE' = 26
        SimKnowledge: 'PersistenceMaster.DATA_TYPE' = 27
        ObjectAgeComponent: 'PersistenceMaster.DATA_TYPE' = 28
        GardeningComponent: 'PersistenceMaster.DATA_TYPE' = 29
        SpawnerComponent: 'PersistenceMaster.DATA_TYPE' = 30
        OccultTracker: 'PersistenceMaster.DATA_TYPE' = 31
        MannequinComponent: 'PersistenceMaster.DATA_TYPE' = 32
        AppearanceTracker: 'PersistenceMaster.DATA_TYPE' = 33
        RetailComponent: 'PersistenceMaster.DATA_TYPE' = 34
        PortalLockingComponent: 'PersistenceMaster.DATA_TYPE' = 35
        StoryProgressionTracker: 'PersistenceMaster.DATA_TYPE' = 36
        ParentToSimHeadComponent: 'PersistenceMaster.DATA_TYPE' = 37
        StolenComponent: 'PersistenceMaster.DATA_TYPE' = 38
        RankedStatistic: 'PersistenceMaster.DATA_TYPE' = 42
        GameComponent: 'PersistenceMaster.DATA_TYPE' = 43
        SicknessTracker: 'PersistenceMaster.DATA_TYPE' = 44
        RelicTracker: 'PersistenceMaster.DATA_TYPE' = 45
        StoredObjectInfoComponent: 'PersistenceMaster.DATA_TYPE' = 46
        StoredAudioComponent: 'PersistenceMaster.DATA_TYPE' = 47
        SituationSchedulerComponent: 'PersistenceMaster.DATA_TYPE' = 48
        LifestyleBrandTracker: 'PersistenceMaster.DATA_TYPE' = 49
        SuntanTracker: 'PersistenceMaster.DATA_TYPE' = 50
        ObjectClaimComponent: 'PersistenceMaster.DATA_TYPE' = 51
        DegreeTracker: 'PersistenceMaster.DATA_TYPE' = 52
        OrganizationTracker: 'PersistenceMaster.DATA_TYPE' = 53
        ScholarshipLetterComponent: 'PersistenceMaster.DATA_TYPE' = 54
        ObjectLockingComponent: 'PersistenceMaster.DATA_TYPE' = 55
        FixupTracker: 'PersistenceMaster.DATA_TYPE' = 56
        UtilitiesComponent: 'PersistenceMaster.DATA_TYPE' = 57
        StoredInfoComponent: 'PersistenceMaster.DATA_TYPE' = 58
        ObjectMarketplaceComponent: 'PersistenceMaster.DATA_TYPE' = 59
        ModularObjectComponent: 'PersistenceMaster.DATA_TYPE' = 60
        StoredActorLocationComponent: 'PersistenceMaster.DATA_TYPE' = 61
        FishingLocationComponent: 'PersistenceMaster.DATA_TYPE' = 62
        AnimalPreferenceComponent: 'PersistenceMaster.DATA_TYPE' = 63
        AnimalObjectComponent: 'PersistenceMaster.DATA_TYPE' = 64
        ObjectFashionMarketplaceComponent: 'PersistenceMaster.DATA_TYPE' = 65
        LunarEffectTracker: 'PersistenceMaster.DATA_TYPE' = 66
        BrandingIconComponent: 'PersistenceMaster.DATA_TYPE' = 67
        PersistableJewelryTracker: 'PersistenceMaster.DATA_TYPE' = 68
        PersistableJewelryComponent: 'PersistenceMaster.DATA_TYPE' = 69
        PersistableChargeableComponent: 'PersistenceMaster.DATA_TYPE' = 70
        HeirloomComponent: 'PersistenceMaster.DATA_TYPE' = 74
        PersistableFamilyRecipes: 'PersistenceMaster.DATA_TYPE' = 75
        PersistableTattooTracker: 'PersistenceMaster.DATA_TYPE' = 76
        TravelDestinationComponent: 'PersistenceMaster.DATA_TYPE' = 77

    SimInfoAttribute = DATA_TYPE.SimInfoAttribute
    StateComponent = DATA_TYPE.StateComponent
    RelationshipTracker = DATA_TYPE.RelationshipTracker
    Relationship = DATA_TYPE.Relationship
    CommodityTracker = DATA_TYPE.CommodityTracker
    StatisticsTracker = DATA_TYPE.StatisticsTracker
    ObjectPreferences = DATA_TYPE.ObjectPreferences
    CraftingComponent = DATA_TYPE.CraftingComponent
    ObjectOwnership = DATA_TYPE.ObjectOwnership
    Stereo = DATA_TYPE.Stereo
    InventoryItemComponent = DATA_TYPE.InventoryItemComponent
    LightingComponent = DATA_TYPE.LightingComponent
    EventDataTracker = DATA_TYPE.EventDataTracker
    NameComponent = DATA_TYPE.NameComponent
    StoredSimInfoComponent = DATA_TYPE.StoredSimInfoComponent
    PregnancyTracker = DATA_TYPE.PregnancyTracker
    SimPermissions = DATA_TYPE.SimPermissions
    TraitTracker = DATA_TYPE.TraitTracker
    CanvasComponent = DATA_TYPE.CanvasComponent
    DeathTracker = DATA_TYPE.DeathTracker
    OwnableComponent = DATA_TYPE.OwnableComponent
    FlowingPuddleComponent = DATA_TYPE.FlowingPuddleComponent
    AdventureTracker = DATA_TYPE.AdventureTracker
    StatisticComponent = DATA_TYPE.StatisticComponent
    GenealogyTracker = DATA_TYPE.GenealogyTracker
    ObjectRelationshipComponent = DATA_TYPE.ObjectRelationshipComponent
    SimKnowledge = DATA_TYPE.SimKnowledge
    ObjectAgeComponent = DATA_TYPE.ObjectAgeComponent
    GardeningComponent = DATA_TYPE.GardeningComponent
    SpawnerComponent = DATA_TYPE.SpawnerComponent
    OccultTracker = DATA_TYPE.OccultTracker
    MannequinComponent = DATA_TYPE.MannequinComponent
    AppearanceTracker = DATA_TYPE.AppearanceTracker
    RetailComponent = DATA_TYPE.RetailComponent
    PortalLockingComponent = DATA_TYPE.PortalLockingComponent
    StoryProgressionTracker = DATA_TYPE.StoryProgressionTracker
    ParentToSimHeadComponent = DATA_TYPE.ParentToSimHeadComponent
    StolenComponent = DATA_TYPE.StolenComponent
    RankedStatistic = DATA_TYPE.RankedStatistic
    GameComponent = DATA_TYPE.GameComponent
    SicknessTracker = DATA_TYPE.SicknessTracker
    RelicTracker = DATA_TYPE.RelicTracker
    StoredObjectInfoComponent = DATA_TYPE.StoredObjectInfoComponent
    StoredAudioComponent = DATA_TYPE.StoredAudioComponent
    SituationSchedulerComponent = DATA_TYPE.SituationSchedulerComponent
    LifestyleBrandTracker = DATA_TYPE.LifestyleBrandTracker
    SuntanTracker = DATA_TYPE.SuntanTracker
    ObjectClaimComponent = DATA_TYPE.ObjectClaimComponent
    DegreeTracker = DATA_TYPE.DegreeTracker
    OrganizationTracker = DATA_TYPE.OrganizationTracker
    ScholarshipLetterComponent = DATA_TYPE.ScholarshipLetterComponent
    ObjectLockingComponent = DATA_TYPE.ObjectLockingComponent
    FixupTracker = DATA_TYPE.FixupTracker
    UtilitiesComponent = DATA_TYPE.UtilitiesComponent
    StoredInfoComponent = DATA_TYPE.StoredInfoComponent
    ObjectMarketplaceComponent = DATA_TYPE.ObjectMarketplaceComponent
    ModularObjectComponent = DATA_TYPE.ModularObjectComponent
    StoredActorLocationComponent = DATA_TYPE.StoredActorLocationComponent
    FishingLocationComponent = DATA_TYPE.FishingLocationComponent
    AnimalPreferenceComponent = DATA_TYPE.AnimalPreferenceComponent
    AnimalObjectComponent = DATA_TYPE.AnimalObjectComponent
    ObjectFashionMarketplaceComponent = DATA_TYPE.ObjectFashionMarketplaceComponent
    LunarEffectTracker = DATA_TYPE.LunarEffectTracker
    BrandingIconComponent = DATA_TYPE.BrandingIconComponent
    PersistableJewelryTracker = DATA_TYPE.PersistableJewelryTracker
    PersistableJewelryComponent = DATA_TYPE.PersistableJewelryComponent
    PersistableChargeableComponent = DATA_TYPE.PersistableChargeableComponent
    HeirloomComponent = DATA_TYPE.HeirloomComponent
    PersistableFamilyRecipes = DATA_TYPE.PersistableFamilyRecipes
    PersistableTattooTracker = DATA_TYPE.PersistableTattooTracker
    TravelDestinationComponent = DATA_TYPE.TravelDestinationComponent

    class PersistableData():
        # __init__
        type: 'PersistenceMaster.PersistableData.DATA_TYPE'

        class DATA_TYPE(IntEnum):
            SimInfoAttribute: 'PersistenceMaster.PersistableData.DATA_TYPE' = 1
            StateComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 2
            RelationshipTracker: 'PersistenceMaster.PersistableData.DATA_TYPE' = 3
            Relationship: 'PersistenceMaster.PersistableData.DATA_TYPE' = 4
            CommodityTracker: 'PersistenceMaster.PersistableData.DATA_TYPE' = 5
            StatisticsTracker: 'PersistenceMaster.PersistableData.DATA_TYPE' = 6
            ObjectPreferences: 'PersistenceMaster.PersistableData.DATA_TYPE' = 7
            CraftingComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 8
            ObjectOwnership: 'PersistenceMaster.PersistableData.DATA_TYPE' = 9
            Stereo: 'PersistenceMaster.PersistableData.DATA_TYPE' = 10
            InventoryItemComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 11
            LightingComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 12
            EventDataTracker: 'PersistenceMaster.PersistableData.DATA_TYPE' = 13
            NameComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 14
            StoredSimInfoComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 15
            PregnancyTracker: 'PersistenceMaster.PersistableData.DATA_TYPE' = 16
            SimPermissions: 'PersistenceMaster.PersistableData.DATA_TYPE' = 17
            TraitTracker: 'PersistenceMaster.PersistableData.DATA_TYPE' = 18
            CanvasComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 19
            DeathTracker: 'PersistenceMaster.PersistableData.DATA_TYPE' = 20
            OwnableComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 21
            FlowingPuddleComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 22
            AdventureTracker: 'PersistenceMaster.PersistableData.DATA_TYPE' = 23
            StatisticComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 24
            GenealogyTracker: 'PersistenceMaster.PersistableData.DATA_TYPE' = 25
            ObjectRelationshipComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 26
            SimKnowledge: 'PersistenceMaster.PersistableData.DATA_TYPE' = 27
            ObjectAgeComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 28
            GardeningComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 29
            SpawnerComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 30
            OccultTracker: 'PersistenceMaster.PersistableData.DATA_TYPE' = 31
            MannequinComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 32
            AppearanceTracker: 'PersistenceMaster.PersistableData.DATA_TYPE' = 33
            RetailComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 34
            PortalLockingComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 35
            StoryProgressionTracker: 'PersistenceMaster.PersistableData.DATA_TYPE' = 36
            ParentToSimHeadComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 37
            StolenComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 38
            RankedStatistic: 'PersistenceMaster.PersistableData.DATA_TYPE' = 42
            GameComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 43
            SicknessTracker: 'PersistenceMaster.PersistableData.DATA_TYPE' = 44
            RelicTracker: 'PersistenceMaster.PersistableData.DATA_TYPE' = 45
            StoredObjectInfoComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 46
            StoredAudioComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 47
            SituationSchedulerComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 48
            LifestyleBrandTracker: 'PersistenceMaster.PersistableData.DATA_TYPE' = 49
            SuntanTracker: 'PersistenceMaster.PersistableData.DATA_TYPE' = 50
            ObjectClaimComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 51
            DegreeTracker: 'PersistenceMaster.PersistableData.DATA_TYPE' = 52
            OrganizationTracker: 'PersistenceMaster.PersistableData.DATA_TYPE' = 53
            ScholarshipLetterComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 54
            ObjectLockingComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 55
            FixupTracker: 'PersistenceMaster.PersistableData.DATA_TYPE' = 56
            UtilitiesComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 57
            StoredInfoComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 58
            ObjectMarketplaceComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 59
            ModularObjectComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 60
            StoredActorLocationComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 61
            FishingLocationComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 62
            AnimalPreferenceComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 63
            AnimalObjectComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 64
            ObjectFashionMarketplaceComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 65
            LunarEffectTracker: 'PersistenceMaster.PersistableData.DATA_TYPE' = 66
            BrandingIconComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 67
            PersistableJewelryTracker: 'PersistenceMaster.PersistableData.DATA_TYPE' = 68
            PersistableJewelryComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 69
            PersistableChargeableComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 70
            HeirloomComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 74
            PersistableFamilyRecipes: 'PersistenceMaster.PersistableData.DATA_TYPE' = 75
            PersistableTattooTracker: 'PersistenceMaster.PersistableData.DATA_TYPE' = 76
            TravelDestinationComponent: 'PersistenceMaster.PersistableData.DATA_TYPE' = 77

    # __init__
    data: 'RepeatedCompositeFieldContainer[PersistenceMaster.PersistableData]'
    type: 'PersistenceMaster.PersistableData.DATA_TYPE'


class PersistableSimInfoAttributes(Message):
    persistable_data: 'PersistableSimInfoAttributes'

    # __init__
    relationship_tracker: 'PersistableRelationshipTracker'
    commodity_tracker: 'PersistableCommodityTracker'
    statistics_tracker: 'PersistableStatisticsTracker'
    object_preferences: 'PersistableObjectPreferences'
    object_ownership: 'PersistableObjectOwnership'
    event_data_tracker: 'PersistableEventDataTracker'
    death_tracker: 'PersistableDeathTracker'
    pregnancy_tracker: 'PersistablePregnancyTracker'
    sim_permissions: 'PersistableSimPermissions'
    trait_tracker: 'PersistableTraitTracker'
    adventure_tracker: 'PersistableAdventureTracker'
    sim_careers: 'PersistableSimCareers'
    skill_tracker: 'PersistableSkillTracker'
    genealogy_tracker: 'PersistableGenealogyTracker'
    unlock_tracker: 'PersistableUnlockTracker'
    royalty_tracker: 'PersistableRoyaltyTracker'
    occult_tracker: 'PersistableOccultTracker'
    notebook_tracker: 'PersistableNotebookTracker'
    appearance_tracker: 'PersistableAppearanceTracker'
    story_progression_tracker: 'PersistableStoryProgressionTracker'
    ranked_statistic_tracker: 'PersistableRankedStatisticTracker'
    sickness_tracker: 'PersistableSicknessTracker'
    relic_tracker: 'PersistableRelicTracker'
    stored_object_info_component: 'PersistableStoredObjectInfoComponent'
    stored_audio_component: 'PersistableStoredAudioComponent'
    lifestyle_brand_tracker: 'PersistableLifestyleBrandTracker'
    suntan_tracker: 'PersistableSuntanTracker'
    familiar_tracker: 'PersistableFamiliarTracker'
    favorites_tracker: 'PersistableFavoritesTracker'
    degree_tracker: 'PersistableDegreeTracker'
    organization_tracker: 'PersistableOrganizationTracker'
    fixup_tracker: 'PersistableFixupTracker'
    trait_statistic_tracker: 'PersistableTraitStatisticTracker'
    lunar_effect_tracker: 'PersistableLunarEffectTracker'
    jewelry_tracker: 'PersistableJewelryTracker'
    family_recipes_tracker: 'PersistableFamilyRecipesTracker'
    tattoo_tracker: 'PersistableTattooTracker'


class LockData(Message):
    # __init__
    lock_type: 'int'  # fixed uint64
    priority: 'int'  # fixed uint64
    sides: 'int'  # fixed uint64
    except_actor: 'bool'
    except_household: 'bool'
    exception_sim_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    participant_enum: 'int'  # fixed uint64
    situation_jobs: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    role_tags: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    negate: 'bool'
    except_retail_employee: 'bool'
    locked_sim_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    gender: 'int'  # fixed uint64
    ages: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    species: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    match_type: 'int'  # uint32
    ranked_stat_id: 'int'  # fixed uint64
    threshold_value: 'int'  # uint64
    threshold_comparison: 'int'  # uint32
    buff_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    creature_types: 'RepeatedCompositeFieldContainer[int]'  # uint32
    remove_sim_exception: 'bool'


class PersistableStateComponent(Message):
    persistable_data: 'PersistableStateComponent'

    # __init__
    states: 'RepeatedCompositeFieldContainer[StateComponentState]'
    states_before_delinquency: 'RepeatedCompositeFieldContainer[StateComponentState]'


class PersistableRelationshipTracker(Message):
    persistable_data: 'PersistableRelationshipTracker'

    # __init__
    relationships: 'RepeatedCompositeFieldContainer[PersistableRelationship]'


class PersistableRelationship(Message):
    persistable_data: 'PersistableRelationship'

    # __init__
    target_id: 'int'  # uint64
    value: 'float'  # float32
    bits: 'RepeatedCompositeFieldContainer[int]'  # uint64
    timeouts: 'RepeatedCompositeFieldContainer[Timeout]'
    tracks: 'RepeatedCompositeFieldContainer[PersistableRelationshipTrack]'
    knowledge: 'SimKnowledge'
    bit_added_buffs: 'RepeatedCompositeFieldContainer[BitAddedBuffList]'
    last_update_time: 'int'  # uint64


class ConfrontedSimSecret(Message):
    # __init__
    secret_id: 'int'  # uint64
    blackmailed: 'bool'


class SimKnowledge(Message):
    persistable_data: 'SimKnowledge'

    # __init__
    trait_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    num_traits: 'int'  # uint32
    knows_career: 'bool'
    stats: 'RepeatedCompositeFieldContainer[int]'  # uint64
    knows_major: 'bool'
    knows_romantic_preference: 'bool'
    knows_woohoo_preference: 'bool'
    known_romantic_genders: 'RepeatedCompositeFieldContainer[int]'  # uint32
    known_woohoo_genders: 'RepeatedCompositeFieldContainer[int]'  # uint32
    known_exploring_sexuality: 'bool'
    unconfronted_secret_id: 'int'  # uint64
    confronted_secrets: 'RepeatedCompositeFieldContainer[ConfrontedSimSecret]'
    known_relationship_expectations_ids: 'RepeatedCompositeFieldContainer[int]'  # uint32
    known_rel_tracks: 'RepeatedCompositeFieldContainer[int]'  # uint64
    known_net_worth: 'int'  # uint64


class Timeout(Message):
    # __init__
    timeout_bit_id_hash: 'int'  # uint64
    elapsed_time: 'float'  # float32


class PersistableRelationshipTrack(Message):
    # __init__
    track_id: 'int'  # uint64
    value: 'float'  # float32
    visible: 'bool'
    ticks_until_decay_begins: 'float'  # float32


class BitAddedBuffList(Message):
    # __init__
    bit_id: 'int'  # uint64
    buff_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64


class PersistableCommodityTracker(Message):
    persistable_data: 'PersistableCommodityTracker'

    # __init__
    commodities: 'RepeatedCompositeFieldContainer[Commodity]'
    time_of_last_save: 'int'  # uint64


class Commodity(Message):
    # __init__
    name_hash: 'int'  # uint64
    value: 'float'  # float32
    apply_buff_on_start_up: 'bool'
    buff_reason: 'LocalizedString'
    time_of_last_value_change: 'int'  # uint64


class PersistableStatisticsTracker(Message):
    persistable_data: 'PersistableStatisticsTracker'

    # __init__
    statistics: 'RepeatedCompositeFieldContainer[Statistic]'


class Statistic(Message):
    # __init__
    name_hash: 'int'  # uint64
    value: 'float'  # float32


class PersistableSkillTracker(Message):
    persistable_data: 'PersistableSkillTracker'

    # __init__
    skills: 'RepeatedCompositeFieldContainer[Skill]'


class Skill(Message):
    # __init__
    name_hash: 'int'  # uint64
    value: 'float'  # float32
    level_0_buffer_full: 'bool'
    time_of_last_value_change: 'int'  # uint64


class StateComponentState(Message):
    # __init__
    state_name_hash: 'int'  # uint64
    value_name_hash: 'int'  # uint64


class PersistableObjectPreferences(Message):
    persistable_data: 'PersistableObjectPreferences'

    # __init__
    preferences: 'RepeatedCompositeFieldContainer[ObjectPreference]'


class PersistableCraftingComponent(Message):
    persistable_data: 'PersistableCraftingComponent'

    # __init__
    process: 'CraftingProcess'
    use_base_recipe: 'bool'
    is_final_product: 'bool'


class IngredientData(Message):
    # __init__
    ingredient_data: 'PersistenceMaster'
    in_sim_inventory: 'bool'


class GenericIngredientData(Message):
    # __init__
    ingredient_id: 'int'  # uint64
    count: 'int'  # uint32


class SimInfoNameData(Message):
    # __init__
    first_name: 'str'
    last_name: 'str'
    gender: 'int'  # uint32
    full_name_key: 'int'  # uint32
    age_flags: 'int'  # uint32


class BucksRefundData(Message):
    # __init__
    sim_id: 'int'  # uint64
    bucks_type: 'int'  # uint32
    amount: 'int'  # uint32


class CraftingProcess(Message):
    # __init__
    recipe_id: 'int'  # uint64
    phase_id: 'int'  # uint32
    previous_phase_id: 'int'  # uint32
    current_ico: 'int'  # fixed uint64
    crafter_sim_id: 'int'  # uint64
    statistic_tracker: 'PersistableStatisticsTracker'
    used_ingredients: 'RepeatedCompositeFieldContainer[IngredientData]'
    inscription: 'str'
    crafted_value: 'int'  # uint32
    crafter_info: 'SimInfoNameData'
    bucks_refund_on_cancel: 'RepeatedCompositeFieldContainer[BucksRefundData]'
    generic_recipe_ingredients: 'RepeatedCompositeFieldContainer[GenericIngredientData]'
    situation_id: 'int'  # uint64
    executed_phases: 'RepeatedCompositeFieldContainer[int]'  # uint64
    defined_ingredients: 'RepeatedCompositeFieldContainer[GenericIngredientData]'
    single_serving_value: 'float'  # float32
    family_recipe: 'FamilyRecipe'


class PersistableObjectOwnership(Message):
    persistable_data: 'PersistableObjectOwnership'

    # __init__
    owned_object: 'RepeatedCompositeFieldContainer[ObjectPreference]'


class PersistableStereo(Message):
    persistable_data: 'PersistableStereo'

    # __init__
    channel: 'int'  # uint64


class PersistableInventoryItemComponent(Message):
    persistable_data: 'PersistableInventoryItemComponent'

    # __init__
    inventory_type: 'int'  # uint32
    owner_id: 'int'  # uint64
    stack_count: 'int'  # uint32
    requires_claiming: 'bool'
    is_hidden: 'bool'


class ObjectPreference(Message):
    # __init__
    tag: 'int'  # uint32
    object_id: 'int'  # uint64


class PersistableLightingComponent(Message):
    persistable_data: 'PersistableLightingComponent'

    # __init__
    dimmer_setting: 'float'  # float32
    color: 'int'  # uint32
    pending_dimmer_setting: 'float'  # float32
    user_intensity: 'float'  # float32
    previous_dimmer_setting: 'float'  # float32
    previous_color: 'int'  # uint32


class TimedAspiration(Message):
    # __init__
    aspiration: 'int'  # fixed uint64
    end_time: 'int'  # uint64
    completed: 'bool'


class MilestoneCompletionCount(Message):
    # __init__
    milestone_guid: 'int'  # uint64
    completion_count: 'int'  # uint32


class AdditionalObjectives(Message):
    # __init__
    milestone_guid: 'int'  # uint64
    objective_guids: 'RepeatedCompositeFieldContainer[int]'  # uint64


class SuggestedAspiration(Message):
    # __init__
    visible_suggested_aspirations: 'RepeatedCompositeFieldContainer[int]'  # uint64
    invisible_suggested_aspirations: 'RepeatedCompositeFieldContainer[int]'  # uint64
    cool_down_dict: 'RepeatedCompositeFieldContainer[CoolDownAspiration]'


class CoolDownAspiration(Message):
    # __init__
    aspiration: 'int'  # uint64
    timestamp: 'int'  # uint64


class PersistableEventDataTracker(Message):
    persistable_data: 'PersistableEventDataTracker'

    # __init__
    milestones_completed: 'RepeatedCompositeFieldContainer[int]'  # uint64
    objectives_completed: 'RepeatedCompositeFieldContainer[int]'  # uint64
    data: 'EventDataObject'
    unlocked_hidden_aspiration_tracks: 'RepeatedCompositeFieldContainer[int]'  # uint64
    timed_aspirations: 'RepeatedCompositeFieldContainer[TimedAspiration]'
    milestone_completion_counts: 'RepeatedCompositeFieldContainer[MilestoneCompletionCount]'
    additional_objectives: 'RepeatedCompositeFieldContainer[AdditionalObjectives]'
    suggested_aspiration: 'SuggestedAspiration'
    childhood_inspirations_completed: 'bool'


class EventDataObject(Message):
    # __init__
    situation_data: 'RepeatedCompositeFieldContainer[EventData_SituationData]'
    objective_data: 'RepeatedCompositeFieldContainer[EventData_Objective_Data]'
    simoleon_data: 'RepeatedCompositeFieldContainer[EventData_EnumToAmount]'
    time_data: 'RepeatedCompositeFieldContainer[EventData_EnumToAmount]'
    interaction_data: 'RepeatedCompositeFieldContainer[EventData_NamedData]'
    relationship_data: 'RepeatedCompositeFieldContainer[EventData_RelationshipData]'
    travel_data: 'RepeatedCompositeFieldContainer[int]'  # uint64
    tag_data: 'RepeatedCompositeFieldContainer[EventData_TagData]'
    career_data: 'RepeatedCompositeFieldContainer[EventData_CareerData]'
    relative_start_data: 'RepeatedCompositeFieldContainer[EventData_RelativeStartingData]'
    club_bucks_data: 'EventData_ClubBucksEarned'
    time_in_gatherings: 'EventData_TimeInClubGathering'
    encouraged_interactions_started: 'EventData_EncouragedInteractions'
    mood_data: 'EventData_Moods'
    bucks_data: 'RepeatedCompositeFieldContainer[EventData_EnumToAmount]'


class EventData_RelativeStartingData(Message):
    # __init__
    objective_guid64: 'int'  # uint64
    starting_values: 'RepeatedCompositeFieldContainer[int]'  # uint64


class EventData_SituationData(Message):
    # __init__
    name: 'str'
    results: 'RepeatedCompositeFieldContainer[EventData_SituationEnums]'


class EventData_SituationEnums(Message):
    # __init__
    result_enum: 'int'  # uint32
    enum_quality: 'RepeatedCompositeFieldContainer[EventData_EnumToAmount]'


class EventData_TagData(Message):
    # __init__
    tag_enum: 'int'  # uint32
    enums: 'RepeatedCompositeFieldContainer[EventData_EnumToAmount]'


class EventData_RelationshipData(Message):
    # __init__
    relationship_id: 'int'  # uint32
    enums: 'RepeatedCompositeFieldContainer[EventData_EnumToAmount]'


class EventData_CareerData(Message):
    # __init__
    name: 'str'
    time: 'int'  # uint64
    money: 'int'  # uint64


class EventData_Objective_Data(Message):
    # __init__
    enum: 'int'  # uint64
    amount: 'int'  # uint32
    ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class EventData_NamedData(Message):
    # __init__
    name: 'str'
    enums: 'RepeatedCompositeFieldContainer[EventData_EnumToAmount]'


class EventData_EnumToAmount(Message):
    # __init__
    enum: 'int'  # uint32
    amount: 'int'  # int64


class EventData_ClubBucksEarned(Message):
    # __init__
    amount: 'int'  # uint32


class EventData_TimeInClubGathering(Message):
    # __init__
    sim_minutes: 'int'  # uint32


class EventData_EncouragedInteractions(Message):
    # __init__
    interactions_started: 'int'  # uint32


class MoodData(Message):
    # __init__
    mood: 'int'  # uint64
    last_time_in_mood: 'int'  # uint64


class EventData_Moods(Message):
    # __init__
    mood_data: 'RepeatedCompositeFieldContainer[MoodData]'


class PersistableNameComponent(Message):
    persistable_data: 'PersistableNameComponent'

    # __init__
    name: 'str'
    description: 'str'


class PersistableStoredSimInfoComponent(Message):
    persistable_data: 'PersistableStoredSimInfoComponent'

    # __init__
    sim_id: 'int'  # fixed uint64
    sim_info_name_data: 'SimInfoNameData'
    sim_id_set: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    sim_info_name_data_set: 'RepeatedCompositeFieldContainer[SimInfoNameData]'
    sim_id_list: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    sim_info_name_data_list: 'RepeatedCompositeFieldContainer[SimInfoNameData]'


class PersistablePregnancyTracker(Message):
    persistable_data: 'PersistablePregnancyTracker'

    # __init__
    deprecated_seed: 'float'  # float32
    parent_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    last_modified: 'int'  # uint64
    seed: 'int'  # uint32
    origin: 'int'  # uint32
    chosen_partner_parent_id: 'int'  # fixed uint64


class PersistableSimPermissions(Message):
    persistable_data: 'PersistableSimPermissions'

    # __init__
    enabled_permissions: 'RepeatedCompositeFieldContainer[int]'  # uint64


class GameplayObjectPreference(Message):
    # __init__
    gameplay_object_preference_id: 'int'  # uint64
    gameplay_object_preference_type: 'int'  # uint64


class PersistableTraitTracker(Message):
    persistable_data: 'PersistableTraitTracker'

    # __init__
    trait_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    gameplay_object_preference_map: 'RepeatedCompositeFieldContainer[GameplayObjectPreference]'


class PersistableCanvasComponent(Message):
    persistable_data: 'PersistableCanvasComponent'

    # __init__
    texture_id: 'int'  # uint64
    reveal_level: 'int'  # uint32
    effect: 'int'  # uint32
    time_stamp: 'str'
    stage_texture_id: 'int'  # uint64
    overlay_texture_id: 'int'  # uint64
    reveal_texture_id: 'int'  # uint64
    outfit_category: 'int'  # uint32
    locked: 'bool'
    no_op_version: 'int'  # uint32
    reveal_texture_id_B: 'int'  # uint64
    is_linked_canvas: 'bool'


class PersistableDeathTracker(Message):
    persistable_data: 'PersistableDeathTracker'

    # __init__
    death_type: 'int'  # uint32
    death_time: 'int'  # uint64
    death_object_id: 'int'  # uint64


class PersistableOwnableComponent(Message):
    persistable_data: 'PersistableOwnableComponent'

    # __init__
    sim_owner_id: 'int'  # uint64
    household_owner_id: 'int'  # uint64
    custom_name: 'str'


class PersistableFlowingPuddleComponent(Message):
    persistable_data: 'PersistableFlowingPuddleComponent'

    # __init__
    puddle_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    is_active: 'bool'


class PersistableAdventureTracker(Message):
    class AdventureMomentPair():
        # __init__
        adventure_id: 'int'  # uint64
        adventure_moment_id: 'int'  # uint64

    class AdventureMomentCooldowns():
        # __init__
        adventure_id: 'int'  # uint64
        adventure_moment_id: 'int'  # uint64
        adventure_cooldown: 'int'  # uint64

    persistable_data: 'PersistableAdventureTracker'

    # __init__
    adventures: 'RepeatedCompositeFieldContainer[PersistableAdventureTracker.AdventureMomentPair]'
    adventure_cooldowns: 'RepeatedCompositeFieldContainer[PersistableAdventureTracker.AdventureMomentCooldowns]'
    adventure_id: 'int'  # uint64
    adventure_moment_id: 'int'  # uint64
    adventure_id: 'int'  # uint64
    adventure_moment_id: 'int'  # uint64
    adventure_cooldown: 'int'  # uint64


class PersistableAppearanceTracker(Message):
    class AppearanceTrackerModifier():
        # __init__
        guid: 'int'  # uint64
        seed: 'int'  # uint32

    persistable_data: 'PersistableAppearanceTracker'

    # __init__
    appearance_modifiers: 'RepeatedCompositeFieldContainer[PersistableAppearanceTracker.AppearanceTrackerModifier]'
    guid: 'int'  # uint64
    seed: 'int'  # uint32


class CareerHistoryEntry(Message):
    # __init__
    career_uid: 'int'  # uint64
    track_uid: 'int'  # uint64
    track_level: 'int'  # uint32
    user_display_level: 'int'  # uint32
    time_left: 'int'  # uint64
    highest_level: 'int'  # uint32
    overmax_level: 'int'  # uint32
    daily_pay: 'int'  # uint32
    days_worked: 'int'  # uint32
    active_days_worked: 'int'  # uint32
    player_rewards_deferred: 'bool'
    schedule_shift_type: 'int'  # uint32


class PhotoPair(Message):
    # __init__
    before_photo: 'ResourceKey'
    after_photo: 'ResourceKey'


class HiLowResPhotoPair(Message):
    # __init__
    hi_res_photo_instance: 'int'  # uint64
    low_res_photo: 'ResourceKey'


class GigHistoryEntry(Message):
    # __init__
    customer_sim_id: 'int'  # fixed uint64
    client_lot_id: 'int'  # uint64
    gig_id: 'int'  # uint64
    career_id: 'int'  # uint64
    gig_result: 'int'  # uint32
    client_hh_name: 'str'
    after_photos: 'RepeatedCompositeFieldContainer[ResourceKey]'
    before_photos: 'RepeatedCompositeFieldContainer[ResourceKey]'
    gig_lot_type: 'int'  # uint32
    project_title: 'LocalizedString'
    selected_pairs: 'RepeatedCompositeFieldContainer[PhotoPair]'
    gig_score: 'float'  # float32
    hi_low_res_pairs: 'RepeatedCompositeFieldContainer[HiLowResPhotoPair]'


class GigHistoryKey(Message):
    # __init__
    customer_sim_id: 'int'  # fixed uint64
    client_lot_id: 'int'  # uint64


class CareerEventData(Message):
    # __init__
    career_event_id: 'int'  # uint64
    required_zone_id: 'int'  # fixed uint64
    event_situation_id: 'int'  # uint64
    state: 'int'  # uint32
    temp_household_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class CareerEventManagerData(Message):
    # __init__
    career_events: 'RepeatedCompositeFieldContainer[CareerEventData]'
    scorable_situation_seed: 'SituationSeedData'


class DetectiveCareerData(Message):
    # __init__
    active_criminal_sim_id: 'int'  # fixed uint64
    crime_scene_event_id: 'int'  # fixed uint64
    unused_clue_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    used_clue_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    case_start_time_in_minutes: 'int'  # fixed uint64


class CareerEventCooldown(Message):
    # __init__
    career_event_id: 'int'  # fixed uint64
    day: 'int'  # int32


class CareerClaimedObjectData(Message):
    # __init__
    guid: 'int'  # uint64
    claimed_object_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64


class PersistableSimCareer(Message):
    # __init__
    career_uid: 'int'  # uint64
    track_uid: 'int'  # uint64
    track_level: 'int'  # uint32
    user_display_level: 'int'  # uint32
    attended_work: 'bool'
    base_work_performance: 'float'  # float32
    positive_work_performance: 'float'  # float32
    negative_work_performance: 'float'  # float32
    company_name_hash: 'int'  # uint64
    current_work_start: 'int'  # uint64
    current_work_end: 'int'  # uint64
    current_work_duration: 'int'  # uint64
    active_situation_id: 'int'  # fixed uint64
    career_situation_guid: 'int'  # fixed uint64
    called_in_sick: 'bool'
    pending_promotion: 'bool'
    join_time: 'int'  # int64
    taking_day_off_reason: 'int'  # uint32
    requested_day_off_reason: 'int'  # uint32
    career_event_manager_data: 'CareerEventManagerData'
    overmax_level: 'int'  # uint32
    detective_data: 'DetectiveCareerData'
    career_session_extended: 'bool'
    zone_id: 'int'  # fixed uint64
    has_attended_first_day: 'bool'
    career_event_cooldowns: 'RepeatedCompositeFieldContainer[CareerEventCooldown]'
    should_restore_career_state: 'bool'
    offered_assignments: 'RepeatedCompositeFieldContainer[int]'  # uint64
    active_assignments: 'RepeatedCompositeFieldContainer[int]'  # uint64
    pto_taken: 'float'  # float32
    fame_moment_completed: 'bool'
    upcoming_gig: 'CareerGigData'
    schedule_shift_type: 'int'  # uint32
    first_gig_completed: 'bool'
    seen_scholarship_info: 'bool'
    familiar_rabbit_hole_id: 'int'  # uint64
    rabbit_hole_id: 'int'  # uint64
    claimed_object_datas: 'RepeatedCompositeFieldContainer[CareerClaimedObjectData]'
    current_gigs: 'RepeatedCompositeFieldContainer[CareerGigData]'
    follow_enabled: 'bool'
    icon_override: 'ResourceKey'
    workplace_rival_id: 'int'  # uint64
    outfit_index: 'int'  # uint32
    small_business_career_data: 'RepeatedCompositeFieldContainer[CareerSmallBusinessData]'


class PersistableSimCareers(Message):
    # __init__
    careers: 'RepeatedCompositeFieldContainer[PersistableSimCareer]'
    career_history: 'RepeatedCompositeFieldContainer[CareerHistoryEntry]'
    retirement_career_uid: 'int'  # uint64
    custom_career_name: 'str'
    custom_career_description: 'str'
    gig_history: 'RepeatedCompositeFieldContainer[GigHistoryEntry]'
    last_gig_history: 'GigHistoryKey'
    retirement_career_track_uid: 'int'  # uint64


class FamilyRelation(Message):
    # __init__
    relation_type: 'RelationshipIndex'
    sim_id: 'int'  # uint64


class RelationshipTrope(Message):
    # __init__
    sim_id: 'int'  # uint64
    trope_id: 'int'  # uint64


class ArchivedFamilyRelbit(Message):
    # __init__
    target_sim_id: 'int'  # uint64
    relationship_bit_id: 'int'  # uint64
    time_archived: 'int'  # uint64


class PersistableGenealogyTracker(Message):
    persistable_data: 'PersistableGenealogyTracker'

    # __init__
    family_relations: 'RepeatedCompositeFieldContainer[FamilyRelation]'
    relationship_tropes: 'RepeatedCompositeFieldContainer[RelationshipTrope]'
    archived_family_relbits: 'RepeatedCompositeFieldContainer[ArchivedFamilyRelbit]'
    pinned_family_relbits: 'RepeatedCompositeFieldContainer[ArchivedFamilyRelbit]'


class ObjectRelationship(Message):
    # __init__
    sim_id: 'int'  # uint64
    value: 'float'  # float32
    commodity_tracker: 'PersistableCommodityTracker'
    statistics_tracker: 'PersistableStatisticsTracker'


class PersistableObjectRelationshipComponent(Message):
    persistable_data: 'PersistableObjectRelationshipComponent'

    # __init__
    relationships: 'RepeatedCompositeFieldContainer[ObjectRelationship]'


class PersistableObjectAgeComponent(Message):
    persistable_data: 'PersistableObjectAgeComponent'

    # __init__
    age: 'int'  # uint64
    saved_tick: 'int'  # uint64


class FruitSpawner(Message):
    # __init__
    definition_id: 'int'  # uint64
    fruit_save_data: 'PersistenceMaster'


class PersistableGardeningComponent(Message):
    persistable_data: 'PersistableGardeningComponent'

    # __init__
    fruit_spawners: 'RepeatedCompositeFieldContainer[FruitSpawner]'
    crop_weights: 'RepeatedCompositeFieldContainer[float]'  # float32
    default_definition_id: 'int'  # uint64
    is_plant: 'bool'


class UnlockData(Message):
    # __init__
    unlock_instance_id: 'int'  # uint64
    unlock_instance_type: 'int'  # uint64
    custom_name: 'str'
    marked_as_new: 'bool'


class PersistableUnlockTracker(Message):
    persistable_data: 'PersistableUnlockTracker'

    # __init__
    unlock_data_list: 'RepeatedCompositeFieldContainer[UnlockData]'


class PersistableSpawnerComponent(Message):
    persistable_data: 'PersistableSpawnerComponent'

    # __init__
    spawned_obj_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    spawner_initialized: 'bool'
    spawner_data_spawn_index: 'int'  # int32
    times_commodity_reset: 'int'  # uint32
    spawner_disabled: 'bool'


class PersistableRoyaltyTracker(Message):
    class Royalty():
        # __init__
        royalty_type: 'int'  # uint32
        royalty_guid64: 'int'  # uint64
        entry_name: 'LocalizedString'
        multiplier: 'float'  # float32
        current_payment: 'int'  # uint32

    persistable_data: 'PersistableRoyaltyTracker'

    # __init__
    royalties: 'RepeatedCompositeFieldContainer[PersistableRoyaltyTracker.Royalty]'
    royalty_type: 'int'  # uint32
    royalty_guid64: 'int'  # uint64
    entry_name: 'LocalizedString'
    multiplier: 'float'  # float32
    current_payment: 'int'  # uint32


class PersistableOccultTracker(Message):
    class OccultSimData():
        # __init__
        occult_type: 'int'  # uint32
        physique: 'str'
        facial_attributes: 'bytes'
        voice_pitch: 'float'  # float32
        voice_actor: 'int'  # uint32
        voice_effect: 'int'  # uint64
        skin_tone: 'int'  # uint64
        genetic_data: 'GeneticData'
        flags: 'int'  # uint32
        outfits: 'OutfitList'
        skin_tone_val_shift: 'float'  # float32
        parts_custom_tattoos: 'RepeatedCompositeFieldContainer[SimPartCustomTattooData]'
        parts_creator_data: 'RepeatedCompositeFieldContainer[SimPartCreatorData]'

    persistable_data: 'PersistableOccultTracker'

    # __init__
    occult_types: 'int'  # uint32
    current_occult_types: 'int'  # uint32
    occult_sim_infos: 'RepeatedCompositeFieldContainer[PersistableOccultTracker.OccultSimData]'
    pending_occult_type: 'int'  # uint32
    occult_form_available: 'bool'
    occult_type: 'int'  # uint32
    physique: 'str'
    facial_attributes: 'bytes'
    voice_pitch: 'float'  # float32
    voice_actor: 'int'  # uint32
    voice_effect: 'int'  # uint64
    skin_tone: 'int'  # uint64
    genetic_data: 'GeneticData'
    flags: 'int'  # uint32
    outfits: 'OutfitList'
    skin_tone_val_shift: 'float'  # float32
    parts_custom_tattoos: 'RepeatedCompositeFieldContainer[SimPartCustomTattooData]'
    parts_creator_data: 'RepeatedCompositeFieldContainer[SimPartCreatorData]'


class MannequinSimData(Message):
    # __init__
    mannequin_id: 'int'  # fixed uint64
    gender: 'int'  # uint32
    age: 'int'  # uint32
    extended_species: 'int'  # uint32
    physique: 'str'
    facial_attributes: 'bytes'
    skin_tone: 'int'  # uint64
    outfits: 'OutfitList'
    current_outfit_type: 'int'  # uint32
    current_outfit_index: 'int'  # uint32
    previous_outfit_type: 'int'  # uint32
    previous_outfit_index: 'int'  # uint32
    zone_id: 'int'  # fixed uint64
    world_id: 'int'  # uint32
    animation_pose: 'AnimationStateRequest'
    skin_tone_val_shift: 'float'  # float32


class PersistableMannequinComponent(Message):
    persistable_data: 'PersistableMannequinComponent'

    # __init__
    sim_info_data: 'MannequinSimData'


class PersistableNotebookTracker(Message):
    class NotebookSubEntryData():
        # __init__
        sub_entry_id: 'int'  # fixed uint64
        new_sub_entry: 'bool'

    class NotebookEntryData():
        # __init__
        object_recipe_id: 'int'  # fixed uint64
        object_entry_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
        tuning_reference_id: 'int'  # fixed uint64
        new_entry: 'bool'
        object_sub_entries: 'RepeatedCompositeFieldContainer[PersistableNotebookTracker.NotebookSubEntryData]'

    persistable_data: 'PersistableNotebookTracker'

    # __init__
    notebook_entries: 'RepeatedCompositeFieldContainer[PersistableNotebookTracker.NotebookEntryData]'
    notes: 'str'
    tooltip: 'str'
    loc_tooltip: 'LocalizedString'
    sub_entry_id: 'int'  # fixed uint64
    new_sub_entry: 'bool'
    object_recipe_id: 'int'  # fixed uint64
    object_entry_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    tuning_reference_id: 'int'  # fixed uint64
    new_entry: 'bool'
    object_sub_entries: 'RepeatedCompositeFieldContainer[PersistableNotebookTracker.NotebookSubEntryData]'


class PersistableRetailComponent(Message):
    persistable_data: 'PersistableRetailComponent'

    # __init__
    cached_value: 'int'  # int32


class PersistablePortalLockingComponent(Message):
    persistable_data: 'PersistablePortalLockingComponent'

    # __init__
    lock_data: 'RepeatedCompositeFieldContainer[LockData]'


class PersistableParentToSimHeadComponent(Message):
    persistable_data: 'PersistableParentToSimHeadComponent'

    # __init__
    parent_sim_info_id: 'int'  # fixed uint64
    bone_hash: 'int'  # fixed uint64


class PersistableFutureStoryProgressionChapter(Message):
    # __init__
    index: 'int'  # uint32
    future_chapter: 'PersistableStoryProgressionChapter'


class PersistableStoryProgressionChapter(Message):
    # __init__
    type: 'int'  # uint64
    future_chapters: 'RepeatedCompositeFieldContainer[PersistableFutureStoryProgressionChapter]'
    action_data: 'bytes'
    completion_time: 'int'  # uint64


class PersistableStoryProgressionSavedParticipant(Message):
    # __init__
    participant_type: 'int'  # uint32
    participant_id: 'int'  # uint64
    participant_str: 'str'
    participant_loc_str: 'LocalizedString'


class PersistableStoryProgressionArc(Message):
    # __init__
    type: 'int'  # uint64
    current_chapter: 'PersistableStoryProgressionChapter'
    historical_chapters: 'RepeatedCompositeFieldContainer[PersistableStoryProgressionChapter]'
    saved_participants: 'RepeatedCompositeFieldContainer[PersistableStoryProgressionSavedParticipant]'


class PersistableStoryProgressionTracker(Message):
    persistable_data: 'PersistableStoryProgressionTracker'

    # __init__
    current_arcs: 'RepeatedCompositeFieldContainer[PersistableStoryProgressionArc]'
    historical_arcs: 'RepeatedCompositeFieldContainer[PersistableStoryProgressionArc]'


class PersistableStolenComponent(Message):
    persistable_data: 'PersistableStolenComponent'

    # __init__
    stolen_from_text: 'str'
    stolen_from_household_id: 'int'  # uint64
    stolen_from_career_guid: 'int'  # fixed uint64


class PersistableRankedStatisticTracker(Message):
    persistable_data: 'PersistableRankedStatisticTracker'

    # __init__
    ranked_statistics: 'RepeatedCompositeFieldContainer[RankedStatistic]'


class RankedStatistic(Message):
    # __init__
    name_hash: 'int'  # uint64
    value: 'float'  # float32
    rank_level: 'int'  # uint64
    highest_level: 'int'  # uint64
    time_of_last_value_change: 'int'  # uint64
    initial_loots_awarded: 'bool'
    inclusive_rank_threshold: 'bool'


class PersistableGameComponent(Message):
    persistable_data: 'PersistableGameComponent'

    # __init__
    high_score_sim_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    high_score: 'float'  # float32


class PersistableSicknessTracker(Message):
    class SicknessData():
        # __init__
        sickness: 'int'  # uint64
        symptoms_discovered: 'RepeatedCompositeFieldContainer[int]'  # uint64
        exams_performed: 'RepeatedCompositeFieldContainer[int]'  # uint64
        treatments_performed: 'RepeatedCompositeFieldContainer[int]'  # uint64
        treatments_ruled_out: 'RepeatedCompositeFieldContainer[int]'  # uint64
        is_discovered: 'bool'

    persistable_data: 'PersistableSicknessTracker'

    # __init__
    previous_sicknesses: 'RepeatedCompositeFieldContainer[int]'  # uint64
    current_sickness: 'PersistableSicknessTracker.SicknessData'
    sickness: 'int'  # uint64
    symptoms_discovered: 'RepeatedCompositeFieldContainer[int]'  # uint64
    exams_performed: 'RepeatedCompositeFieldContainer[int]'  # uint64
    treatments_performed: 'RepeatedCompositeFieldContainer[int]'  # uint64
    treatments_ruled_out: 'RepeatedCompositeFieldContainer[int]'  # uint64
    is_discovered: 'bool'


class PersistableRelicTracker(Message):
    persistable_data: 'PersistableRelicTracker'

    # __init__
    known_relics: 'RepeatedCompositeFieldContainer[int]'  # uint64


class PersistableLifestyleBrandTracker(Message):
    persistable_data: 'PersistableLifestyleBrandTracker'

    # __init__
    product: 'int'  # uint32
    target_market: 'int'  # uint32
    logo: 'ResourceKey'
    brand_name: 'str'
    days_active: 'int'  # uint64


class PersistableStoredObjectInfoComponent(Message):
    class StoredObjectData():
        # __init__
        stored_object_type: 'int'  # uint32
        object_definition_id: 'int'  # uint64
        custom_name: 'str'
        states: 'RepeatedCompositeFieldContainer[StateComponentState]'
        object_id: 'int'  # fixed uint64

    persistable_data: 'PersistableStoredObjectInfoComponent'

    # __init__
    object_definition_id: 'int'  # uint64
    custom_name: 'str'
    states: 'RepeatedCompositeFieldContainer[StateComponentState]'
    object_id: 'int'  # uint64
    stored_object_data: 'RepeatedCompositeFieldContainer[PersistableStoredObjectInfoComponent.StoredObjectData]'
    stored_object_type: 'int'  # uint32
    object_definition_id: 'int'  # uint64
    custom_name: 'str'
    states: 'RepeatedCompositeFieldContainer[StateComponentState]'
    object_id: 'int'  # fixed uint64


class PersistableStoredAudioComponent(Message):
    persistable_data: 'PersistableStoredAudioComponent'

    # __init__
    sound_resource: 'SoundResource'
    channel_values_int: 'int'  # uint32


class PersistableSituationSchedulerComponent(Message):
    persistable_data: 'PersistableSituationSchedulerComponent'

    # __init__
    situation_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64


class TravelDestinationComponent(Message):
    persistable_data: 'TravelDestinationComponent'

    # __init__
    zone_id: 'int'  # uint64


class MissionCreatedSituations(Message):
    # __init__
    zone_id: 'int'  # uint64
    situation_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64


class MissionObjectiveData(Message):
    # __init__
    objective_id: 'int'  # uint64
    state: 'int'  # uint32
    created_situations: 'RepeatedCompositeFieldContainer[MissionCreatedSituations]'


class CareerGigData(Message):
    # __init__
    gig_type: 'int'  # uint64
    gig_time: 'int'  # uint64
    cast_list: 'RepeatedCompositeFieldContainer[int]'  # uint64
    customer_sim_id: 'int'  # fixed uint64
    gig_attended: 'bool'
    mission_objective_data: 'RepeatedCompositeFieldContainer[MissionObjectiveData]'
    client_preferences: 'RepeatedCompositeFieldContainer[int]'  # uint64
    known_client_preferences: 'RepeatedCompositeFieldContainer[int]'  # uint64
    client_lot_id: 'int'  # uint64
    budget_spent: 'int'  # uint32
    gig_budget: 'int'  # uint32
    client_hh_name: 'str'


class CareerSmallBusinessData(Message):
    # __init__
    career_level: 'int'  # int32
    owner_id: 'int'  # uint64


class PersistableSuntanTracker(Message):
    persistable_data: 'PersistableSuntanTracker'

    # __init__
    tan_level: 'int'  # uint32
    outfit_part_data_list: 'RepeatedCompositeFieldContainer[PartData]'


class PersistableObjectClaimComponent(Message):
    persistable_data: 'PersistableObjectClaimComponent'

    # __init__
    requires_claiming: 'bool'


class CollegeCourseInfo(Message):
    # __init__
    course_slot: 'int'  # uint64
    course_data: 'int'  # uint64
    final_grade: 'int'  # int64
    known_grade: 'int'  # int64
    lectures: 'int'  # int64
    final_requirement_completed: 'bool'
    homework_cheated: 'int'  # int64
    initial_skill: 'float'  # float32


class AcceptedDegrees(Message):
    # __init__
    university_id: 'int'  # uint64
    degree_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64


class ScholarshipInfo(Message):
    # __init__
    scholarship_id: 'int'  # uint64
    remaining_evaluation_time: 'int'  # uint64


class ElectiveCoursesInfo(Message):
    # __init__
    university_id: 'int'  # uint64
    elective_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64


class PersistableDegreeTracker(Message):
    persistable_data: 'PersistableDegreeTracker'

    # __init__
    current_major: 'int'  # uint64
    current_university: 'int'  # uint64
    current_credits: 'int'  # int64
    total_gradepoints: 'float'  # float32
    total_courses: 'int'  # int64
    previous_majors: 'RepeatedCompositeFieldContainer[int]'  # uint64
    previous_courses: 'RepeatedCompositeFieldContainer[int]'  # uint64
    current_courses: 'RepeatedCompositeFieldContainer[CollegeCourseInfo]'
    accepted_degrees: 'RepeatedCompositeFieldContainer[AcceptedDegrees]'
    enrollment_status: 'int'  # int64
    end_of_term_time: 'int'  # uint64
    reenrollment_time: 'int'  # uint64
    start_term_alarm_time: 'int'  # uint64
    term_started_time: 'int'  # uint64
    kickout_reason: 'int'  # uint64
    kickout_destination_zone: 'int'  # uint64
    diploma_mail_time: 'int'  # uint64
    active_scholarships: 'RepeatedCompositeFieldContainer[int]'  # uint64
    accepted_scholarships: 'RepeatedCompositeFieldContainer[int]'  # uint64
    rejected_scholarships: 'RepeatedCompositeFieldContainer[int]'  # uint64
    pending_scholarships: 'RepeatedCompositeFieldContainer[ScholarshipInfo]'
    elective_timestamp: 'int'  # uint64
    elective_courses: 'RepeatedCompositeFieldContainer[ElectiveCoursesInfo]'
    show_reenrollment_dialog_on_spin_up: 'bool'


class OrganizationStatusInfo(Message):
    # __init__
    org_id: 'int'  # uint64
    membership_status: 'int'  # uint64


class OrganizationActiveTasks(Message):
    # __init__
    org_id: 'int'  # uint64
    active_tasks: 'RepeatedCompositeFieldContainer[TimedAspiration]'


class PersistableOrganizationTracker(Message):
    persistable_data: 'PersistableOrganizationTracker'

    # __init__
    org_status_map: 'RepeatedCompositeFieldContainer[OrganizationStatusInfo]'
    tasks_map: 'RepeatedCompositeFieldContainer[OrganizationActiveTasks]'
    unenrolled_org_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64


class FamiliarData(Message):
    # __init__
    familiar_uid: 'int'  # uint64
    familiar_type: 'int'  # uint32
    familiar_name: 'str'
    pet_familiar_id: 'int'  # uint64


class PersistableFamiliarTracker(Message):
    persistable_data: 'PersistableFamiliarTracker'

    # __init__
    active_familiar_uid: 'int'  # uint64
    familiars: 'RepeatedCompositeFieldContainer[FamiliarData]'


class FavoritesData(Message):
    # __init__
    favorite_type: 'int'  # uint32
    favorite_id: 'int'  # uint64
    favorite_def_id: 'int'  # uint64


class ItemStackFavoritesData(Message):
    # __init__
    key: 'int'  # uint64
    custom_key: 'int'  # uint64
    stack_scheme: 'int'  # uint32


class PersistableFavoritesTracker(Message):
    persistable_data: 'PersistableFavoritesTracker'

    # __init__
    favorites: 'RepeatedCompositeFieldContainer[FavoritesData]'
    stack_favorites: 'RepeatedCompositeFieldContainer[ItemStackFavoritesData]'


class PersistableScholarshipLetterComponent(Message):
    persistable_data: 'PersistableScholarshipLetterComponent'

    # __init__
    applicant_sim_id: 'int'  # uint64
    scholarship_id: 'int'  # uint64


class PersistableObjectLockingComponent(Message):
    persistable_data: 'PersistableObjectLockingComponent'

    # __init__
    lock_data: 'RepeatedCompositeFieldContainer[LockData]'


class PersistableFixupTracker(Message):
    persistable_data: 'PersistableFixupTracker'

    # __init__
    pending_fixups: 'RepeatedCompositeFieldContainer[int]'  # uint64


class AllowUtilityUsageData(Message):
    # __init__
    utility_enum: 'int'  # uint32
    allow_usage: 'bool'


class PersistableUtilitiesComponent(Message):
    persistable_data: 'PersistableUtilitiesComponent'

    # __init__
    allow_utility_usage_list: 'RepeatedCompositeFieldContainer[AllowUtilityUsageData]'


class PersistableStoredInfoComponent(Message):
    persistable_data: 'PersistableStoredInfoComponent'

    # __init__
    custom_data: 'bytes'


class PersistableObjectMarketplaceComponent(Message):
    persistable_data: 'PersistableObjectMarketplaceComponent'

    # __init__
    sale_price: 'int'  # uint32
    seller_sim_id: 'int'  # uint64
    buyer_name: 'str'
    expiration_timer_time: 'int'  # uint64
    sale_timer_time: 'int'  # uint64
    delivery_timer_time: 'int'  # uint64


class PersistableTraitStatisticTracker(Message):
    persistable_data: 'PersistableTraitStatisticTracker'

    # __init__
    trait_statistics: 'RepeatedCompositeFieldContainer[TraitStatistic]'
    time_to_next_periodic_test: 'int'  # uint64


class TraitStatistic(Message):
    # __init__
    trait_statistic_id: 'int'  # uint64
    value: 'float'  # float32
    state: 'int'  # uint32
    neglect_buff_index: 'int'  # uint32
    value_added: 'bool'
    max_daily_cap: 'float'  # float32
    min_daily_cap: 'float'  # float32


class PersistableModularObjectComponent(Message):
    persistable_data: 'PersistableModularObjectComponent'

    # __init__
    piece_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class PersistableStoredActorLocationComponent(Message):
    persistable_data: 'PersistableStoredActorLocationComponent'

    # __init__
    stored_location: 'StoredLocation'


class StoredLocation(Message):
    # __init__
    x: 'float'  # float32
    y: 'float'  # float32
    z: 'float'  # float32
    rot_x: 'float'  # float32
    rot_y: 'float'  # float32
    rot_z: 'float'  # float32
    rot_w: 'float'  # float32
    level: 'int'  # int32
    surface_type: 'int'  # uint32
    zone: 'int'  # uint64


class FishingData(Message):
    # __init__
    possible_fish_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class PersistableFishingLocationComponent(Message):
    persistable_data: 'PersistableFishingLocationComponent'

    # __init__
    fishing_data: 'FishingData'


class PersistableAnimalPreferenceComponent(Message):
    persistable_data: 'PersistableAnimalPreferenceComponent'

    # __init__
    preferences_data: 'AnimalPreferenceData'


class AnimalPreferenceData(Message):
    # __init__
    like_preferences: 'RepeatedCompositeFieldContainer[int]'  # uint32
    dislike_preferences: 'RepeatedCompositeFieldContainer[int]'  # uint32
    favorite_preference: 'int'  # uint32
    preference_knowledge: 'RepeatedCompositeFieldContainer[PreferenceKnowledge]'


class PreferenceKnowledge(Message):
    # __init__
    household_id: 'int'  # uint64
    unknown_tags: 'RepeatedCompositeFieldContainer[int]'  # uint32
    known_tags: 'RepeatedCompositeFieldContainer[int]'  # uint32
    general_timestamp: 'int'  # uint64
    category_timestamp: 'RepeatedCompositeFieldContainer[CategoryKnowledge]'


class CategoryKnowledge(Message):
    # __init__
    category_tag: 'int'  # uint32
    timestamp: 'int'  # uint64


class PersistableAnimalObjectComponent(Message):
    persistable_data: 'PersistableAnimalObjectComponent'

    # __init__
    assigned_home_id: 'int'  # uint64


class PersistableObjectFashionMarketplaceComponent(Message):
    persistable_data: 'PersistableObjectFashionMarketplaceComponent'

    # __init__
    sale_price: 'int'  # uint32
    seller_sim_id: 'int'  # uint64
    buyer_name: 'str'
    expiration_timer_time: 'int'  # uint64
    sale_timer_time: 'int'  # uint64
    delivery_timer_time: 'int'  # uint64


class PersistableBrandingIconComponent(Message):
    persistable_data: 'PersistableBrandingIconComponent'

    # __init__
    icon: 'ResourceKey'


class PersistableLunarEffectTracker(Message):
    persistable_data: 'PersistableLunarEffectTracker'

    # __init__
    applied_effects: 'RepeatedCompositeFieldContainer[AppliedLunarEffect]'


class AppliedLunarEffect(Message):
    # __init__
    lunar_effect_id: 'int'  # fixed uint64
    effect_start_time: 'int'  # uint64


class BodyPartCasPartObjectId(Message):
    # __init__
    body_part: 'int'  # uint32
    cas_part: 'int'  # uint32
    object_id: 'int'  # uint64
    outfit_category: 'int'  # uint32
    outfit_id: 'int'  # uint64


class PersistableJewelryTracker(Message):
    persistable_data: 'PersistableJewelryTracker'

    # __init__
    cas_part_object_id_map: 'RepeatedCompositeFieldContainer[BodyPartCasPartObjectId]'


class PersistableJewelryComponent(Message):
    persistable_data: 'PersistableJewelryComponent'

    # __init__
    current_body_part: 'int'  # uint32
    current_cas_part: 'int'  # uint32
    buff_handle: 'int'  # uint64
    sim_id: 'int'  # fixed uint64


class PersistableChargeableComponent(Message):
    persistable_data: 'PersistableChargeableComponent'

    # __init__
    has_been_charged: 'bool'


class PersistableHeirloomComponent(Message):
    persistable_data: 'PersistableHeirloomComponent'

    # __init__
    creator_sim_id: 'int'  # fixed uint64
    creator_sim_info_name_data: 'SimInfoNameData'
    engraved_message: 'str'


class FamilyRecipe(Message):
    # __init__
    recipe_id: 'int'  # uint64
    recipe_name: 'str'
    ingredient_id: 'int'  # uint64
    buff_id: 'int'  # uint64
    recipe_owner: 'str'


class PersistableFamilyRecipesTracker(Message):
    persistable_data: 'PersistableFamilyRecipesTracker'

    # __init__
    family_recipes: 'RepeatedCompositeFieldContainer[FamilyRecipe]'
    initial_loot_applied: 'bool'


class TattooData(Message):
    # __init__
    body_type: 'int'  # uint32
    quality: 'int'  # uint32
    body_part_hash: 'int'  # uint32
    sentimental_type: 'int'  # uint32
    sentimental_target: 'int'  # uint64
    body_part_hashes: 'RepeatedCompositeFieldContainer[int]'  # uint64
    body_part_custom_texture: 'int'  # uint64
    occult_type: 'int'  # uint32


class PersistableTattooTracker(Message):
    persistable_data: 'PersistableTattooTracker'

    # __init__
    body_type_tattoo_data: 'RepeatedCompositeFieldContainer[TattooData]'
    pending_tattoo_data: 'TattooData'
    stored_picked_tattoo: 'int'  # uint64
