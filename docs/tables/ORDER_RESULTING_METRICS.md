# ORDER_RESULTING_METRICS

> This table contains information about how your procedural orders were resulted.

**Primary key:** `ORDER_ID`  
**Columns:** 26  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) of the order record associated with this procedure order. |
| 2 | `TEXT_GENERATION_COUNT` | INTEGER |  | The count of text generation statements used for study findings. |
| 3 | `TEXT_GENERATION_EDIT_COUNT` | INTEGER |  | The count of edited text generation statements used for study findings. This is only possible with compact forms. |
| 4 | `SUMMARY_STMT_ACTIVE_AUTO_COUNT` | INTEGER |  | The count of active automatic summary statements generated from study findings and not removed by user. |
| 5 | `SUMMARY_STMT_AUTO_COUNT` | INTEGER |  | The count of automatic summary statements generated from study findings. |
| 6 | `SUMMARY_STMT_ACTIVE_EDIT_COUNT` | INTEGER |  | The count of active edited summary statements that were not removed by the user. |
| 7 | `SUMMARY_STMT_EDIT_COUNT` | INTEGER |  | The count of edited summary statements. |
| 8 | `FINDINGS_SDE_COUNT` | INTEGER |  | The count of SmartData elements documented on study findings. |
| 9 | `INTRA_FINDINGS_INCLUDED_COUNT` | INTEGER |  | The count of SmartData elements recorded by intraprocedural findings events in the procedural narrator that are included in final report. |
| 10 | `INTRA_FINDINGS_REMOVED_COUNT` | INTEGER |  | The count of SmartData elements recorded by intraprocedural findings events in the procedural narrator excluded from the final report. |
| 11 | `VESSEL_ANNOTATION_COUNT` | INTEGER |  | The count of vessel annotations documented in Study Review. |
| 12 | `COMPACT_FORM_YN` | VARCHAR |  | Indicates whether the order has been resulted with a Compact Form in Study Review. |
| 13 | `MEASUREMENT_COUNT` | INTEGER |  | The count of result components on the order. |
| 14 | `CALCULATED_MEASUREMENT_COUNT` | INTEGER |  | The count of calculated result components on the order. |
| 15 | `XML_MEASUREMENT_COUNT` | INTEGER |  | The count of measurements exchanged with measurement exchange on the order. |
| 16 | `MODIFIED_XML_MEASUREMENT_COUNT` | INTEGER |  | The count of exchanged measurements that were modified on the order. |
| 17 | `ORDER_TYPE_C_NAME` | VARCHAR | org | The order type category number for the procedure order. |
| 18 | `RADIOLOGY_STATUS_C_NAME` | VARCHAR |  | Stores the imaging status of the study. |
| 19 | `ACTV_EXCLUDE_FROM_CDS_REASON_C_NAME` | VARCHAR |  | The Exclude From Decision Support reason for the order. It will be either 1 - Unsuccessful Attempt represents an order that was not successfully completed. or 2 - Documented on Wrong Patient represents the order's result information was documented on the incorrect patient. |
| 20 | `TOTAL_STUDY_RVW_TIME` | INTEGER |  | Total time study review was open for the study. |
| 21 | `FINAL_PHYS_STUDY_RVW_TIME` | INTEGER |  | Total time study review was open by the finalizing physician. |
| 22 | `READ_PHYS_STUDY_RVW_TIME` | INTEGER |  | Total time study review was open by reading physicians who are not the finalizing physician. |
| 23 | `NON_READ_USER_STUDY_RVW_TIME` | INTEGER |  | Total time study review was open by all users not listed as a reading physician. |
| 24 | `FINAL_PHYS_SDE_COUNT` | INTEGER |  | Total number of SmartData elements documented on study findings by the finalizing physician. |
| 25 | `READ_PHYS_SDE_COUNT` | INTEGER |  | Total number of SmartData elements documented on study findings by reading physicians who are not the finalizing physician. |
| 26 | `NON_READ_USER_SDE_COUNT` | INTEGER |  | Total number of SmartData elements documented on study findings by all users not listed as a reading physician. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

