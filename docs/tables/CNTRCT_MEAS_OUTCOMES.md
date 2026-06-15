# CNTRCT_MEAS_OUTCOMES

> This table will hold measurement contract associated with an outcome.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PRIMSRC_QUALITY_MEAS_OUTCOME_C_NAME` | VARCHAR |  | The outcome as calculated by the primary sources. This will be a single value that says whether the patient is in the numerator for the measure, in the denominator only, or excluded from the measure. |
| 4 | `SUPPSRC_QUALITY_MEAS_OUTCOME_C_NAME` | VARCHAR |  | The outcome as calculated by the supplemental sources. This will be a single value that says whether the patient is in the numerator for the measure, in the denominator only, or excluded from the measure. |
| 5 | `ATTR_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 6 | `ATTR_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 7 | `ATTR_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 8 | `ATTR_SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 9 | `OUTCOME_IS_VALID_YN` | VARCHAR |  | Indicates whether or not the calculated measure outcome is valid. For example, if the outcome was deleted from the source database, the relevant outcome would be considered invalid (0-No). |
| 10 | `QM_EVENT_DATE` | DATETIME |  | For event-based measures, this is the date the qualifying event occurred for the measure outcome. |
| 11 | `LAST_REL_SERV_DATE` | DATETIME |  | The last date the service that satisfies the quality measure was performed. |
| 12 | `CLINICAL_DUE_DATE` | DATETIME |  | The next date that a clinical service that satisfies a quality measure is due. This due date is based on the frequency with which the service needs to be completed and the last date that it was completed. |
| 13 | `PROP_DAYS_COVERED` | NUMERIC |  | The current Proportion of Days Covered (PDC) for the associated outcome. The expected range of values are 0-1 with decimal values allowed. |
| 14 | `IMPACTABLE_YN` | VARCHAR |  | Indicates if there are enough days left in the measurement year that a fill today could move the patient to meet the adherence threshold. |
| 15 | `FIRST_FILL_YN` | VARCHAR |  | Is this outcome in the First Fill status? This status is where the patient has filled the medication once, but has not filled it a second time. During this timeframe the patient is not technically in the denominator yet, but once they pick up that second fill they will be. |
| 16 | `ATTR_PROV_GROUP_ID` | NUMERIC |  | The attributed provider group for the calculated contract measure outcome. |
| 17 | `ATTR_PROV_GROUP_ID_PROV_GROUP_NAME` | VARCHAR |  | Record name |
| 18 | `INDEX_RX_START_DATE` | DATETIME |  | The prescription start date during the measurement period for a medication adherence measure. This is the start date to use when calculating a Proportion of Days Covered (PDC) value. |
| 19 | `LAST_IMPACTABLE_DATE` | DATETIME |  | The current last impactable date for the associated outcome. After the last impactable date has passed, there are not enough days remaining in the performance period for the patient to meet the measure's proportion of days covered (PDC) goal. |
| 20 | `HYB_SRC_QUALITY_MEAS_OUTCOME_C_NAME` | VARCHAR |  | The category number for the hybrid source outcome. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 21 | `ADMSN_DATE` | DATETIME |  | The admission date for encounter level outcomes. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

