# IP_FLOWSHEET_ROWS

> This table contains flowsheet row (FLO) data for an encounter. This table is a key table in tying LDA assessment row lines in flowsheet data records to the LDAs, and the necessary joins are: IP_FLOWSHEET_ROWS.IP_LDA_ID with IP_LDA_NOADDSINGLE.IP_LDA_ID IP_FLOWSHEET_ROWS.INPATIENT_DATA_ID with IP_FLWSHT_REC.INPATIENT_DATA_ID IP_FLOWSHEET_ROWS.LINE with IP_FLWSHT_MEAS.OCCURANCE IP_FLWSHT_REC.FSD_ID with IP_FLWSHT_MEAS.FSD_ID.

**Primary key:** `INPATIENT_DATA_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INPATIENT_DATA_ID` | VARCHAR | PK shared | The unique ID of the inpatient data store record. |
| 2 | `LINE` | INTEGER | PK | The line count for the item. |
| 3 | `FLO_MEAS_ID` | VARCHAR | FK→ | The unique ID of the flowsheet group/row. |
| 4 | `FLO_MEAS_ID_DISP_NAME` | VARCHAR |  | The display name given to the flowsheet group/row. |
| 5 | `FLOWSHT_ROW_NAME` | VARCHAR |  | The flowsheet row name. Especially comes into play when a custom name is given to a duplicable row/group, either by a user typing it upon manually adding a row/group or from the order that fired the task template which added the duplicable row/group. |
| 6 | `IP_LDA_ID` | VARCHAR | shared | Stores the Lines/Drains/Airways (LDA) ID for the flowsheet group. |
| 7 | `ROW_VARIANCE_C_NAME` | VARCHAR |  | The flowsheet row variance. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FLO_MEAS_ID` | [IP_FLO_GP_DATA](IP_FLO_GP_DATA.md) | sole_pk | high |

