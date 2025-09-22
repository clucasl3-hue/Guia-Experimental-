let edades = [];
for (let i = 1; i <= 3; i++) {
    edades.push(parseInt(prompt(`Ingrese la edad del hermano ${i}`)));
}
let mayor = edades[0];
for (let i = 1; i < edades.length; i++) {
    if (edades[i] > mayor) {
        mayor = edades[i];
    }
}
console.log(`El hermano mayor tiene ${mayor} años`);
