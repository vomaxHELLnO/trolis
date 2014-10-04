$( document ).ready(function() {
    test_button = function() {
        alert("Test button pressed: kebabas");
    };

    // alert("Puslapis uzsikrove");
    $('.test').click(test_button);
    $('#exit-button').click(function (){
        window.close();
    });

    $(".checker").draggable({revert: "invalid"});
    $(".droppable").droppable();

    $("#video video").width($(window).width());
    $(window).resize(function() {
        $("#video video").width($(window).width());
        // $("#video video").height($(window).height());
    });

});


