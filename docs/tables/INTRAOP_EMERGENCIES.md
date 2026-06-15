# INTRAOP_EMERGENCIES

> Holds the instants that the anesthesia emergency call was initiated and when the sender marked it as help was no longer needed.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `INTRAOP_EMERG_START_UTC_DTTM` | DATETIME (UTC) |  | The start instant of when a request for Emergency Help was sent out via the Anesthesia Emergency notification activity |
| 7 | `INTRAOP_EMERG_END_UTC_DTTM` | DATETIME (UTC) |  | The end instant of when a request for Emergency Help was marked as "help no longer needed" with the Anesthesia Emergency notification activity. |
| 8 | `INTRAOP_EMERG_SEND_PROVIDER_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 9 | `INTRAOP_EMERG_ST_LOCAL_DTTM` | DATETIME (Local) |  | The start instant in local time of when a request for Emergency Help was sent out via the Anesthesia Emergency call activity |
| 10 | `INTRAOP_EMERG_END_LOCAL_DTTM` | DATETIME (Local) |  | The end local instant of when a request for Emergency Help was marked as "help no longer needed" with the Anesthesia Emergency call activity. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

