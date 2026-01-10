import fischertechnik.factories as txt_factory

txt_factory.init()
txt_factory.init_input_factory()
txt_factory.init_output_factory()
txt_factory.init_motor_factory()
txt_factory.init_servomotor_factory()


# Headlights
# Reverse light
# Taillights
# Horn (buzzer)
TXT_M = txt_factory.controller_factory.create_graphical_controller()

TXT_M_I1_mini_switch = txt_factory.input_factory.create_mini_switch(TXT_M, 1)
TXT_M_O7_led = txt_factory.output_factory.create_led(TXT_M, 7)
TXT_M_O8_led = txt_factory.output_factory.create_led(TXT_M, 8)
TXT_M_O5_led = txt_factory.output_factory.create_led(TXT_M, 5)
TXT_M_O6_buzzer = txt_factory.output_factory.create_magnetic_valve(TXT_M, 6)
TXT_M_M1_motor = txt_factory.motor_factory.create_motor(TXT_M, 1)
TXT_M_S1_servomotor = txt_factory.servomotor_factory.create_servomotor(TXT_M, 1)

txt_factory.initialized()