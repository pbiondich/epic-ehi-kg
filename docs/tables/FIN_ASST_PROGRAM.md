# FIN_ASST_PROGRAM

> This table contains information related to financial assistance program records.

**Primary key:** `FIN_ASST_PROGRAM_ID`  
**Columns:** 3  
**Joined by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FIN_ASST_PROGRAM_ID` | NUMERIC | PK | The unique identifier for the financial assistance case record. |
| 2 | `FIN_ASST_PROGRAM_ID_PROGRAM_NAME` | VARCHAR |  | The name of the financial assistance program record. |
| 3 | `PROGRAM_NAME` | VARCHAR |  | The name of the financial assistance program record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (3)

| From | Column | Confidence |
|------|--------|------------|
| [FIN_ASST_CASE_ASSOC_TRKR](FIN_ASST_CASE_ASSOC_TRKR.md) | `FIN_ASST_PROGRAM_ID` | high |
| [FIN_ASST_TRACKER](FIN_ASST_TRACKER.md) | `FIN_ASST_PROGRAM_ID` | high |
| [SOCIAL_CARE_TRACKER](SOCIAL_CARE_TRACKER.md) | `FIN_ASST_PROGRAM_ID` | high |

