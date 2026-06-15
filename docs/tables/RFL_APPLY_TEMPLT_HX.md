# RFL_APPLY_TEMPLT_HX

> Clarity table for apply template history on referral.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `APY_RTP_HX_USER_ID` | VARCHAR |  | Apply Template History. Stores the user who applied the template to the referral or who caused it to be applied. |
| 4 | `APY_RTP_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `APY_RTP_HX_UTC_DTTM` | DATETIME (UTC) |  | Apply Template History. Stores the instant when the template was applied to the referral. |
| 6 | `APY_RTPHX_RFL_APPLY_RTP_MTHD_C_NAME` | VARCHAR |  | Apply Template History. Stores the template application method. |
| 7 | `APY_RTP_HX_FAIL_TEMPLATE_ID` | NUMERIC |  | Apply Template History: Stores the template that failed to apply to the referral. |
| 8 | `APY_RTP_HX_FAIL_TEMPLATE_ID_TEMPLATE_NAME` | VARCHAR |  | Referral template record name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

