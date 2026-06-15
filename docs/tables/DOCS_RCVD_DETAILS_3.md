# DOCS_RCVD_DETAILS_3

> Details about received documents, including request audit information.

**Overflow of:** [DOCS_RCVD_DETAILS](DOCS_RCVD_DETAILS.md)  
**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `EXT_MED_QUERY_START_DATE` | DATETIME |  | Medication dispense queries include a date range for which dispenses should be returned. This column stores the minimum lookback date requested from the medication dispense data source. This column will not generally be equal to the date of the first dispense returned. |
| 4 | `EXT_MED_QUERY_END_DATE` | DATETIME |  | Medication dispense queries include a date range for which dispenses should be returned. This column stores the maximum lookback date requested from the medication dispense data source. This column will not generally be equal to the date of the last dispense returned. |
| 5 | `MANIFEST_CSN_ID` | NUMERIC |  | The CSN of the received DICOM Manifest (DCM) that is associated with this DXR contact. |
| 6 | `HAS_TOBACCO_INFO_YN` | VARCHAR |  | This item indicates whether the contact stores discrete tobacco information. |
| 7 | `DICOM_IMAGE_LOCATION_C_NAME` | VARCHAR | org | The DICOM system that Instances requested for this contact will be stored to if received. If the study is stored, this corresponds to the study storage location (I DCM 1000) in the corresponding DCM record. |
| 8 | `PAT_DEMOGRAPHIC_SOURCE_C_NAME` | NUMERIC |  | Demographics populated on received document records can come from many different workflows. This item describes how the demographics were populated on this received document. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

