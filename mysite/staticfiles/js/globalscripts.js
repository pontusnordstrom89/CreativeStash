$("#show-add-category").click(function () {
    $("#add-category-form").toggle();
});

$("#{{idea_data.idea_id}}").click(function () {
    $.ajax({
        url: '/theStash/ajax/like_counter/',
        data: {
            'idea_id': idea_data.idea_id
        },
        dataType: 'json',
        success: function (data) {
            $("#{{idea_data.id}}").text(data);
        }
    });
    
});

