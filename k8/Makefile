reg_name := kind-registry
reg_port := 5001

create-cluster:
	kind create cluster --name local --config kind-config.yml
	# use calico instead of CNI to have network policies 
	kubectl apply -f calico.yaml


cluster-info:
	kubectl cluster-info --context kind-local

create-ns: create-cluster
	kubectl apply -f ns.yml

deploy: create-ns
	helm install php-hello ./helm/php-hello --set service.type=NodePort --set service.nodePort=31234

clean:
	helm delete php-hello
	kind delete cluster --name local

start_local_registry:

	# create a registry
	@if [ "$$(docker inspect -f '{{.State.Running}}' "$(reg_name)" 2>/dev/null || true)" != 'true' ]; then \
		docker run \
			-d --restart=always -p "127.0.0.1:$(reg_port):5000" --name "$(reg_name)" \
			registry:2; \
	fi

	# connect to the registry
	@if [ "$$(docker inspect -f='{{json .NetworkSettings.Networks.kind}}' "$(reg_name)")" = 'null' ]; then \
		docker network connect "kind" "$(reg_name)"; \
	fi

push:
	docker tag php-hello localhost:$(reg_port)/php-hello
	docker push localhost:$(reg_port)/php-hello