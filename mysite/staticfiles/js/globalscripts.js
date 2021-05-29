$("#show-add-category").click(function () {
    $("#add-category-form").toggle();
});

$(".like_button").click(function () {
    $.ajax({
        url: '/theStash/ajax/like_counter',
        data: {
            'idea_id': $(".like_button").attr("id")
        },
        dataType: 'json',
        success: function (data) {
            $("#{{idea_data.id}}").text(data);
        }
    });
    
});



