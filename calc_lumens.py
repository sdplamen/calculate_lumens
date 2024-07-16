# Lux (lx) measures the amount of light that falls on a surface area.
# Lumens (lm) measure the total amount of visible light emitted by a source.
# The formula for calculating lumens per square meter is:
# Lumens per square meter = Lux × area in square meters
# lux = lumen / m2
# Luminous intensity [cd] = luminous flux [lm] / solid angle [sr]
# Illuminance Lux [lx] = luminous flux [lm] / area [m2]

def calculate_lumens(lux, area_m2):
    ranges = []
    for area_m2, lux in lux_range.items():
        if lux == lux_range[lux]:
            ranges.append(lux_range)
def lookup_lux(lux, area_m2, lux_range):
    lumens = calculate_lumens(lux, area_m2)
    for lux_range_key, space_type in lux_range.items():
        min_lux, max_lux = lux_range_key
        min_lumens = min_lux * area_m2
        max_lumens = max_lux * area_m2
        if min_lumens <= lumens <= max_lumens:
            return space_type
    return 'Unknown space type'

lux_range = {# Residential and Living Spaces:
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

lux = input('Type of lux category space - general living, kitchen, reading, general office, detailed office, classroom, warehouse, library, detailed_mechanical, retail,  overcast_day, full_daylight : ')  # Lux value
area_m2 = int(input('Type area value : '))

result = lookup_lux(lux, area_m2, lux_range)

if result:
    print(f'For the category {lux_range.values()} and area {area_m2} square meters, the lumen range is {result[0]} to {result[1]} lumens.')
else:
    print(f'Type error ! Lux value is not in the list of "{lux}"')

# Calculates total lumen level in a room