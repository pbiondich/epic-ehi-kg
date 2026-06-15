# PROVTEAM_REC_INFO

> This table extracts the basic record information for the provider team including the name and the date the record was created. Provider teams are groups of providers that can be assigned to a patient.

**Primary key:** `ID`  
**Columns:** 3  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ID` | NUMERIC | PK | The unique ID of the team record for this row. |
| 2 | `ID_RECORD_NAME` | VARCHAR |  | The name of the record. |
| 3 | `RECORD_NAME` | VARCHAR |  | The name of the record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [IP_FSD_TOTALS](IP_FSD_TOTALS.md) | `ID` | high |

