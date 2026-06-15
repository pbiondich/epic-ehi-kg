# CLM_VALUES_6

> All values associated with a claim are stored in the Claim External Value record. The CLM_VALUES_6 table holds claim-level values set by the system during claims processing or by user edits.

**Overflow of:** [CLM_VALUES](CLM_VALUES.md)  
**Primary key:** `RECORD_ID`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the claim value record. |
| 2 | `RESUBMISSION_COMMENT` | VARCHAR |  | This item stores the resubmission comments for the claim. |
| 3 | `SUBSCR_EMPLOYER_PHONE` | VARCHAR |  | This item holds the subscriber's employer's phone number. |
| 4 | `PAT_SEX_ASSIGNED_AT_BIRTH` | VARCHAR |  | Patient Sex Assigned at Birth |
| 5 | `ENC_START_DATE` | DATETIME |  | This item stores the encounter start date for the claim. |
| 6 | `ENC_START_TIME_TM` | DATETIME (Local) |  | This item stores the encounter start time for the claim. |
| 7 | `ENC_END_DATE` | DATETIME |  | This item stores the encounter end date for the claim. |
| 8 | `ENC_END_TIME_TM` | DATETIME (Local) |  | This item stores the encounter end time for the claim. |
| 9 | `ENC_END_TYPE` | VARCHAR |  | This item stores the encounter end type for the claim. |
| 10 | `SVC_PROV_NAME` | VARCHAR |  | Freetext name assigned to a pharmacy |
| 11 | `CONTRACT_NUMBER` | VARCHAR |  | Account number assigned during installation for segments of business. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

