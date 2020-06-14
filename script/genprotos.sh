#!/usr/bin/env bash
python -m grpc_tools.protoc -I../server/pb --python_out=../server/pb --grpc_python_out=../server/pb ../server/pb/SimpleChatbot.proto
