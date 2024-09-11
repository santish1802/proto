import os
import grpc
from concurrent import futures
import hello_pb2
import hello_pb2_grpc
import time
import pysqlite3 as sqlite3

print("server.py")

class Greeter(hello_pb2_grpc.GreeterServicer):
    def __init__(self):
        self.conn = sqlite3.connect('nombre.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        
    def SayHello(self, request, context):
        name = request.name
        print(f"Received request to SayHello to {name}")
        
        self.cursor.execute('SELECT mensaje FROM saludos WHERE nombre = ?', (name,))
        result = self.cursor.fetchone()
        
        if result:
            message = result[0]
        else:
            self.cursor.execute('SELECT mensaje FROM saludos WHERE nombre = "Default"')
            result = self.cursor.fetchone()
            message = result[0] if result else f"Hello, {name}!"

        return hello_pb2.HelloReply(message=message)

def serve():
    port = os.environ.get('PORT', '50051')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port(f'[::]:{port}')
    print(f"Server started. Listening on port {port}.")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()