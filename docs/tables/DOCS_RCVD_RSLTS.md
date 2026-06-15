# DOCS_RCVD_RSLTS

> This table stores discrete results received from outside sources.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 47  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `RESULT_INST_DTTM` | DATETIME (Local) |  | Local instant for the result |
| 6 | `RESULT_PROC_NAME` | VARCHAR |  | Free text name of the procedure |
| 7 | `RESULT_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 8 | `PROC_LOINC` | VARCHAR |  | The LOINC code associated with this procedure. |
| 9 | `RESULT_ENC_IDENT` | VARCHAR |  | Link to the ordering encounter |
| 10 | `RESULT_KEY` | VARCHAR |  | Key to link the other result information to this order |
| 11 | `RESULT_STATUS_C_NAME` | VARCHAR |  | Status for this result |
| 12 | `RESULT_ABNORMAL_C` | VARCHAR |  | Indicates whether this result was flagged as abnormal |
| 13 | `SPECIMEN_DISP` | VARCHAR |  | The displayable specimen name(s) for this result. |
| 14 | `RESULT_SOURCE_CSN` | NUMERIC |  | The unique ID of the Document Received record contact originally storing this result. |
| 15 | `RSLT_LST_UPD_INST_DTTM` | DATETIME (UTC) |  | Stores the last update instant of the result in UTC. |
| 16 | `RESULT_RESULTING_STATUS_C_NAME` | VARCHAR |  | This items stores the resulting status of the result. |
| 17 | `RSLT_ABNORMAL_ID_C_NAME` | VARCHAR |  | This item stores the mapped result abnormality. |
| 18 | `RESULT_LOINC_ID_LNC_LONG_NAME` | VARCHAR |  | The more readable format than the fully specified name in Logical Observation Identifiers Names and Codes (LOINC®) code. |
| 19 | `EXTERNAL_RESULT_TYPE_C_NAME` | VARCHAR |  | This item stores the type of the result. |
| 20 | `RESULT_INVALID_YN` | VARCHAR |  | This item indicates whether or not this line of result data is invalid. |
| 21 | `RESULT_UTC_DTTM` | DATETIME (UTC) |  | Stores the UTC instant of the moment this order was resulted. |
| 22 | `SPECIMEN_COLLECTION_UTC_DTTM` | DATETIME (UTC) |  | UTC Instant of collection for this order's specimen(s) |
| 23 | `RSLT_UNSUCCESSFUL_FLG_C_NAME` | VARCHAR |  | Indicates whether a result was an unsuccessful attempt |
| 24 | `RSLT_UNSUCCESS_INST_UTC_DTTM` | DATETIME (UTC) |  | Instant the result unsuccessful flag was set |
| 25 | `RSLT_PT_SRC_APP_C_NAME` | VARCHAR | org | If this result is a patient-entered result, this item stores the application which was used to submit it for the contact (e.g. MyChart). |
| 26 | `RSLT_SRC_WPR_ID` | VARCHAR |  | Stores the ID of the MyChart user who edited the result for the contact. |
| 27 | `RSLT_SRC_ORG_ID` | NUMERIC |  | Stores the Data Exchange Organization record ID of the source organization for this order. |
| 28 | `RSLT_SRC_ORG_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 29 | `RSLT_AUTH_PROV_NAME` | VARCHAR |  | The full name of the provider responsible for authorizing this result. |
| 30 | `RESULT_CONTACT_SRC_C_NAME` | VARCHAR |  | Stores the source of the result from the sending system. |
| 31 | `RSLT_IMAGE_TYPE_C_NAME` | VARCHAR |  | This item stores the type of the imaging result. |
| 32 | `RSLT_EXAM_BEGIN_UTC_DTTM` | DATETIME (UTC) |  | This item stores the exam begin instant of the result. |
| 33 | `RSLT_EXAM_END_UTC_DTTM` | DATETIME (UTC) |  | This item stores the exam end instant of the result. |
| 34 | `RSLT_RPT_TYPE_C_NAME` | VARCHAR |  | This item stores the report type for the result. |
| 35 | `RSLT_LATERALITY` | VARCHAR |  | This item stores the laterality for the result. |
| 36 | `RSLT_READING_ACTIVITY_ID` | NUMERIC |  | This item stores the reading activity for the result. |
| 37 | `RSLT_READING_ACTIVITY_ID_ADV_ACTIVITY_NAME` | VARCHAR |  | Internal name of the Advantage Activity record |
| 38 | `LAB_RSLT_TYPE_C_NAME` | VARCHAR |  | This item stores the type of lab result |
| 39 | `RSLT_HAS_VAR_YN` | VARCHAR |  | This item is set to Yes if the result has any associated Genomic Variants |
| 40 | `RSLT_STUDY_UID` | VARCHAR |  | The DICOM Study Instance Unique Identifier (UID) as recorded by the image archive. |
| 41 | `RSLT_LAB_REF_IDENT` | VARCHAR |  | This item stores the lab reference ID for the result. |
| 42 | `RSLT_SRC_ORG_HSI` | VARCHAR |  | Stores the HSI of the source organization for this order |
| 43 | `SPECIMEN_COLLECTION_INST_DTTM` | DATETIME (Local) |  | Local Instant of collection for this order's specimen(s). |
| 44 | `SPECIMEN_COLLECTION_DATE` | DATETIME |  | Date of collection for this order's specimen(s) |
| 45 | `RESULT_BULK_STAT_C_NAME` | VARCHAR |  | The status of this data element within DINE. |
| 46 | `RSLT_HAS_SEQDATA_YN` | VARCHAR |  | This item is set to Yes if the result has any associated sequencing data |
| 47 | `RSLT_BULK_INCL_DATE` | DATETIME |  | The date to compare to the change tracking window when loading flat files in bulk via DINE. If the date is within the window, but the data element is missing from the load, then the data element is invalidated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

