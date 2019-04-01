// this function executes our search via an AJAX call
function runSearch( term ) {
    
    // transforms all the form parameters into a string we can send to the server
    var frmStr = $('#usr_login').serialize();
    
    $.ajax({
        url: './some_cgi',
        dataType: 'json',
        data: frmStr,
        success: function(data, textStatus, jqXHR) {
            // some function to get
        },
        error: function(jqXHR, textStatus, errorThrown){
            alert("Some popup error messag: (" + textStatus +
                  ") and errorThrown: (" + errorThrown + ")");
        }
    });
}


function return_msg() {
    var submit_button = document.getElementById('submit');

    submit_button.onclick = function() {
        var login_form = document.getElementById('usr_login');
        login_form.style.display = 'none';
        var msg = document.getElementById('login_success');  
        msg.style.display = 'block';          
    }
}




// run our javascript once the page is ready
$(document).ready( function() {
    // define what should happen when a user clicks submit on our search form
    $('#submit').click( function() {
        return_msg();
        return false;  // prevents 'normal' form submission
    });
});