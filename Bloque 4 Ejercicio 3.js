function Arreglosuscripcionstreaming (){
    let costoT=[], costoU=[], n=0, grupos=[], c=0;
    n=parseInt(prompt("Ingrese el número de grupos:"));
    while (c < n) {
        grupos[c] = parseInt(prompt(`Ingrese la cantidad de usuarios del grupo ${c+1}:`));
     if (grupos[c] >= 100) {
     costoT[c] = grupos[c] * 5;
     costoU[c] = 5;
     } else if (grupos[c] >= 50) {
     costoT[c] = grupos[c] * 6;
     costoU[c] = 6;
     } else if (grupos[c] >= 30) {
     costoT[c] = grupos[c] * 8;
     costoU[c] = 8;
     } else {
      costoT[c] = 300;
     costoU[c] = costoT[c] / grupos[c];
     }
     c=c+1
    }
    alert(Resultados);
    c=0;
    while (c < n) {
     alert(`Grupo ${c+1}: ${grupos[c]} usuarios, Costo total: $${costoT[c]}, Costo por usuario: $${costoU[c]}`);
     c=c+1
    }
}   
debugger;
Arreglosuscripcionstreaming ()
