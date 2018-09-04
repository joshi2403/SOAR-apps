# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_create_webex_meeting"""

from __future__ import print_function
from resilient_circuits.util import *


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Function inputs:
    #     webex_meeting_agenda
    #     webex_meeting_end_time
    #     webex_meeting_name
    #     webex_meeting_password
    #     webex_meeting_start_time
    #   Message Destinations:
    #     fn_create_webex_meeting
    #   Functions:
    #     fn_create_webex_meeting
    #   Workflows:
    #     example_create_webex_meeting
    #   Rules:
    #     Example: Create WebEx Meeting: Incident


    yield ImportDefinition(u"""
eyJ0YXNrX29yZGVyIjogW10sICJ3b3JrZmxvd3MiOiBbeyJ1dWlkIjogIjRjNWI3ZWIzLTFjMmIt
NDExZi1iZDgzLWI0YTExZTA2ZjgwMSIsICJkZXNjcmlwdGlvbiI6ICJBbiBleGFtcGxlIHRoYXQg
Y3JlYXRlcyBhIENpc2NvIFdlYkV4IG1lZXRpbmcgYmFzZWQgb24gaW5jaWRlbnQgcHJvcGVydGll
cy4iLCAib2JqZWN0X3R5cGUiOiAiaW5jaWRlbnQiLCAiZXhwb3J0X2tleSI6ICJleGFtcGxlX2Ny
ZWF0ZV93ZWJleF9tZWV0aW5nIiwgIndvcmtmbG93X2lkIjogMSwgImxhc3RfbW9kaWZpZWRfYnki
OiAiYUBhLmNvbSIsICJjb250ZW50IjogeyJ4bWwiOiAiPD94bWwgdmVyc2lvbj1cIjEuMFwiIGVu
Y29kaW5nPVwiVVRGLThcIj8+PGRlZmluaXRpb25zIHhtbG5zPVwiaHR0cDovL3d3dy5vbWcub3Jn
L3NwZWMvQlBNTi8yMDEwMDUyNC9NT0RFTFwiIHhtbG5zOmJwbW5kaT1cImh0dHA6Ly93d3cub21n
Lm9yZy9zcGVjL0JQTU4vMjAxMDA1MjQvRElcIiB4bWxuczpvbWdkYz1cImh0dHA6Ly93d3cub21n
Lm9yZy9zcGVjL0RELzIwMTAwNTI0L0RDXCIgeG1sbnM6b21nZGk9XCJodHRwOi8vd3d3Lm9tZy5v
cmcvc3BlYy9ERC8yMDEwMDUyNC9ESVwiIHhtbG5zOnJlc2lsaWVudD1cImh0dHA6Ly9yZXNpbGll
bnQuaWJtLmNvbS9icG1uXCIgeG1sbnM6eHNkPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxT
Y2hlbWFcIiB4bWxuczp4c2k9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYS1pbnN0
YW5jZVwiIHRhcmdldE5hbWVzcGFjZT1cImh0dHA6Ly93d3cuY2FtdW5kYS5vcmcvdGVzdFwiPjxw
cm9jZXNzIGlkPVwiZXhhbXBsZV9jcmVhdGVfd2ViZXhfbWVldGluZ1wiIGlzRXhlY3V0YWJsZT1c
InRydWVcIiBuYW1lPVwiRXhhbXBsZTogQ3JlYXRlIFdlYkV4IE1lZXRpbmc6IEluY2lkZW50XCI+
PGRvY3VtZW50YXRpb24+QW4gZXhhbXBsZSB0aGF0IGNyZWF0ZXMgYSBDaXNjbyBXZWJFeCBtZWV0
aW5nIGJhc2VkIG9uIGluY2lkZW50IHByb3BlcnRpZXMuPC9kb2N1bWVudGF0aW9uPjxzdGFydEV2
ZW50IGlkPVwiU3RhcnRFdmVudF8xNTVhc3htXCI+PG91dGdvaW5nPlNlcXVlbmNlRmxvd18weHp5
b2tpPC9vdXRnb2luZz48L3N0YXJ0RXZlbnQ+PHNlcnZpY2VUYXNrIGlkPVwiU2VydmljZVRhc2tf
MGIwb3V3ZFwiIG5hbWU9XCJDcmVhdGUgV2ViRXggTWVldGluZ1wiIHJlc2lsaWVudDp0eXBlPVwi
ZnVuY3Rpb25cIj48ZXh0ZW5zaW9uRWxlbWVudHM+PHJlc2lsaWVudDpmdW5jdGlvbiB1dWlkPVwi
YWI5YmQ2M2EtNzI4ZS00YzgwLWFhMzYtMjdlMjg4ODEzYzM0XCI+e1wiaW5wdXRzXCI6e30sXCJw
cmVfcHJvY2Vzc2luZ19zY3JpcHRcIjpcIiMgVG8gc2V0IG1lZXRpbmcgbmFtZSB0byB0aGUgd29y
a2Zsb3cgaW5wdXRzLCB1bmNvbW1lbnQgdGhlIGZvbGxvd2luZyBsaW5lc1xcbiMgaW5wdXRzLndl
YmV4X21lZXRpbmdfbmFtZSA9IGluY2lkZW50Lm5hbWVcXG4jIGlmIGluY2lkZW50LmRlc2NyaXB0
aW9uIGlzIG5vdCBOb25lIGFuZCBpbmNpZGVudC5kZXNjcmlwdGlvbi5jb250ZW50IGlzIG5vdCBO
b25lOlxcbiMgICBpbnB1dHMud2ViZXhfbWVldGluZ19hZ2VuZGEgPSBpbmNpZGVudC5kZXNjcmlw
dGlvbi5jb250ZW50XFxuIyBlbHNlOlxcbiMgICBpbnB1dHMud2ViZXhfbWVldGluZ19hZ2VuZGEg
PSBcXFwiXFxcIlwiLFwicmVzdWx0X25hbWVcIjpcIlwiLFwicG9zdF9wcm9jZXNzaW5nX3Njcmlw
dFwiOlwiXFxuXFxuaG9zdF91cmwgPSByZXN1bHRzLmhvc3RfdXJsXFxuYXR0ZW5kZWVfdXJsID0g
cmVzdWx0cy5hdHRlbmRlZV91cmxcXG5cXG5pZiBob3N0X3VybCBpcyBOb25lOlxcbiAgaG9zdF91
cmwgPSBcXFwiXFxcIlxcblxcbmlmIGF0dGVuZGVlX3VybCBpcyBOb25lOlxcbiAgYXR0ZW5kZWVf
dXJsID0gXFxcIlxcXCJcXG5cXG50ZXh0ID0gXFxcIkNpc2NvIFdlYkV4IE1lZXRpbmc6XFxcXG5c
XFxcdEhvc3QgVVJMOiBcXFwiICsgcmVzdWx0cy5ob3N0X3VybCArIFxcXCJcXFxcblxcXFx0QXR0
ZW5kZWUgVVJMOiBcXFwiICsgcmVzdWx0cy5hdHRlbmRlZV91cmxcXG5ub3RlID0gaGVscGVyLmNy
ZWF0ZVBsYWluVGV4dCh0ZXh0KVxcbmluY2lkZW50LmFkZE5vdGUobm90ZSlcIn08L3Jlc2lsaWVu
dDpmdW5jdGlvbj48L2V4dGVuc2lvbkVsZW1lbnRzPjxpbmNvbWluZz5TZXF1ZW5jZUZsb3dfMHh6
eW9raTwvaW5jb21pbmc+PG91dGdvaW5nPlNlcXVlbmNlRmxvd18wa2xyY245PC9vdXRnb2luZz48
L3NlcnZpY2VUYXNrPjxzZXF1ZW5jZUZsb3cgaWQ9XCJTZXF1ZW5jZUZsb3dfMHh6eW9raVwiIHNv
dXJjZVJlZj1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlNlcnZpY2VUYXNrXzBi
MG91d2RcIi8+PGVuZEV2ZW50IGlkPVwiRW5kRXZlbnRfMHJ1bjRseFwiPjxpbmNvbWluZz5TZXF1
ZW5jZUZsb3dfMGtscmNuOTwvaW5jb21pbmc+PC9lbmRFdmVudD48c2VxdWVuY2VGbG93IGlkPVwi
U2VxdWVuY2VGbG93XzBrbHJjbjlcIiBzb3VyY2VSZWY9XCJTZXJ2aWNlVGFza18wYjBvdXdkXCIg
dGFyZ2V0UmVmPVwiRW5kRXZlbnRfMHJ1bjRseFwiLz48dGV4dEFubm90YXRpb24gaWQ9XCJUZXh0
QW5ub3RhdGlvbl8xa3h4aXl0XCI+PHRleHQ+U3RhcnQgeW91ciB3b3JrZmxvdyBoZXJlPC90ZXh0
PjwvdGV4dEFubm90YXRpb24+PGFzc29jaWF0aW9uIGlkPVwiQXNzb2NpYXRpb25fMXNldWo0OFwi
IHNvdXJjZVJlZj1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlRleHRBbm5vdGF0
aW9uXzFreHhpeXRcIi8+PHRleHRBbm5vdGF0aW9uIGlkPVwiVGV4dEFubm90YXRpb25fMW84bWR4
b1wiPjx0ZXh0PmlucHV0czpcdTAwYTB3ZWJleF9tZWV0aW5nX25hbWUsIHdlYmV4X21lZXRpbmdf
YWdlbmRhLCBhbmQgd2ViZXhfbWVldGluZ19wYXNzd29yZDwvdGV4dD48L3RleHRBbm5vdGF0aW9u
Pjxhc3NvY2lhdGlvbiBpZD1cIkFzc29jaWF0aW9uXzBmMzBxb3hcIiBzb3VyY2VSZWY9XCJTZXJ2
aWNlVGFza18wYjBvdXdkXCIgdGFyZ2V0UmVmPVwiVGV4dEFubm90YXRpb25fMW84bWR4b1wiLz48
dGV4dEFubm90YXRpb24gaWQ9XCJUZXh0QW5ub3RhdGlvbl8wZTdkcXN6XCI+PHRleHQ+b3V0cHV0
czogaG9zdF91cmwgYW5kIGF0dGVuZGVlX3VybCBhZGRlZCB0byBpbmNpZGVudCBub3RlczwvdGV4
dD48L3RleHRBbm5vdGF0aW9uPjxhc3NvY2lhdGlvbiBpZD1cIkFzc29jaWF0aW9uXzE3M2s1dm5c
IiBzb3VyY2VSZWY9XCJTZXJ2aWNlVGFza18wYjBvdXdkXCIgdGFyZ2V0UmVmPVwiVGV4dEFubm90
YXRpb25fMGU3ZHFzelwiLz48L3Byb2Nlc3M+PGJwbW5kaTpCUE1ORGlhZ3JhbSBpZD1cIkJQTU5E
aWFncmFtXzFcIj48YnBtbmRpOkJQTU5QbGFuZSBicG1uRWxlbWVudD1cInVuZGVmaW5lZFwiIGlk
PVwiQlBNTlBsYW5lXzFcIj48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlN0YXJ0RXZl
bnRfMTU1YXN4bVwiIGlkPVwiU3RhcnRFdmVudF8xNTVhc3htX2RpXCI+PG9tZ2RjOkJvdW5kcyBo
ZWlnaHQ9XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiMTYyXCIgeT1cIjE4OFwiLz48YnBtbmRpOkJQ
TU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjBcIiB3aWR0aD1cIjkwXCIgeD1cIjE1N1wi
IHk9XCIyMjNcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRp
OkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIiBpZD1cIlRl
eHRBbm5vdGF0aW9uXzFreHhpeXRfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjMwXCIgd2lk
dGg9XCIxMDBcIiB4PVwiOTlcIiB5PVwiMjU0XCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRp
OkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiQXNzb2NpYXRpb25fMXNldWo0OFwiIGlkPVwiQXNzb2Np
YXRpb25fMXNldWo0OF9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTY5XCIgeHNpOnR5cGU9XCJv
bWdkYzpQb2ludFwiIHk9XCIyMjBcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIxNTNcIiB4c2k6dHlw
ZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjI1NFwiLz48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQ
TU5TaGFwZSBicG1uRWxlbWVudD1cIlNlcnZpY2VUYXNrXzBiMG91d2RcIiBpZD1cIlNlcnZpY2VU
YXNrXzBiMG91d2RfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjgwXCIgd2lkdGg9XCIxMDBc
IiB4PVwiMzE1XCIgeT1cIjE2NlwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRn
ZSBicG1uRWxlbWVudD1cIlNlcXVlbmNlRmxvd18weHp5b2tpXCIgaWQ9XCJTZXF1ZW5jZUZsb3df
MHh6eW9raV9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTk4XCIgeHNpOnR5cGU9XCJvbWdkYzpQ
b2ludFwiIHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIzMTVcIiB4c2k6dHlwZT1cIm9t
Z2RjOlBvaW50XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhl
aWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjI1Ni41XCIgeT1cIjE4NFwiLz48L2JwbW5kaTpC
UE1OTGFiZWw+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9
XCJFbmRFdmVudF8wcnVuNGx4XCIgaWQ9XCJFbmRFdmVudF8wcnVuNGx4X2RpXCI+PG9tZ2RjOkJv
dW5kcyBoZWlnaHQ9XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiNTI0XCIgeT1cIjE4OFwiLz48YnBt
bmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1c
IjU0MlwiIHk9XCIyMjdcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48
YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVuY2VGbG93XzBrbHJjbjlcIiBpZD1c
IlNlcXVlbmNlRmxvd18wa2xyY245X2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCI0MTVcIiB4c2k6
dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjUyNFwi
IHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxv
bWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiNDY5LjVcIiB5PVwiMTg0
XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQTU5TaGFw
ZSBicG1uRWxlbWVudD1cIlRleHRBbm5vdGF0aW9uXzFvOG1keG9cIiBpZD1cIlRleHRBbm5vdGF0
aW9uXzFvOG1keG9fZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjMxXCIgd2lkdGg9XCI0MTFc
IiB4PVwiLTk1XCIgeT1cIjYxXCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdl
IGJwbW5FbGVtZW50PVwiQXNzb2NpYXRpb25fMGYzMHFveFwiIGlkPVwiQXNzb2NpYXRpb25fMGYz
MHFveF9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMzE1XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2lu
dFwiIHk9XCIxODFcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIxNDFcIiB4c2k6dHlwZT1cIm9tZ2Rj
OlBvaW50XCIgeT1cIjkyXCIvPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJw
bW5FbGVtZW50PVwiVGV4dEFubm90YXRpb25fMGU3ZHFzelwiIGlkPVwiVGV4dEFubm90YXRpb25f
MGU3ZHFzel9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzBcIiB3aWR0aD1cIjMzNlwiIHg9
XCI0MDVcIiB5PVwiNjJcIi8+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBt
bkVsZW1lbnQ9XCJBc3NvY2lhdGlvbl8xNzNrNXZuXCIgaWQ9XCJBc3NvY2lhdGlvbl8xNzNrNXZu
X2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCI0MTNcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIg
eT1cIjE3NFwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjUzMlwiIHhzaTp0eXBlPVwib21nZGM6UG9p
bnRcIiB5PVwiOTJcIi8+PC9icG1uZGk6QlBNTkVkZ2U+PC9icG1uZGk6QlBNTlBsYW5lPjwvYnBt
bmRpOkJQTU5EaWFncmFtPjwvZGVmaW5pdGlvbnM+IiwgIndvcmtmbG93X2lkIjogImV4YW1wbGVf
Y3JlYXRlX3dlYmV4X21lZXRpbmciLCAidmVyc2lvbiI6IDIzfSwgImxhc3RfbW9kaWZpZWRfdGlt
ZSI6IDE1MzU0NjY2ODM5MDcsICJjcmVhdG9yX2lkIjogImFAYS5jb20iLCAiYWN0aW9ucyI6IFtd
LCAicHJvZ3JhbW1hdGljX25hbWUiOiAiZXhhbXBsZV9jcmVhdGVfd2ViZXhfbWVldGluZyIsICJu
YW1lIjogIkV4YW1wbGU6IENyZWF0ZSBXZWJFeCBNZWV0aW5nOiBJbmNpZGVudCJ9XSwgImFjdGlv
bnMiOiBbeyJsb2dpY190eXBlIjogImFsbCIsICJuYW1lIjogIkV4YW1wbGU6IENyZWF0ZSBXZWJF
eCBNZWV0aW5nOiBJbmNpZGVudCIsICJ2aWV3X2l0ZW1zIjogW10sICJ0eXBlIjogMSwgIndvcmtm
bG93cyI6IFsiZXhhbXBsZV9jcmVhdGVfd2ViZXhfbWVldGluZyJdLCAib2JqZWN0X3R5cGUiOiAi
aW5jaWRlbnQiLCAidGltZW91dF9zZWNvbmRzIjogODY0MDAsICJ1dWlkIjogImZiODRkZWRjLWMw
NWEtNDAwMy04YTM1LWM2MjYyZTIwNTIwZCIsICJhdXRvbWF0aW9ucyI6IFtdLCAiZXhwb3J0X2tl
eSI6ICJFeGFtcGxlOiBDcmVhdGUgV2ViRXggTWVldGluZzogSW5jaWRlbnQiLCAiY29uZGl0aW9u
cyI6IFtdLCAiaWQiOiAzNCwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogW119XSwgImxheW91dHMi
OiBbXSwgImV4cG9ydF9mb3JtYXRfdmVyc2lvbiI6IDIsICJpZCI6IDQsICJpbmR1c3RyaWVzIjog
bnVsbCwgInBoYXNlcyI6IFtdLCAiYWN0aW9uX29yZGVyIjogW10sICJnZW9zIjogbnVsbCwgInNl
cnZlcl92ZXJzaW9uIjogeyJtYWpvciI6IDMwLCAidmVyc2lvbiI6ICIzMC4zLjcyIiwgImJ1aWxk
X251bWJlciI6IDcyLCAibWlub3IiOiAzfSwgInRpbWVmcmFtZXMiOiBudWxsLCAid29ya3NwYWNl
cyI6IFtdLCAiYXV0b21hdGljX3Rhc2tzIjogW10sICJmdW5jdGlvbnMiOiBbeyJkaXNwbGF5X25h
bWUiOiAiQ3JlYXRlIFdlYkV4IE1lZXRpbmciLCAiZGVzY3JpcHRpb24iOiB7ImNvbnRlbnQiOiAi
Q3JlYXRlcyBhIHdlYmV4IG1lZXRpbmcgYW5kIHJldHVybnMgdGhlIFVSTCIsICJmb3JtYXQiOiAi
dGV4dCJ9LCAiY3JlYXRvciI6IHsiZGlzcGxheV9uYW1lIjogIlJlc2lsaWVudCBTeXNhZG1pbiIs
ICJ0eXBlIjogInVzZXIiLCAiaWQiOiAyLCAibmFtZSI6ICJhQGEuY29tIn0sICJ2aWV3X2l0ZW1z
IjogW3sic2hvd19pZiI6IG51bGwsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hvd19s
aW5rX2hlYWRlciI6IGZhbHNlLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImNvbnRlbnQiOiAi
MTQ0MzhkYzctNDg3NC00OTcxLTlhYTctNTU5NmIxMzI3NmExIiwgInN0ZXBfbGFiZWwiOiBudWxs
fSwgeyJzaG93X2lmIjogbnVsbCwgImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2xp
bmtfaGVhZGVyIjogZmFsc2UsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiY29udGVudCI6ICI0
YjE3OTg5Ny0zY2ZjLTRhOTgtODg2NC1kOWMwOWU2ODVkNWEiLCAic3RlcF9sYWJlbCI6IG51bGx9
LCB7InNob3dfaWYiOiBudWxsLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9uIiwgInNob3dfbGlu
a19oZWFkZXIiOiBmYWxzZSwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJjb250ZW50IjogIjAz
ZGQxNTMxLWFjYmItNGRiOC05OTUwLTUzNTIwZWFiYmI1YyIsICJzdGVwX2xhYmVsIjogbnVsbH0s
IHsic2hvd19pZiI6IG51bGwsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hvd19saW5r
X2hlYWRlciI6IGZhbHNlLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImNvbnRlbnQiOiAiNTcw
NmFjNjItOTdlZS00YjU0LTk4MDctOWY0YjEyNGVjZWNjIiwgInN0ZXBfbGFiZWwiOiBudWxsfSwg
eyJzaG93X2lmIjogbnVsbCwgImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2xpbmtf
aGVhZGVyIjogZmFsc2UsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiY29udGVudCI6ICI5ZDM2
OGEyZi1lZGY0LTQzNTMtYThiYS0zN2Y4NmM1YTg0ZTciLCAic3RlcF9sYWJlbCI6IG51bGx9XSwg
ImV4cG9ydF9rZXkiOiAiZm5fY3JlYXRlX3dlYmV4X21lZXRpbmciLCAidXVpZCI6ICJhYjliZDYz
YS03MjhlLTRjODAtYWEzNi0yN2UyODg4MTNjMzQiLCAibGFzdF9tb2RpZmllZF9ieSI6IHsiZGlz
cGxheV9uYW1lIjogIlJlc2lsaWVudCBTeXNhZG1pbiIsICJ0eXBlIjogInVzZXIiLCAiaWQiOiAy
LCAibmFtZSI6ICJhQGEuY29tIn0sICJ2ZXJzaW9uIjogMywgIndvcmtmbG93cyI6IFt7ImRlc2Ny
aXB0aW9uIjogbnVsbCwgIm9iamVjdF90eXBlIjogImluY2lkZW50IiwgImFjdGlvbnMiOiBbXSwg
Im5hbWUiOiAiRXhhbXBsZTogQ3JlYXRlIFdlYkV4IE1lZXRpbmc6IEluY2lkZW50IiwgIndvcmtm
bG93X2lkIjogMSwgInByb2dyYW1tYXRpY19uYW1lIjogImV4YW1wbGVfY3JlYXRlX3dlYmV4X21l
ZXRpbmciLCAidXVpZCI6IG51bGx9XSwgImxhc3RfbW9kaWZpZWRfdGltZSI6IDE1MzU0NjU4NDA2
OTAsICJkZXN0aW5hdGlvbl9oYW5kbGUiOiAiZm5fY3JlYXRlX3dlYmV4X21lZXRpbmciLCAiaWQi
OiAxLCAibmFtZSI6ICJmbl9jcmVhdGVfd2ViZXhfbWVldGluZyJ9XSwgIm5vdGlmaWNhdGlvbnMi
OiBudWxsLCAicmVndWxhdG9ycyI6IG51bGwsICJpbmNpZGVudF90eXBlcyI6IFt7ImNyZWF0ZV9k
YXRlIjogMTUzNTQ2NzYxOTAwNiwgImRlc2NyaXB0aW9uIjogIkN1c3RvbWl6YXRpb24gUGFja2Fn
ZXMgKGludGVybmFsKSIsICJleHBvcnRfa2V5IjogIkN1c3RvbWl6YXRpb24gUGFja2FnZXMgKGlu
dGVybmFsKSIsICJpZCI6IDAsICJuYW1lIjogIkN1c3RvbWl6YXRpb24gUGFja2FnZXMgKGludGVy
bmFsKSIsICJ1cGRhdGVfZGF0ZSI6IDE1MzU0Njc2MTkwMDYsICJ1dWlkIjogImJmZWVjMmQ0LTM3
NzAtMTFlOC1hZDM5LTRhMDAwNDA0NGFhMCIsICJlbmFibGVkIjogZmFsc2UsICJzeXN0ZW0iOiBm
YWxzZSwgInBhcmVudF9pZCI6IG51bGwsICJoaWRkZW4iOiBmYWxzZX1dLCAic2NyaXB0cyI6IFtd
LCAidHlwZXMiOiBbXSwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogW3sidXVpZCI6ICI5N2NiMzJl
Yy04YmJmLTRkZGItYTNhZC00ZWNiNDY2NDM2ZDEiLCAiZXhwb3J0X2tleSI6ICJmbl9jcmVhdGVf
d2ViZXhfbWVldGluZyIsICJuYW1lIjogImZuX2NyZWF0ZV93ZWJleF9tZWV0aW5nIiwgImRlc3Rp
bmF0aW9uX3R5cGUiOiAwLCAicHJvZ3JhbW1hdGljX25hbWUiOiAiZm5fY3JlYXRlX3dlYmV4X21l
ZXRpbmciLCAiZXhwZWN0X2FjayI6IHRydWUsICJ1c2VycyI6IFsiYUBhLmNvbSJdfV0sICJpbmNp
ZGVudF9hcnRpZmFjdF90eXBlcyI6IFtdLCAicm9sZXMiOiBbXSwgImZpZWxkcyI6IFt7Im9wZXJh
dGlvbnMiOiBbXSwgInJlYWRfb25seSI6IHRydWUsICJuYW1lIjogImluY190cmFpbmluZyIsICJ0
ZW1wbGF0ZXMiOiBbXSwgInR5cGVfaWQiOiAwLCAiY2hvc2VuIjogZmFsc2UsICJ0ZXh0IjogIlNp
bXVsYXRpb24iLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJleHBvcnRfa2V5
IjogImluY2lkZW50L2luY190cmFpbmluZyIsICJ0b29sdGlwIjogIldoZXRoZXIgdGhlIGluY2lk
ZW50IGlzIGEgc2ltdWxhdGlvbiBvciBhIHJlZ3VsYXIgaW5jaWRlbnQuICBUaGlzIGZpZWxkIGlz
IHJlYWQtb25seS4iLCAicmljaF90ZXh0IjogZmFsc2UsICJvcGVyYXRpb25fcGVybXMiOiB7fSwg
InByZWZpeCI6IG51bGwsICJpbnRlcm5hbCI6IGZhbHNlLCAidmFsdWVzIjogW10sICJibGFua19v
cHRpb24iOiBmYWxzZSwgImlucHV0X3R5cGUiOiAiYm9vbGVhbiIsICJjaGFuZ2VhYmxlIjogdHJ1
ZSwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJpZCI6IDUwLCAidXVpZCI6ICJjM2YwZTNl
ZC0yMWUxLTRkNTMtYWZmYi1mZTVjYTMzMDhjY2EifSwgeyJvcGVyYXRpb25zIjogW10sICJ0eXBl
X2lkIjogMTEsICJvcGVyYXRpb25fcGVybXMiOiB7fSwgInRleHQiOiAid2ViZXhfbWVldGluZ19z
dGFydF90aW1lIiwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAicHJlZml4IjogbnVsbCwgImNoYW5n
ZWFibGUiOiB0cnVlLCAiaWQiOiAxMDMsICJyZWFkX29ubHkiOiBmYWxzZSwgInV1aWQiOiAiNTcw
NmFjNjItOTdlZS00YjU0LTk4MDctOWY0YjEyNGVjZWNjIiwgImNob3NlbiI6IGZhbHNlLCAiaW5w
dXRfdHlwZSI6ICJkYXRldGltZXBpY2tlciIsICJ0b29sdGlwIjogIiIsICJpbnRlcm5hbCI6IGZh
bHNlLCAicmljaF90ZXh0IjogZmFsc2UsICJ0ZW1wbGF0ZXMiOiBbXSwgImV4cG9ydF9rZXkiOiAi
X19mdW5jdGlvbi93ZWJleF9tZWV0aW5nX3N0YXJ0X3RpbWUiLCAiaGlkZV9ub3RpZmljYXRpb24i
OiBmYWxzZSwgInBsYWNlaG9sZGVyIjogIiIsICJuYW1lIjogIndlYmV4X21lZXRpbmdfc3RhcnRf
dGltZSIsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgInZhbHVlcyI6IFtdfSwg
eyJvcGVyYXRpb25zIjogW10sICJ0eXBlX2lkIjogMTEsICJvcGVyYXRpb25fcGVybXMiOiB7fSwg
InRleHQiOiAid2ViZXhfbWVldGluZ19uYW1lIiwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAicHJl
Zml4IjogbnVsbCwgImNoYW5nZWFibGUiOiB0cnVlLCAiaWQiOiAxMDIsICJyZWFkX29ubHkiOiBm
YWxzZSwgInV1aWQiOiAiMTQ0MzhkYzctNDg3NC00OTcxLTlhYTctNTU5NmIxMzI3NmExIiwgImNo
b3NlbiI6IGZhbHNlLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgInRvb2x0aXAiOiAiTWVldGluZyBu
YW1lIiwgImludGVybmFsIjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRlbXBsYXRlcyI6
IFtdLCAiZXhwb3J0X2tleSI6ICJfX2Z1bmN0aW9uL3dlYmV4X21lZXRpbmdfbmFtZSIsICJoaWRl
X25vdGlmaWNhdGlvbiI6IGZhbHNlLCAicGxhY2Vob2xkZXIiOiAiIiwgIm5hbWUiOiAid2ViZXhf
bWVldGluZ19uYW1lIiwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAidmFsdWVz
IjogW119LCB7Im9wZXJhdGlvbnMiOiBbXSwgInR5cGVfaWQiOiAxMSwgIm9wZXJhdGlvbl9wZXJt
cyI6IHt9LCAidGV4dCI6ICJ3ZWJleF9tZWV0aW5nX2VuZF90aW1lIiwgImJsYW5rX29wdGlvbiI6
IGZhbHNlLCAicHJlZml4IjogbnVsbCwgImNoYW5nZWFibGUiOiB0cnVlLCAiaWQiOiAxMDQsICJy
ZWFkX29ubHkiOiBmYWxzZSwgInV1aWQiOiAiOWQzNjhhMmYtZWRmNC00MzUzLWE4YmEtMzdmODZj
NWE4NGU3IiwgImNob3NlbiI6IGZhbHNlLCAiaW5wdXRfdHlwZSI6ICJkYXRldGltZXBpY2tlciIs
ICJ0b29sdGlwIjogIiIsICJpbnRlcm5hbCI6IGZhbHNlLCAicmljaF90ZXh0IjogZmFsc2UsICJ0
ZW1wbGF0ZXMiOiBbXSwgImV4cG9ydF9rZXkiOiAiX19mdW5jdGlvbi93ZWJleF9tZWV0aW5nX2Vu
ZF90aW1lIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJwbGFjZWhvbGRlciI6ICIiLCAi
bmFtZSI6ICJ3ZWJleF9tZWV0aW5nX2VuZF90aW1lIiwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZl
ciI6IGZhbHNlLCAidmFsdWVzIjogW119LCB7Im9wZXJhdGlvbnMiOiBbXSwgInR5cGVfaWQiOiAx
MSwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidGV4dCI6ICJ3ZWJleF9tZWV0aW5nX3Bhc3N3b3Jk
IiwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAicHJlZml4IjogbnVsbCwgImNoYW5nZWFibGUiOiB0
cnVlLCAiaWQiOiAxMDEsICJyZWFkX29ubHkiOiBmYWxzZSwgInV1aWQiOiAiMDNkZDE1MzEtYWNi
Yi00ZGI4LTk5NTAtNTM1MjBlYWJiYjVjIiwgImNob3NlbiI6IGZhbHNlLCAiaW5wdXRfdHlwZSI6
ICJ0ZXh0IiwgInRvb2x0aXAiOiAiTWVldGluZyBwYXNzd29yZCIsICJpbnRlcm5hbCI6IGZhbHNl
LCAicmljaF90ZXh0IjogZmFsc2UsICJ0ZW1wbGF0ZXMiOiBbXSwgImV4cG9ydF9rZXkiOiAiX19m
dW5jdGlvbi93ZWJleF9tZWV0aW5nX3Bhc3N3b3JkIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFs
c2UsICJwbGFjZWhvbGRlciI6ICIiLCAibmFtZSI6ICJ3ZWJleF9tZWV0aW5nX3Bhc3N3b3JkIiwg
ImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAidmFsdWVzIjogW119LCB7Im9wZXJh
dGlvbnMiOiBbXSwgInR5cGVfaWQiOiAxMSwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidGV4dCI6
ICJ3ZWJleF9tZWV0aW5nX2FnZW5kYSIsICJibGFua19vcHRpb24iOiBmYWxzZSwgInByZWZpeCI6
IG51bGwsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImlkIjogMTAwLCAicmVhZF9vbmx5IjogZmFsc2Us
ICJ1dWlkIjogIjRiMTc5ODk3LTNjZmMtNGE5OC04ODY0LWQ5YzA5ZTY4NWQ1YSIsICJjaG9zZW4i
OiBmYWxzZSwgImlucHV0X3R5cGUiOiAidGV4dCIsICJ0b29sdGlwIjogIk1lZXRpbmcgYWdlbmRh
IiwgImludGVybmFsIjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRlbXBsYXRlcyI6IFtd
LCAiZXhwb3J0X2tleSI6ICJfX2Z1bmN0aW9uL3dlYmV4X21lZXRpbmdfYWdlbmRhIiwgImhpZGVf
bm90aWZpY2F0aW9uIjogZmFsc2UsICJwbGFjZWhvbGRlciI6ICIiLCAibmFtZSI6ICJ3ZWJleF9t
ZWV0aW5nX2FnZW5kYSIsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgInZhbHVl
cyI6IFtdfV0sICJvdmVycmlkZXMiOiBbXSwgImV4cG9ydF9kYXRlIjogMTUzNTQ2NjcwMDcxMH0=
"""
    )
