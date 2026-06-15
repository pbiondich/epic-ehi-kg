# V_EHI_REG_ITEM_AUDIT_BEN

> Benefit record audit events. This view contains audit information for benefit records for the purpose of Electronic Health Information (EHI) export. If not in the EHI context, REG_ITEM_AUDIT_BEN and REG_ITEM_AUDIT_LINES_BEN should be used instead.

**Primary key:** `ITEM_AUDIT_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ITEM_AUDIT_ID` | NUMERIC | PK | The unique identifier (.1 item) for the audit event record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUDIT_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | The instant the audit was recorded in the UTC time zone. |
| 4 | `AUDIT_INSTANT_LOCAL_DTTM` | DATETIME (Attached) |  | The instant the audit was recored in the local time zone where the change took place. |
| 5 | `BENEFIT_ID` | NUMERIC |  | Benefit record that was changed in this audit event. |
| 6 | `CHANGED_DATA_ELEMENT` | VARCHAR |  | The name of the Clarity table and column corresponding to the changed data. |
| 7 | `CHANGED_LINE` | INTEGER |  | Item line that was changed in the audit event. |
| 8 | `CHANGED_SUB_LINE` | INTEGER |  | Item subline that was changed in the audit event. |
| 9 | `OLD_VALUE_EXTERNAL` | VARCHAR |  | External value of the item line before the item was changed. |
| 10 | `NEW_VALUE_EXTERNAL` | VARCHAR |  | External value of the item line after the item was changed. |
| 11 | `USER_ID` | VARCHAR | FK→ | User who changed the items in this audit event. |
| 12 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

