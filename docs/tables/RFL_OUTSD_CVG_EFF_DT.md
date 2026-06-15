# RFL_OUTSD_CVG_EFF_DT

> This table extracts the effective date for the coverage stored in RFL_OUTSD_CVG. The corresponding payer, plan, insurance ID, termination date, authorization and precert number and comments can be found in RFL_OUTSD_CVG_PAYER, RFL_OUTSD_CVG_PLAN, RFL_OUTSD_CVG_INS, RFL_OUTSD_CVG_TERM_DT, RFL_OUTSD_CVG_AUTH_NUM, RFL_OUTSD_CVG_PRECERT_NUM and RFL_OUTSD_CVG_CMT tables for matching values of REFERRAL_ID, GROUP_LINE, and VALUE_LINE.

**Primary key:** `REFERRAL_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the referral record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of one of the multiple updates received from an outside organization for a referral. Together with REFERRAL_ID, this forms the foreign key to the RFL_OUTSD_CVG table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple outside coverages received in a referral update from an outside organization for a referral in the RFL_OUTSD_CVG table. |
| 4 | `OUT_CVG_EFF_DATE` | DATETIME |  | Effective date for one of the multiple outside coverages received in a referral update from an outside organization for a referral in the RFL_OUTSD_CVG table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

