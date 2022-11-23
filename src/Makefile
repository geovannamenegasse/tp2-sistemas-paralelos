run_serv_ident:
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./ident.proto
	python3 ident_server.py $(arg1) $(arg2)
run_cli_ident:
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./ident.proto
	python3 ident_client.py $(arg1)

clean:
	rm -f *pb2*
	rm -r __pycache__