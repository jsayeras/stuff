## Cluster Configuration

- **Kind:** Cluster
- **API Version:** kind.x-k8s.io/v1alpha4
- **Containerd Config Patches:**
  - `[plugins."io.containerd.grpc.v1.cri".registry.mirrors."localhost:5001"]`
    - `endpoint = ["http://kind-registry:5000"]`

  Explanation: This section defines the cluster configuration. It specifies that the cluster is using Kind as the cluster provider with version v1alpha4. The containerd config patches are used to configure the container registry mirror. In this case, it sets up a mirror for the registry "localhost:5001" and points it to "http://kind-registry:5000".

## Nodes

### Control Plane Node

- **Role:** control-plane
- **Image:** kindest/node:v1.26.3@sha256:61b92f38dff6ccc29969e7aa154d34e38b89443af1a2c14e6cfbd2df6419c66f
- **Kubeadm Config Patches:**
  - ```
    kind: ClusterConfiguration
    apiServer:
        extraArgs:
          enable-admission-plugins: NodeRestriction
    ```

  Explanation: This section describes the control plane node configuration. The control-plane node is responsible for managing the cluster control plane components. It uses the `kindest/node:v1.26.3` image with a specific SHA256 digest. The Kubeadm config patches specify additional configuration for the control plane node. In this case, it enables the `NodeRestriction` admission plugin for the API server.

- **Extra Port Mappings:**
  - _(No extra port mappings configured)_

  Explanation: No additional port mappings are configured for the control plane node in this configuration.

### Worker Node

- **Role:** worker
- **Image:** kindest/node:v1.26.3@sha256:61b92f38dff6ccc29969e7aa154d34e38b89443af1a2c14e6cfbd2df6419c66f
- **Extra Port Mappings:**
  - - **Container Port:** 31234
    - **Host Port:** 8080
    - **Protocol:** TCP

  Explanation: This section describes the worker node configuration. Worker nodes are responsible for running the application workloads in the cluster. It uses the `kindest/node:v1.26.3` image with a specific SHA256 digest. The extra port mappings are used to map a container port (31234) to a host port (8080) for TCP traffic.

## Networking Configuration

- **Pod Subnet:** "10.244.0.0/16"
- **Service Subnet:** "10.96.0.0/16"
- **Disable Default CNI:** true

  Explanation: This section specifies the networking configuration for the cluster. The pod subnet is the CIDR range allocated for assigning IP addresses to pods in the cluster. The service subnet is the CIDR range used for Kubernetes service IP addresses. Disabling the default CNI (Container Network Interface) indicates that a custom networking solution is being used.

