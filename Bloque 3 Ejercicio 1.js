function Celulares() {
  let ptlf = parseInt(prompt("Ingrese precio del celular"));
  let marca = prompt("Ingrese Marca A o Marca B");
  let capacidad = parseInt(prompt("Ingrese la capacidad del teléfono"));
  let pfinal; 

  if (marca === "A" && capacidad === 64) {
    pfinal = ptlf + 20;
  } else if (marca === "A" && capacidad === 128) {
    pfinal = ptlf + 30;
  } else if (marca === "B" && capacidad === 64) {
    pfinal = ptlf - 30;
  } else if (marca === "B" && capacidad === 128) {
    pfinal = ptlf - 50;
  } 
  alert("Su Precio final a pagar es de: $ " + pfinal);
} 
