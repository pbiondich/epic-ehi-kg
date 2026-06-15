# DENT_TREATMENT

> This contains dental treatment plan information which is not expected to change over time.

**Primary key:** `TREATMENT_ID`  
**Columns:** 16  
**Org-specific columns:** 1  
**Joined by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_ID` | NUMERIC | PK | The unique identifier for the treatment plan record |
| 2 | `DENTAL_TYPE_C_NAME` | VARCHAR |  | Type of dental treatment |
| 3 | `COMPLETED_DTTM_DTTM` | DATETIME (Local) |  | Date and time the dental treatment was completed |
| 4 | `TR_STATUS_NOADD_C_NAME` | VARCHAR |  | This keeps track of the latest status of a treatment. |
| 5 | `DENTAL_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 6 | `TR_SUG_START_DATE` | DATETIME |  | The suggested start date for a treatment. |
| 7 | `TR_SEQUENCE_NUM` | INTEGER |  | Keep track of relative orders for a treatment within a treatment plan |
| 8 | `DENTAL_TREAT_SER_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 9 | `DENT_PARENT_TRMT_ID` | NUMERIC |  | This points to the parent treatment of which this treatment is part. |
| 10 | `DENT_OPTION_STAT_C_NAME` | VARCHAR |  | The status of an option for treatment within a dental treatment. |
| 11 | `DENTAL_ESTIMATE_ID` | NUMERIC |  | The linked patient estimate record detailing cost information for the procedures in this treatment. |
| 12 | `TR_APRV_DTTM` | DATETIME (Attached) |  | The date and time when the dental treatment was last approved. |
| 13 | `TR_APRV_USER_ID` | VARCHAR |  | The user who last approved the treatment. |
| 14 | `TR_APRV_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 15 | `TR_APRV_STATUS_C_NAME` | VARCHAR |  | The approval status category ID for the treatment. |
| 16 | `TR_RESCIND_RSN_C_NAME` | VARCHAR | org | The rescind reason category ID for the treatment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (5)

| From | Column | Confidence |
|------|--------|------------|
| [DENTAL_TREATMENT_CMT](DENTAL_TREATMENT_CMT.md) | `TREATMENT_ID` | high |
| [DENTAL_TREAT_FINDINGS](DENTAL_TREAT_FINDINGS.md) | `TREATMENT_ID` | high |
| [DENT_TREAT_CMT_HIST_RM](DENT_TREAT_CMT_HIST_RM.md) | `TREATMENT_ID` | high |
| [DENT_TREAT_FIND_HIST_RM](DENT_TREAT_FIND_HIST_RM.md) | `TREATMENT_ID` | high |
| [DENT_TREAT_HX](DENT_TREAT_HX.md) | `TREATMENT_ID` | high |

