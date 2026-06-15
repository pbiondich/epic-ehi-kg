# ARPB_TX_CHG_REV_HX

> Charge Review History Related Information. This information is copied from the TAR (temporary transaction) record when a charge in charge review is filed to ETR (permanent transaction).

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CR_HX_USER_ID` | VARCHAR |  | Charge Review History User ID. This is the user that performs the activity reflected in this line in the charge review history. |
| 4 | `CR_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `CR_HX_DATE` | DATETIME |  | The charge review history date. |
| 6 | `CR_HX_TIME` | DATETIME (Local) |  | Displays the date the recall must be made by. |
| 7 | `CR_HX_ACTIVITY_C_NAME` | VARCHAR |  | The charge review history activity category ID for the transaction. Examples include Entry, Review, Resubmit, etc. |
| 8 | `CR_HX_CONT_LINE_YN` | VARCHAR |  | Charge Review History Continuation Flag. This flag is set to yes if this line is a continuation of the previous line |
| 9 | `CR_HX_USER_COMMENT` | VARCHAR |  | The comment associated to a Charge Review history action. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

