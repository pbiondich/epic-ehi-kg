# PAT_SURG_DATA

> This table contains information about items related to surgery, including: primary surgeon, procedure, location, and case and log status.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 17  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is populated only if you use IntraConnect. |
| 5 | `CS_SURG_SURGEON_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 6 | `CS_SURG_PROC_ID` | VARCHAR |  | The unique ID of the primary procedure for the surgery, stored here so that it can be synched across deployments to be shown in the chart review. |
| 7 | `CS_SURG_PROC_ID_PROC_NAME` | VARCHAR |  | The name of the surgical procedure record. |
| 8 | `CS_SURG_LOCATION_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 9 | `CS_SURG_CASE_STAT_C_NAME` | VARCHAR | org | The case status category number for the associated surgery, stored here so that it can be synched across deployments to be shown in the chart review. |
| 10 | `CS_SURG_LOG_STAT_C_NAME` | VARCHAR | org | The log status category number for the associated surgery, stored here so that it can be synched across deployments to be shown in the chart review. |
| 11 | `CS_SURG_EAP_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 12 | `CS_SURG_PROC_FRTXT` | VARCHAR |  | The procedure name as exactly ordered by the surgeon/provider, stored here so that it can be synced across deployments to be shown in the chart review. |
| 13 | `CS_SURG_PROC_LAT_C_NAME` | VARCHAR | org | The procedure laterality, stored here so that it can be synced across deployments to be shown in the chart review. |
| 14 | `CS_SURG_SCHED_DTTM` | DATETIME (UTC) |  | The procedure scheduled time, stored here so that it can be synced across deployments to be shown in the chart review. |
| 15 | `CS_SURG_PROC_CMT` | VARCHAR |  | The procedure comments, stored here so that it can be synced across deployments to be shown in the chart review. |
| 16 | `CS_SURG_NOT_PERF_YN` | VARCHAR |  | The flag determining if the surgery was marked as procedure not performed, stored here so that it can be synced across deployments. |
| 17 | `CS_SURG_CASE_CLASS_C_NAME` | VARCHAR |  | Stores the class of the case (either Inpatient or Outpatient), stored here so that the class of the case can be determined across deployments. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

