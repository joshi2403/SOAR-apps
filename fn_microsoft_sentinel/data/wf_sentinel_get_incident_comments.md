<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-circuits codegen
-->

# Sentinel Get Incident Comments

## Function - Sentinel Get Incident Comments

### API Name
`sentinel_get_incident_comments`

### Output Name
`None`

### Message Destination
`fn_microsoft_sentinel`

### Pre-Processing Script
```python
inputs.sentinel_incident_id = incident.properties.sentinel_incident_number
inputs.incident_id = incident.id
inputs.sentinel_profile = incident.properties.sentinel_profile
```

### Post-Processing Script
```python
if results.success:
  for comment in results.content['value']:
    incident.addNote(helper.createRichText(comment['properties']['message']))
      
    # remember the comment in our datatable
    row = incident.addRow('sentinel_comment_ids')
    row['comment_id'] = comment['name']

```

---

