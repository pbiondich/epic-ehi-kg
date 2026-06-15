# V_EHI_AUDIT_ERT_ITEMS

> This view contains audit information for document records for the purpose of Electronic Health Information (EHI) export. If not in the EHI context, RADIOTHERAPY_AUDIT_TRAIL should be used instead.

**Primary key:** `RT_SUMMARY_ID`  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RT_SUMMARY_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the radiotherapy summary record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER |  | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `ITEM_LINE` | INTEGER |  | Stores the line number of the old value in the associated item. |
| 5 | `ITEM_PIECE` | INTEGER |  | For related-multi items, stores the piece number of the old value in the associated item on the associated line. |
| 6 | `AUDIT_USER_ID` | VARCHAR |  | This item contains the user ID associated with the data changed on this line of the audit trail. |
| 7 | `AUDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `OLD_VALUE_INTERNAL` | VARCHAR |  | Contains the old value of the item in internal chronicles format. |
| 9 | `NEW_VALUE_INTERNAL` | VARCHAR |  | Contains the new value of the item in internal chronicles format. |
| 10 | `OLD_VALUE_EXTERNAL` | VARCHAR |  | Contains the old value of the item in external format. |
| 11 | `NEW_VALUE_EXTERNAL` | VARCHAR |  | Contains the new value of the item in external format. |
| 12 | `ITEM_NUMBER` | NUMERIC |  | Stores the changed item number for an audit trail entry. |
| 13 | `INSTANT_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant the change being audited was applied to the contact. |
| 14 | `CHANGED_DATA_ELEMENT` | VARCHAR |  | The table and column descriptor associated with the item in the ITEM_NUMBER column. |
| 15 | `VERSION_NUMBER` | INTEGER |  | Contains the version ID of the resource that this audit entry originated from. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

