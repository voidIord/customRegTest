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

var alertPlaceholder = document.getElementById('liveAlertPlaceholder')
var alertTrigger = document.getElementById('liveAlertBtn')

function alert(message, type) {
  var wrapper = document.createElement('div')
  wrapper.innerHTML = '<div class="alert alert-' + type + ' alert-dismissible" role="alert">' + message + '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>'

  alertPlaceholder.append(wrapper)
}

if (alertTrigger) {
  alertTrigger.addEventListener('click', function () {
    alert('Nice, you triggered this alert message!', 'success')
  })
}
