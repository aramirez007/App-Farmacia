
//Guarda categoria
function guardarCategoria() {
    
    var formData = new FormData(document.getElementById('nuevaCategoria-form'));
    const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  
    fetch('', {
      method: 'POST',
      body: formData,
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      }
  
    }).then(function (response) {

      if (response.ok) {
        Swal.fire({
          title: "Categoria Agregada.",
          icon: "success",
          timer: 2000,
          timerProgressBar: true
        });
        
        setTimeout(() =>{
          location.reload();
        }, 2000);
        
        console.log("Datos guardados correctamente!");

      } else {
        throw new Error('Hubo un problema al aguardar la nueva categoria');

      }
  
    }).catch(function(error){
      console.error('Error: ', error.message);
      Swal.fire('Error', 'Hubo un error al guardar la categoria', error.message);
      
    });
  
}
  

//Elimina categoria
function eliminarCategoria(id){
  var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

  Swal.fire({
    title: '¿Estás seguro?',
    text: 'Los cambios no se podrán revertir!',
    icon: 'warning', 
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Sí, eliminar',
    cancelButtonText: 'Cancelar'
  
  }).then(function(result){

    if(result.isConfirmed){

      var url = `eliminar_categoria/${id}/`;

      fetch(url,{
        method: 'GET', 
        headers: {'X-CSRFToken': csrftoken},
      })
      .then(function(response){
        if(response.ok){
          Swal.fire({
            title: "Categoria eliminada.",
            icon: "success",
            timer: 3000,
            timerProgressBar: true
          });

          console.log("Datos eliminados correctamente!");
          setTimeout(() =>{
            location.reload();
          }, 2000);
        
        }else{
          throw new Error('Error al eliminar el registro!');

        }
      
      }).catch(function(error){
        console.error('Error: ', error.message);
        Swal.fire('Error', 'Hubo un error al eliminar la categoria', error.message);

      })
    }
  })
  
}