# PAT_GUEST_PROXY_AUDIT

> An audit trail that tracks when a patient's guest proxy relationships are created, changed, or removed.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PROXY_AUD_MYPT_ID` | VARCHAR |  | Guest proxy relationship to audit |
| 4 | `GSTPRXYAUD_ACT_C_NAME` | VARCHAR |  | Action done on the guest proxy relationship |
| 5 | `PROXY_AUD_UTC_DTTM` | DATETIME (UTC) |  | The time at which an action was audited for a guest proxy relationship |
| 6 | `PROXY_AUD_USER_ID` | VARCHAR |  | Stores the user who performed the action being audited |
| 7 | `PROXY_AUD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

