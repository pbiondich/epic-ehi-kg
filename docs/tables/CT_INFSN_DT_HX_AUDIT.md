# CT_INFSN_DT_HX_AUDIT

> This table contains the day 0 entry history audit trail for a cell therapy episode. This includes the day 0 dates, the users who updated the day 0, and the update instants.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `INFSN_DT_HX_AUDIT_DATE` | DATETIME |  | This item stores the audit trail of the day 0/day 1 date of a cell therapy episode. |
| 4 | `INFSN_DT_USER_AUD_USER_ID` | VARCHAR |  | This item stores the audit trail for the users who updated the day 0/day 1 date of a cell therapy episode. |
| 5 | `INFSN_DT_USER_AUD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `INFSN_DT_INST_AUD_LOCAL_DTTM` | DATETIME (Local) |  | This item stores the audit trail for the instant when the day 0/day 1 date of a cell therapy episode is updated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

