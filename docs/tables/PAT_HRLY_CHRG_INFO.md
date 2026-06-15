# PAT_HRLY_CHRG_INFO

> This table contains information on hourly charges on patient records.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 5 | `START_TIME` | DATETIME (Local) |  | The start time of an hourly charge on this patient contact. |
| 6 | `STOP_TIME` | DATETIME |  | The stop time of an hourly charge on this patient contact. |
| 7 | `CHARGE_HTR_ID` | VARCHAR |  | This column contains the id of the hourly charge's hospital transaction record. |
| 8 | `PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 9 | `UNIT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 10 | `BCC_ID` | NUMERIC |  | The unique ID of the cost center record associated with the bed charge. |
| 11 | `BCC_ID_COST_CENTER_NAME` | VARCHAR |  | The name of the cost center. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

