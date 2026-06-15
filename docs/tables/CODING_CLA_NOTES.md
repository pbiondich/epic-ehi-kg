# CODING_CLA_NOTES

> This table contains information on queries sent during coding (including documentation queries) and clinical documentation improvement (CDI) reviews.

**Primary key:** `NOTE_ID`  
**Columns:** 39  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique ID of the notes record. |
| 2 | `PATIENT_ID` | VARCHAR |  | The patient associated with the coding query. |
| 3 | `CCR_EMP_ID` | VARCHAR |  | The user who created the coding query. |
| 4 | `CCR_EMP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `CCR_NOTE_DT_TIME` | DATETIME (Local) |  | The date and time the coding query created. |
| 6 | `CCR_NOTE_SUMMARY` | VARCHAR |  | The subject line (free text) of the coding query. |
| 7 | `CCR_STATUS_C_NAME` | VARCHAR |  | The status of the coding query. |
| 8 | `CCR_HOSP_ACCT_ID` | NUMERIC |  | The hospital account associated with the coding query. |
| 9 | `NOTE_TYPE_NOADD_C_NAME` | VARCHAR | org | The note type of the coding query. |
| 10 | `QUERY_WORKFLOW_C_NAME` | VARCHAR |  | The workflow type category number for the query. NULL or 0 is returned for a coding query. |
| 11 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for the patient contact associated with this coding query. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 12 | `COD_QRY_HNO_TYP_C_NAME` | VARCHAR | org | The coding query type category number for the query. |
| 13 | `CDI_QRY_HNO_TYP_C_NAME` | VARCHAR | org | The clinical documentation improvement (CDI) query type category number for the query. |
| 14 | `CODING_DOC_DFI_ID` | NUMERIC |  | The unique ID of the deficiency which is associated with a documentation query. This column is frequently used to link to the DFI_DETAILS table. |
| 15 | `CODING_DOC_CREATE_C_NAME` | VARCHAR |  | The creation method category ID for the documentation query. |
| 16 | `CCR_ASSN_TO_POOL_ID` | NUMERIC |  | The pool to whom the documentation query was sent. |
| 17 | `CCR_ASSN_TO_POOL_ID_REGISTRY_NAME` | VARCHAR |  | The name of the In Basket registry in the HIP master file. |
| 18 | `CCR_OUTCOME_C_NAME` | VARCHAR | org | The query outcome category ID for the query. This indicates the conclusion of the query (recipient agrees, disagrees, or doesn't respond). |
| 19 | `RESP_USER_ID` | VARCHAR |  | To store the provider's ID whose response to a query satisfies the query sender. |
| 20 | `RESP_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 21 | `QRY_RESP_NOTE_ID` | VARCHAR |  | Holds the note ID of the note used to respond to a coding/CDI query. |
| 22 | `QRY_RESP_SMRTTXT_ID` | VARCHAR |  | Specifies the smart text to use to populate a new note in response to a query. |
| 23 | `QRY_RESP_SMRTTXT_ID_SMARTTEXT_NAME` | VARCHAR |  | The name of the SmartText record. |
| 24 | `DOC_QRY_REP_TYPE_C_NAME` | VARCHAR |  | Indicates the reporting workflow of the query based on the presence of an attached deficiency. Use this instead of workflow value when breaking CDI and Coding queries out by whether they are a documentation query as well. |
| 25 | `CCR_UPD_INST_UTC_DTTM` | DATETIME (UTC) |  | The instant that the query was updated, in UTC time. |
| 26 | `CCR_NOTE_INST_UTC_DTTM` | DATETIME (UTC) |  | The date and time the coding query was created, in UTC time. |
| 27 | `QRY_SUGG_RESP_NOTE_CSN_ID` | NUMERIC |  | The unique contact serial number (CSN) of the suggested response note linked to the query. |
| 28 | `QRY_PEND_NOTE_CSN_ID` | NUMERIC |  | The unique contact serial number (CSN) of the note pended by the provider responding to a query. |
| 29 | `QRY_SUGG_REJECT_REASON_C_NAME` | VARCHAR |  | The reason a query suggestion was rejected and not shown to a provider. |
| 30 | `QRY_IS_AI_SUGG_YN` | VARCHAR |  | Whether this query is suggested by an AI. |
| 31 | `PB_CODING_QUERY_TYPE_C_NAME` | VARCHAR | org | This item stores the actual type of PB coding query, which the user can choose when composing a new PB coding query. |
| 32 | `BASE_CODING_RECORD_CSN_ID` | NUMERIC |  | The Coding/CDI review that captures the pre-query state of codes. |
| 33 | `IMPACT_CODING_RECORD_CSN_ID` | NUMERIC |  | The Coding/CDI review that captures the post-query state of codes. |
| 34 | `QRY_AI_SUGG_REASON` | VARCHAR |  | The reason the AI query was suggested. |
| 35 | `QRY_SUGG_FEEDBACK` | VARCHAR |  | User provided feedback for the query suggestion. |
| 36 | `QRY_AI_SUGG_SRC_C_NAME` | VARCHAR |  | The source of what created the reason for the AI query suggestion. |
| 37 | `QRY_CONDITION_C_NAME` | VARCHAR |  | The condition associated with this query. |
| 38 | `QRY_AI_SUGG_INV_YN` | VARCHAR |  | Whether or not the query suggestion was invalidated by a subsequent run of the AI model. If null, then the model didn't run. If set to No, then the model ran and determined the query suggestion is still valid. If set to Yes, then the query suggestion was invalidated. |
| 39 | `QRY_AI_SUGG_INV` | VARCHAR |  | The reason an existing AI query suggestion that has not been acted upon is no longer valid. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

