# AN_HSB_LINK_AUDIT

> The AN_HSB_LINK_AUDIT table contains an audit trail of anesthesia linking operations. This table applies to episode (HSB) records of the type specified for anesthesia episodes in clinical system definitions.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique ID for the Episode record for this row. This column is frequently used to link to the EPISODE table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AN_AUDIT_TYPE_C_NAME` | VARCHAR |  | Anesthesia linking audit trail item representing the type of link being done. |
| 4 | `AN_AUDIT_VALUE` | VARCHAR |  | Anesthesia linking audit trail item representing the value of the link. If the linking type is 1-Encounter, this will be the unique patient contact serial number (EPT CSN) of the linked procedure contact. If the linking type is 2-Order, this will be the unique order (ORD) ID of the linked order. If the linking type is 3-Unlinked, this will be the user-entered episode description. |
| 5 | `AN_AUDIT_INST_TM` | DATETIME (UTC) |  | Anesthesia linking audit trail item representing the instant the link was changed. |
| 6 | `AN_AUDIT_USER_ID` | VARCHAR |  | Anesthesia linking audit trail item representing the user doing the linking. |
| 7 | `AN_AUDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

