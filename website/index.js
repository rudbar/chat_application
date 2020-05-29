$(function() {
    $('#sendBtn').bind('click', function() {
        var value = document.getElementById("msg").value
        $.getJSON('/send_message',
            {val:value},
            function(data) {

            });
        return false;
    });
});

function validate(name) {
    if(name.length >= 2){
        return true;
    }
    return false;
}

fetch('/get_messages')
    .then(function (resopnse) {
            return response.text();
    }).then(function (text) {
            console.log('GET response text:');
            console.log(text);
    });