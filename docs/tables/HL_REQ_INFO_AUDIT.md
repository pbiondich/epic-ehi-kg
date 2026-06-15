# HL_REQ_INFO_AUDIT

> Hospital Logistics Request Information Audit.

**Primary key:** `HLR_ID`, `LINE`  
**Columns:** 24  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HLR_ID` | NUMERIC | PK shared | The unique identifier for the request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ENTRY_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant when a change was made to this Logistics Request's info. |
| 4 | `ENTRY_USER_ID` | VARCHAR |  | The user that made the change to this Logistics Request. |
| 5 | `ENTRY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `ENTRY_TECH_ID` | NUMERIC |  | The Logistics Technician that made the change to this Logistics Request. |
| 7 | `START_UTC_DTTM` | DATETIME (UTC) |  | The audit trail for this Logistics Request's start instant (I HLR 115). |
| 8 | `PRIORITY_C_NAME` | VARCHAR |  | The audit trail for this Logistics Request's priority (I HLR 120). |
| 9 | `START_PLF_ID_RECORD_NAME` | VARCHAR |  | The name of the PLF record. |
| 10 | `DYNAMIC_START_TYPE_C_NAME` | VARCHAR |  | The audit trail for this Logistics Request's dynamic start location type (I HLR 126). |
| 11 | `END_PLF_ID_RECORD_NAME` | VARCHAR |  | The name of the PLF record. |
| 12 | `DYNAMIC_END_TYPE_C_NAME` | VARCHAR |  | The audit trail for this Logistics Request's dynamic end location type (I HLR 131). |
| 13 | `TECHS_NUM` | INTEGER |  | The audit trail for this Logistics Request's number of required techs (I HLR 135). |
| 14 | `MODE_C_NAME` | VARCHAR | org | The audit trail for this Logistics Request's mode (I HLR 140). |
| 15 | `REGION_SEC_ID` | NUMERIC |  | The audit trail for this Logistics Request's region (I HLR 240). |
| 16 | `REGION_SEC_ID_RECORD_NAME` | VARCHAR |  | The name of this cleaning sector. |
| 17 | `SECTOR_SEC_ID` | NUMERIC |  | The audit trail for this Logistics Request's sector (I HLR 241). |
| 18 | `SECTOR_SEC_ID_RECORD_NAME` | VARCHAR |  | The name of this cleaning sector. |
| 19 | `DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 20 | `HOSP_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 21 | `SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 22 | `PHONE_NUMBER` | VARCHAR |  | The audit trail for this Logistics Request's phone number (I HLR 260). |
| 23 | `BED_TYPE_C_NAME` | VARCHAR | org | The audit trail for this Logistics Request's bed type (I HLR 148). |
| 24 | `TRIP_TYPE_C_NAME` | VARCHAR |  | The audit trail indicating this request's trip type. Blank is interpreted as One-Way. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

