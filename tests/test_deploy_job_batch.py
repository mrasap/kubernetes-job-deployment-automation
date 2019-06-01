from mock import Mock
from app.deploy import deploy_job_batch


def test_deploy_job_batch():
    api_mock = Mock()
    deploy_job_batch(api_client=api_mock,
                     job_id="two",
                     project_env="latest",
                     completions=1,
                     parallelism=1)

    api_mock.create_namespaced_job.assert_called()
