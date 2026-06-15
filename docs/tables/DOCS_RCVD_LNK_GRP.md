# DOCS_RCVD_LNK_GRP

> Contains information about linked order groups.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `LNK_GRP_TYPE_C_NAME` | VARCHAR |  | Link group type |
| 6 | `LNK_GRP_ID` | VARCHAR |  | Linked group ID |
| 7 | `LNK_ORD_SEQ_NUM` | INTEGER |  | Sequence number of this linked order in the group |
| 8 | `LNK_ORD_DISP_NAM` | VARCHAR |  | Linked order display name |
| 9 | `LNK_ORD_SUM` | VARCHAR |  | Linked order summary |
| 10 | `LNK_ORD_REC_ACT_C_NAME` | VARCHAR |  | Recommended reconciliation action for this linked order |
| 11 | `LNK_MED_REF_ID` | VARCHAR |  | Unique reference ID for a medication in a linked group |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

