function calcularIMC() {
    var peso = document.getElementById("calculoimc-peso").value.replace(",", ".");
    var altura = document.getElementById("calculoimc-altura").value.replace(",", ".");

    if (peso !== "" && altura !== "" && !isNaN(peso) && !isNaN(altura)) {
      var imc = peso / (altura * altura);
      var resultado = "";

      if (imc < 18.5) {
        resultado = "Abaixo do Peso";
      } else if (imc >= 18.5 && imc < 24.9) {
        resultado = "Peso Normal";
      } else if (imc >= 25 && imc < 29.9) {
        resultado = "Sobrepeso";
      } else if (imc >= 30 && imc < 34.9) {
        resultado = "Obesidade Grau 1";
      } else if (imc >= 35 && imc < 39.9) {
        resultado = "Obesidade Grau 2";
      } else {
        resultado = "Obesidade Grau 3";
      }

      document.getElementById("calculoimc-resultado-valor").innerText = "Seu IMC é " + imc.toFixed(2) + ". " + resultado;
    } else {
      document.getElementById("calculoimc-resultado-valor").innerText = "Por favor, preencha campos válidos.";
    }
  }

  function limparCampos() {
    document.getElementById("calculoimc-peso").value = "";
    document.getElementById("calculoimc-altura").value = "";
    document.getElementById("calculoimc-resultado-valor").innerText = "Seu IMC:";
  }