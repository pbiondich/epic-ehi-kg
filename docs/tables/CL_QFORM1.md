# CL_QFORM1

> The CL_QFORM1 table is the second master table for questionnaire forms. It is used along with CL_QFORM.

**Primary key:** `FORM_ID`  
**Columns:** 3  
**Joined by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FORM_ID` | VARCHAR | PK | The unique identifier for the form record. |
| 2 | `FORM_ID_FORM_NAME` | VARCHAR |  | The name of the form associated with the questionnaire. |
| 3 | `FORM_NAME` | VARCHAR |  | The name of the form associated with the questionnaire. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (5)

| From | Column | Confidence |
|------|--------|------------|
| [BEREAVE_FOL_INFO](BEREAVE_FOL_INFO.md) | `FORM_ID` | high |
| [ENROLL_QUESR](ENROLL_QUESR.md) | `FORM_ID` | high |
| [OR_LOG_IMG_FORMS](OR_LOG_IMG_FORMS.md) | `FORM_ID` | high |
| [SRS_RESP_OVER_TM](SRS_RESP_OVER_TM.md) | `FORM_ID` | high |
| [SYN_FORMS](SYN_FORMS.md) | `FORM_ID` | high |

