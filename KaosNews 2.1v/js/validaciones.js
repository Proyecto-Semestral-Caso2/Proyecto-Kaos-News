function validarNombre(nombre){
    if(nombre.length >= 3 && nombre.length <=21){
        return true;
    }
    return false;
}

function validarApellido(apellido){
    if(apellido.length >= 3 && apellido.length <=36){
        return true;
    }
    return false;
}

function validarTitular(titular){
    if(titular.length >= 8 && titular.length <=50){
        return true;
    }
    return false;
}

function validarCuerpo(cuerpo){
    if(cuerpo.length >= 5 && cuerpo.length <=1000){
        return true;
    }
    return false;
}

function validarContrasenia(password){
    if(password.length >= 5 && password.length <=25){
        return true;
    }
    return false;
}

function validarCorreo(correo){
    if(correo.length >= 5 && correo.length <=50){
        return true;
    }
    return false;
}


function checkName(name) {
    if (name.length >= 3 && name.length <= 50) {
        return true;
    }
    return false;
}

function checkPhoneLength(phone) {

    if (phone.length == 9) {
        return true;
    }
    return false;
}

function checkMessage(message) {

    if (message.length >= 10 && message.length <=1000) {
        return true;
    }
    return false;
}




// dudas profe

function checkMail() {

    var mail = document.getElementById("mail").value;

    var regx = /^([a-zA-Z0-9._])+@([a-zA-Z0-9])+.([a-z]+)(.[a-z]+)?$/

    if (regx.test(mail)) {
        $("#mail").addClass("is-invalid");
        $("#mail ").removeClass("is-valid");
    }

    else {
        $("#mail").addClass("is-valid");
        $("#mail").removeClass("is-invalid");
    }
}






//validar si el archivo es imagen o no
function validarExt() {
    var archivoInput = document.getElementById('imagenes');
    var archivoRuta = archivoInput.value;
    var extPermitidas = /(.jpg|.png|.JPG|.PNG)$/i;

    if (!extPermitidas.exec(archivoRuta)){
        alert('selecciona una imagen con tipo de extension jpg o png');
        archivoInput.value='';
        return false;
    }
    
    else{
        if(archivoInput.files && archivoInput.files[0]){
            var visor = new FileReader();
            visor.onload = function(e){
                document.getElementById('visorImagen').innerHTML = 
                '<embed src="'+e.target.result+'" width="250" height="250">';
            };
            visor.readAsDataURL(archivoInput.files[0]);
        }
    }
    

}
