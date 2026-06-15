# DOCS_RCVD_PROBS

> This table stores problems received from outside sources.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 41  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `PROB_REF_ID` | VARCHAR |  | This item stores the unique reference identifier associated with the problem. |
| 6 | `PROB_NAME` | VARCHAR |  | This item stores the problem name sent by the external source. |
| 7 | `PROB_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 8 | `PROB_DAT_NOT_DT` | DATETIME |  | This item stores the problem noted date. |
| 9 | `PROB_DAT_RSLV_DT` | DATETIME |  | This item stores the problem resolved date. |
| 10 | `PROB_PRIORITY` | VARCHAR |  | This item stores the priority of the problem. |
| 11 | `PROB_PRIORITY_ID_C_NAME` | VARCHAR | org | This item stores the mapped problem priority category ID. |
| 12 | `PROB_IS_CHRONIC_YN` | VARCHAR |  | This item is set if the problem is chronic. |
| 13 | `PROB_STATUS` | VARCHAR |  | This item stores the problem status. |
| 14 | `PROB_STATUS_ID_C_NAME` | VARCHAR |  | This item stores the mapped problem status category value. |
| 15 | `PROB_SRC_LPL_ID` | NUMERIC |  | This item stores the ID of the source problem. |
| 16 | `PROB_TYP_OF_CHNG_C_NAME` | VARCHAR |  | This item stores the type of change associated with the problem. |
| 17 | `PROB_SRC_DXR_CSN` | NUMERIC |  | This item will store the contact serial number of the received document record that owns the instance of this problem. |
| 18 | `PROB_OVRD_LPL_ID` | NUMERIC |  | This item stores the record identifier of the local problem that this external problem should be grouped with. |
| 19 | `PROB_COMMENTS_ID` | VARCHAR |  | This item stores the identifier of the Notes (HNO) record that stores problem comments. |
| 20 | `PROB_LAST_UPD_DTTM` | DATETIME (UTC) |  | This item stores the date and time when the problem was last updated by the external system. |
| 21 | `PROB_PT_SRC_APP_C_NAME` | VARCHAR | org | If this problem is a patient-entered problem (i.e. Received Documents type = 25), this item stores the application which was used to edit the problem for the contact (e.g. MyChart or Welcome). If blank, this is assumed to be MyChart. |
| 22 | `PROB_DT_NOTED_NF_C_NAME` | VARCHAR |  | This item stores the nullFlavor value from the effectiveTime low node in a received CDA document. |
| 23 | `PROB_DT_RESOLV_NF_C_NAME` | VARCHAR |  | This item stores the nullFlavor value from the effectiveTime high node in a received CDA document. |
| 24 | `PROB_STATE_C_NAME` | VARCHAR |  | This item stores the value from the statusCode node for a problem entry in a received CDA document. |
| 25 | `PROB_STATUS_ENTRY_C_NAME` | VARCHAR |  | This item stores the value from the status entryRelationship node in a received CDA document. This item itself is not the status of the problem. |
| 26 | `PROB_HIST_STATUS_C_NAME` | VARCHAR |  | The item indicates whether the problem is current or historic. |
| 27 | `PROB_HIST_DATE` | DATETIME |  | This item stores the date that the historical status for this problem is valid through. After this date, the historical status needs to be rechecked. |
| 28 | `PROB_SRC_WPR_ID` | VARCHAR |  | Stores the ID of the MyChart user who edited the problem for the contact. |
| 29 | `PROB_EVENT_IDENT` | VARCHAR |  | This item stores the ID of the event that is associated with a problem. In cases where there are multiple encounters that link to a problem, the earliest encounter is represented here. |
| 30 | `PROB_DUP_LPL_ID` | NUMERIC |  | Stores the Problem List ID of an internal problem that is a duplicate of this row in the Received Document. |
| 31 | `PROB_PAT_ENC_CSN_ID` | NUMERIC | FK→ | Stores the contact serial number of the encounter that the problem was added on |
| 32 | `PROB_DX_LATERALITY_C_NAME` | VARCHAR | org | The laterality category ID for the problem. |
| 33 | `PROB_ANATOMICAL_LOC_CODE` | VARCHAR |  | The anatomical location code of the problem. |
| 34 | `PROB_ANATOMICAL_LOC_DISP_NAME` | VARCHAR |  | The anatomical location display name of the problem. |
| 35 | `PROB_OVERVIEW_NOTE_ID` | VARCHAR |  | The unique ID of the Note for the overview note of this problem. |
| 36 | `PROB_COMMENTS_CHECKSUM` | VARCHAR |  | This item stores the checksum of the Overview note and most recent Assessment and Plan Note along with the creation instant of the most recent Assessment and Plan Note in UTC and the Author's first and last name of the Assessment and Plan note. The format of the data is "checksum C127 instant C127 first C127 last". C127 is character 127. There are no spaces between the data elements. |
| 37 | `PROB_FILTER_REASON_C_NAME` | VARCHAR |  | Stores the reason why an external problem should be filtered from the composite record |
| 38 | `PROB_DX_MIN_DATE` | DATETIME |  | This column represents the earliest possible date that a problem could have been diagnosed on. The latest possible date is in PROB_DX_MAX_DATE. If these values are the same, then the date is exact rather than fuzzy. For a problem or condition affecting a patient, the diagnosis date is defined as the date when a qualified professional first recognized the presence of that condition with sufficient certainty, regardless of whether it was fully characterized at that time. For diseases such as cancer, this may be the earliest date of a clinical diagnosis from before it was histologically confirmed, not the date of confirmation if that occurred later. |
| 39 | `PROB_DX_MAX_DATE` | DATETIME |  | This column represents the last possible date that a problem could have been diagnosed on. The earliest possible date is in PROB_DX_MIN_DATE. If these values are the same, then the date is exact rather than fuzzy. For a problem or condition affecting a patient, the diagnosis date is defined as the date when a qualified professional first recognized the presence of that condition with sufficient certainty, regardless of whether it was fully characterized at that time. For diseases such as cancer, this may be the earliest date of a clinical diagnosis from before it was histologically confirmed, not the date of confirmation if that occurred later. |
| 40 | `PROBLEM_BULK_STAT_C_NAME` | VARCHAR |  | The status of this data element within DINE. |
| 41 | `PROB_BULK_INCL_DATE` | DATETIME |  | The date to compare to the change tracking window when loading flat files in bulk via DINE. If the date is within the window, but the data element is missing from the load, then the data element is invalidated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROB_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

