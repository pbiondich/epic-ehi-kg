# SC_EPISODE_EXT_ENC_AUD

> Data about the audit history for external encounters linked to a Compass Rose episode.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUDIT_REFERENCE` | VARCHAR |  | The audit history composite DXR reference ID for an external encounter linked to this episode. |
| 4 | `AUDIT_USER_ID` | VARCHAR |  | The unique ID associated with the user record for this row. This column is frequently used to link to the CLARITY_EMP table. |
| 5 | `AUDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `AUDIT_UTC_DTTM` | DATETIME (UTC) |  | The audit history update date and time in UTC when the external encounter link to this episode was updated. |
| 7 | `AUDIT_BND_EPSD_SRC_C_NAME` | VARCHAR |  | The source category ID for the audit history for an external encounter linked to this episode. |
| 8 | `AUDIT_EPISODE_LINK_ST_C_NAME` | VARCHAR |  | The status category ID for the audit history for an external encounter linked to this episode. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

