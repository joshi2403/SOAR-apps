<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-circuits codegen
-->

# Example: Phish.AI Scan URL

## Function - Phish.AI Scan URL

### API Name
`phish_ai_scan_url`

### Output Name
`phishai_scan_output`

### Message Destination
`phish_ai_message_destination`

### Pre-Processing Script
```python
inputs.artifact_value = artifact.value
```

### Post-Processing Script
```python
"""
Example response

{  
   "content":{  
      "url":"https://startup417.gb.net/M3?mes1=asdf@asdf.com",
      "scan_id":"gGBSaVvlN5qc5PcwvnuT"
   },
   "inputs":{  
      "artifact_value":"https://startup417.gb.net/M3?mes1=asdf@asdf.com"
   },
   "run_time":"0.446181058884"
}
"""
```

---

## Function - Phish.AI Get Report

### API Name
`phish_ai_get_report`

### Output Name
`None`

### Message Destination
`phish_ai_message_destination`

### Pre-Processing Script
```python
inputs.phishai_scan_id = workflow.properties.phishai_scan_output["content"]["scan_id"]
```

### Post-Processing Script
```python
if results.content:
  note = "Phish.AI url: " + results.content.url
  note = note + "<br/>Phish.AI verdict: " + results.content.verdict
  note = note + "<br/><a href=\"https://app.phish.ai/incident/{}\">Phish.AI report link</a>".format(results.inputs.phishai_scan_id)
  incident.addNote(helper.createRichText(note))


"""
Example Response

{  
   "content":{  
      "status":"completed",
      "domain":"startup417.gb.net",
      "user_agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36",
      "target":"Microsoft",
      "title":"sign_in_to_your_microsoft_account",
      "url":"https://startup417.gb.net/M3?mes1=asdf@asdf.com",
      "time":"2018-12-06T22:39:34.210Z",
      "verdict":"malicious",
      "plan":"free",
      "tld":"net",
      "iso_code":"US",
      "first_seen":"2018-12-06T19:16:20.825Z",
      "ip_address":"104.24.104.116",
      "asn":13335,
      "user_email":"api",
      "user":"free-api"
   },
   "inputs":{  
      "phishai_scan_id":"gGBSaVvlN5qc5PcwvnuT"
   },
   "run_time":"0.419372797012"
}
"""
```

---

