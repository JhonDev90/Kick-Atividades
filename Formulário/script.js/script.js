function validacao() {
  var termos = document.getElementById("concordo").checked;
   if (!termos) {
     alert("Você deve concordar com os termos antes de enviar o formulário.");
      return false;
    }

  var idade = document.getElementById("idade").value;
    if (idade < 18) {
       alert("Você ainda não tem idade suficiente para fazer o curso, pois envolve transações e outras atividades restritas.");
       return false;
    }

    var senha = document.getElementById("senha").value;
    var senhaConfirm = document.getElementById("senhaConfirm").value;
     if (senha.length < 9) {
         alert("A senha deve ter pelo menos 9 caracteres");
         return false;
      }

    var nome = document.getElementById("nome").value;
    var sobrenome = document.getElementById("sobrenome").value;
    var nascimento = document.getElementById("nascimento").value;
    var email = document.getElementById("email").value;
    var linguagem = document.getElementById("linguagem").value;
    var nivel = document.querySelector('input[name="opcao"]:checked');
     if (nome === "" || sobrenome === "" || idade === "" || nascimento === "" || email === "" || linguagem === "" || nivel === null || senha === "" || senhaConfirm === "") {
         alert("Por favor, preencha todos os campos.");
         return false;
      } else if (senha !== senhaConfirm) {
         alert("As senhas não coincidem. Por favor, digite novamente.");
         return false;
      } else {
         alert("Formulário enviado com sucesso!");
          document.getElementById("form").reset();
      }

   window.location.reload(false);
}