
create-cluster:
	kind create cluster --name local --config kind-config.yml

delete-cluster:
	kind delete cluster --name local

cluster-info:
	kubectl cluster-info --context kind-local

create-ns:
	kubectl apply -f ns.yml

helm-deploy:
	helm install php-hello ./helm/php-hello --set service.type=NodePort --set service.nodePort=31234

helm-delete:
	helm delete php-hello

