from django import forms

SPACE_TYPES = [
    ('general living', 'General Living'),
    ('kitchen', 'Kitchen'),
    ('reading', 'Reading'),
    ('bathrooms', 'Bathrooms'),
    ('general office', 'General Office'),
    ('detailed office', 'Detailed Office'),
    ('classroom', 'Classroom'),
    ('library', 'Library'),
    ('warehouse', 'Warehouse'),
    ('workshops - detailed mechanical', 'Workshops - Detailed Mechanical'),
    ('retail space', 'Retail Space'),
    ('overcast day', 'Overcast Day'),
    ('full daylight', 'Full Daylight'),
]

class LumenForm(forms.Form):
    space_type = forms.ChoiceField(choices=SPACE_TYPES, required=True, label='Space Type')
    area = forms.FloatField(required=True, label='Area (m²)', min_value=0.0)