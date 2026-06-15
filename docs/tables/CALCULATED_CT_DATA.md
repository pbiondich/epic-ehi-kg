# CALCULATED_CT_DATA

> Stores information about calculations made on CT scan data.

**Primary key:** `IMY_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMY_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the sop instance record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CM_PHY_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| 4 | `CT_DOSE_IMG_QLTY_C_NAME` | VARCHAR |  | A category value representing the type of CT scan based on its location and dose. This is used to compare the relative dose and image quality of CT scans. |
| 5 | `DOSE_VAL` | NUMERIC |  | A numeric value representing the radiation dose, normalized by patient size calculated for a CT scan. This is a measure of the risk of the CT scan. |
| 6 | `DOSE_UNIT_C_NAME` | VARCHAR | org | The unit corresponding with this related group line's calculated CT size-adjusted dose value. |
| 7 | `NOISE_VAL` | NUMERIC |  | A numeric value representing the global noise calculated for a CT scan. This is a measure of the quality of the CT scan. |
| 8 | `NOISE_UNIT_C_NAME` | VARCHAR |  | The unit corresponding with this related group line's calculated CT global noise value. |
| 9 | `EFF_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant at which this related group line's data is in effect. This is given by external source and corresponds with the effective time of the CT scan. |
| 10 | `FILED_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant at which this related group line's data was filed. |
| 11 | `IS_EXTERNAL_SOURCE_YN` | VARCHAR |  | Whether or not the related group line's data was filed from an external (non-Epic) source? |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

