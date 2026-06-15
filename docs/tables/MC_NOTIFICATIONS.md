# MC_NOTIFICATIONS

> This table contains information relating to Tapestry notifications sent to members.

**Primary key:** `OUTREACH_ID`, `CONTACT_DATE_REAL`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OUTREACH_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the outreach record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `PB_ACCT_ID` | VARCHAR | FK→ | The premium billing account record ID associated with the member for this communication. |
| 4 | `PAYMENT_ID` | VARCHAR |  | The premium payment record ID associated with the communication to the member. |
| 5 | `PB_INVC_ID` | VARCHAR | FK→ | The premium invoice record ID related to the communication being sent to the member. |
| 6 | `COVERAGE_ID` | NUMERIC | FK→ | The coverage record ID related to the communication being sent to the member. |
| 7 | `ESTIMATE_ID` | NUMERIC | shared | The estimate record ID related to the communication being sent to the member. |
| 8 | `CLAIM_ID` | NUMERIC | FK→ | The claim record ID related to the communication being sent to the member. |
| 9 | `EOB_DOCUMENT_ID` | VARCHAR |  | The periodic Explanation of Benefits document record ID associated with the communication being sent. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `OUTREACH_ID` | [MC_NOTIF_INFO](MC_NOTIF_INFO.md) | sole_pk | high |
| `PB_ACCT_ID` | [PB_ACCT](PB_ACCT.md) | name_stem | high |
| `PB_INVC_ID` | [PB_INVOICE](PB_INVOICE.md) | sole_pk | high |

