# UNOS_IMMUNO_INFO

> This table contains immunosuppression information reported to the United Network for Organ Sharing (UNOS) for each registry record or form. Information from this table can be linked to the PATIENT table by joining with the UNOS_INFO table.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | Registry data record ID. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IMMUNO_IDENTIFIER` | INTEGER |  | The immunosuppression drug ID. |
| 4 | `UNOS_DRUG_CODE_C_NAME` | VARCHAR |  | The immunosuppression drug code. |
| 5 | `IMM_PREV_MAINT_YN` | VARCHAR |  | Indicates whether the drug was used previously for maintenance. |
| 6 | `IMM_CUR_MAINT_YN` | VARCHAR |  | Indicates whether the drug is currently being used in the follow-up period for maintenance. |
| 7 | `IMM_ANTI_REJECT_YN` | VARCHAR |  | Indicates whether the drug was used as an anti-rejection agent. |
| 8 | `IMM_DRUG_CODE_OTHER` | VARCHAR |  | The drug code's description, if it is not one of the available options in column UNOS_DRUG_CODE_C. |
| 9 | `UNOS_IMM_INDU_YN` | VARCHAR |  | Indicates whether this drug was used for induction. |
| 10 | `UNOS_IMM_INDU_DAYS` | NUMERIC |  | The total number of days this drug was administered for induction if this drug was used for induction. |
| 11 | `UNOS_IMM_INDU_ST_C_NAME` | VARCHAR |  | If this drug was used for induction, and the number of days used for induction is not available, this indicates why. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

