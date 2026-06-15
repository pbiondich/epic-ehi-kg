# CRF_AUDIT_HISTORY

> Audit History Data Model for Claim Reference Data records.

**Primary key:** `REF_DATA_ID`, `LINE`  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REF_DATA_ID` | NUMERIC | PK FK→ | The unique identifier for the Claim Reference Data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CHANGE_UTC_DTTM` | DATETIME (UTC) |  | The instant of the audit history event. |
| 4 | `CHANGE_USER_ID` | VARCHAR |  | The ID of the user responsible for the record event logged in the Audit History. |
| 5 | `CHANGE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `CHANGE_ACTION_C_NAME` | VARCHAR |  | The action type of the event in the record Audit History. |
| 7 | `CHANGE_ITEM` | INTEGER |  | The item changed in the event of the record Audit History. |
| 8 | `PREVIOUS_RAW_VALUE` | VARCHAR |  | The previous raw value of the edited item in the record. |
| 9 | `NEW_RAW_VALUE` | VARCHAR |  | The new raw value of the edited item in the record. |
| 10 | `PREVIOUS_VENDOR_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 11 | `NEW_VENDOR_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 12 | `PREVIOUS_CLAIM_ID` | NUMERIC |  | The claim which was previously associated with the CRF record before the audit history event. |
| 13 | `NEW_CLAIM_ID` | NUMERIC |  | The claim which is newly associated with the CRF record after the audit history event. |
| 14 | `NEW_ROI_ID` | VARCHAR |  | The release record which was created using the CRF record during the audit history event. |
| 15 | `NEW_IS_CANCELLED_BY_PROV_C_NAME` | VARCHAR |  | The new is cancelled flag which was updated during the audit history event. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REF_DATA_ID` | [CLAIM_REFERENCE_DATA](CLAIM_REFERENCE_DATA.md) | sole_pk | high |

