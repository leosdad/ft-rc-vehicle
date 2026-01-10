"""Minimal Motor stub for editor/type-checking.

Provides direction constants and no-op control methods.
"""


class Motor:
    """Basic Motor: direction constants and no-op methods."""

    CW = 0
    CCW = 1

    def __init__(self, *args, **kwargs):
        """Create stub instance."""
        pass

    def set_speed(self, speed, direction=0):
        """Set motor speed (no-op)."""
        return None

    def start(self):
        """Start motor (no-op)."""
        return None

    def stop(self):
        """Stop motor (no-op)."""
        return None
