function ArregloCelulares() { 
  let marcas = ["A", "A", "B", "B"];
  let capacidades = [64, 128, 64, 128];
  let preciosIniciales = [500, 600, 400, 700];
  let preciosFinales = [];
  let c = 0;
  while (c < marcas.length) {
    let marca = marcas[c];
    let capacidad = capacidades[c];
    let precio = preciosIniciales[c];
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
    preciosFinales.push(pfinal);
    alert("Celular N° " + (c + 1));
    alert("Su precio final es de $ " + pfinal);
    c= c + 1;
  }
}

Celulares();
SerieCelulares();
ArregloCelulares();
