run_serv_arm:
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./armazenamento.proto
	python3 armazenamento_server.py $(arg)
run_cli_arm:
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./armazenamento.proto
	python3 armazenamento_client.py $(arg)

run_serv_comp:
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./armazenamento.proto
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./consulta.proto
	python3 consulta_server.py $(arg1) $(arg2) $(arg3)
run_cli_comp:
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./armazenamento.proto
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./consulta.proto
	python3 consulta_client.py $(arg)

clean:
	rm -f *pb2*
	rm -r __pycache__