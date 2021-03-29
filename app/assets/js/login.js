$("#sign-form").on("submit", (e) => {
    e.preventDefault();
    console.log('submitting...');
    $.ajax({
        type: 'POST',
        url: '/login',
        data: JSON.stringify({
            "email": $("#mail").val(),
            "password": $("#pw").val()
        }),
        success: (data) => {
            if (data.success) {
                localStorage.setItem('user_token', data.token);
                console.log('token', data.token);
                window.location = '/user';
            } else {
                $("#alerts").html(
                    `<div class="alert alert-warning alert-dismissible fade show" role="alert">${data.message}<button type="button" class="btn-close" data-bs-dismiss="alert"></button></div>`
                );
            }
        },
        contentType: 'application/json',
        dataType: 'json'
    })
    .fail((e=undefined) => { 
        console.log('error', e);       
        console.log('type', typeof(e));
        if (e.hasOwnProperty('responseJSON')) {
            $("#alerts").html(`<div class="alert alert-warning alert-dismissible fade show" role="alert">${e.responseJSON.message}<button type="button" class="btn-close" data-bs-dismiss="alert"></button></div>`);
        } else {
            $("#alerts").html(`<div class="alert alert-warning alert-dismissible fade show" role="alert">An error occurred. Try again.<button type="button" class="btn-close" data-bs-dismiss="alert"></button></div>`);
        }
    });
});