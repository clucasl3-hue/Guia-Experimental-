let N = parseInt(prompt("Ingrese el numero de grupos"));
for (let i = 1; i <= N; i++) {
    let edad1 = parseInt(prompt(`Grupo ${i}: Ingrese la edad del primer hermano`));
    let edad2 = parseInt(prompt(`Grupo ${i}: Ingrese la edad del segundo hermano`));
    let edad3 = parseInt(prompt(`Grupo ${i}: Ingrese la edad del tercer hermano`));
    let mayor = edad1;
    if (edad2 > mayor) {
        mayor = edad2;
    } 
    if (edad3 > mayor) {
        mayor = edad3;
    }
    console.log(`Grupo ${i}: El hermano mayor tiene ${mayor} años`);
}
