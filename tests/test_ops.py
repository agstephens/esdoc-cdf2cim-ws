# -*- coding: utf-8 -*-

"""
.. module:: test_ops.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Executes web-service operations (ops) endpoint tests.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import os

import requests



# Set of target urls.
_URL_HEARTBEAT = "{}/".format(os.getenv("CDF2CIM_WS_HOST"))


def test_heartbeat():
    """CDF2CIM :: WS :: Postive Test :: Ops heartbeat.

    """
    # Invoke WS endpoint.
    url = _URL_HEARTBEAT
    response = requests.get(_URL_HEARTBEAT)

    # Assert WS response.
    response = _assert_ws_response(url, response)

    assert "message" in response
    assert "version" in response


def _assert_ws_response(
    url,
    response,
    status_code=requests.codes.OK,
    expected_content=None
    ):
    """Asserts a response received from web-service.

    """
    # WS url.
    assert response.url == url

    # WS response HTTP status code.
    assert response.status_code == status_code

    # WS response = unicode.
    assert isinstance(response.text, unicode)

    # WS response has no cookies.
    assert len(response.cookies) == 0

    # WS response history is empty (i.e. no intermediate servers).
    assert len(response.history) == 0
    assert response.is_permanent_redirect == False
    assert response.is_redirect == False
    assert len(response.links) == 0

    # Default WS respponse headers.
    assert len(response.headers) >= 3
    for header in {
        # 'Content-Length',
        'Content-Type',
        'Date',
        'Server',
        'Vary'
        }:
        assert header in response.headers

    # WS response content must be utf-8 encoded JSON.
    if response.text:
        assert response.encoding == u'utf-8'
        content = response.json()
        assert isinstance(content, dict)

        # WS response content.
        if expected_content is not None:
            assert content == expected_content

        return content
