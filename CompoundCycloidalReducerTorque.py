def calculate_dynamic_torques(motor_torque: float, first_stage_reduction_ratio: int, second_stage_reduction_ratio: int):
    """Calculates torques in a two-stage cycloidal speed reducer.

    Note: This calculation is a simplified model and does not account for real-world
          factors like friction losses, which would reduce the actual output torque.

    Args:
        motor_torque (float): Input torque in Newton-meters (Nm).
        first_stage_reduction_ratio (int): Reduction ratio of the first stage.
        second_stage_reduction_ratio (int): Reduction ratio of the second stage.

    Returns:
        dict: A dictionary containing the calculated torques (in Nm):
            - First stage drive torque
            - First stage ring gear torque
            - First stage disc torque
            - Second stage disc torque
            - Second stage ring gear torque (The final output torque in this system)
            - Second stage cycloid disc torque 
    """
    # Torque calculations (These are placeholders and would need to be replaced with the appropriate equations)
    first_stage_drive_torque = motor_torque / (first_stage_reduction_ratio + 1)
    first_stage_ring_gear_torque = motor_torque - first_stage_drive_torque 
    first_stage_disc_torque = -motor_torque * first_stage_reduction_ratio / (1 + first_stage_reduction_ratio)

    second_stage_disc_torque = first_stage_drive_torque  / (second_stage_reduction_ratio + 1)
    second_stage_ring_gear_torque = first_stage_drive_torque * second_stage_reduction_ratio
    second_stage_cycloid_disc_torque = -second_stage_disc_torque * second_stage_reduction_ratio 

    return {
        "First stage drive torque": first_stage_drive_torque,
        "First stage ring gear torque": first_stage_ring_gear_torque,
        "First stage disc torque": first_stage_disc_torque,
        "Second stage disc torque": second_stage_disc_torque,
        "Second stage ring gear torque (The final output torque in this system)": second_stage_ring_gear_torque,
        "Second stage cycloid disc torque": second_stage_cycloid_disc_torque,
    }

# Example usage:
motor_torque = 0.40  # Nm (example using 40 cmN (.4NM) Nema 17 Stepper 17HE19-2004S @ 24V, 2.2A, 1600 Microstep, 100 RPM, 100 kHz pwm )
first_stage_reduction_ratio = 8
second_stage_reduction_ratio = 7

torques = calculate_dynamic_torques(motor_torque, first_stage_reduction_ratio, second_stage_reduction_ratio)

for key, value in torques.items():
    print(f"{key}: {value:.2f} Nm")
