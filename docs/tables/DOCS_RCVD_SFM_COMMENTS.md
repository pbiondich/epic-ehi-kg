# DOCS_RCVD_SFM_COMMENTS

> This table contains the information about the comments info received from SFM query.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `SFM_COMMENT_MED_REFID` | VARCHAR |  | This item contains the medication ref id this comment is linked to. |
| 6 | `SFM_COMMENT_TYPE_C_NAME` | VARCHAR |  | This item stores the SFM comment type. |
| 7 | `SFM_COMMENT_TEXT` | VARCHAR |  | This item stores the comments text. |
| 8 | `SFM_COMMENT_RESPONSE_TYPE_C_NAME` | VARCHAR |  | This item contains the SFM comment response type. |
| 9 | `SFM_COMMENT_RESPONSE_TEXT` | VARCHAR |  | This item stores the free text comments response. |
| 10 | `SFM_COMMENT_IDENT` | VARCHAR |  | This item stores the id of the sfm comment. |
| 11 | `COMMENT_REG_BY` | VARCHAR |  | This item stores the user that has registered the comment. |
| 12 | `SFM_COMMENT_RECEIVER` | VARCHAR |  | This item stores the reciver info of the sfm comment. |
| 13 | `SFM_COMMENT_RESPONDER` | VARCHAR |  | This item stores the responder info of the sfm comment. |
| 14 | `SFM_COMMENT_TIME_UTC_DTTM` | DATETIME (UTC) |  | This item stores the sfm comment timestamp. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

