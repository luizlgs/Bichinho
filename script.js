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
    fetch('http://127.0.0.1:5000/status')
        .then(response => {
            if (!response.ok)
                throw new Error('Erro na requisição ' + response.nome);

            return response.json();
        })
        .then(data => {
            console.log("Status recebido!\nNome do Bichinho:", data.nome);
            saude.textContent = data.saude;
            comida.textContent = data.comida;
            felicidade.textContent = data.felicidade;
            energia.textContent = data.energia;
            idade.textContent = data.idade;
            nome.textContent = data.nome;

        })
        .catch(error => {
            console.error('Erro: ', error);
        })

        if(Number(saude.textContent) == 0 && dead==0) {
                imagembichinho.src = 'bichinhostates/deadpou.png';
                nome.textContent = 'Dead ' + nome.textContent;
                dead=1;
                clearInterval(time);
        }
}, 1000);





