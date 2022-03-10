import grpc
from sp_client.client.grpc import PostControllerStub, \
    Post, PostRetrieveRequest, PostListRequest

class Operation:
    def __init__(self):
        self.channel = grpc.insecure_channel('localhost:50051')
        self.stub = PostControllerStub(self.channel)
    
    def create_post(self, title=None, content=None):
        response = self.stub.Create(Post(title=title, content=content))
        print("create resp: ", response)
        return response
    def get_post(self, id=None):
        response = self.stub.Retrieve(PostRetrieveRequest(id=id))
        print("get resp: ", response)
        return response
