# V_EHI_PBI_FILTER_STATIC

> This view supports extracting RTF data for EHI from the invoice masterfile.

**Primary key:** `INVOICE_ID`, `PAT_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INVOICE_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the invoice record. |
| 2 | `PAT_ID` | VARCHAR | PK FK→ | This item contains the subscriber patient Id of a coverage and will be used to associate patients with linked premium billing accounts for EHI. |
| 3 | `CM_LOG_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INVOICE_ID` | [INVOICE](INVOICE.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

