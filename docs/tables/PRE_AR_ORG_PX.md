# PRE_AR_ORG_PX

> Stores information about current procedure in charge review session. The following details are stored: Quantity (units/days) of procedure, Amount of the procedure, and Modifier if any.

**Primary key:** `TAR_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TAR_ID` | NUMERIC | PK shared | The unique identifier for the temporary transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ORG_CHG_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 4 | `ORG_CHG_MOD` | VARCHAR |  | Modifier associated with a procedure in charge review session. |
| 5 | `ORG_CHG_QUANTITY` | NUMERIC |  | Number of units/days for a procedure in charge review session. |
| 6 | `ORG_CHG_AMOUNT` | NUMERIC |  | Charge amount of a procedure in charge review session. |
| 7 | `ORG_CHG_DX` | VARCHAR |  | Tells which diagnoses apply to this charge procedure (comma-separated numbers). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

