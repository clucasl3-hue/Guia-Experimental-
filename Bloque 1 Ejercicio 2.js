let N = parseInt(prompt("Ingrese la cantidad de grupos:"));
for (let i = 1; i <= N; i++) {
    console.log("=== Grupo " + i + " ===");
    let e1 = parseInt(prompt("Edad del primer hermano:"));
    let e2 = parseInt(prompt("Edad del segundo hermano:"));
    let e3 = parseInt(prompt("Edad del tercer hermano:"));
    let mayor = e1;
    if (e2 > mayor) mayor = e2;
    if (e3 > mayor) mayor = e3;
    console.log("El hermano mayor del grupo " + i + " tiene " + mayor + " años.");
}
