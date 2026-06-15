# CRITERIA_REVIEW_GEN_TRACK

> This table contains information for reviews created with the Generated Drafts for Utilization Review feature in the Manual Review activity.

**Primary key:** `CRITERIA_REVIEW_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CRITERIA_REVIEW_ID` | NUMERIC | PK FK→ | The unique identifier for the criteria review record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `GEN_START_UTC_DTTM` | DATETIME (UTC) |  | The date and time that the user started this generation. |
| 4 | `GEN_RESP_UTC_DTTM` | DATETIME (UTC) |  | The date and time the draft or error was returned to the user for this generated draft. |
| 5 | `GEN_DECISN_UTC_DTTM` | DATETIME (UTC) |  | The date and time a user accepts or discards the generated review draft. |
| 6 | `GEN_DECISN_C_NAME` | VARCHAR |  | The decision category ID for the generated review draft. |
| 7 | `GEN_STYLE_C_NAME` | VARCHAR |  | The style category ID for the generated review draft. |
| 8 | `LOOKBACK_START_INST_UTC_DTTM` | DATETIME (UTC) |  | The date and time of the start of the lookback time period for this generated draft. |
| 9 | `LOOKBACK_END_INST_UTC_DTTM` | DATETIME (UTC) |  | The date and time of the end of the lookback time period for this generated draft. |
| 10 | `GEN_FEEDBACK_C_NAME` | VARCHAR |  | The feedback category ID for the generated review draft. |
| 11 | `GEN_ERR_YN` | VARCHAR |  | Indicates whether an error occured during the review draft generation. 'Y' indicates that an error was logged. 'N' or NULL indicates that no error was logged. |
| 12 | `GEN_PROMPT_VERS` | VARCHAR |  | The version of the prompt used to generate the draft. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CRITERIA_REVIEW_ID` | [CRITERIA_REVIEW](CRITERIA_REVIEW.md) | sole_pk | high |

