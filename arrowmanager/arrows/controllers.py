import os

from kubernetes import client, config

# TODO: Would be nice to create a Flask-Kube extension
from arrowmanager import models

config.load_kube_config(os.environ["HOME"] + '/.kube/config')
k8s = client.ExtensionsV1beta1Api()


def get_pod_status(namespace):
    ingress = k8s.list_namespaced_ingress(namespace=namespace)
    endpoints = [r.to_dict() for r in ingress.items[0].spec.rules]

    # Simplify while learning C# deserialization
    # return {'success': {'applications': endpoints}}
    return endpoints


def get_applications(tenant):
    result = models.Application.query.filter_by(tenant=tenant).all()
    return result
