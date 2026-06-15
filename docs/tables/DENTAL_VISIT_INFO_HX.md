# DENTAL_VISIT_INFO_HX

> The DENTAL_VISIT_INFO_HX table contains the edit history of a dental visit record.

**Primary key:** `REGIMEN_ID`, `LINE`  
**Columns:** 23  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGIMEN_ID` | NUMERIC | PK shared | The unique ID of the visit record for this row. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `VISIT_MOD_INST_DTTM` | DATETIME (Local) |  | The date and time the visit was modified. |
| 4 | `VISIT_MOD_USER_ID` | VARCHAR |  | The unique ID associated with the user record that modified data for a visit. |
| 5 | `VISIT_MOD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `VISIT_LINKED_CSN` | NUMERIC |  | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 7 | `TREATMENT_HX_ID` | NUMERIC | FK→ | The revision history of the treatment ID containing the visit. |
| 8 | `VISIT_SPAC_DAYS_HX` | INTEGER |  | The revision history of the requested spacing, in days, for a visit. |
| 9 | `VISIT_SCHED_INST_HX` | VARCHAR |  | The revision history of the scheduling instructions for a visit. |
| 10 | `VISIT_APPT_LEN_HX` | INTEGER |  | The revision history of the requested appointment length for a visit. |
| 11 | `VISIT_APPT_HX` | NUMERIC |  | The revision history of the appointment linked to a visit. |
| 12 | `VISIT_NUMBER_HX` | INTEGER |  | The revision history of a visit's order within a dental treatment. |
| 13 | `VISIT_CHRON_INSTANT_DTTM` | DATETIME (Attached) |  | This column records the date and time of a documentation change to the dental visit within the dental treatment plan. |
| 14 | `DENT_SCH_STAT_HX_C_NAME` | VARCHAR |  | Audit trail for dental scheduling status |
| 15 | `DENT_REQ_DATE_HX_DATE` | DATETIME |  | Audit trail for Requested Date to Schedule |
| 16 | `DENT_VIS_TYPE_HX_ID_PRC_NAME` | VARCHAR |  | The name of the visit type. |
| 17 | `DENT_VIS_DEPT_HX_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 18 | `DENT_VIS_PROV_HX_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 19 | `DENT_VIS_PTYPE_HX_C_NAME` | VARCHAR | org | Audit trail for a visit's requested provider type for scheduling |
| 20 | `DENT_VIS_STAT_HX_C_NAME` | VARCHAR |  | Dental visit status audit item |
| 21 | `VISIT_NAME_HX` | VARCHAR |  | The historical name of the dental visit. |
| 22 | `RFL_ORDER_HX_ID` | NUMERIC |  | History of linked referral orders for a dental visit. |
| 23 | `DENT_RDY_SCHED_HX_YN` | VARCHAR |  | Audit trail for ready for scheduling flag. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `TREATMENT_HX_ID` | [PSYCH_TREATMENT_HISTORY](PSYCH_TREATMENT_HISTORY.md) | sole_pk | high |

