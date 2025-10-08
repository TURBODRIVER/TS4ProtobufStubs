from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer


class CalendarFavoriteData(Message):
    # __init__
    household_id: 'int'  # fixed uint64
    favorited_event_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class PersistableCalendarService(Message):
    # __init__
    favorite_data: 'RepeatedCompositeFieldContainer[CalendarFavoriteData]'
