"""stub of `fischertechnik.factories` for editor/type-checking."""

from typing import Any


class Controller:
    """Represents a generic controller (placeholder)."""
    def __repr__(self) -> str:  # pragma: no cover - trivial
        """Return a string representation."""
        return "Controller()"


class MiniSwitch:
    """Placeholder for a mini switch input."""


class LED:
    """Placeholder for an LED output."""


class MagneticValve:
    """Placeholder for a buzzer/magnetic valve output."""


class Motor:
    """Placeholder for a motor object."""


class Servomotor:
    """Placeholder for a servomotor object."""


class ControllerFactory:
    """Factory to create controller instances."""

    def create_graphical_controller(self) -> Controller:
        """Return a lightweight Controller placeholder."""
        return Controller()


class InputFactory:
    """Factory to create input objects (switches, sensors)."""

    def create_mini_switch(self, controller: Controller, port: int) -> MiniSwitch:
        """Create a mini switch bound to `controller` and `port`.

        Parameters are present to match the real API surface so editors
        and type checkers can infer call signatures.
        """
        return MiniSwitch()


class OutputFactory:
    """Factory to create output devices (LEDs, buzzers, valves)."""

    def create_led(self, controller: Controller, port: int) -> LED:
        """Create an LED output placeholder."""
        return LED()

    def create_magnetic_valve(self, controller: Controller, port: int) -> MagneticValve:
        """Create a magnetic valve / buzzer placeholder."""
        return MagneticValve()


class MotorFactory:
    """Factory to create motor objects."""

    def create_motor(self, controller: Controller, port: int) -> Motor:
        """Create a Motor placeholder."""
        return Motor()


class ServomotorFactory:
    """Factory to create servomotors."""

    def create_servomotor(self, controller: Controller, port: int) -> Servomotor:
        """Create a Servomotor placeholder."""
        return Servomotor()


# Module-level factory instances (mirror the real library's shape)
controller_factory = ControllerFactory()
input_factory = InputFactory()
output_factory = OutputFactory()
motor_factory = MotorFactory()
servomotor_factory = ServomotorFactory()


def init() -> None:
    """Initialize the (stub) library. No-op for editor usage."""
    return None


def init_input_factory() -> None:
    """No-op placeholder to match real API."""
    return None


def init_output_factory() -> None:
    """No-op placeholder to match real API."""
    return None


def init_motor_factory() -> None:
    """No-op placeholder to match real API."""
    return None


def init_servomotor_factory() -> None:
    """No-op placeholder to match real API."""
    return None


def initialized() -> None:
    """Signal that initialization completed (stub)."""
    return None


__all__ = [
    "init",
    "init_input_factory",
    "init_output_factory",
    "init_motor_factory",
    "init_servomotor_factory",
    "initialized",
    "controller_factory",
    "input_factory",
    "output_factory",
    "motor_factory",
    "servomotor_factory",
]
