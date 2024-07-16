# Lux (lx) measures the amount of light that falls on a surface area.
# Lumens (lm) measure the total amount of visible light emitted by a source.
# The formula for calculating lumens per square meter is:
# Lumens per square meter = Lux × area in square meters
# lux = lumen / m2
# Luminous intensity [cd] = luminous flux [lm] / solid angle [sr]
# Illuminance Lux [lx] = luminous flux [lm] / area [m2]

def calculate_lumens(space_type, area, lux_range):
    lux_values = lookup_lux(space_type, lux_range)
    if lux_values is None:
        return None

    min_lux, max_lux = lux_values
    min_lumens = min_lux * area
    max_lumens = max_lux * area

    return (min_lumens, max_lumens), space_type


def lookup_lux(space_type, lux_range):
    for space_room, (min_lux, max_lux) in lux_range.items():
        if space_room == space_type:
            return (min_lux, max_lux)
    return None


lux_range = {
    # Residential and Living Spaces:
    'general living': (100, 300),
    'kitchen': (300, 750),
    'reading': (500, 800),
    'bathrooms': (500, 800),

    # Office Spaces:
    'general office': (300, 500),
    'detailed office': (500, 1000),

    # Educational and Learning Environments:
    'classroom': (300, 500),
    'library': (500, 800),

    # Industrial and Commercial Settings:
    'warehouse': (200, 300),
    'workshops - detailed mechanical': (500, 1000),
    'retail space': (750, 1500),

    # Outdoor Areas:
    'overcast day': (1000, 2000),
    'full daylight': (10000, 25000)
}

space_type = input('Type of lux category space - \n\
general living, kitchen, reading, bathrooms, general office, detailed office, classroom,\n\
warehouse, library, workshops - detailed mechanical, retail, overcast day, full daylight : \n')
area_m2 = float(input('Type area value : '))

lumens, space_room = calculate_lumens(space_type, area_m2, lux_range)

if lumens:
    print(f'For the space type "{space_room}" :\nMinimum lumens - {int(lumens[0])}\nMaximum lumens - {int(lumens[1])}')
else:
    print(f'Type error ! Lux value is not in the list of "{space_room}"')