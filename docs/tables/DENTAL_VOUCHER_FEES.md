# DENTAL_VOUCHER_FEES

> Dental voucher fees documented on procedures using the Dental Voucher Calculator navigator section. This is only available for Australian organizations.

**Primary key:** `FINDING_ID`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the finding record. |
| 2 | `DENTAL_VCH_DEFAULT_FEE` | NUMERIC |  | The default voucher fee for a procedure at the time the fee was calculated. This item is primarily used for determining if the voucher adjustment and reason for adjustment should be cleared when re-calculating a voucher. |
| 3 | `DENTAL_VCH_ADJ_FEE` | NUMERIC |  | The adjusted fee for the procedure. If a user hasn't adjusted the fee, then this will be the default fee for the procedure. |
| 4 | `DENTAL_VCH_ADJ_REASON` | VARCHAR |  | Reason for adjusting the default voucher fee. |
| 5 | `DENTAL_VCH_MOD_UTC_DTTM` | DATETIME (UTC) |  | Instant the dental voucher fee was last calculated for the procedure. |
| 6 | `DENTAL_VCH_ADJ_USER_ID` | VARCHAR |  | The user that adjusted the cost for the voucher. |
| 7 | `DENTAL_VCH_ADJ_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The CSN this procedure's voucher fee was last calculated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

