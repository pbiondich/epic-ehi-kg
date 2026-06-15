# DENTAL_PERIO_EXAM_CSNS

> This table contains the list of encounter contact serial numbers (CSNs) in which a periodontal exam has been documented.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DENT_PERI_EPT_CSN` | NUMERIC |  | This item contains the list of contact serial numbers (CSN) of encounters that have a periodontal exam documented. |
| 4 | `DENT_PERIO_TYPE_C_NAME` | VARCHAR |  | This item contains the special exam type of the associated periodontal contact serial number (CSN). If left blank, then the CSN is a regular periodontal exam. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

