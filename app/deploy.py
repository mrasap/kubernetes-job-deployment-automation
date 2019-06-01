from jinja2 import Environment, PackageLoader, select_autoescape
from kubernetes import config
from kubernetes.client import V1Job, BatchV1Api
from kubernetes.client.rest import ApiException
import yaml

# The environment of jinja to retrieve jinja templates from filesystem
env = Environment(
    loader=PackageLoader(package_name=__name__, package_path='templates'),
    autoescape=select_autoescape(enabled_extensions=['yaml'])
)

# Retrieve the template of the job that we will be running
job_template = env.get_template('job.yaml')


def deploy_job_batch(api_client: BatchV1Api,
                     job_id: str,
                     project_env: str,
                     completions: int,
                     parallelism: int) -> V1Job:
    """
    Deploy a batch of jobs on the kubernetes cluster.

    This is based on https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/BatchV1Api.md

    :param api_client: the API client where the job batch should be requested from.
    :param job_id: the name of the job, this needs to be unique.
    :param project_env: the environment in which the project is running. This will be used as the image tag of the job.
    :param completions: the total amount of jobs within this batch.
    :param parallelism: the amount of jobs that is allowed to run simultaneously.
    :return: The API response.
    """
    # this is the rendered job
    job: V1Job = yaml.safe_load(job_template.render(
        jobID=job_id,
        tag=project_env,
        completions=completions,
        parallelism=parallelism))

    try:
        api_response = api_client.create_namespaced_job(namespace="default", body=job)
        return api_response
    except ApiException as e:
        print("Exception when calling BatchV1Api->create_namespaced_job: %s\n" % e)


def main():
    JOB_ID: str = "one"
    PROJECT_ENV: str = "latest"
    COMPLETIONS: int = 4
    PARALLELISM: int = 2

    # Configure the kubernetes client to connect to our cluster
    # The default config expects a config file with valid credentials in ~/.kube/
    # config.load_kube_config()
    # You can also request the access from within the cluster
    # it works only if this script is run by K8s as a POD
    config.load_incluster_config()

    # this is the RESTful API instance that we can post requests to
    api_client = BatchV1Api()

    deploy_job_batch(api_client=api_client,
                     job_id=JOB_ID,
                     project_env=PROJECT_ENV,
                     completions=COMPLETIONS,
                     parallelism=PARALLELISM)


if __name__ == '__main__':
    main()
