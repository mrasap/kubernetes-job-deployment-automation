# kubernetes-job-deployment-automation
Demo app to try out kubernetes python client to automate deployment of jobs

The jobs are doing nothing useful (printing out to shell), they are placeholders just to prove the principle.
You can add your own image and command args in the job template to make it useful.

## Requirements
You have a kubernetes cluster running somewhere with valid kubeconfig credentials in `~/.kube/config`.

My kubernetes setup (`kubectl version`):   
```
Client Version: version.Info{Major:"1", Minor:"14", GitVersion:"v1.14.1", GitCommit:"b7394102d6ef778017f2ca4046abbaa23b88c290", GitTreeState:"clean", BuildDate:"2019-04-08T17:11:31Z", GoVersion:"go1.12.1", Compiler:"gc", Platform:"linux/amd64"}
Server Version: version.Info{Major:"1", Minor:"14", GitVersion:"v1.14.2", GitCommit:"66049e3b21efe110454d67df4fa62b08ea79a19b", GitTreeState:"clean", BuildDate:"2019-05-16T16:14:56Z", GoVersion:"go1.12.5", Compiler:"gc", Platform:"linux/amd64"}
```

## How to run

#### DISCLAMER
Never run a shell script without verifying the code yourself. 

```
chmod +x ./deploy.sh
./deploy.sh
```


It is useful to have another command line watching your pods on the background:   
`watch -n 5 kubectl get pods --namespace jobs`

You can verify the output of your container with:   
`kubectl logs <<POD NAME>> --namespace jobs`

#### Cleanup
Completed jobs may not be automatically deleted. This requires the TTLAFterFinished, which is still in alpha phase.
You can delete the batch of jobs manually with:   
`kubectl delete jobs.batch <<BATCH NAME>> --namespace jobs`   
or, if you have multiple batches of jobs:         
`kubectl delete jobs.batch --all --namespace jobs`

Alternatively, you can also just delete the complete namespace:   
`kubectl delete namespace jobs`   

**Note**: If the image cannot be found, you may need to rebuild the docker image, push to a registry and update the image.

## Tools used
**Jinja2 templating**: http://jinja.pocoo.org/docs/2.10/api/   
This is used to dynamically inject variables into the yaml file

**kubernetes python client**: https://github.com/kubernetes-client/python/blob/master/kubernetes/   
This is used to access the kubernetes API from within python