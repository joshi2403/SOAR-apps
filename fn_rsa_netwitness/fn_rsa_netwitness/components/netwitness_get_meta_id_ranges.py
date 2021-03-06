# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright © IBM Corporation 2010, 2019
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, \
    StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, ResultPayload, RequestsCommon
from fn_rsa_netwitness.util.helper import get_headers

log = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'netwitness_get_meta_id_ranges"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_rsa_netwitness", {})

        # Validate app.config fields
        validate_fields(["nw_packet_server_url", "nw_packet_server_user",
                         "nw_packet_server_password"], self.options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_rsa_netwitness", {})
        # Validate app.config fields
        validate_fields(["nw_packet_server_url", "nw_packet_server_user",
                         "nw_packet_server_password"], self.options)

    @function("netwitness_get_meta_id_ranges")
    def _netwitness_get_meta_id_ranges(self, event, *args, **kwargs):
        """Function: Returns back the meta id ranges for a single session or consecutive sessions"""
        try:
            yield StatusMessage("Getting meta id ranges...")
            # Get the function parameters:
            nw_session_id1 = str(kwargs.get("nw_session_id1"))  # number
            nw_session_id2 = str(kwargs.get("nw_session_id2"))  # number
            nw_results_size = str(kwargs.get("nw_results_size", ''))  # number

            # Initialize resilient_lib objects
            result_payload = ResultPayload("fn_rsa_netwitness", **kwargs)
            req_common = RequestsCommon(self.opts)

            log.info("nw_event_session_id1: %s", nw_session_id1)
            log.info("nw_event_session_id2: %s", nw_session_id2)
            log.info("nw_results_size: %s", nw_results_size)

            # Get meta id ranges from Netwitness
            nw_query_metadata = get_meta_id_ranges(self.options.get("nw_packet_server_url"),
                                                   self.options.get("nw_packet_server_user"),
                                                   self.options.get("nw_packet_server_password"),
                                                   self.options.get("nw_packet_server_verify"),
                                                   nw_session_id1, nw_session_id2,
                                                   req_common, size=nw_results_size)

            log.debug(nw_query_metadata)

            if nw_query_metadata:
                StatusMessage("Meta ID ranges found")
            else:
                StatusMessage("No meta ID ranges found")
            yield StatusMessage("Complete...")
            results = result_payload.done(True,\
                nw_query_metadata.json() if nw_query_metadata else None)
            log.debug("RESULTS: %s", results)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as error:
            yield FunctionError(error)


def get_meta_id_ranges(url, user, passw, cafile, id1, id2, req_common, size=""):
    headers = get_headers(user, passw)
    if size:
        size = "&size={}".format(size)
    request_url = "{}/sdk?msg=session&id1={}&id2={}&force-content-type=application/json{}" \
        .format(url, id1, id2, size)

    return req_common.execute_call_v2("GET", request_url, verify=cafile, headers=headers)
