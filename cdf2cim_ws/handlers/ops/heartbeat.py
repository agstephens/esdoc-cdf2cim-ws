# -*- coding: utf-8 -*-

"""
.. module:: handlers.heartbeat.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: ES-DOC CDF2CIM - heartbeat endpoint.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import datetime as dt

import tornado

import cdf2cim_ws
from cdf2cim_ws.utils.http import process_request



class HeartbeatRequestHandler(tornado.web.RequestHandler):
    """Operations heartbeat request handler.

    """
    def get(self):
        """HTTP GET handler.

        """
        def _set_output():
            """Sets response to be returned to client.

            """
            self.output = {
                "message": "ES-DOC CDF2CIM web service is operational @ {}".format(dt.datetime.now()),
                "version": cdf2cim_ws.__version__
            }

        # Process request.
        process_request(self, _set_output)
