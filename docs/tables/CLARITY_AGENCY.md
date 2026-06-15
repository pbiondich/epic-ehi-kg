# CLARITY_AGENCY

> The CLARITY_AGENCY table is the parent table for the agency database.

**Primary key:** `AGENCY_ID`  
**Columns:** 3  
**Joined by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AGENCY_ID` | VARCHAR | PK | The unique ID of the agency record. |
| 2 | `AGENCY_ID_AGENCY_NAME` | VARCHAR |  | The name of the agency. |
| 3 | `AGENCY_NAME` | VARCHAR |  | The name of the agency. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (4)

| From | Column | Confidence |
|------|--------|------------|
| [ACCT_COLL_AGENCY_HX](ACCT_COLL_AGENCY_HX.md) | `AGENCY_ID` | high |
| [ARPB_TX_AGCY_HX](ARPB_TX_AGCY_HX.md) | `AGENCY_ID` | high |
| [PAYOR_COMM_HX](PAYOR_COMM_HX.md) | `AGENCY_ID` | high |
| [PAYOR_COMM_RECIPIENT](PAYOR_COMM_RECIPIENT.md) | `AGENCY_ID` | high |

