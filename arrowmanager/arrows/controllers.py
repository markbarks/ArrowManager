import os

from kubernetes import client, config

# TODO: Would be nice to create a Flask-Kube extension
from arrowmanager import models

config.load_kube_config(os.environ["HOME"] + '/.kube/config')
k8s = client.ExtensionsV1beta1Api()


def get_pod_status(namespace):
    ingress = k8s.list_namespaced_ingress(namespace=namespace)

    endpoints = [
        {"key": r.host.split(".")[0],
         "host": r.host}
        for r in ingress.items[0].spec.rules
        ]

    if 'FLASK_DEBUG' in os.environ:
        import socket
        myip = socket.gethostbyname(socket.gethostname())
        endpoints.append({
            "key": "devapp",
            "host": "{}:50051".format(myip)})

    # Simplify while learning C# deserialization
    # return {'success': {'applications': endpoints}}
    return endpoints


def get_applications(tenant):
    result = models.Application.query.filter_by(tenant=tenant).all()
    return result
