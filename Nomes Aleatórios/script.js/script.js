function nomes() {
  var nomes = ["Daniela", "Carlos", "Pedro", "João", "Leandra", "Lorenzo", "Levi", "Alice", "Samuel", "Lara", "Raquel","Denner","Mateus","Kevin","Maicon","Ryan"];
  var indiceAleatorio = Math.floor(Math.random() * nomes.length);
  document.getElementById("nomes").innerHTML = nomes[indiceAleatorio];
  return nomes[indiceAleatorio];
}