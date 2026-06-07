let segundos = 0;
let minutos = 0;
let dead = 0;

let saude = document.getElementById("saude");
let comida = document.getElementById("comida");
let felicidade = document.getElementById("felicidade");
let energia = document.getElementById("energia");
let idade = document.getElementById("idade");
let nome = document.getElementById("nome");
const imagembichinho = document.getElementById("imagempou");


const time = setInterval(() => {
    segundos++;
    console.log(`Tempo decorrido: ${segundos} segundos`);
    if(segundos%60 == 0){
        minutos++;
        idade.textContent = Number(idade.textContent)+1;
    }

    if(segundos%1 == 0) {
        if(Number(comida.textContent) == 0){
            saude.textContent = Number(saude.textContent)-1;
            
            if(Number(energia.textContent > 2))
                energia.textContent = Number(energia.textContent)-2;
            else
                energia.textContent = 0;

            if(Number(felicidade.textContent > 3)) 
                felicidade.textContent = Number(felicidade.textContent)-3;
            else 
                felicidade.textContent = 0;
        }
        else{
            comida.textContent = Number(comida.textContent)-1;
        }

        if(Number(saude.textContent) == 0 && dead==0) {
                imagembichinho.src = 'bichinhostates/deadpou.png';
                nome.textContent = 'Dead ' + nome.textContent;
                dead=1;
                clearInterval(time);
        }
    }

}, 100);


