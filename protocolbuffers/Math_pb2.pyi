from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer


class Vector2(Message):
    # __init__
    x: 'float'  # float32
    y: 'float'  # float32


class Vector3(Message):
    # __init__
    x: 'float'  # float32
    y: 'float'  # float32
    z: 'float'  # float32


class Quaternion(Message):
    # __init__
    x: 'float'  # float32
    y: 'float'  # float32
    z: 'float'  # float32
    w: 'float'  # float32


class Transform(Message):
    # __init__
    translation: 'Vector3'
    orientation: 'Quaternion'


class LinearCurve(Message):
    class CurvePoint():
        # __init__
        x: 'float'  # float32
        y: 'float'  # float32

    # __init__
    points: 'RepeatedCompositeFieldContainer[LinearCurve.CurvePoint]'
    x: 'float'  # float32
    y: 'float'  # float32
