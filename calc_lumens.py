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
    for (min_lux, max_lux), space_room in lux_range.items():
        if space_room == space_type:
            return (min_lux, max_lux)
    return None


lux_range = {
    # Residential and Living Spaces:
    (100, 300): 'general living',
    (300, 750): 'kitchen',
    (500, 800): 'reading',

    # Office Spaces:
    (300, 500): 'general office',
    (500, 1000): 'detailed office',

    # Educational and Learning Environments:
    (300, 500): 'classroom',
    (500, 800): 'library',

    # Industrial and Commercial Settings:
    (200, 300): 'warehouse',
    (500, 1000): 'detailed mechanical',
    (750, 1500): 'retail',

    # Outdoor Areas:
    (1000, 2000): 'overcast_day',
    (10000, 25000): 'full daylight'
}

space_type = input('Type of lux category space - \
general living, kitchen, reading, general office, detailed office,\
classroom, warehouse, library, detailed_mechanical, retail, \
overcast_day, full_daylight : ')
area_m2 = float(input('Type area value : '))

lumens, condition = calculate_lumens(space_type, area_m2, lux_range)

if lumens:
    print(f'For the space type {condition}:\nMinimum lumens: {lumens[0]} Maximum lumens: {lumens[1]}')
else:
    print(f'Type error ! Lux value is not in the list of "{condition}"')

# Calculates total lumen level in a room
