# MRG_POSITIVE_DCIS

> Stores data for College of American Pathologists (CAP) form field Margin Positive for DCIS.

**Primary key:** `RESULT_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MRG_POSITIVE_DCIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Margins Positive for Ductal Carcinoma In Situ (DCIS). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

