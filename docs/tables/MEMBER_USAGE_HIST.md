# MEMBER_USAGE_HIST

> This table contains the history of different activities associated with the member.

**Primary key:** `BENEFIT_USAGE_ID`, `CONTACT_DATE_REAL`  
**Columns:** 10  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BENEFIT_USAGE_ID` | VARCHAR | PK FK→ | The unique ID of the benefit usage record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | The date when benefit usage is recorded. |
| 3 | `BENEFIT_USG_TYP_C` | VARCHAR |  | The type of usage record. |
| 4 | `BENEFIT_DATE` | DATETIME |  | The date when the benefit is used. |
| 5 | `BENEFIT_ID_MEMBERSHIP_NAME` | VARCHAR |  | The name for membership/benefit record. |
| 6 | `START_DATE` | DATETIME |  | The start date for the benefit usage. |
| 7 | `EXP_DATE` | DATETIME |  | The end date for the benefit usage. |
| 8 | `EVENT_ATTENDEES` | INTEGER |  | The number of benefits used. |
| 9 | `DEACT_RSN_C` | VARCHAR | org | The reason for deactivating the membership/benefit. |
| 10 | `CARD_REQ_RSN_C` | VARCHAR | org | The reason for requesting new card. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BENEFIT_USAGE_ID` | [MEMBER_INFO](MEMBER_INFO.md) | sole_pk | high |

