# HSP_CLAIM_PAT_RESP

> This table contains information about how the patient responsibility for the claim was calculated.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the claim print record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CLAIM_PX_LINE_NUM` | INTEGER |  | Stores the line number in related group 710 that this detail line corresponds to. If blank, then the patient responsibility detail on this line is for DRG reimbursement. |
| 4 | `SERVICE_TYPE_ID` | VARCHAR | FK→ | Stores the service type associated with the benefits on this line. If coverage level benefits are used, then the service type will be blank. |
| 5 | `SERVICE_TYPE_ID_SERVICE_TYPE_NAME` | VARCHAR |  | The name of this benefit service type. |
| 6 | `SERVICE_TYPE_SOURCE_DESC` | VARCHAR |  | Stores a description of how the service type was calculated for the line. |
| 7 | `DEDUCTIBLE_AMOUNT` | NUMERIC |  | Stores the amount of deductible that was applied to this line. |
| 8 | `COPAY_AMOUNT` | NUMERIC |  | Stores the amount of copay that was applied to this line. |
| 9 | `COINSURANCE_AMOUNT` | NUMERIC |  | Stores the amount of coinsurance that was applied to this line. |
| 10 | `NON_COVERED_AMOUNT` | NUMERIC |  | Stores the amount that was not covered by insurance on this line. |
| 11 | `NON_COVERED_RSN_C_NAME` | VARCHAR |  | Stores the reason that the not covered amount is not covered by insurance. |
| 12 | `ANNUAL_MOOP_CONTRIB_AMOUNT` | NUMERIC |  | Stores the amount that this line contributed to the maximum out of pocked accumulation. |
| 13 | `VISIT_MOOP_CONTRIB_AMOUNT` | NUMERIC |  | Stores the amount that this line contributed to the maximum visit out of pocked accumulation. |
| 14 | `OUT_OF_POCKET_LMT_RSN_C_NAME` | VARCHAR |  | Stores the reason that the out-of-pocket maximum limited the patient responsibility for the current line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SERVICE_TYPE_ID` | [BENEFIT_SVC_TYPE](BENEFIT_SVC_TYPE.md) | sole_pk | high |

