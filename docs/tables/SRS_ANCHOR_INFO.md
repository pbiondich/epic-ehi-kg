# SRS_ANCHOR_INFO

> This table stores information on anchor event option(s) a questionnaire series is related to.

**Primary key:** `SERIES_ANS_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SERIES_ANS_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the series answer record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SERIES_ANCHOR_CAT_C_NAME` | VARCHAR | org | This item stores the category item of the anchor event criteria that was matched. |
| 4 | `SERIES_ANCH_RULE_ID` | VARCHAR |  | This item stores the rule that was satisfied to classify the patient into this anchor event categorization (SERIES_ANCHOR_CAT_C). |
| 5 | `SERIES_ANCH_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 6 | `SERIES_ANCH_LPP_ID` | NUMERIC |  | This item stores the extension that was satisfied to classify the patient into this anchor event categorization (SERIES_ANCHOR_CAT_C). |
| 7 | `SERIES_ANCH_LPP_ID_LPP_NAME` | VARCHAR |  | The name of the extension. |
| 8 | `SERIES_ANCH_FILE_DT` | DATETIME |  | To store the date when the patient is categorized into an anchor event. |
| 9 | `SERIES_ANCH_ENC_CSN_ID` | NUMERIC | FK→ | This item stores a single unique contact serial number (CSN) from the day on which an anchor event rule was satisfied for a patient's questionnaire series. An anchor event rule being satisfied will convert a patient's questionnaire series (questionnaires being asked to the patient on a specified period) to a post-anchor mode, meaning different questionnaires might now be asked to the patient than were asked before the anchor event. An anchor event might be a medication being given or a procedure being performed, for example. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SERIES_ANCH_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `SERIES_ANS_ID` | [SRS_ASGN_INFO](SRS_ASGN_INFO.md) | sole_pk | high |

