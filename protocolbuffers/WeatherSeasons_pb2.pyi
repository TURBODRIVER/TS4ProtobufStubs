from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer
from enum import IntEnum

from protocolbuffers.ResourceKey_pb2 import *
from protocolbuffers.Localization_pb2 import *
from protocolbuffers.Lot_pb2 import *


class SeasonWeatherInterpolationMessage(Message):
    class SeasonWeatherInterpolatedType(IntEnum):
        SEASON: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 0
        LEAF_ACCUMULATION: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 1
        FLOWER_GROWTH: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 2
        FOLIAGE_REDUCTION: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 3
        FOLIAGE_COLORSHIFT: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 4
        RAINFALL: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 1000
        SNOWFALL: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 1001
        RAIN_ACCUMULATION: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 1002
        SNOW_ACCUMULATION: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 1003
        WINDOW_FROST: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 1004
        WATER_FROZEN: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 1005
        WIND: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 1006
        TEMPERATURE: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 1007
        THUNDER: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 1008
        LIGHTNING: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 1009
        SNOW_FRESHNESS: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 1010
        STORY_ACT: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 1011
        ECO_FOOTPRINT: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 1012
        ACID_RAIN: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 1013
        STARWARS_RESISTANCE: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 1014
        STARWARS_FIRST_ORDER: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 1015
        SNOW_ICINESS: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 1016
        SKYBOX_PARTLY_CLOUDY: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 2000
        SKYBOX_CLEAR: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 2001
        SKYBOX_LIGHTRAINCLOUDS: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 2002
        SKYBOX_DARKRAINCLOUDS: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 2003
        SKYBOX_LIGHTSNOWCLOUDS: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 2004
        SKYBOX_DARKSNOWCLOUDS: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 2005
        SKYBOX_CLOUDY: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 2006
        SKYBOX_HEATWAVE: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 2007
        SKYBOX_STRANGE: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 2008
        SKYBOX_VERYSTRANGE: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 2009
        SKYBOX_INDUSTRIAL: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType' = 2010

    SEASON = SeasonWeatherInterpolatedType.SEASON
    LEAF_ACCUMULATION = SeasonWeatherInterpolatedType.LEAF_ACCUMULATION
    FLOWER_GROWTH = SeasonWeatherInterpolatedType.FLOWER_GROWTH
    FOLIAGE_REDUCTION = SeasonWeatherInterpolatedType.FOLIAGE_REDUCTION
    FOLIAGE_COLORSHIFT = SeasonWeatherInterpolatedType.FOLIAGE_COLORSHIFT
    RAINFALL = SeasonWeatherInterpolatedType.RAINFALL
    SNOWFALL = SeasonWeatherInterpolatedType.SNOWFALL
    RAIN_ACCUMULATION = SeasonWeatherInterpolatedType.RAIN_ACCUMULATION
    SNOW_ACCUMULATION = SeasonWeatherInterpolatedType.SNOW_ACCUMULATION
    WINDOW_FROST = SeasonWeatherInterpolatedType.WINDOW_FROST
    WATER_FROZEN = SeasonWeatherInterpolatedType.WATER_FROZEN
    WIND = SeasonWeatherInterpolatedType.WIND
    TEMPERATURE = SeasonWeatherInterpolatedType.TEMPERATURE
    THUNDER = SeasonWeatherInterpolatedType.THUNDER
    LIGHTNING = SeasonWeatherInterpolatedType.LIGHTNING
    SNOW_FRESHNESS = SeasonWeatherInterpolatedType.SNOW_FRESHNESS
    STORY_ACT = SeasonWeatherInterpolatedType.STORY_ACT
    ECO_FOOTPRINT = SeasonWeatherInterpolatedType.ECO_FOOTPRINT
    ACID_RAIN = SeasonWeatherInterpolatedType.ACID_RAIN
    STARWARS_RESISTANCE = SeasonWeatherInterpolatedType.STARWARS_RESISTANCE
    STARWARS_FIRST_ORDER = SeasonWeatherInterpolatedType.STARWARS_FIRST_ORDER
    SNOW_ICINESS = SeasonWeatherInterpolatedType.SNOW_ICINESS
    SKYBOX_PARTLY_CLOUDY = SeasonWeatherInterpolatedType.SKYBOX_PARTLY_CLOUDY
    SKYBOX_CLEAR = SeasonWeatherInterpolatedType.SKYBOX_CLEAR
    SKYBOX_LIGHTRAINCLOUDS = SeasonWeatherInterpolatedType.SKYBOX_LIGHTRAINCLOUDS
    SKYBOX_DARKRAINCLOUDS = SeasonWeatherInterpolatedType.SKYBOX_DARKRAINCLOUDS
    SKYBOX_LIGHTSNOWCLOUDS = SeasonWeatherInterpolatedType.SKYBOX_LIGHTSNOWCLOUDS
    SKYBOX_DARKSNOWCLOUDS = SeasonWeatherInterpolatedType.SKYBOX_DARKSNOWCLOUDS
    SKYBOX_CLOUDY = SeasonWeatherInterpolatedType.SKYBOX_CLOUDY
    SKYBOX_HEATWAVE = SeasonWeatherInterpolatedType.SKYBOX_HEATWAVE
    SKYBOX_STRANGE = SeasonWeatherInterpolatedType.SKYBOX_STRANGE
    SKYBOX_VERYSTRANGE = SeasonWeatherInterpolatedType.SKYBOX_VERYSTRANGE
    SKYBOX_INDUSTRIAL = SeasonWeatherInterpolatedType.SKYBOX_INDUSTRIAL

    # __init__
    message_type: 'SeasonWeatherInterpolationMessage.SeasonWeatherInterpolatedType'
    start_value: 'float'  # float32
    start_time: 'int'  # uint64
    end_value: 'float'  # float32
    end_time: 'int'  # uint64


