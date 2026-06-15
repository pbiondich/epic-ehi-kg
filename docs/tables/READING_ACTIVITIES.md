# READING_ACTIVITIES

> This table stores the activity used to edit the study for various imaging applications.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `READING_ADV_ACT_ID` | NUMERIC |  | The Advantage Activity (HAA) ID that was used to edit the imaging study. |
| 4 | `READING_ADV_ACT_ID_ADV_ACTIVITY_NAME` | VARCHAR |  | Internal name of the Advantage Activity record |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

