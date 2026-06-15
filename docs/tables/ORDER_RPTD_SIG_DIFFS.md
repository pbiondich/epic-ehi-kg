# ORDER_RPTD_SIG_DIFFS

> When a patient reports taking a medication differently from how it was prescribed, the specific fields (dose, frequency, etc.) that differ from the prescription are recorded as entries in this table. Sig lines in ORDER_RPTD_SIG_HX that don't indicate a variance (e.g. the line for the sig as it was first prescribed) have no entries in this table.

**Primary key:** `ORDER_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record, indicating where the reported sig differs. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of where the patient sig differs from the prescribed sig within this record. |
| 4 | `DIFFERENCE_C_NAME` | VARCHAR |  | Exactly which discrete portion of the sig differs between what was prescribed and what the patient reports taking. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

