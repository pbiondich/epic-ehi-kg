# RESULT_AUDIT_ITEMS

> This table contains the items that were changed during a finding record audit action. For one audit action there can be multiple items that were changed; this corresponds to the third primary key in this table, VALUE_LINE. This table will likely be joined to from RESULT_AUDIT, which holds the majority of the finding audit information.

**Primary key:** `FINDING_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique ID of the finding record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated audit information in this finding record. Together with FINDING_ID, this forms the foreign key to the RESULT_AUDIT table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple items that are associated with the finding audit information from the RESULT_AUDIT table. |
| 4 | `ITEM_CHANGED` | VARCHAR |  | The items that were changed during the particular action being audited. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

