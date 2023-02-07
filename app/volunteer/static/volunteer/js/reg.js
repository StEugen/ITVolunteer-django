document.addEventListener("DOMContentLoaded", function(e){
    $('#password, #repeat_password').on('keyup', function(){
        if ($('#password').val() != $('#repeat_password').val()){
            $('#message').html('passwords do not match').css('color', 'red');
        }
        else{
            $('#message').html('');
        }
    })

})