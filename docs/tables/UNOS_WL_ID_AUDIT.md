# UNOS_WL_ID_AUDIT

> This table contains auditing information about usage of the UNOS Waitlist ID Correction activity.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `UNOS_WLID_AUD_UNOS_ORGAN_C_NAME` | VARCHAR |  | Audit item tracking manual changes to I HSB 30722 in the UNOS Waitlist ID Correction activity; stores the organ modified in I HSB 30202 |
| 4 | `UNOS_WLID_AUD_WLID` | VARCHAR |  | Audit item tracking manual changes to I HSB 30722 in the UNOS Waitlist ID Correction activity; stores the WL ID saved to I HSB 30722 |
| 5 | `UNOS_WLIDAUD_USER_ID` | VARCHAR |  | Audit item tracking manual changes to I HSB 30722 in the UNOS Waitlist ID Correction activity; stores the user who modified the ID |
| 6 | `UNOS_WLIDAUD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `UNOS_WLID_AUD_INST_UTC_DTTM` | DATETIME (UTC) |  | Audit item tracking manual changes to I HSB 30722 in the UNOS Waitlist ID Correction activity; stores the instant the ID was modified |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

