
//Selecciona el producto a añadir
function seleccionarProducto(id, nombre, descripcion, existencias, precio){
    precio = parseFloat(precio, 2);
    
    $("#producto").val(nombre);
    $("#descripcion").val(descripcion);
    $("#existencias").val(existencias);
    $("#precio").val(precio);
}

//Se añade el producto al carro/venta
function aniadirAlCarro(){

    let producto = $("#producto").val();
    let descripcion = $("#descripcion").val();
    let existencias = $("#existencias").val();
    let precio = $("#precio").val();
    let cantidad = $("#cantidad").val();

    let subtotal = (parseInt(cantidad)*parseFloat(precio));
    let total = 0;

    if(producto && cantidad){
        //añadinomos los productos al detalle
        $("#contenidoCarro").append(`<div class="row">
                                        <div class="col d-inline p-2">
                                            <div id="listaCarroDetalle" class="card-body">
                                                <div class="row">
                                                    <table id="renglonCarro">
                                                        <tr>
                                                            <td class="col-8">
                                                                <div class="container">
                                                                    <div class="row"><strong id="producto"><i class="fa-solid fa-capsules"></i>${producto}</strong></div>
                                                                    <br>
                                                                    <div class="row">
                                                                        <div class="col col-lg-2"><p id="descripcion">${descripcion}</p></div>
                                                                        <div class="col col-lg-2"><p id="existencias">En stock: ${existencias}</p></div>
                                                                        <div class="col col-lg-2"><p id="precio">Precio: $${precio}</p></div>
                                                                    </div>
                                                                    <div class="row">
                                                                        <div class="col col-lg-2"><p id="cantidad">Cantidad: ${cantidad}</p></div>
                                                                        <div class="col col-lg-2">
                                                                            <p id="subtotal"><i class="fa-solid fa-dollar-sign"></i><strong>${subtotal}</strong></p>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </td>
                                                            <td class="col-4">
                                                                <button onclick="quitarDelCarro()" type="button" class="btn btn-danger">Quitar</button>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </div>
                                            </div>
                                        </div>
                                    </div>`);

        //Limpiamos el producto seleccionado
        $("#producto").val("");
        $("#descripcion").val("");
        $("#existencias").val("");
        $("#precio").val("");
        $("#cantidad").val("");

    }else if(!producto){
        alert("Para añadir al carro debe selecionar un producto");
        return false;

    }else if(!cantidad){
        alert("Falta capturar la cantidad.");
        return false;
    }

    let noProductos = $("#renglonCarro tr").length;
    $("#noproductos").text(noProductos);

    
    $("#renglonCarro tr .row:last-child").each(function(){
        let subtotalVenta = parseFloat($(this).find("#subtotal").text());

        total += subtotalVenta;
    });

    $("#totalVenta").text(total);

}

function obtenerDatos(){
    var detalleDatosVenta = [];
    var totalVenta = $("#totalVenta").text();
    
    $("#detalleVenta tr").each(function(){
        let producto = $(this).find("#producto").text();
        let cantidad = $(this).find("#cantidad").text();
        let subtotal = $(this).find("#subtotal").text();

        detalleDatosVenta.push({
            producto: producto,
            cantidad: cantidad,
            precio_unitario: subtotal
        });
        
    });

    Swal.fire({
        title: '¿Envíar?',
        text: 'Se guardarán los detalles de la venta.',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, envíar',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            
            //Enviamos la petición AJAX
            enviarDatos(detalleDatosVenta, totalVenta);

        }
    });
}

function enviarDatos(datos, totalventa){
    const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

    fetch('',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({
            datos: datos, 
            total: totalventa
        })
    }).then(function(response){
        
        if(response.ok){
            console.log("Datos enviados correctamente!!!");
            Swal.fire({
                title: 'Se ha completado la venta.',
                //text: '',
                icon: 'success',
                timer: 2000,
                timerProgressBar: true
            });

            setTimeout(()=>{
                location.reload();
            }, 2000);

        }else{
            console.log("Error al enviar los datos.");
        }
    }).catch(function(error){
        console.error("Error en la solicitud: ", error);
    })
}

function quitarDelCarro(){
    
}