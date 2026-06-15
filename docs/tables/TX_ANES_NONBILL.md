# TX_ANES_NONBILL

> The TX_ANES_NONBILL table contains information concerning the non-billable items for an anesthesia charge.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique key or identification number for a given transaction. |
| 2 | `LINE` | INTEGER | PK | This column contains the line count for the non-billable information in this table. Each piece of non-billable information is stored on a separate line, one line for each entry. |
| 3 | `PX_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 4 | `PX_MOD_ID` | VARCHAR |  | Non-billing anesthesia procedure modifier for this procedure. |
| 5 | `PX_MOD_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |
| 6 | `BASE_UNITS` | NUMERIC |  | Non-billing units value of anesthesia base units for this procedure. |
| 7 | `VAR_UNITS` | NUMERIC |  | Non-billing units value of anesthesia variable units for this procedure. |
| 8 | `ASA_CODE_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 9 | `IS_NB_ANES_CVR_C_NAME` | VARCHAR |  | Non-billing anesthesia covered flag for this procedure. created to replace column CVRDFLG_YN. return category number. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

