let usuarios, costoT=0, costoU=0;
usuarios=parseInt(prompt("Ingrese la cantidad de usuarios:"));
if (usuarios >= 100){
  costoT=usuarios*5;
  costoU= 5;
}else if (usuarios >= 50) {
  costoT=usuarios*6;
  costoU= 6;
}else if (usuarios >= 30) {
  costoT=usuarios*8;
  costoU= 8;
}else {
  costoT=300;
  costoU=costoT/usuarios;
}
console.log (`Costo total: $${costoT}`);
console.log (`Costo por usuario: $${costoU}`);
k
