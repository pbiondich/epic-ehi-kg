# PAT_CORRSP_ADDL_ADDR_INFO

> Additional Correspondence Address Info.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CORRSP_ADDL_ADDR_FIELD_C_NAME` | VARCHAR |  | The type of additional correspondence address data (floor, unit, building name, etc.) stored in the related field (I EPT 686). |
| 4 | `CORRSP_ADDL_ADDR_DATA` | VARCHAR |  | The additional correspondence address data that the related "type" (I EPT 685) line applies to |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

