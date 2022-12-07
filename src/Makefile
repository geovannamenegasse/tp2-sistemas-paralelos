stubs:
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./ident.proto
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./pares.proto
	
run_serv_ident:
	python3 svc_ident.py $(arg1) $(arg2)

run_cli_ident:
	python3 cln_ident.py $(arg1)

run_serv_pares:
	python3 svc_pares.py $(arg1) $(arg2)

run_cli_pares:
	python3 cln_pares.py $(arg1) $(arg2)

clean:
	rm -f *pb2*