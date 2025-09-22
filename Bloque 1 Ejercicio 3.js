let edades = [];
for (let i = 0; i < 3; i++) {
    edades[i] = parseInt(prompt("Ingrese la edad del hermano " + (i + 1) + ":"));
}
let mayor = edades[0];
for (let i = 1; i < edades.length; i++) {
    if (edades[i] > mayor) {
        mayor = edades[i];
    }
}
console.log("El hermano mayor tiene " + mayor + " años.");
