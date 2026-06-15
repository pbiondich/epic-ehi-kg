# AN_HSB_SIGNOFF

> This table stores the Anesthesia Pre-op evaluation signoff information.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique ID of the Episode (HSB) record for this row. Episodes store information including the start and end dates, episode status and type, and any contacts associated with the episode. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ANES_SIGNOFF_USR_ID` | VARCHAR |  | Stores the user who signed off. |
| 4 | `ANES_SIGNOFF_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `ANES_SIGNOFF_INST` | DATETIME (Local) |  | Stores the instant that this signoff occurred on. |
| 6 | `ANES_SIGNOFF_CMMT` | VARCHAR |  | Stores the comment for the anesthesia signoff. |
| 7 | `ANES_SIGNOFF_TYPE_C_NAME` | VARCHAR |  | Stores the type of signoff event. |
| 8 | `ANES_SIGNOFF_REC_DTTM` | DATETIME (Local) |  | Stores the instant that the signoff was documented. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

