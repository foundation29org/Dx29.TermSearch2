# Get credentials
az aks get-credentials --resource-group <resource_group_name> --name <aks_name>

# Apply sample-ingress staging
kubectl apply -f svc-deployment.yaml --namespace <namespace>
