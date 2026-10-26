$(document).ready(function() {
    $('#lumen-form').submit(function(e) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: '{% url "calculator:calculate" %}',
            data: {
                space_type: $('#space_type').val(),
                area: $('#area').val(),
                csrfmiddlewaretoken: '{{ csrf_token }}'
            },
            success: function(response) {
                if (response.success) {
                    $('#result').html(
                        `<p>For the space type "${response.space_type}":</p>` +
                        `<p>Minimum lumens - ${response.min_lumens}</p>` +
                        `<p>Maximum lumens - ${response.max_lumens}</p>`
                    );
                } else {
                    $('#result').html(`<p style="color: red;">${response.error}</p>`);
                }
            }
        });
    });
});