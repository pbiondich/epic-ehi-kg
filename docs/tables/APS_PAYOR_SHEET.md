# APS_PAYOR_SHEET

> Contains information about payer sheet records. These include the name, National Council for Prescription Drug Programs (NCPDP) version, and the date the record was created. Payer sheets are used by Willow Ambulatory during prescription copay adjudication.

**Primary key:** `PAYOR_SHEET_ID`  
**Columns:** 3  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAYOR_SHEET_ID` | NUMERIC | PK | The unique identifier of the payor sheet record. |
| 2 | `PAYOR_SHEET_ID_RECORD_NAME` | VARCHAR |  | The name of this payor sheet |
| 3 | `RECORD_NAME` | VARCHAR |  | The name of this payor sheet |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [RXA_CVG_TABLE](RXA_CVG_TABLE.md) | `PAYOR_SHEET_ID` | high |

