// Conexión WebSocket
const ws = new WebSocket('ws://localhost:8765');
const contadorElemento = document.getElementById('contador');

ws.onopen = () => {
    console.log('Conectado al servidor WebSocket');
};

ws.onmessage = (evento) => {
    const datos = JSON.parse(evento.data);
    contadorElemento.textContent = datos.contador.toString().padStart(2, '0');
};

ws.onclose = () => {
    console.log('Desconectado del servidor');
    contadorElemento.textContent = '--';
};

ws.onerror = (error) => {
    console.error('Error WebSocket:', error);
};