import os

from kubernetes import client, config

# TODO: Would be nice to create a Flask-Kube extension
from arrowmanager import models

config.load_kube_config(os.environ["HOME"] + '/.kube/config')
k8s = client.ExtensionsV1beta1Api()


def get_pod_status(namespace):
    # TODO: use this k8s.list_namespaced_pod()
    # pods = k8s.list_pod_for_all_namespaces()
    pods = k8s.list_namespaced_ingress(namespace=namespace)

    return {'success': [u.to_dict() for u in pods.items]}


def get_applications(tenant):
    result = models.Application.query.filter_by(tenant=tenant).all()
    return result
