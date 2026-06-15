# PAT_GUEST_PROXY

> Lists the guest proxies for a patient, and the relationship types of those guest proxies.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PROXY_MYPT_ID` | VARCHAR |  | The MyChart account ID (WPR) of the delegate who has guest proxy access to this patient. |
| 4 | `PROXY_REL_C_NAME` | VARCHAR | org | Lists the relationship type of this proxy relationship |
| 5 | `PROXY_UPG_STAT_C_NAME` | VARCHAR |  | Lists the current status of the guest proxy's upgrade request |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

