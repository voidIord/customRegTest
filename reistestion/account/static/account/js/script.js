// login_form action

$(".login_click").click(function() {
    $(".overlay").css("display", "block");
    $(".login_alert").css("display", "block");
});

$(".overlay").not(".login_alert").click(function() {
    $(".overlay").css("display", "none");
    $(".login_alert").css("display", "none");
});

$(".close_form_click").click(function() {
    $(".overlay").css("display", "none");
    $(".login_alert").css("display", "none");
});
