# HL_ASGN_INFO

> Hospital Logistics Assignment Information.

**Primary key:** `HLR_ID`, `ASSIGNMENT_DATE_REAL`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HLR_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the request record. |
| 2 | `ASSIGNMENT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. Each represents an individual assignment of the Logistics request. |
| 3 | `ASGN_STATUS_C_NAME` | VARCHAR |  | The current status of each Assignment on this Logistics Request. |
| 4 | `ASGN_CANCEL_RSN_C_NAME` | VARCHAR | org | When an Assignment's status (I HLR 410) is Canceled or Skipped, this item contains the Assignment's cancel or skip reason. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

