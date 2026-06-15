# BILL_SCHED_PMT_CONSENT_HX

> The history of the consent-to-be-charged-later information for the Visit Auto Pay arrangement represented by a Billing Scheduled Payment record.

**Primary key:** `SCHED_PMT_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SCHED_PMT_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the scheduled payment record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CONSENT_HX_UTC_DTTM` | DATETIME (UTC) |  | The instant at which consent was given for the Visit Auto Pay arrangement represented by this scheduled payment. |
| 4 | `CONSENT_HX_BSP_CONSENT_TYPE_C_NAME` | VARCHAR |  | The method by which a guarantor consented to be charged automatically for the Visit Auto Pay agreement represented by this scheduled payment. |
| 5 | `CONSENT_HX_USER_ID` | VARCHAR |  | The user that collected or updated the consent for Visit Auto Pay. |
| 6 | `CONSENT_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `CONSENT_HX_DOCUMENT_ID` | VARCHAR |  | The document record representing the guarantor's consent for the Visit Auto Pay arrangement represented by this scheduled payment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SCHED_PMT_ID` | [BILL_SCHED_PMT](BILL_SCHED_PMT.md) | sole_pk | high |

