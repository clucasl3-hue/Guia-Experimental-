function SerieCelulares() {
  let n = parseInt(prompt("Ingrese cantidad de celulares a vender:"));
  let c = 1;
  while (c <= n) {
    let precio = parseFloat(prompt("Ingrese el precio del celular N°" + c));
    let marca = prompt("Ingrese Marca A o Marca B");
    let capacidad = parseInt(prompt("Ingrese la capacidad del celular"));
    let pfinal; 
    if (marca === "A" && capacidad === 64) {
      pfinal = precio + 20;
    } else if (marca === "A" && capacidad === 128) {
      pfinal = precio + 30;
    } else if (marca === "B" && capacidad === 64) {
      pfinal = precio - 30;
    } else if (marca === "B" && capacidad === 128) {
      pfinal = precio - 50;
    } 
    alert("Su Precio final a pagar es de: $ " + pfinal);
    c = c + 1; 
  }
} 
