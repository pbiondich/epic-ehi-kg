# V_EHI_AUDIT_TAG

> This view contains audit information for appeal and grievance records for the purpose of EHI export. This view only contains data that applies to all members on a coverage. If not in the EHI context, APPEAL_GRV_AUDIT_TRAIL should be used instead.

**Primary key:** `APPEAL_GRV_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `APPEAL_GRV_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the appeal/grievance record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUDIT_TRAIL_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | The date and time that the user changed the item. |
| 4 | `AUDIT_TRAIL_ITEM` | INTEGER |  | The item that changed. |
| 5 | `AUDIT_TRAIL_LINE` | INTEGER |  | The line that was changed. |
| 6 | `OLD_VALUE_INTERNAL` | VARCHAR |  | The value of the item prior to the change. |
| 7 | `NEW_VALUE_INTERNAL` | VARCHAR |  | The value the item was changed to. |
| 8 | `OLD_VALUE_EXTERNAL` | VARCHAR |  | This item stores the value of the item prior to the change. This column shows the translated external value as of when the the item was changed. |
| 9 | `NEW_VALUE_EXTERNAL` | VARCHAR |  | This item stores the value the item was changed to. This column shows the translated external value as of when the item was changed. |
| 10 | `AUDIT_TRAIL_USER_ID` | VARCHAR |  | The unique ID associated with the user record who made the change. This column is frequently used to link to the CLARITY_EMP table. |
| 11 | `AUDIT_TRAIL_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `CHANGED_DATA_ELEMENT` | VARCHAR |  | The name of the Clarity table and column corresponding to the changed data. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `APPEAL_GRV_ID` | [APPEAL_GRV](APPEAL_GRV.md) | sole_pk | high |

