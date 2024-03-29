function quiz(pergunta) {
  let resposta = prompt(pergunta);
  return resposta;
}

function contarAcertos(resposta, esperado) {
  return resposta === esperado ? 1 : 0;
}

function contarErros(resposta, esperado) {
  return resposta !== esperado ? 1 : 0;
}

alert("Vamos começar");

let acertos = 0;
let erros = 0;

let pergunta1 = "Qual é o nome verdadeiro do Batman?\n 1: Bruce Wayne \n 2: Chris Wayne \n 3: Thomas Wayne";
let resposta1 = quiz(pergunta1);

if (resposta1 === "1") {
  alert("Correto");
  acertos += contarAcertos(resposta1, "1");
  erros += contarErros(resposta1, "1");
} else {
  alert("Errado");
  acertos += contarAcertos(resposta1, "1");
  erros += contarErros(resposta1, "1");
}

let pergunta2 = "Qual é a fraqueza do Superman? \n 1: Radiação Gama \n 2: Adamantium \n 3: Kryptonita";
let resposta2 = quiz(pergunta2);

if (resposta2 === "3") {
  alert("Correto");
  acertos += contarAcertos(resposta2, "3");
  erros += contarErros(resposta2, "3");
} else {
  alert("Errado");
  acertos += contarAcertos(resposta2, "3");
  erros += contarErros(resposta2, "3");
}

let pergunta3 = "Complete a frase: No dia mais claro, na noite mais densa, o mal sucumbirá perante minha: \n 1: Ausência \n 2: Presença \n 3: luz";
let resposta3 = quiz(pergunta3);

if (resposta3 === "2") {
  alert("Correto");
  acertos += contarAcertos(resposta3, "2");
  erros += contarErros(resposta3, "2");
} else {
  alert("Errado");
  acertos += contarAcertos(resposta3, "2");
  erros += contarErros(resposta3, "2");
}

let pergunta4 = "Qual é a trincadade do universo DC? \n 1: Superman, Flash e Mulher Maravilha \n 2: Batman, Superman e Mulher Maravilha \n 3: Batman, Lanterna Verde e Flash";
let resposta4 = quiz(pergunta4)

if (resposta4 === "2") {
  alert("Correto");
  acertos += contarAcertos(resposta4, "2");
  erros += contarErros(resposta4, "2");
}else{
  alert("Errado");
  acertos += contarAcertos(resposta4, "2");
  erros += contarErros(resposta4, "2");
}

let pergunta5 = "Qual é o nome do avô materno e da mãe de Damian Wayne? \n 1: Ra's Al Ghul, Thalia Al Ghul \n 2: David Barton, Alice Barton \n 3: Ben Cooblepot, Alice Cooblepot";
let resposta5 = quiz(pergunta5)

if (resposta5 === "1") {
  alert("Correto");
  acertos += contarAcertos(resposta5, "1");
  erros += contarErros(resposta5, "1");
}else{
  alert("Errado");
  acertos += contarAcertos(resposta5, "1");
  erros += contarErros(resposta5, "1");
}
 alert("Acertos: " + acertos + "\nErros: "+ erros);