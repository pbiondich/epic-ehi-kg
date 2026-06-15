# APPEAL_GRV_LETTER

> Letters that were sent or were attempted to have been sent from an appeal or grievance record.

**Primary key:** `APPEAL_GRV_ID`, `LINE`  
**Columns:** 49  
**Org-specific columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `APPEAL_GRV_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the appeal/grievance record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CM_PHY_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| 4 | `LETTER_SENT_DOCUMENT_ID` | VARCHAR |  | The contents of the letter that were delivered or are waiting to be delivered. |
| 5 | `APPEAL_GRV_LETTER_STS_C_NAME` | VARCHAR |  | Where this letter is in the generation process. |
| 6 | `LETTER_GUID` | VARCHAR |  | Unique identifier for this letter. This column can be used to join to APPEAL_GRV_LETTER_GEN_HX.LETTER_HX_GUID. |
| 7 | `APPEAL_GRV_LETTER_TYPE_C_NAME` | VARCHAR | org | Which letter type this line counts as. Released letters correspond to common letter types for timeliness requirements and will be automatically triggered during the workflow with no additional build. |
| 8 | `RECIPIENT_CLASS_EVENT_ID` | VARCHAR |  | The recipient class used to determine the specific recipient to send to. |
| 9 | `RECIPIENT_CLASS_EVENT_ID_EVENT_NAME` | VARCHAR |  | The name of the event. |
| 10 | `RESOLVED_FEV_SEND_TO_C_NAME` | VARCHAR |  | The specific type of the recipient found with the recipient class. |
| 11 | `RESOLVED_RECIPIENT_INI` | VARCHAR |  | The INItials of the master file containing the record of this letter's recipient. |
| 12 | `RESOLVED_RECIPIENT_ID` | VARCHAR |  | The ID of the record of this letter's recipient. The corresponding value in RESOLVED_RECIPIENT_INI indicates what table this can be used to join to. |
| 13 | `RESOLVED_RECIPIENT_GUID` | VARCHAR |  | The GUID of this letter's recipient. This column can be used to join to MEMBER_RESP_PERSON.MEM_RESP_GUID and will be populated when column RESOLVED_FEV_SEND_TO_C is set to 58 (Authorized Representative). |
| 14 | `DELIVERY_LOGIC_C_NAME` | VARCHAR |  | When resolving a delivery method for a particular recipient, this is how we chose that delivery method. |
| 15 | `RESOLVED_FEV_DLVR_MTHD_C_NAME` | VARCHAR |  | The ideal delivery method chosen for the recipient of this letter. |
| 16 | `BATCH_PRINT_LTR_HX_JOB_TYPE_C_NAME` | VARCHAR | org | If a letter was submitted to batch print to be mailed out, this is the job type that the letter was queued to. |
| 17 | `BODY_SMARTTEXT_ID` | VARCHAR |  | When the letter was created, this is the SmartText template that we used to generate the contents of the body. |
| 18 | `BODY_SMARTTEXT_ID_SMARTTEXT_NAME` | VARCHAR |  | The name of the SmartText record. |
| 19 | `COVER_SMARTTEXT_ID` | VARCHAR |  | When the letter was created, this is the SmartText template that we used to generate the cover sheet which was rendered before the body. |
| 20 | `COVER_SMARTTEXT_ID_SMARTTEXT_NAME` | VARCHAR |  | The name of the SmartText record. |
| 21 | `BACK_SMARTTEXT_ID` | VARCHAR |  | When the letter was created, this is the SmartText template that we used to generate the back sheet which was rendered after the body. |
| 22 | `BACK_SMARTTEXT_ID_SMARTTEXT_NAME` | VARCHAR |  | The name of the SmartText record. |
| 23 | `RESOLVED_IB_POOL_ID` | NUMERIC |  | If this letter was sent as an In Basket message, this will store the pool that we delivered to. |
| 24 | `RESOLVED_IB_POOL_ID_REGISTRY_NAME` | VARCHAR |  | The name of the In Basket registry in the HIP master file. |
| 25 | `RESOLVED_PROV_ADDR_UNIQUE_ID` | VARCHAR |  | The unique ID of the provider's address when the resolved recipient is a provider. This can be used to join to CLARITY_SER_ADDR in combination with column RESOLVED_RECIPIENT_ID when RESOLVED_RECIPIENT_INI = 'SER'. |
| 26 | `CITY` | VARCHAR |  | The city of this letter's recipient. A city may be recorded, even if the letter was not mailed. |
| 27 | `STATE_C_NAME` | VARCHAR | org | A category value for the state of this letter's recipient. A state may be recorded, even if the letter was not mailed. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 28 | `ZIP` | VARCHAR |  | The ZIP code of this letter's recipient. A ZIP code may be recorded, even if the letter was not mailed. |
| 29 | `DISTRICT_C_NAME` | VARCHAR | org | A category value for the district of this letter's recipient. A district may be recorded, even if the letter was not mailed. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 30 | `COUNTY_C_NAME` | VARCHAR | org | A category value for the county of this letter's recipient. A county may be recorded, even if the letter was not mailed. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 31 | `COUNTRY_C_NAME` | VARCHAR | org | A category value for the country of this letter's recipient. A country may be recorded, even if the letter was not mailed. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 32 | `BUILDING_NUMBER` | VARCHAR |  | The building/house number of this letter's recipient. A building/house number may be recorded, even if the letter was not mailed. |
| 33 | `RECIPIENT_NAME` | VARCHAR |  | The name of this letter's recipient. |
| 34 | `SENT_SYS_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant that this letter was printed or electronically sent, as determined by the system. This does not take into account the manual override (SENT_OVD_UTC_DTTM). |
| 35 | `SENT_SYS_LOCAL_DTTM` | DATETIME (Attached) |  | The local instant that this letter was printed or electronically sent, as determined by the system. This does not take into account the manual override (SENT_OVD_LOCAL_DTTM). This item represents the same data as the UTC sent instant (SENT_SYS_UTC_DTTM) but is converted to the appeal's/grievance's local time zone (APPEAL_GRV.TAT_RPT_TIME_ZONE_C). |
| 36 | `SENT_OVD_UTC_DTTM` | DATETIME (UTC) |  | A user-entered override UTC instant for when this letter was printed or electronically sent. If the system calcuated instant (SENT_SYS_UTC_DTTM) was incorrect, this item can be used to manully specify the correct date/time. |
| 37 | `SENT_OVD_LOCAL_DTTM` | DATETIME (Attached) |  | A user-entered override local instant for when this letter was printed or electronically sent. If the system calcuated instant (SENT_SYS_UTC_DTTM) was incorrect, this item can be used to manully specify the correct date/time. This item represents the same data as the UTC sent instant override (SENT_OVD_UTC_DTTM) but is converted to the appeal's/grievance's local time zone (APPEAL_GRV.TAT_RPT_TIME_ZONE_C). |
| 38 | `SENT_RPT_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant when this letter was printed or electronically sent. This item uses the user-entered override (SENT_OVD_UTC_DTTM) if one was specified. Otherwise, the system calculated value (SENT_SYS_UTC_DTTM) is used. |
| 39 | `SENT_RPT_LOCAL_DTTM` | DATETIME (Attached) |  | The local instant when this letter was printed or electronically sent. This item uses the user-entered override (SENT_OVD_LOCAL_DTTM) if one was specified. Otherwise, the system calculated value (SENT_SYS_LOCAL_DTTM) is used. This item represents the same data as the UTC sent reportable instant (SENT_RPT_UTC_DTTM) but is converted to the appeal's/grievance's local time zone (APPEAL_GRV.TAT_RPT_TIME_ZONE_C). |
| 40 | `MAILED_SYS_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant that this letter was mailed or electronically sent, as calcuated by the system. This item uses the reportable sent instant (SENT_RPT_UTC_DTTM) and adds mail lag if the letter used a delivery method (RESOLVED_FEV_DLVR_MTHD_C) of 1-Letter to indicate a mailed letter. The value will match the reportable sent instant for all other delivery methods. This item doesn't take into account the user-entered mailed override (MAILED_OVR_UTC_DTTM). |
| 41 | `MAILED_SYS_LOCAL_DTTM` | DATETIME (Attached) |  | The local instant that this letter was mailed or electronically sent, as calcuated by the system. This item uses the reportable sent instant (SENT_RPT_LOCAL_DTTM) and adds mail lag if the letter used a delivery method (RESOLVED_FEV_DLVR_MTHD_C) of 1-Letter to indicate a mailed letter. The value will match the reportable sent instant for all other delivery methods. This item doesn't take into account the user-entered mailed override (MAILED_OVR_LOCAL_DTTM). This item represents the same data as the system-calculated UTC mailed instant (MAILED_SYS_UTC_DTTM) but is converted to the appeal's/grievance's local time zone (APPEAL_GRV.TAT_RPT_TIME_ZONE_C). |
| 42 | `MAILED_OVR_UTC_DTTM` | DATETIME (UTC) |  | A user-entered UTC instant that represents when the letter was mailed or electronically sent in case the system calculated mailed instant (MAILED_SYS_UTC_DTTM) is wrong, |
| 43 | `MAILED_OVR_LOCAL_DTTM` | DATETIME (Attached) |  | A user-entered local instant that represents when the letter was mailed or electronically sent in case the system calculated mailed instant (MAILED_SYS_LOCAL_DTTM) is wrong, This item represents the same data as the UTC mailed instant override (MAILED_SYS_LOCAL_DTTM) but is converted to the appeal's/grievance's local time zone (APPEAL_GRV.TAT_RPT_TIME_ZONE_C). |
| 44 | `MAILED_RPT_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant when this letter was printed or electronically sent. This item uses the user-entered override (MAILED_SYS_UTC_DTTM) if one was specified. Otherwise, the system calculated value (MAILED_OVR_UTC_DTTM) is used. |
| 45 | `MAILED_RPT_LOCAL_DTTM` | DATETIME (Attached) |  | The local instant when this letter was printed or electronically sent. This item uses the user-entered override (MAILED_SYS_LOCAL_DTTM) if one was specified. Otherwise, the system calculated value (MAILED_OVR_LOCAL_DTTM) is used. This item represents the same data as the UTC mailed instant (MAILED_RPT_UTC_DTTM) but is converted to the appeal's/grievance's local time zone (APPEAL_GRV.TAT_RPT_TIME_ZONE_C). |
| 46 | `BODY_NOTE_ID` | VARCHAR |  | The unique ID of the note containing the letter's main contents. |
| 47 | `COVER_SHEET_NOTE_ID` | VARCHAR |  | The unique ID of the note containing the letter's cover sheet. |
| 48 | `BACK_NOTE_ID` | VARCHAR |  | The unique ID of the note containing the letter's back sheet. |
| 49 | `FAX_FACE_SHEET_NOTE_ID` | VARCHAR |  | The unique ID of the note containing the letter's face sheet if it was faxed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `APPEAL_GRV_ID` | [APPEAL_GRV](APPEAL_GRV.md) | sole_pk | high |

