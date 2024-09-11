import os
import grpc
from concurrent import futures
import hello_pb2
import hello_pb2_grpc
import time
import sqlite3
import sys

print("server.py - Script started", file=sys.stderr)

class Greeter(hello_pb2_grpc.GreeterServicer):
    def __init__(self):
        print("Initializing Greeter", file=sys.stderr)
        self.conn = sqlite3.connect('nombre.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        print("Database connected", file=sys.stderr)
        
    def SayHello(self, request, context):
        name = request.name
        print(f"Received request to SayHello to {name}", file=sys.stderr)
        
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
    print(f"Starting server on port {port}", file=sys.stderr)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port(f'[::]:{port}')
    print(f"Server started. Listening on port {port}.", file=sys.stderr)
    server.start()
    print("Server is running. Waiting for termination.", file=sys.stderr)
    server.wait_for_termination()

if __name__ == '__main__':
    print("Main block entered", file=sys.stderr)
    serve()