# CASE_EXTRA_CHARGES

> The CASE_EXTRA_CHARGES table contains reasons for incurring extra charges in the case master database.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | NUMERIC | PK shared | The unique identifier for the case record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EXTRA_CHARGE_AMOUNT` | NUMERIC |  | Specifies the extra charge amount. |
| 4 | `EXTRA_CHARGE_TYPE_C_NAME` | VARCHAR | org | Specifies the extra charge type. |
| 5 | `EXTRA_CHARGE_REASON` | VARCHAR |  | Specifies the extra charge reason. |
| 6 | `EXTRA_CHARGE_DATE` | DATETIME |  | Specifies the extra charge date. |
| 7 | `EXTRA_CHARGE_USR_ID` | VARCHAR |  | Specifies the extra charge user. |
| 8 | `EXTRA_CHARGE_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `EXTRA_CHARGE_ENT_DT` | DATETIME |  | Specifies the extra charge entry date. |
| 10 | `CHARGE_REVERSAL_LINE` | INTEGER |  | Holds the line number of the charge-related group that this line is a reversal of. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

