# MERGED_PROTOCOLS

> This table links Pathway and SmartSet uses to the Pathway or SmartSet templates that were used to create them.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique identifier for the plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MERGE_PROTOCOL_ID` | NUMERIC |  | The unique ID of a protocol added to the treatment plan. |
| 4 | `MERGE_PROTOCOL_ID_PROTOCOL_NAME` | VARCHAR |  | The SmartSet/Protocol record name. This is different from the display name, which is stored in CL_PRL_SS_OT.DISPLAY_NAME. |
| 5 | `MERGED_PROTOCOL_DTE` | FLOAT |  | The CONTACT_DATE_REAL of a protocol added to the treatment plan. |
| 6 | `MERGE_PROTOCOL_TY_C_NAME` | VARCHAR |  | The add method category number for a protocol added to this treatment plan. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

