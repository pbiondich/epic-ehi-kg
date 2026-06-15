# REFERRAL_ATTACHMENTS

> Table for attachments associated with referrals.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The referral ID for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DOC_ID` | VARCHAR |  | Stores a list of attachments associated with the referral. |
| 4 | `DOC_ATTACH_USER_ID` | VARCHAR |  | Indicates the user who attached the document to the referral. |
| 5 | `DOC_ATTACH_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `DOC_ATTACH_DTTM` | DATETIME (UTC) |  | Indicates the instant, in UTC, when the document was attached to the referral. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

