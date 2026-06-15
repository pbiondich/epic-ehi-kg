# AP_CLAIM_ANSI_DATA

> Stores the information from the ANSI 837 file.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DATA_TYPE_C_NAME` | VARCHAR |  | Stores the type of data from the ANSI 837 file. |
| 4 | `DATA_VALUE` | VARCHAR |  | Stores the data from the ANSI 837 file. |
| 5 | `DATA_LINE_NUM` | INTEGER |  | For data that can occur multiple times in an ANSI 837 file, this is the repetition number. |
| 6 | `DATA_ENTITY_NUM` | INTEGER |  | For entities that can occur multiple times in an ANSI 837 file, this is the repetition number. |
| 7 | `SVC_LN_NUM` | INTEGER |  | If data on this row is for a service line, then this column has the service line number. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

