from django import forms

LUX_RANGE = {
    # Residential and Living Spaces
    'general living' :(100, 300),  # Living rooms, casual spaces
    'kitchen' :(300, 750),  # General kitchen lighting
    'kitchen task' :(500, 1000),  # Task areas (e.g., countertops)
    'reading' :(500, 800),  # Reading or study areas
    'bathroom' :(200, 500),  # General bathroom lighting
    'bathroom task' :(500, 800),  # Task areas (e.g., mirrors)
    # Office Spaces
    'general office' :(300, 500),  # General office work
    'detailed office' :(500, 1000),  # Detailed tasks (e.g., drafting)
    'conference room' :(300, 500),  # Meetings and presentations
    # Educational and Learning Environments
    'classroom' :(300, 500),  # General classroom lighting
    'library' :(500, 800),  # Reading and study areas
    'laboratory' :(500, 1000),  # Science labs or technical work
    # Industrial and Commercial Settings
    'warehouse' :(100, 300),  # General storage areas
    'workshop' :(500, 1000),  # Detailed mechanical work
    'retail space' :(500, 1500),  # Retail displays and sales areas
    'supermarket' :(750, 1000),  # Grocery stores
    # Healthcare Settings
    'hospital general' :(100, 300),  # Waiting areas, corridors
    'hospital exam room' :(500, 1000),  # Examination rooms
    # Outdoor Areas
    'overcast day' :(1000, 2000),  # Outdoor lighting (overcast)
    'full daylight' :(10000, 25000),  # Bright daylight conditions
    'parking lot' :(20, 50),  # Outdoor parking areas
}

class LumenForm(forms.Form):
    space_type = forms.ChoiceField(
        choices=[(key, key) for key in LUX_RANGE.keys()],
        label="Space Type",
        widget=forms.Select(attrs={'required': 'required'}),
    )
    area = forms.FloatField(
        label="Area (square meters)",
        min_value=0.01,
        widget=forms.NumberInput(attrs={'step': 'any', 'required': 'required'}),
        error_messages={
            'min_value': 'Area must be a positive number.',
            'required': 'Please enter an area.',
            'invalid': 'Please enter a valid number for the area.'
        }
    )