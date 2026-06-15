# VERIF_ENC_CVGS

> The VERIF_ENC_CVGS table contains information about your verification records. These records track the state of the effective coverages for an encounter or a hospital account.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the verification record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ENC_CVG_ID` | NUMERIC |  | List of coverages for this encounter |
| 4 | `ENC_CVG_VERIF_ID` | NUMERIC |  | Verification records of the coverages for this encounter |
| 5 | `ENC_CVG_FILE_ORD` | NUMERIC |  | Calculated filing order for the coverages for this encounter |
| 6 | `ENC_CVG_MEMBER_ID` | VARCHAR |  | Effective member of the coverages for this encounter |
| 7 | `ENC_CVG_MEM_VRF_ID` | NUMERIC |  | Verification record for the coverage members for this encounter |
| 8 | `ENC_CVG_EFF_MEM_LN` | NUMERIC |  | Member line for the coverage members for this encounter |
| 9 | `ENC_CVG_SNAPSHOT_C_NAME` | VARCHAR | org | The verification status of the coverages for this encounter at the time the encounter was verified. |
| 10 | `ENC_MEM_SNAPSHOT_C_NAME` | VARCHAR |  | The verification status of the coverage members for this encounter at the time the encounter was verified. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

