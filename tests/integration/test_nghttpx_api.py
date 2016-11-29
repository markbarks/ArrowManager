import pytest
import requests


def _nghttpx_not_running():
    return False


"""
API ENDPOINTS
nghttpx exposes API endpoints to manipulate it via HTTP based API.
By default, API endpoint is disabled. To enable it, add a dedicated
frontend for API using --frontend option with "api" parameter. All
requests which come from this frontend address, will be treated as
API request.

The response is normally JSON dictionary, and at least includes the
following keys:

status
    The status of the request processing. The following values are defined:

    Success
        The request was successful.
    Failure
        The request was failed. No change has been made.

code
    HTTP status code

We wrote "normally", since nghttpx may return ordinal HTML response
in some cases where the error has occurred before reaching API
endpoint (e.g., header field is too large).

The following section describes available API endpoints.

PUT /api/v1beta1/backendconfig

    This API replaces the current backend server settings with the
    requested ones. The request method should be PUT, but POST is also
    acceptable. The request body must be nghttpx configuration file
    format. For configuration file format, see FILES section. The line
    separator inside the request body must be single LF (0x0A).
    Currently, only backend option is parsed, the others are simply
    ignored. The semantics of this API is replace the current backend
    with the backend options in request body. Describe the desired set
    of backend severs, and nghttpx makes it happen. If there is no
    backend option is found in request body, the current set of
    backend is replaced with the backend option's default value,
    which is 127.0.0.1,80.

    The replacement is done instantly without breaking existing connections
    or requests. It also avoids any process creation as is the case with
    hot swapping with signals.

    The one limitation is that only numeric IP address is allowd in backend
    in request body while non numeric hostname is allowed in command-line
    or configuration file is read using --conf.
"""


class TestK8sclient:

    # def test_update_ingress(self):


    @pytest.mark.skipif(_nghttpx_not_running(), reason="Kubernetes is not available")
    def test_update_backendconfig(self):
        conf = open('/Volumes/Users/markns/Projects/Alder/ArrowKube/nghttpx/nghttpx.conf').read()

        print(conf)

        r = requests.put('http://192.168.99.100:30481/api/v1beta1/backendconfig'
                         , data=conf)
        # )
        print(r.status_code)

        # endpoints = k8s.list_endpoints_for_all_namespaces()
        # assert len(endpoints.items) > 0
