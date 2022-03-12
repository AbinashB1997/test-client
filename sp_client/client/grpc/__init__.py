from sp_client.client.grpc.protos.post_pb2_grpc import PostControllerStub
from sp_client.client.grpc.protos.post_pb2 import Post, PostListRequest, PostRetrieveRequest
from sp_client.client.grpc.protos.server2_pb2_grpc import GetControllerStub
from sp_client.client.grpc.protos.server2_pb2 import GetListRequest

__all__ = ["PostControllerStub", "Post", "PostListRequest", "PostRetrieveRequest",
           "GetControllerStub", "GetListRequest"]
