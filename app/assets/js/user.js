token = localStorage.getItem('user_token');

if(token == null){window.location = 'http://localhost/login'}

$.ajax({
    url: '/user-data',
    type: 'GET',
    headers: {"Authorization": `bearer ${token}`},
    success: (data) => {
        $("body").html('<div class="container"></div>');
        container = $('.container');
        if (data.success) {
            container.html(`<div class="alert alert-info"><h1>${data.name}</h1><h2>${data.email}</h2></div>`);
        } else {
            window.location = '/login';
        }
    }
})
.fail((e=undefined) => {
    window.location='/login';
});