class SeasonWeatherInterpolations(Message):
    # __init__
    season_weather_interlops: 'RepeatedCompositeFieldContainer[SeasonWeatherInterpolationMessage]'


class RegionWeather(Message):
    # __init__
    region: 'int'  # fixed uint64
    weather: 'SeasonWeatherInterpolations'
    weather_event: 'int'  # fixed uint64
    forecast_time_stamp: 'int'  # uint64
    next_weather_event_time: 'int'  # uint64
    forecasts: 'RepeatedCompositeFieldContainer[int]'  # uint64
    override_forecast: 'int'  # uint64
    override_forecast_season_stamp: 'int'  # uint64


class PersistableWeatherService(Message):
    # __init__
    region_weathers: 'RepeatedCompositeFieldContainer[RegionWeather]'


class UiWeatherUpdate(Message):
    # __init__
    weather_type_enums: 'RepeatedCompositeFieldContainer[int]'  # int64


class UiWeatherForecastUpdate(Message):
    # __init__
    forecast_instance_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64


class MoonPhaseUpdate(Message):
    class MoonPhase(IntEnum):
        NEW_MOON: 'MoonPhaseUpdate.MoonPhase' = 0
        WAXING_CRESCENT: 'MoonPhaseUpdate.MoonPhase' = 1
        FIRST_QUARTER: 'MoonPhaseUpdate.MoonPhase' = 2
        WAXING_GIBBOUS: 'MoonPhaseUpdate.MoonPhase' = 3
        FULL_MOON: 'MoonPhaseUpdate.MoonPhase' = 4
        WANING_GIBBOUS: 'MoonPhaseUpdate.MoonPhase' = 5
        THIRD_QUARTER: 'MoonPhaseUpdate.MoonPhase' = 6
        WANING_CRESCENT: 'MoonPhaseUpdate.MoonPhase' = 7

    NEW_MOON = MoonPhase.NEW_MOON
    WAXING_CRESCENT = MoonPhase.WAXING_CRESCENT
    FIRST_QUARTER = MoonPhase.FIRST_QUARTER
    WAXING_GIBBOUS = MoonPhase.WAXING_GIBBOUS
    FULL_MOON = MoonPhase.FULL_MOON
    WANING_GIBBOUS = MoonPhase.WANING_GIBBOUS
    THIRD_QUARTER = MoonPhase.THIRD_QUARTER
    WANING_CRESCENT = MoonPhase.WANING_CRESCENT

    # __init__
    current_moon_phase: 'MoonPhaseUpdate.MoonPhase'
    skip_environment_changes: 'bool'


class UiLunarEffectTooltipUpdate(Message):
    # __init__
    current_moon_phase: 'int'  # uint32
    tooltip_text: 'LocalizedString'


class MoonForecastUpdate(Message):
    class MoonPhase(IntEnum):
        NEW_MOON: 'MoonForecastUpdate.MoonPhase' = 0
        WAXING_CRESCENT: 'MoonForecastUpdate.MoonPhase' = 1
        FIRST_QUARTER: 'MoonForecastUpdate.MoonPhase' = 2
        WAXING_GIBBOUS: 'MoonForecastUpdate.MoonPhase' = 3
        FULL_MOON: 'MoonForecastUpdate.MoonPhase' = 4
        WANING_GIBBOUS: 'MoonForecastUpdate.MoonPhase' = 5
        THIRD_QUARTER: 'MoonForecastUpdate.MoonPhase' = 6
        WANING_CRESCENT: 'MoonForecastUpdate.MoonPhase' = 7

    NEW_MOON = MoonPhase.NEW_MOON
    WAXING_CRESCENT = MoonPhase.WAXING_CRESCENT
    FIRST_QUARTER = MoonPhase.FIRST_QUARTER
    WAXING_GIBBOUS = MoonPhase.WAXING_GIBBOUS
    FULL_MOON = MoonPhase.FULL_MOON
    WANING_GIBBOUS = MoonPhase.WANING_GIBBOUS
    THIRD_QUARTER = MoonPhase.THIRD_QUARTER
    WANING_CRESCENT = MoonPhase.WANING_CRESCENT

    # __init__
    forecast_moon_phases: 'RepeatedCompositeFieldContainer[MoonForecastUpdate.MoonPhase]'
