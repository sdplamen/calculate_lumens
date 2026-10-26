from rest_framework import serializers
from calculator.forms import LUX_RANGE

class LumenCalculatorSerializer(serializers.Serializer):
    space_type = serializers.ChoiceField(
        choices=[(key, key) for key in LUX_RANGE.keys()],
        required=True,
        help_text='Type of space (e.g., Office, Kitchen)'
    )
    area = serializers.FloatField(
        min_value=0.01,
        required=True,
        help_text='Area of the space in square meters (must be positive)'
    )

    def validate_area(self, value):
        if value <= 0:
            raise serializers.ValidationError('Area must be a positive number.')
        return value