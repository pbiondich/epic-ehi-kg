# AP_CLM_RX_PROGRAM_HISTORY

> This table tracks the history of changes to the Value Based Programs associated with pharmacy claims.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim info record |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `UPDATE_PROGRAM_ID` | NUMERIC |  | The Value Based Program that was modified. |
| 4 | `UPDATE_PROGRAM_ID_RECORD_NAME` | VARCHAR |  | The name of the program record. |
| 5 | `UPDATE_INSTANT_DTTM` | DATETIME (Local) |  | The local instant when the Value Based Program was modified. |
| 6 | `CLAIM_PROG_HX_ACTION_C_NAME` | VARCHAR |  | The action that modified the Value Based Program. |
| 7 | `UPDATE_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant when the Value Based Program was modified. |
| 8 | `VBP_HX_SENT_DXO_ID` | NUMERIC |  | The DXO ID to which this claim was sent. |
| 9 | `VBP_HX_SENT_DXO_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

