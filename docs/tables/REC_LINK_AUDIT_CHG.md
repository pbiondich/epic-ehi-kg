# REC_LINK_AUDIT_CHG

> This table contains the source of the change, user or system, for a recommendation audit trail entry.

**Primary key:** `FINDING_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique ID of the recommendation record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated workflow in this recommendation record. Together with FINDING_ID, this forms the foreign key to the REC_LINK_AUDIT_TRL. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple audit trail changers that are associated with the recommendation and the workflow from the REC_LINK_AUDIT_TRL table. |
| 4 | `AUDIT_CHANGER_C_NAME` | VARCHAR |  | The changer category number for the recommendation audit trail entry. The changer is the source of the change logged in the audit trail entry, either User or System. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

