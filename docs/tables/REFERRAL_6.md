# REFERRAL_6

> The REFERRAL_6 table is a continuation of the REFERRAL_5 table. The REFERRAL_* tables are the primary tables for referral information stored in the system.

**Overflow of:** [REFERRAL](REFERRAL.md)  
**Primary key:** `REFERRAL_ID`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK | The unique identifier (.1 item) for the referral record. |
| 2 | `RFL_TRIAGE_STATUS_C_NAME` | VARCHAR |  | Indicates the triage status of the referral. |
| 3 | `ECONSULT_TYPE_C_NAME` | VARCHAR |  | The type of e-Consult this referral represents. |
| 4 | `ECONSULT_CONVERT_YN` | VARCHAR |  | Item representing if this e-Consult can be converted into a regular referral. |
| 5 | `CONV_ECON_REFERRAL_ID` | NUMERIC |  | The e-Consult that this referral was converted from. |
| 6 | `ADVICE_GUIDANCE_UBRN` | VARCHAR |  | The eReferrals unique booking reference number from NHS eReferrals specific to advice and guidance e-Consult workflows. |
| 7 | `UM_UCN_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number of the health plan contact on the EPT record that is linked with UM UCN Notes |
| 8 | `EXPECTED_ADMSN_DATE` | DATETIME |  | The expected admit date documented on the referral bed days navigator section. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `UM_UCN_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

## Joined in

Inbound joins are tracked on the logical base [REFERRAL](REFERRAL.md).

