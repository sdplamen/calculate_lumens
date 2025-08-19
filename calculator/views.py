from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from calculator.forms import LUX_RANGE, LumenForm
from serializers import LumenCalculatorSerializer


def calculate_lumens(space_type, area):
    min_lux, max_lux = LUX_RANGE.get(space_type, (0, 0))

    if min_lux == 0 and max_lux == 0 and space_type not in LUX_RANGE :
        return None

    min_lumens = min_lux * area
    max_lumens = max_lux * area
    avg_lumens = (min_lumens + max_lumens) / 2

    return {
        'space_type' :space_type,
        'area' :area,
        'min_lux' :min_lux,
        'max_lux' :max_lux,
        'min_lumens' :int(min_lumens),
        'max_lumens' :int(max_lumens),
        'avg_lumens' :int(avg_lumens),
    }

def lumens_calculator(request):
    results = None
    form = LumenForm(request.POST or None)

    if request.method == 'POST' and form.is_valid() :
        space_type = form.cleaned_data['space_type']
        area = form.cleaned_data['area']
        results = calculate_lumens(space_type, area)

    context = {
        'form': form,
        'results': results,
    }
    return render(request, 'index.html', context)

class LumenCalculatorAPIView(APIView):
    serializer_class = LumenCalculatorSerializer
    def post(self, request, *args, **kwargs) :
        serializer = LumenCalculatorSerializer(data=request.data)

        if not serializer.is_valid() :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        space_type = serializer.validated_data['space_type']
        area = serializer.validated_data['area']

        results = calculate_lumens(space_type, area)

        if results :
            return Response(results, status=status.HTTP_200_OK)
        else :
            return Response(
                {"error" :f"Space type '{space_type}' not found or invalid."},
                status=status.HTTP_400_BAD_REQUEST
            )