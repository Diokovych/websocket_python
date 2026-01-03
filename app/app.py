import asyncio
import websockets
import json

# Conjunto de clientes conectados
clientes_conectados = set()

async def contador():
    """Genera números del 0 al 99 y los envía a todos los clientes."""
    contador_actual = 0
    
    while True:
        if clientes_conectados:
            mensaje = json.dumps({"contador": contador_actual})
            # Enviar a todos los clientes conectados
            websockets.broadcast(clientes_conectados, mensaje)
        
        await asyncio.sleep(1)
        contador_actual = (contador_actual + 1) % 100  # Reinicia a 0 después de 99

async def manejar_cliente(websocket):
    """Maneja la conexión de un cliente."""
    clientes_conectados.add(websocket)
    print(f"Cliente conectado. Total: {len(clientes_conectados)}")
    
    try:
        async for mensaje in websocket:
            # Por si necesitamos recibir mensajes del cliente
            pass
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        clientes_conectados.remove(websocket)
        print(f"Cliente desconectado. Total: {len(clientes_conectados)}")

async def main():
    """Inicia el servidor WebSocket."""
    print("Servidor WebSocket iniciado en ws://localhost:8765")
    
    # Iniciar el servidor y el contador en paralelo
    async with websockets.serve(manejar_cliente, "localhost", 8765):
        await contador()

if __name__ == "__main__":
    asyncio.run(main())