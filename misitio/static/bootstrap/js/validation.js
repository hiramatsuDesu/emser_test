var m = "Verifique los datos ingresados";
function validar_campo(formulario){
    let nombre = document.forms["formulario"]["nombre"].value;
    let apellido = document.forms["formulario"]["apellido"].value;

    var valid = false;

    var num = /^[a-zA-Z\ áéíóúÁÉÍÓÚñÑ\s]*$/;

    
    if(nombre.match(num) == null){
        console.log("erroneo");
        m = "Nombre no debe llevar números";
        return false;
    }
    else{
        console.log("no erroneo");

    }

    if(apellido.match(num) == null){
        console.log("erroneo");
        m = "Apellido no debe llevar números";
        return false;

    }
    else{
        console.log("no erroneo");

    }
}


const alertPlaceholder = document.getElementById('liveAlertPlaceholder')
const appendAlert = (message, type) => {
  const wrapper = document.createElement('div')
  wrapper.innerHTML = [
    `<div class="alert alert-danger alert-dismissible" role="alert">`,
    `   <div>${message}</div>`,
    '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
    '</div>'
  ].join('')

  alertPlaceholder.append(wrapper)
}

const alertTrigger = document.getElementById('liveAlertBtn')
if (alertTrigger) {
  alertTrigger.addEventListener('click', () => {
    //appendAlert('Complete correctamente los campos', 'por favor')
    appendAlert(m)
  })
}

function abrir_modal_edicion(url){
  var $ =jQuery.noConflict();
  console.log("ingresa");
  $('#edicion').load(url, function(){
    $(this).modal('show');
  });
}