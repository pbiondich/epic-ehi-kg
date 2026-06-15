# BDC_LOINC_CODES

> This table contains LOINC code and mapping information that will help identify documentations needed from loading a 277 RF(A)I message.

**Primary key:** `BDC_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BDC_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the den/corr rec record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LOINC_CODE` | VARCHAR |  | Logical Observation Identifiers Names and Codes (LOINC®) code loaded from an ANSI 277 Request for Information(RFI) message that indicates what information was requested. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BDC_ID` | [BDC_INFO](BDC_INFO.md) | sole_pk | high |

