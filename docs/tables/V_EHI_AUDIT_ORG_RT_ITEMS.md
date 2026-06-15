# V_EHI_AUDIT_ORG_RT_ITEMS

> This view contains audit information for document records for the purpose of Electronic Health Information (EHI) export. If not in the EHI context, RAD_THP_VOLUME_AUDIT should be used instead.

**Primary key:** `ORG_RECORD_ID`  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORG_RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the radiotherapy volume record. |
| 2 | `LINE` | INTEGER |  | The line number for the information associated with this contact. |
| 3 | `AUDIT_USER_ID` | VARCHAR |  | This item contains the user ID associated with the data changed on this line of the audit trail. |
| 4 | `AUDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `ITEM_LINE` | INTEGER |  | Stores the line number of the old value in the associated item. |
| 6 | `INSTANT_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant the change being audited was applied to the record. |
| 7 | `RT_VOL_AUD_ITEM` | NUMERIC |  | Stores the changed item number for an audit trail entry. |
| 8 | `CHANGED_DATA_ELEMENT` | VARCHAR |  | The table and column descriptor associated with the item in the RT_VOL_AUD_ITEM column. |
| 9 | `OLD_VALUE_INTERNAL` | VARCHAR |  | Contains the old value of the item in internal chronicles format. |
| 10 | `NEW_VALUE_INTERNAL` | VARCHAR |  | Contains the new value of the item in internal chronicles format. |
| 11 | `OLD_VALUE_EXTERNAL` | VARCHAR |  | Contains the old value of the item in external format. |
| 12 | `NEW_VALUE_EXTERNAL` | VARCHAR |  | Contains the new value of the item in external format. |
| 13 | `VERSION_NUMBER` | VARCHAR |  | Contains the version ID of the resource that this audit entry originated from. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

