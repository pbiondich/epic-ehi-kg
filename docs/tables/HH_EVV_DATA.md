# HH_EVV_DATA

> Will contain Electronic Visit Verification data and documentation for each visit.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 13  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `EVV_METHOD_C_NAME` | VARCHAR |  | The EVV trigger, such as the start of end of the visit, for the corresponding line in the related item. |
| 7 | `EVV_FAIL_TYPE_C_NAME` | VARCHAR |  | Describes how EVV failed on the client. |
| 8 | `EVV_RSN_CODE_C_NAME` | VARCHAR | org | The reason code to justify the change made to override the EVV failure. |
| 9 | `EVV_RSN_CODE_TYPE_C_NAME` | VARCHAR |  | The type of reason code, and whether the code was entered on mobile or through the Remote Client. |
| 10 | `EVV_RSN_CODE_CMT` | VARCHAR |  | Comments accompanying the reason code. |
| 11 | `EVV_RES_CODE_C_NAME` | VARCHAR | org | The resolution code corresponding to the actions taken to override the EVV failure. |
| 12 | `EVV_EXC_CODE_C_NAME` | VARCHAR | org | The exception code to be acknowledged corresponding to the EVV failure. |
| 13 | `EVV_FAIL_SOURCE_C_NAME` | VARCHAR |  | Indicates the source of the EVV failure for the corresponding line in the related group. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

