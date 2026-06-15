# CLM_ADJUD_INFO

> This table contains claim adjudication information.

**Primary key:** `CLAIM_PRINT_ID`  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The unique identifier for the claim print record. |
| 2 | `COMPONENT_ID` | VARCHAR | shared | The unique ID of the component or component group used in adjudicating this claim line. |
| 3 | `COMPONENT_ID_COMPONENT_INDEX_NAME` | VARCHAR |  | The name of the component index record |
| 4 | `CONTRACT_ID` | NUMERIC | shared | The unique ID of the contract used in adjudicating this claim line. |
| 5 | `CONTRACT_ID_CONTRACT_NAME` | VARCHAR |  | The name of the Vendor-Network contract. |
| 6 | `CONTRACT_CONTACT_DATE_REAL` | FLOAT |  | A numerical representation of the contact date for the contract used in adjudicating this claim line. Used to help link to the VEN_NET_CONT_SVC table. |
| 7 | `CONTRACT_LN` | INTEGER |  | The contract line number used in adjudicating this claim line. |
| 8 | `PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 9 | `MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 10 | `DRG_ID` | VARCHAR | FK→ | The unique ID of the DRG that is associated with this claim line. |
| 11 | `DRG_ID_DRG_NAME` | VARCHAR |  | The name of the Diagnoses Related Group name. |
| 12 | `COMPONENT_GROUP_ID_COMP_GRP_NAME` | VARCHAR |  | The name for the whole claim component group. |
| 13 | `PROC_COMMENT` | VARCHAR |  | The free text comment about the procedure that is associated with this claim line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `DRG_ID` | [CLARITY_DRG](CLARITY_DRG.md) | sole_pk | high |

