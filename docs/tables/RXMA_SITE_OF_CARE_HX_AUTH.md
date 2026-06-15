# RXMA_SITE_OF_CARE_HX_AUTH

> This table extracts the related multiple response MED ACCESS - SITE AUDIT TRAIL - LINKED AUTH REFERRAL (I HSB 48843) item.

**Primary key:** `SUMMARY_BLOCK_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the episode record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `HX_AUTH_REFERRAL_ID` | NUMERIC |  | Stores the historical site of care linked authorization referral (I HSB 48833). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

