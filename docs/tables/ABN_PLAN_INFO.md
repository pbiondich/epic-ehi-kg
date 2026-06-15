# ABN_PLAN_INFO

> This table contains Advanced Beneficiary Notice (ABN) treatment/therapy plan information.

**Primary key:** `NOTE_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique ID of the note (HNO) record that contains the Advance Beneficiary Notice (ABN) information. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ABN_OTP_ID` | NUMERIC |  | Stores the IDs of the linked order templates in item 2050 of the ABN record. |
| 4 | `ABN_OTP_COUNT` | NUMERIC |  | Stores the number of patient order templates in the plan linked to the ABN in item 2050 of the ABN record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

