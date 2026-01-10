"""Small math helpers used by the RC project (editor stubs)."""

from typing import Union

Number = Union[int, float]


def map(x: Number, in_min: Number, in_max: Number, out_min: Number, out_max: Number) -> Number:
    """Map value `x` from one range to another (stub)."""
    return out_min


__all__ = ["map"]
