# IB_MESSAGES_5

> The IB_MESSAGES_5 table contains basic information about in Basket messages.

**Overflow of:** [IB_MESSAGES](IB_MESSAGES.md)  
**Primary key:** `MSG_ID`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MSG_ID` | VARCHAR | PK | The unique identifier (.1 item) for the in basket message record. |
| 2 | `RESULT_TREND_C_NAME` | VARCHAR |  | Summarized result trend for the message. |
| 3 | `RSH_RECRUIT_MSG_SOURCE_C_NAME` | VARCHAR |  | The message source category ID for the message. This may be set for messages with a message type (I EOW 30) of Research Recruitment. |
| 4 | `APPEAL_GRV_ID` | NUMERIC | FK→ | The Appeal or Grievance record that triggered this In Basket message |
| 5 | `SUBJECT_UTF` | VARCHAR |  | Short description of the message contents in UTF. |
| 6 | `COVERAGE_ID` | NUMERIC | FK→ | Stores coverage record that is related to the inbasket message |
| 7 | `ORIGINAL_EXPIRING_ORDER_ID` | NUMERIC |  | Order ID of the original order that generated the expiring order message. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `APPEAL_GRV_ID` | [APPEAL_GRV](APPEAL_GRV.md) | sole_pk | high |
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |

## Joined in

Inbound joins are tracked on the logical base [IB_MESSAGES](IB_MESSAGES.md).

