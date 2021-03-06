# Lab 9
```bash
minikube start

kubectl create deployment hello-node  --image=zhandos1609/moscow-time:latest
kubectl expose deployment hello-node --type=LoadBalancer --port=5000
```


```bash
~ >>> kubectl get pods,svc                                                                                                                                                                                        
NAME                              READY   STATUS    RESTARTS   AGE
pod/hello-node-79b587b694-rtsn2   1/1     Running   0          9m19s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/hello-node   LoadBalancer   10.107.86.210   <pending>     5000:31154/TCP   2m44s
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          9m34s
```

```bash
kubectl delete deployment,svc hello-node
```

## Run with configuration files

```bash
~/.../lab_1_2/k8s >>> kubectl get pods,svc                                                                                                                                                              ±[●][main]
NAME                               READY   STATUS    RESTARTS   AGE
pod/moscow-time-7fb75cb9fc-jsdr5   1/1     Running   0          2m22s
pod/moscow-time-7fb75cb9fc-s8pc6   1/1     Running   0          2m22s
pod/moscow-time-7fb75cb9fc-sppkz   1/1     Running   0          2m22s

NAME                  TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes    ClusterIP      10.96.0.1        <none>        443/TCP          54m
service/moscow-time   LoadBalancer   10.101.194.113   <pending>     5000:32170/TCP   13s
```

# Lab 10

```bash
helm create moscow-time
helm package moscow-time
helm install moscow-time ./moscow-time-0.1.0.tgz

minikube service moscow-time
```

```bash
~/.../lab_1_2/k8s >>> kubectl get pod,svc                                                                                                                                                               ±[●][main]
NAME                               READY   STATUS    RESTARTS   AGE
pod/moscow-time-8475cf98cb-2vfth   1/1     Running   0          8m48s

NAME                  TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes    ClusterIP      10.96.0.1       <none>        443/TCP          85m
service/moscow-time   LoadBalancer   10.100.26.151   <pending>     5000:30246/TCP   8m48s
```
