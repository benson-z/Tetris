from enum import Enum

class State(Enum):
    T = (128, 0, 128)
    I = (0, 128, 128)
    L = (0, 0, 255)
    J = (255, 165, 0)
    S = (0, 128, 0)
    Z = (255, 0, 0)
    O = (225, 225, 0)
    NONE = (0, 0, 0)
    EMPTY = (0, 0, 0)


def toState(str):
    match str:
        case 'T':
            return State.T
        case 'I':
            return State.I
        case 'O':
            return State.O
        case 'L':
            return State.L
        case 'J':
            return State.J
        case 'Z':
            return State.Z
        case 'S':
            return State.S