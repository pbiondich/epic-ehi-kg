# HH_EPSD_DME

> This table contains the user-entered durable medical equipment (DME) information for Home Health episodes. It contains a list of the DMEs that are applicable to a specific patient for a specific episode. This information is entered on the Home Health Remote Client and in the Referral Info 2 form in Intake.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | Unique identifier for the episode. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DME_C_NAME` | VARCHAR | org | This column stores the DME category list selection for the episode. This column links to category table ZC_DME. |
| 4 | `DME_START_DT` | DATETIME |  | This column stores the DME start date for the episode. |
| 5 | `DME_END_DT` | DATETIME |  | This column stores the DME end date for the episode. |
| 6 | `DME_COMMENTS` | VARCHAR |  | This column stores comments entered by a user for the DME for the episode. |
| 7 | `DME_DELETED_YN` | VARCHAR |  | This column stores deleted DME information. |
| 8 | `DME_ORDER_ID` | VARCHAR |  | This item stores the most recent LVO ID linked to the DME in the related line. |
| 9 | `DME_POC_CSN` | NUMERIC |  | This item stores the CSN of the current Plan of Care the DME is on. |
| 10 | `HSPC_COVERED_C_NAME` | VARCHAR |  | The durable medical equipment - hospice coverage category ID for the episode. |
| 11 | `HSPC_NONCVRD_RSN_C_NAME` | VARCHAR | org | The durable medical equipment - hospice not covered reason category ID for the episode. |
| 12 | `HSPC_NONCVRD_RSN_C_CMT` | VARCHAR |  | The durable medical equipment - hospice not covered reason category comment for the episode. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

