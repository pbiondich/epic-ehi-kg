# V_EHI_AUDIT_PAYOR_AND_DP_COMM

> This view contains audit data for the Continued Care and Services Coordination (CCSC) and Payer Communication workflows. Each row corresponds to a single audited event from those workflows.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 16  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `AUDIT_EVENT_TYPE_C_NAME` | VARCHAR |  | This is the event type (adding recipient, changing status, changing override fax, or changing override phone) of the item being changed. |
| 5 | `AUDIT_USER_ID` | VARCHAR |  | This is the ID of the user who is making the item change. |
| 6 | `AUDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `AUDIT_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | This is the time instant of the item change. |
| 8 | `RECIPIENT_EXTERNAL` | VARCHAR |  | This column stores the name of the recipient for this audit event in external format. For CCSC audit events this is the name of the service provider. For Payer Communication audit events this is the name of the payer recipient. |
| 9 | `DP_COORD_TYPE_C_NAME` | VARCHAR | org | The coordination type of an item being changed as part of the Continued Care and Services Coordination (post-discharge services or placement for the patient) workflow. |
| 10 | `OLD_VALUE_INTERNAL` | VARCHAR |  | This is the old value of the item being changed. |
| 11 | `NEW_VALUE_INTERNAL` | VARCHAR |  | This is the new value of the item being changed. |
| 12 | `OLD_VALUE_EXTERNAL` | VARCHAR |  | This is the externally formatted old value of the item being changed. The internally formatted value is stored in the AUDIT_OLD_VALUE column. For example, if the AUDIT_OLD_VALUE includes a category value, then this column will store the category title that describes the category value. This column shows the translated external value as of when the column was last extracted. |
| 13 | `NEW_VALUE_EXTERNAL` | VARCHAR |  | This is the externally formatted new value of the item being changed. The internally formatted value is stored in the AUDIT_NEW_VALUE column. For example, if the AUDIT_NEW_VALUE includes a category value, then this column will store the category title that describes the category value. This column shows the translated external value as of when the column was last extracted. |
| 14 | `CHANGED_DATA_ELEMENT` | VARCHAR |  | The column descriptor that contains the metadata to be associated with data stored in columns OLD_VALUE_INTERNAL and NEW_VALUE_INTERNAL. |
| 15 | `DP_RECIPIENT_SVC_LN_ID` | NUMERIC |  | This is the recipient's Service Line ID (HCS ID) of the item being changed, only used by DP workflows. |
| 16 | `DP_RECIPIENT_SVC_LN_ID_SVC_LN_NAME` | VARCHAR |  | The name (.2 item) of the service line record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

