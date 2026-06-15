# V_EHI_REG_ITEM_AUDIT_EPT

> Patient record audit events. This view contains audit information for patient records for the purpose of Electronic Health Information (EHI) export. If not in the EHI context, REG_ITEM_AUDIT_EPT and REG_ITEM_AUDIT_LINES_EPT should be used instead.

**Primary key:** `ITEM_AUDIT_ID`, `LINE`  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ITEM_AUDIT_ID` | NUMERIC | PK | The unique identifier (.1 item) for the audit event record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUDIT_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | The instant the audit was recorded in the UTC time zone. |
| 4 | `AUDIT_INSTANT_LOCAL_DTTM` | DATETIME (Attached) |  | The instant the audit was recored in the local time zone where the change took place. |
| 5 | `PAT_ID` | VARCHAR | FK→ | Patient that was changed in this audit event. |
| 6 | `CHANGED_PAT_ENC_CSN_ID` | NUMERIC | FK→ | Contact serial number of the contact that was changed in this audit event. |
| 7 | `CHANGED_DATA_ELEMENT` | VARCHAR |  | The name of the Clarity table and column corresponding to the changed data. |
| 8 | `CHANGED_ITEM_NAME` | VARCHAR |  | Name of the item that was changed in the audit event. |
| 9 | `CHANGED_LINE` | INTEGER |  | Item line that was changed in the audit event. |
| 10 | `CHANGED_SUB_LINE` | INTEGER |  | Item subline that was changed in the audit event. |
| 11 | `OLD_VALUE_EXTERNAL` | VARCHAR |  | External value of the item line before the item was changed. |
| 12 | `NEW_VALUE_EXTERNAL` | VARCHAR |  | External value of the item line after the item was changed. |
| 13 | `USER_ID` | VARCHAR | FK→ | User who changed the items in this audit event. |
| 14 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CHANGED_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

