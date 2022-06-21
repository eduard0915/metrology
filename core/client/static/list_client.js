$(function ()  {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        language: {
            url: "//cdn.datatables.net/plug-ins/1.10.21/i18n/Spanish.json",

        },
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {'data': 'client'},
            {'data': 'nit_client'},
            {'data': 'address_client'},
            {'data': 'phone_client'},
            {'data': 'mail_client'},
            {'data': 'active_client'},
            {'data': 'active_client'},
        ],
        columnDefs: [
            {
                targets: [0,1,2,3,4],
                class: 'td-actions text-center'
            },
            {
                targets: [5],
                className: 'td-actions text-center',
                render: function (data, type, row) {
                    var estado = null
                    switch (row.active_client) {
                        case true:
                            estado = 'Activo'
                            break;
                        case false:
                            estado = 'Inactivo'
                            break;
                    }
                    return estado;
                }
            },
            {
                targets: [6],
                class: 'td-actions text-center',
                orderable: false,
                render: function (data, type, row) {
                    return '<a href="/client/update/' + row.id + '/" type="button" rel="tooltip" class="btn btn-link btn-warning edit"><i class="fa fa-edit"></i></a>';
                }
            },
        ],
        initComplete: function (settings, json) {
        }
    });
});