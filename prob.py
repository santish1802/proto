import grpc
import hello_pb2
import hello_pb2_grpc

def run():
    with grpc.insecure_channel('junction.proxy.rlwy.net:18083') as channel:
        stub = hello_pb2_grpc.GreeterStub(channel)
        
        # Lista de nombres para probar
        names = ['Alice', 'Bob', 'Charlie', 'xd']
        
        for name in names:
            response = stub.SayHello(hello_pb2.HelloRequest(name=name))
            print(f"Respuesta para {name}: {response.message}")

if __name__ == '__main__':
    run()