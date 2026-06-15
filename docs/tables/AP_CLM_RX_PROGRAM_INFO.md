# AP_CLM_RX_PROGRAM_INFO

> This table contains information about the program that a pharmacy claim is associated with.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim info record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PROGRAM_ID` | NUMERIC | FK→ | This item contains the external ID of a Value Based Program record or records representing the programs that the claim is associated with. |
| 4 | `PROGRAM_ID_RECORD_NAME` | VARCHAR |  | The name of the program record. |
| 5 | `CLAIM_PROG_LINK_STATUS_C_NAME` | VARCHAR |  | Indicates the current status of the Value Based Program, whether it is active, inactive, or planned to be removed (loaded in error). |
| 6 | `PROGRAM_MOD_DTTM` | DATETIME (Local) |  | The local instant when the claim was last modified for the Value Based Plan. |
| 7 | `PROGRAM_MOD_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant when the claim was last modified for the Value Based Plan. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |
| `PROGRAM_ID` | [VALUE_BASED_PROGRAM](VALUE_BASED_PROGRAM.md) | sole_pk | high |

