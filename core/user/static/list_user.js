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
            {'data': 'is_active'},
            {'data': 'first_name'},
            {'data': 'username'},
            {'data': 'cargo'},
            {'data': 'groups__name'},
            {'data': 'email'},
            {'data': 'is_active'},
            {'data': 'is_active'},
        ],
        columnDefs: [
            {
                targets: [7],
                class: 'td-actions text-center',
                orderable: false,
                render: function (data, type, row) {
                    return '<a href="/user/update-password/' + row.id + '/" type="button" rel="tooltip" class="btn btn-link btn-warning"><i class="fa fa-edit"></i></a>';
                }
            },
            {
                targets: [0],
                class: 'td-actions text-center',
                orderable: false,
                render: function (data, type, row) {
                    return '<a href="/user/detail/' + row.id + '/" type="button" rel="tooltip" class="btn btn-link btn-info"><i class="fa fa-info-circle"></i></a>';
                }
            },
            {
                targets: [2,3,5],
                class: 'td-actions text-center'
            },
            {
                targets: [4],
                class: 'td-actions text-center',
                render: function (data, type, row) {
                    return '<span class="badge badge-pill badge-success">'+row.groups__name+'</span>'
                }
            },
            {
                 targets: [1],
                 className: 'td-actions text-center',
                 render: function (data, type, row) {
                     return row.first_name + ' ' +row.last_name;
                 }
             },
            {
                targets: [6],
                className: 'td-actions text-center',
                render: function (data, type, row) {
                    var estado = null
                    switch (row.is_active) {
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
        ],
        initComplete: function (settings, json) {
        }
    });
});