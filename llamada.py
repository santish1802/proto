import grpc
import hello_pb2
import hello_pb2_grpc

def run():
    while True:
        names_input = input("Ingresa los nombres separados por comas: ")
                
        names = [name.strip() for name in names_input.split(',')]
        
        with grpc.insecure_channel('junction.proxy.rlwy.net:15617') as channel:
            stub = hello_pb2_grpc.GreeterStub(channel)
            
            for name in names:
                response = stub.SayHello(hello_pb2.HelloRequest(name=name))
                print(f"\nRespuesta para {name}: {response.message}\n")

if __name__ == '__main__':
    run()
