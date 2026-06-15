# HSPC_EPSD_BENEFIT_PRDS_HX

> This table contains audit history for Hospice Benefit Periods.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `START_DATE` | DATETIME |  | History of the Hospice Benefit Period Start Dates. |
| 4 | `END_DATE` | DATETIME |  | History of the Hospice Benefit Period End Dates. |
| 5 | `HSPC_BENEFIT_PRDS_COMMENT_HX` | VARCHAR |  | History of the comments left on Hospice Benefit Periods. |
| 6 | `PERIOD_CNT` | INTEGER |  | History of the Hospice Benefit Period number. |
| 7 | `VCTI_DATE` | DATETIME |  | History of the Hospice Benefit Period first CTI date. |
| 8 | `VCTI_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 9 | `VCTI_RECEIVER_USER_ID` | VARCHAR |  | History of the ID of the user who received the Hospice Benefit Period first CTI. |
| 10 | `VCTI_RECEIVER_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `EDIT_USER_ID` | VARCHAR |  | History of the ID of the user who made edits to the Hospice Benefit Period data. |
| 12 | `EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 13 | `EDIT_INST_DTTM` | DATETIME (UTC) |  | History of the instants at which the Hospice Benefit Period data was edited. |
| 14 | `EDIT_LINE` | INTEGER |  | History of which line of the Hospice Benefit Period was edited. This is the line number found in column LINE of HH_EPSD_BEN_PRDS. |
| 15 | `SECOND_VCTI_DATE` | DATETIME |  | History of the Hospice Benefit Period second CTI date. |
| 16 | `SECOND_VCTI_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 17 | `SECOND_VCTI_RECEIVER_USER_ID` | VARCHAR |  | History of the user ID who received Hospice Benefit Period second CTI. |
| 18 | `SECOND_VCTI_RECEIVER_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

