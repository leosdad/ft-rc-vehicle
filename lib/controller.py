"""
Initializes the controller and its components.
"""

import fischertechnik.factories as txt_factory

# Initialize the TXT controller and its components
txt_factory.init()
txt_factory.init_input_factory()
txt_factory.init_output_factory()
txt_factory.init_motor_factory()
txt_factory.init_servomotor_factory()

# Create the graphical controller
TXT_M = txt_factory.controller_factory.create_graphical_controller()

# Create inputs and outputs
rumble_switch = txt_factory.input_factory.create_mini_switch(TXT_M, 1)
headlights_led = txt_factory.output_factory.create_led(TXT_M, 7)
reverse_led = txt_factory.output_factory.create_led(TXT_M, 8)
taillights_led = txt_factory.output_factory.create_led(TXT_M, 5)
horn_buzzer = txt_factory.output_factory.create_magnetic_valve(TXT_M, 6)
drive_motor = txt_factory.motor_factory.create_motor(TXT_M, 1)
steer_servo = txt_factory.servomotor_factory.create_servomotor(TXT_M, 1)

# Finalize initialization
txt_factory.initialized()
