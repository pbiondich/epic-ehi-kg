# PYR_FEEDBACK_PAT_INSIGHT

> This table contains information about individual patient insights feedback shared via Payer Platform.

**Primary key:** `FEEDBACK_ID`, `LINE`  
**Columns:** 24  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FEEDBACK_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the Payer Platform feedback record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `INSIGHT_SRC_TYPE_C_NAME` | VARCHAR |  | The insight source type Category ID for the feedback insight. |
| 4 | `REGISTRY_DATA_CSN_ID` | NUMERIC |  | The unique contact serial number of the quality measure outcome record that this feedback applies to, populated if the insight source type is Care Gaps Exchange. |
| 5 | `CALC_OUTCOME_KEY` | VARCHAR |  | The unique outcome key that identifies a specific measure outcome the feedback applies to, populated if the insight source type is Care Gaps Exchange. |
| 6 | `INSIGHT_CODE_TYPE_C_NAME` | VARCHAR |  | The insight code type category ID that the feedback applies to that is stored in column INSIGHT_CODE_VALUE. |
| 7 | `INSIGHT_CODE_VALUE` | VARCHAR |  | The code value that served as the source of the insight. This code is of the type stored in column INSIGHT_CODE_TYPE_C. |
| 8 | `HM_CARE_GAP_TYPE_C_NAME` | VARCHAR |  | The care gap type category ID for the feedback record, populated if the insight source type is Care Gaps Exchange. |
| 9 | `RISK_ADJ_C_NAME` | VARCHAR | org | The ID of the risk adjustment category associated with the feedback, populated if the insight source type is Observed Condition (Diagnosis Exchange). |
| 10 | `SHOWN_TO_USER_YN` | VARCHAR |  | Indicates whether the insight was based on data from your organization. If not, either your organization did not provide data for this insight, or your organization's data was not used by the provider organization and another source's data was used instead. 'Y' indicates that this insight data was from your organization, 'N' or NULL indicates it was not. |
| 11 | `PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 12 | `PROV_NPI` | VARCHAR |  | The NPI associated with the provider record that acted on the shared insight. |
| 13 | `PROV_TAX_IDENT` | VARCHAR |  | The tax ID associated with the provider record that acted on the shared insight. |
| 14 | `PROV_YN` | VARCHAR |  | Indicates whether the user who acted on the shared insight is a provider or not. 'Y' indicates the user is a provider. 'N' or NULL indicates the user is not a provider. |
| 15 | `PCP_YN` | VARCHAR |  | Indicates whether the user who acted on the shared insight is the patient's PCP or not. 'Y' indicates the user is the patient's PCP. 'N' or NULL indicates the user is not the patient's PCP. |
| 16 | `ACTION_TAKEN_C_NAME` | VARCHAR |  | The action taken category ID of the action the user took on the insight. |
| 17 | `ACTION_RESULT_C_NAME` | VARCHAR |  | The action result category ID of the subsequent result of the action that was taken on the insight. |
| 18 | `RESULT_CODE_TYPE_C_NAME` | VARCHAR |  | The result code type category ID of the record added to the patient's chart that is stored in column RESULT_CODE_VALUE. |
| 19 | `RESULT_CODE_VALUE` | VARCHAR |  | The code value of the record added to patient's chart as the result of the insight action. This code is of the type stored in column RESULT_CODE_TYPE_C. |
| 20 | `ACTION_COMMENT` | VARCHAR |  | The free-text comment the user entered as they were taking action on the insight, if entered. |
| 21 | `ACTION_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | The date and time the user took action on the insight, stored in UTC. |
| 22 | `SRC_CARE_GAP_PROGRAM_ID` | NUMERIC |  | The unique ID of the program record the feedback applies to, populated if the insight source type is Care Gaps Exchange. |
| 23 | `SRC_CARE_GAP_PROGRAM_ID_RECORD_NAME` | VARCHAR |  | The name of the program record. |
| 24 | `NOT_SRC_REASON_C_NAME` | VARCHAR |  | The reason why 'Was Insight Source?' (I PPF 220) was set to No. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FEEDBACK_ID` | [PYR_FEEDBACK](PYR_FEEDBACK.md) | sole_pk | high |

