# COD_CONTACT_STAT_HX

> This table contains history information about a contact on a coding (COD) record, including the contact status history, contact action Coordinated Universal Time (UTC) date and time, contact action local date and time, user acting on the contact, and the reason why the contact is acted on. Currently, Clinical Documentation Improvement (CDI) Reviews are stored as contacts (or rows) on the COD record. This table contains CDI Review status, CDI Review action UTC date and time, CDI Review action local date and time, user acting on the CDI Review, and the reason why the user is acting on the CDI Review.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the coding record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `COD_CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `COD_CONTACT_STAT_HX_C_NAME` | VARCHAR | org | This item stores the history of the contact status of the coding record. |
| 6 | `COD_CONTACT_ACT_UTC_DTTM` | DATETIME (UTC) |  | This item stores the UTC instant when an action is taken on a contact on the coding record. |
| 7 | `COD_CONTACT_ACT_DTTM` | DATETIME (Local) |  | This virtual item displays the local instant when an action is taken on a contact on the coding record. |
| 8 | `COD_CONTACT_ACT_USR_ID` | VARCHAR |  | This item stores the user ID of the user that takes action on a contact on the coding record. |
| 9 | `COD_CONTACT_ACT_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `COD_CONTACT_ACT_RSN_C_NAME` | VARCHAR | org | This item stores the reason for an action taken on a contact on the coding record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

