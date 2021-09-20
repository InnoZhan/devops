```bash
~ >>> kubectl get pods,svc                                                                                                                                                                                        
NAME                              READY   STATUS    RESTARTS   AGE
pod/hello-node-79b587b694-rtsn2   1/1     Running   0          9m19s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/hello-node   LoadBalancer   10.107.86.210   <pending>     5000:31154/TCP   2m44s
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          9m34s
```



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