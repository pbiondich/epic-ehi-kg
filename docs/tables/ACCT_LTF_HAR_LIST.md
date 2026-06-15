# ACCT_LTF_HAR_LIST

> Late fee history list of hospital accounts.

**Primary key:** `ACCT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique ID of the guarantor account for this row. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated late fee history in this guarantor account. Together with ACCT_ID, this forms the foreign key to the ACCT_EB_LTFEE_HIST table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple hospital accounts that are associated with the guarantor account and the late fee history from the ACCT_EB_LTFEE_HIST table. |
| 4 | `LTF_HX_HAR_LST` | VARCHAR |  | This row contains the hospital accounts upon which late fees were applied for the guarantor. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

