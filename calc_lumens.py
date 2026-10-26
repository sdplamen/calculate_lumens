def calculate_lumens(space_type, area, lux_range) :
    if not isinstance(area, (int, float)) or area <= 0 :
        return None, None, space_type, 'Area must be a positive number.'

    space_type_lower = space_type.lower().strip()
    for key in lux_range :
        if key.lower() == space_type_lower :
            min_lux, max_lux = lux_range[key]
            min_lumens = min_lux * area
            max_lumens = max_lux * area
            avg_lumens = (min_lumens + max_lumens) / 2
            return (min_lumens, max_lumens, avg_lumens), key, None

    return None, None, space_type, f"Space type '{space_type}' not found."

lux_range = {
    # Residential and Living Spaces
    'general living': (100, 300),  # Living rooms, casual spaces
    'kitchen': (300, 750),  # General kitchen lighting
    'kitchen task': (500, 1000),  # Task areas (e.g., countertops)
    'reading': (500, 800),  # Reading or study areas
    'bathroom': (200, 500),  # General bathroom lighting
    'bathroom task': (500, 800),  # Task areas (e.g., mirrors)

    # Office Spaces
    'general office': (300, 500),  # General office work
    'detailed office': (500, 1000),  # Detailed tasks (e.g., drafting)
    'conference room': (300, 500),  # Meetings and presentations

    # Educational and Learning Environments
    'classroom': (300, 500),  # General classroom lighting
    'library': (500, 800),  # Reading and study areas
    'laboratory': (500, 1000),  # Science labs or technical work

    # Industrial and Commercial Settings
    'warehouse': (100, 300),  # General storage areas
    'workshop': (500, 1000),  # Detailed mechanical work
    'retail space': (500, 1500),  # Retail displays and sales areas
    'supermarket': (750, 1000),  # Grocery stores

    # Healthcare Settings
    'hospital general': (100, 300),  # Waiting areas, corridors
    'hospital exam room': (500, 1000),  # Examination rooms

    # Outdoor Areas
    'overcast day': (1000, 2000),  # Outdoor lighting (overcast)
    'full daylight': (10000, 25000),  # Bright daylight conditions
    'parking lot': (20, 50),  # Outdoor parking areas
}


def main():
    print('Available space types:', ', '.join(lux_range.keys()))
    space_type = input('Enter the type of space: ')

    try:
        area_m2 = float(input('Enter area in square meters: '))
    except ValueError:
        print('Error: Please enter a valid number for the area.')
        return

    lumens, matched_space, error = calculate_lumens(space_type, area_m2, lux_range)

    if error:
        print(error)
        return

    min_lumens, max_lumens, avg_lumens = lumens
    min_lux, max_lux = lux_range[matched_space]

    print(f"For the space type '{matched_space}' (Area: {area_m2} m²):\n"
          f"Lux range: {min_lux} - {max_lux} lux\n"
          f"Minimum lumens required: {int(min_lumens)}\n"
          f"Maximum lumens required: {int(max_lumens)}\n"
          f"Recommended average lumens: {int(avg_lumens)}")


if __name__ == "__main__" :
    main()