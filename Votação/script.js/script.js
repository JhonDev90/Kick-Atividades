alert("Você pode votar quantas vezes quiser, ao votar aperte 6 para sair");

 let v = "";
 let v1 = 0;
 let v2 = 0;
 let v3 = 0;
 let v4 = 0;
 let v5 = 0;
 let v6 = 0;

 do {
   v = parseInt(prompt("Vote: 1 João, 2 Maria, 3 Pedro, 4 Thalita, 5 Nulo, 6 Sair"));
   switch(v) {
     case 1:
       v1 += 1;
       break;
     case 2:
       v2 += 1;
       break;
     case 3:
       v3 += 1;
       break;
     case 4:
       v4 += 1;
       break;
     case 5:
       v5 += 1;
       break;
     case 6:
       v6 += 1;
       break;
     default:
       alert("Número inválido");
       break;
   }
 } while (v != 6);
 document.getElementById("p").innerHTML += `Votos para João: ${v1} <br>`;
 document.getElementById("p").innerHTML += `Votos para Maria: ${v2} <br>`;
 document.getElementById("p").innerHTML += `Votos para Pedro: ${v3} <br>`;
 document.getElementById("p").innerHTML += `Votos para Thalita: ${v4} <br>`;
 document.getElementById("p").innerHTML += `Votos Nulos: ${v5} <br>`;
 alert("Você saiu");