# kubernetes-job-deployment-automation
Demo app to try out kubernetes python client to automate deployment of jobs

The jobs are doing nothing useful (printing out to shell), they are placeholders just to prove the principle.
You can add your own image and command args in the job template to make it useful.

It is useful to have another command line watching your pods on the background:   
`watch -n 5 kubectl get pods`

You can verify the output of your container with:   
`kubectl logs <<POD NAME>>`

Completed jobs will not be automatically deleted. This requires the TTLAFterFinished, which is still in alpha phase.
You can delete the batch of jobs manually with:   
`kubectl delete jobs.batch <<BATCH NAME>>`   
or, if you are living on the edge:      
`kubectl delete jobs.batch --all`


## Requirements
You have a kubernetes cluster running somewhere with valid kubeconfig credentials in `~/.kube/config`.


## Tools used
**Jinja2 templating**: http://jinja.pocoo.org/docs/2.10/api/   
This is used to dynamically inject variables into the yaml file

**kubernetes python client**: https://github.com/kubernetes-client/python/blob/master/kubernetes/   
This is used to access the kubernetes API from within python