document.addEventListener('keydown', (event) => {
    var keyValue = event.key;
    var codeValue = event.code;

    if (keyValue=='w'){
        document.form_avanzar.submit()
    }
    if (keyValue=='d'){
        document.form_derecha.submit()
    }
    if (keyValue=='a'){
        document.form_izquierda.submit()
    }
    if (keyValue=='s'){
        document.form_retroceder.submit()
    }
     //console.log("keydown event, keyValue: " + keyValue);
    //console.log("keydown event, codeValue: " + codeValue);
    
  
  }, false);
  
  document.addEventListener('keyup', (event) => {
    var keyValue = event.key;
    var codeValue = event.code;

    if(keyValue=='w'){
        document.form_stop.submit();
    }
    if (keyValue=='d'){
        document.form_stop.submit()
    }
    if (keyValue=='a'){
        document.form_stop.submit()
    }
    if (keyValue=='s'){
        document.form_stop.submit()
    }
    //console.log("keyup event, keyValue: " + keyValue);
    //console.log("keyup event, codeValue: " + codeValue);
    

  }, false);