toHash.addEventListener('blur', function(){
    var hashed = CryptoJS.SHA512(toHash.value);
    hash.innerHTML = hashed; 
  });
  
  var getHashWord = function(){
    var xhr = new XMLHttpRequest();
    xhr.onload = function(){
      if (this.status == 200){
        onlineResult.innerHTML = this.response;
      }
    };
    xhr.open("GET", "https://vip.udel.edu/crypto/sha512_with_answer.php");
    xhr.send();
  };
  
  document.getElementById('ajax').addEventListener('click', getHashWord);