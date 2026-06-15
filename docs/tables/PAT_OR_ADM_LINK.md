# PAT_OR_ADM_LINK

> This table stores the link between encounter ID and the associated log or case ID.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique ID of the patient encounter. |
| 2 | `PAT_ENC_DATE_REAL` | FLOAT |  | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `CM_CT_OWNER_ID` | VARCHAR |  | The community ID of the owner of this encounter. |
| 4 | `OR_LINK_CSN` | NUMERIC |  | The unique contact serial number of the admission linked to the procedural case/log . This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 5 | `OR_LINK_INP_ID` | VARCHAR |  | The inpatient data ID used by the case and log. |
| 6 | `OR_SHARE_PERIOP_YN` | VARCHAR |  | Do OR management system Periop activities share data with Inpatient? |
| 7 | `OR_SUM_BLOCKS_ID` | NUMERIC |  | The summary block record associated with this surgery. |
| 8 | `OR_SRC_VISIT_CSN` | NUMERIC |  | This item will store the Contact Serial Number (CSN) for the visit in which this surgery was created. |
| 9 | `OR_CASELOG_ID` | VARCHAR |  | The unique ID of the procedural case/log. NOTE: Use the CASE_ID or LOG_ID columns to link to the case or log record, respectively. This column should not be used to write reports. |
| 10 | `UPDATE_DATE` | DATETIME (Local) |  | The date and time when this row was extracted into enterprise reporting. |
| 11 | `OR_MED_REV_HSB_ID` | NUMERIC |  | The summary block record associated with the medication review workflow. This summary block record will store all of the review history. |
| 12 | `CASE_ID` | VARCHAR | shared | The unique ID of the case (ORC) that is associated with this encounter. |
| 13 | `LOG_ID` | VARCHAR | shared | The unique ID of the log (ORL) that is associated with this encounter. |
| 14 | `PXPASS_ID` | NUMERIC |  | The unique ID of the Procedure Pass that is associated with this surgical encounter. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

