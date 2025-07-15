def sort(width, height, length, mass):
    """
    Determines how a robotic arm should dispatch a package based on its dimensions and mass.

    Parameters:
    - width (int): width in cm
    - height (int): height in cm
    - length (int): length in cm
    - mass (int or float): mass in kg

    Returns:
    - str: 'STANDARD', 'SPECIAL', or 'REJECTED'
    """

    volume = width * height * length
    is_bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
