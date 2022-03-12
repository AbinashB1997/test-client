import grpc
from sp_client.client.grpc import PostControllerStub, \
    Post, PostRetrieveRequest, PostListRequest, GetControllerStub, GetListRequest

class Operation:
    def __init__(self):
        self.channel = grpc.insecure_channel('localhost:50051')
        self.stub = PostControllerStub(self.channel)
        self.server2_stub = GetControllerStub(self.channel)
    
    def create_post(self, title=None, content=None):
        response = self.stub.Create(Post(title=title, content=content))
        print("create resp: ", response)
        return response
    def get_post(self, id=None):
        response = self.stub.Retrieve(PostRetrieveRequest(id=id))
        print("get resp: ", response)
        return response
    def get_from_server2(self, id=1):
        response = self.server2_stub.List(GetListRequest(id=1))
        print("get resp from server2: ", response)
        return response
