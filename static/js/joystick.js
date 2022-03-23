document.addEventListener('keydown', (event) => {
    var keyValue = event.key;
    var codeValue = event.code;

    if (keyValue=='w'){
      $.ajax({
              type:'post',
              url:'/avanzar/'
          });
          return false;
    }
    if (keyValue=='d'){
      $.ajax({
        type:'post',
        url:'/derecha/'
    });
    return false;
    }
    if (keyValue=='a'){
      $.ajax({
        type:'post',
        url:'/izquierda/'
    });
    return false;
    }
    if (keyValue=='s'){
      $.ajax({
        type:'post',
        url:'/retroceder/'
    });
    return false;
    }
     //console.log("keydown event, keyValue: " + keyValue);
    //console.log("keydown event, codeValue: " + codeValue);
    
  
  }, false);
  
  document.addEventListener('keyup', (event) => {
    var keyValue = event.key;
    var codeValue = event.code;

    if(keyValue=='w'){
            $.ajax({
              type:'post',
              url:'/stop/'
          });
          return false;
    }
    if (keyValue=='d'){
            $.ajax({
              type:'post',
              url:'/stop/'
          });
          return false;
    }
    if (keyValue=='a'){
            $.ajax({
              type:'post',
              url:'/stop/'
          });
          return false;
    }
    if (keyValue=='s'){
            $.ajax({
              type:'post',
              url:'/stop/'
          });
          return false;
    }
    //console.log("keyup event, keyValue: " + keyValue);
    //console.log("keyup event, codeValue: " + codeValue);
    

  }, false);