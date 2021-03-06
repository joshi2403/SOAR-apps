# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_calendar_invite"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_calendar_invite]
# Setup the email information for the sender of the calendar_invite email 
email_username=user@example.com
email_password=xxx
email_nickname=Resilient Meeting Organizer
email_host=mail.example.com
email_port=25
#http_proxy=
#https_proxy= 
"""
    return config_data