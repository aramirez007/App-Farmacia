
function guardarCategoria() {
  enviarCategoria();

}

function enviarCategoria() {
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
      return response.json();

    } else {
      throw new Error('Hubo un problema al aguardar la nueva categoria');
    }

  }).then(function (data) {
    Swal.fire({
      icon: 'success',
      title: data.message,
      showConfirmButton: false
    });

    setTimeout(function(){
      Swal.close();
    }, 2000);

  }).catch(function(error){
    Swal.fire({
      icon: 'error',
      title: 'Error',
      text: error.message
    });

    setTimeout(function(){
      Swal.close();
    }, 2000);
    
  });

}

function eliminarCategoria() {
  const swalWithBootstrapButtons = Swal.mixin({
    customClass: {
      confirmButton: "btn btn-success",
      cancelButton: "btn btn-danger"
    },
    buttonsStyling: false
  });
  swalWithBootstrapButtons.fire({
    title: "Are you sure?",
    text: "You won't be able to revert this!",
    icon: "warning",
    showCancelButton: true,
    confirmButtonText: "Yes, delete it!",
    cancelButtonText: "No, cancel!",
    reverseButtons: true
  }).then((result) => {
    if (result.isConfirmed) {
      swalWithBootstrapButtons.fire({
        title: "Deleted!",
        text: "Your file has been deleted.",
        icon: "success"
      });
    } else if (
      /* Read more about handling dismissals below */
      result.dismiss === Swal.DismissReason.cancel
    ) {
      swalWithBootstrapButtons.fire({
        title: "Cancelled",
        text: "Your imaginary file is safe :)",
        icon: "error"
      });
    }
  });
}