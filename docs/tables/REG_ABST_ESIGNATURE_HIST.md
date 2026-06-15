# REG_ABST_ESIGNATURE_HIST

> This table contains the past e-signature data for fields in each abstraction.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ESIG_AUDIT_FIELD` | VARCHAR |  | The e-signature field that was modified. |
| 4 | `ESIG_AUDIT_INST_DTTM` | DATETIME (UTC) |  | The date and time in UTC associated with this line of the e-signature audit trail. |
| 5 | `ESIG_AUDIT_ACTION_C_NAME` | VARCHAR |  | The action category ID for this line of the e-signature audit trail. |
| 6 | `ESIG_AUDIT_USER_ID` | VARCHAR |  | The unique ID of the user associated with the action for this line of the e-signature audit trail. |
| 7 | `ESIG_AUDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `ESIG_AUDIT_SIGNATURE_KEY` | VARCHAR |  | The key for the e-signature set at the instant of this event. |
| 9 | `ESIG_AUDIT_META_INDEX` | INTEGER |  | The line number for the associated e-signature metadata used in this action. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

