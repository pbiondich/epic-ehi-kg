# CLARITY_UCL

> Universal Charge Lines (UCL) information. Each row represents one UCL transaction.

**Overflow family:** [CLARITY_UCL_2](CLARITY_UCL_2.md)  
**Primary key:** `UCL_ID`  
**Columns:** 7  
**Joined by:** 14 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `UCL_ID` | VARCHAR | PK | The unique ID associated with the charge record. |
| 2 | `PATIENT_ID` | VARCHAR |  | The patient the charge is associated with. |
| 3 | `START_INST` | DATETIME (Local) |  | The start date and time associated with the charge. |
| 4 | `END_INST` | DATETIME (Local) |  | The end date and time associated with the charge. |
| 5 | `INSTI_PATIENT_ID` | VARCHAR |  | Institutional Billing - linked patient |
| 6 | `PROV_BILL_AREA_C` | NUMERIC |  | The bill area for this charge. |
| 7 | `PROV_BILL_AREA_C_BILL_AREA_NAME` | VARCHAR |  | The record name of this bill area, financial subdivision, or financial division. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (14)

| From | Column | Confidence |
|------|--------|------------|
| [CLARITY_UCL_FRMCHG](CLARITY_UCL_FRMCHG.md) | `UCL_ID` | high |
| [UCL_AMBRX_COVERAGE](UCL_AMBRX_COVERAGE.md) | `UCL_ID` | high |
| [UCL_ANES_EXCLUSION](UCL_ANES_EXCLUSION.md) | `UCL_ID` | high |
| [UCL_ANES_PERIOD](UCL_ANES_PERIOD.md) | `UCL_ID` | high |
| [UCL_BUNDLED_EPISODE](UCL_BUNDLED_EPISODE.md) | `UCL_ID` | high |
| [UCL_CRC](UCL_CRC.md) | `UCL_ID` | high |
| [UCL_DOC_PROVIDER](UCL_DOC_PROVIDER.md) | `UCL_ID` | high |
| [UCL_MEA](UCL_MEA.md) | `UCL_ID` | high |
| [UCL_NDC_CODES](UCL_NDC_CODES.md) | `UCL_ID` | high |
| [UCL_PAT_VST_PROG](UCL_PAT_VST_PROG.md) | `UCL_ID` | high |
| [UCL_TOOTH](UCL_TOOTH.md) | `UCL_ID` | high |
| [UNIV_CHG_LN_DX](UNIV_CHG_LN_DX.md) | `UCL_ID` | high |
| [UNIV_CHG_LN_MOD](UNIV_CHG_LN_MOD.md) | `UCL_ID` | high |
| [UNIV_CHG_LN_MSG_HX](UNIV_CHG_LN_MSG_HX.md) | `UCL_ID` | high |

