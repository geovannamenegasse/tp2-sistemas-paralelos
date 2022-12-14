stubs:
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./ident.proto
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./pares.proto
	
run_serv_ident:
ifeq ($(wildcard ./*pb2*.py),)
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./ident.proto
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./pares.proto
	python3 svc_ident.py $(arg1) $(arg2)
else
	python3 svc_ident.py $(arg1) $(arg2)
endif

run_cli_ident: 
ifeq ($(wildcard ./*pb2*.py),)
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./ident.proto
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./pares.proto
	python3 cln_ident.py $(arg1)
else
	python3 cln_ident.py $(arg1)
endif

run_serv_pares: 
ifeq ($(wildcard ./*pb2*.py),)
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./ident.proto
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./pares.proto
	python3 svc_pares.py $(arg1) $(arg2)
else
	python3 svc_pares.py $(arg1) $(arg2)
endif

run_cli_pares:
ifeq ($(wildcard ./*pb2*.py),)
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./ident.proto
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./pares.proto
	python3 cln_pares.py $(arg1) $(arg2)
else
	python3 cln_pares.py $(arg1) $(arg2)
endif

clean:
	rm -f *pb2*
