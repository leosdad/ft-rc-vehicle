"""The content of this package depends on the local controller.
If you execute the source code on a Txt controller,
then this python file creates factories to instanciate
controller, sensors and actors for the the Txt controller.
"""
import ft
import ftlock
import atexit
import signal
import sys

from ..utility.txt_state import TxtState

controller_factory = None
camera_factory = None
usb_factory = None
counter_factory = None
input_factory = None
output_factory = None
motor_factory = None
i2c_factory = None
servomotor_factory = None

api_model = 2

def exception_handler(exception_type, exception, traceback):
    # print("{}: {}".format(exception_type.__name__, exception))
    sys.__excepthook__(exception_type, exception, traceback)

sys.excepthook = exception_handler

def init():
    """Lock process, notify INIT state, and init controller factory."""
    ftlock.lock(sys.argv[0])
    ftlock.notify(TxtState.INIT.value)
    init_controller_factory()

def initialized():
    """Lock process and notify RUNNING state."""
    ftlock.lock(sys.argv[0])
    ftlock.notify(TxtState.RUNNING.value)

def onDestroy():
    """Notify FINALIZING if lock held, then unlock on exit."""
    if ftlock.try_lock(sys.argv[0]) == 0:
        ftlock.notify(TxtState.FINALIZING.value)
    ftlock.unlock()

atexit.register(onDestroy)

def onSignal(*args):
    """Exit cleanly on termination signal."""
    sys.exit()

try:
    signal.signal(signal.SIGTERM, onSignal)
except ValueError:
    pass

def init_controller_factory():
    """Instantiate the Txt4 controller factory."""
    global controller_factory
    from ..controller.txt4.Txt4ControllerFactory import Txt4ControllerFactory
    controller_factory = Txt4ControllerFactory()


def init_usb_factory():
    """Instantiate the Txt4 USB factory."""
    global usb_factory
    from ..controller.txt4.Txt4USBFactory import Txt4USBFactory
    usb_factory = Txt4USBFactory()


def init_camera_factory():
    """Instantiate the camera factory."""
    global camera_factory
    from ..camera.CameraFactory import CameraFactory
    camera_factory = CameraFactory()


def init_counter_factory():
    """Instantiate the Txt4 counter factory."""
    global counter_factory
    from ..controller.txt4.Txt4CounterFactory import Txt4CounterFactory
    counter_factory = Txt4CounterFactory()


def init_input_factory():
    """Instantiate the Txt4 input factory."""
    global input_factory
    from ..controller.txt4.Txt4InputFactory import Txt4InputFactory
    input_factory = Txt4InputFactory()


def init_motor_factory():
    """Instantiate the Txt4 motor factory."""
    global motor_factory
    from ..controller.txt4.Txt4MotorFactory import Txt4MotorFactory
    motor_factory = Txt4MotorFactory()


def init_output_factory():
    """Instantiate the Txt4 output factory."""
    global output_factory
    from ..controller.txt4.Txt4OutputFactory import Txt4OutputFactory
    output_factory = Txt4OutputFactory()


def init_i2c_factory():
    """Instantiate the Txt4 I2C factory."""
    global i2c_factory
    from ..controller.txt4.Txt4I2CFactory import Txt4I2CFactory
    i2c_factory = Txt4I2CFactory()


def init_servomotor_factory():
    """Instantiate the Txt4 servomotor factory."""
    global servomotor_factory
    from ..controller.txt4.Txt4ServomotorFactory import Txt4ServomotorFactory
    servomotor_factory = Txt4ServomotorFactory()
