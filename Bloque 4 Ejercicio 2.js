function Seriesuscripcionstreaming (){
    let usuarios, costoT=0, costoU=0, n=0, c=1;
    n=parseInt(prompt("Ingrese el número de grupos:"));
    while (c <= n) {
        usuarios = parseInt(prompt("Ingrese la cantidad de usuarios del grupo " + c + ":"));
     if (usuarios >= 100){
        costoT=usuarios * 5;
        costoU= 5;
     }else if (usuarios >= 50) {
        costoT=usuarios * 6;
        costoU= 6;
     }else if (usuarios >= 30) {
        costoT=usuarios * 8;
        costoU= 8;
     }else {
        costoT= 300;
        costoU= costoT/usuarios;
     }
     alert(`Grupo ${c}: ${usuarios} usuarios, Costo total: $${costoT}, Costo por usuario: $${costoU}`);
     c=c+1
    }
        
}
debugger;
Seriesuscripcionstreaming ()
