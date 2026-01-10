"""Small math helpers used by the RC project (editor stubs).

Provides a `map` function compatible with the project's usage in
`lib/Math_lib.py`.
"""

from typing import Union

Number = Union[int, float]


def map(x: Number, in_min: Number, in_max: Number, out_min: Number, out_max: Number) -> Number:
    """Map value `x` from one range to another.

    Behaves like Arduino's `map` but returns a float when inputs are
    non-integer; clamps output to the `out_min`/`out_max` interval.
    """
    if in_max == in_min:
        raise ValueError("in_min and in_max cannot be equal")

    # Linear mapping
    ratio = (x - in_min) / (in_max - in_min)
    out = out_min + ratio * (out_max - out_min)

    # Clamp
    if out_min <= out_max:
        return max(out_min, min(out_max, out))
    else:
        return max(out_max, min(out_min, out))


__all__ = ["map"]
