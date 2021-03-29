$("#sign-form").on("submit", (e) => {
    e.preventDefault();
    console.log('submitting...');
    $.ajax({
        type: 'POST',
        url: '/signup',
        data: JSON.stringify({
            "name": $("#name").val(),
            "email": $("#mail").val(),
            "password": $("#pw").val()
        }),
        success: (data) => {
            if (data.success) {
                window.location = '/login';
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
        console.log(('error', e));
        $("#alerts").html(
            `<div class="alert alert-warning alert-dismissible fade show" role="alert">${e.responseJSON.message}<button type="button" class="btn-close" data-bs-dismiss="alert"></button></div>`
        )
    });
});