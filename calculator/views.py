from django.shortcuts import render
from .forms import LumenForm


def lookup_lux(space_type, lux_range) :
    for space_room, (min_lux, max_lux) in lux_range.items() :
        if space_room == space_type :
            return (min_lux, max_lux)
    return None


def calculate_lumens(space_type, area, lux_range) :
    lux_values = lookup_lux(space_type, lux_range)
    if lux_values is None :
        return None

    min_lux, max_lux = lux_values
    min_lumens = min_lux * area
    max_lumens = max_lux * area

    return (min_lumens, max_lumens), space_type


lux_range = {
    'general living' :(100, 300),
    'kitchen' :(300, 750),
    'reading' :(500, 800),
    'bathrooms' :(500, 800),
    'general office' :(300, 500),
    'detailed office' :(500, 1000),
    'classroom' :(300, 500),
    'library' :(500, 800),
    'warehouse' :(200, 300),
    'workshops - detailed mechanical' :(500, 1000),
    'retail space' :(750, 1500),
    'overcast day' :(1000, 2000),
    'full daylight' :(10000, 25000)
}


def calculate_view(request) :
    if request.method == 'POST' :
        form = LumenForm(request.POST)
        if form.is_valid() :
            space_type = form.cleaned_data['space_type']
            area = form.cleaned_data['area']

            result = calculate_lumens(space_type, area, lux_range)

            if result :
                lumens, space_room = result
                context = {
                    'form' :form,
                    'success' :True,
                    'space_type' :space_room,
                    'min_lumens' :int(lumens[0]),
                    'max_lumens' :int(lumens[1])
                }
            else :
                context = {
                    'form' :form,
                    'success' :False,
                    'error' :f'Type error! Lux value is not in the list of "{space_type}"'
                }
        else :
            context = {'form' :form}
    else :
        context = {'form' :LumenForm()}

    return render(request, 'index.html', context)