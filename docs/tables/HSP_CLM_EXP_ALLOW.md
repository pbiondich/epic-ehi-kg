# HSP_CLM_EXP_ALLOW

> This table contains information at a claim line level for expected allowances.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 33

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | This column stores the unique identifier for the claim print record. |
| 2 | `LINE` | INTEGER | PK | The claim line number for the information associated with this claim. Multiple claim lines can be associated with this claim. |
| 3 | `PX_BILLED_AMT` | NUMERIC |  | The billed amount for this claim line. |
| 4 | `CONTRACT_PRICE` | NUMERIC |  | The contract price for this claim line. If the expected reimbursement is calculated with an Epic contract, this is the reimbursement amount calculated for the claim line before any reimbursement caps are applied. If the expected reimbursement is calculated from an external source that supports line-level reimbursement, this is the claim line's payment amount. |
| 5 | `EXPECTED_PRICE` | NUMERIC |  | The expected reimbursement amount for this claim line. If the expected reimbursement is calculated with an Epic contract, this is the reimbursement amount calculated for the claim line after any reimbursement caps are applied. If the expected reimbursement is calculated from an external source that supports line-level reimbursement, this is the claim line's payment amount. |
| 6 | `PYMT_METHOD_C_NAME` | VARCHAR |  | The category number for the payment method that is associated with this claim line. |
| 7 | `PRIMARY_PMT_RATE` | VARCHAR |  | The primary payment rate describing how this claim line was primarily reimbursed by. The structure of this item is a delimited string based on what the payment mechanism in I CLP 740 is set to. Details of this structure can be found in Chronicles in the help text of item CLP 741. |
| 8 | `PRIMARY_CVD_QTY` | INTEGER |  | The primary quantity for this claim line. |
| 9 | `ADDL_PYMT_MTHDS` | VARCHAR |  | Any additional payment methods for this claim line. |
| 10 | `ADDL_PYMT_RATES` | VARCHAR |  | Any additional payment rates for this claim line. |
| 11 | `ADDL_CVD_QTY` | VARCHAR |  | Any additional quantities for this claim line. |
| 12 | `LINE_PENALTY_PRCNT` | VARCHAR |  | The penalty percent for this claim line. |
| 13 | `LATE_SUBMIT_DAYS` | INTEGER |  | This column stores how late this claim was submitted, in days. |
| 14 | `LATE_SUBMIT_PERCENT` | VARCHAR |  | The late submit penalty percent for this claim line. |
| 15 | `U_AND_C_AMOUNT` | NUMERIC |  | This column stores the Usual and Customary amount for this claim line. |
| 16 | `CLM_PX_OUTLIER_INFO` | VARCHAR |  | The outlier payment information for this claim line. |
| 17 | `PX_INS_PORTION` | NUMERIC |  | The portion of the claim line that is the insurance's responsibility. |
| 18 | `PX_PATIENT_PORTION` | NUMERIC |  | The portion of the claim line that is the patient's responsibility. |
| 19 | `PX_PYMT_MTHD_DESC` | VARCHAR |  | Free text method description for this claim line. |
| 20 | `PX_PYMT_TERM_DESC` | VARCHAR |  | Free text term description for this claim line. |
| 21 | `COMPONENT_ID` | VARCHAR | shared | This column stores the unique identifier for the component or component group used in adjudicating this claim line. |
| 22 | `COMPONENT_ID_COMPONENT_INDEX_NAME` | VARCHAR |  | The name of the component index record |
| 23 | `CONTRACT_ID` | NUMERIC | shared | This column stores the unique identifier for the contract used in adjudicating this claim line. |
| 24 | `CONTRACT_ID_CONTRACT_NAME` | VARCHAR |  | The name of the Vendor-Network contract. |
| 25 | `CONTRACT_DATE_REAL` | FLOAT |  | A numerical representation of the contact date for the contract used in adjudicating this claim line. Used to help link to the VEN_NET_CONT_SVC table. |
| 26 | `CONTRACT_LN` | INTEGER |  | The contract line number used in adjudicating this claim line. |
| 27 | `PX_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 28 | `MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 29 | `DRG_ID` | VARCHAR | FK→ | This column stores the unique identifier for the diagnosis-related group (DRG) that is associated with this claim line. |
| 30 | `DRG_ID_DRG_NAME` | VARCHAR |  | The name of the Diagnoses Related Group name. |
| 31 | `COMPONENT_GROUP_ID_COMP_GRP_NAME` | VARCHAR |  | The name for the whole claim component group. |
| 32 | `PX_COMMENT` | VARCHAR |  | The free text comment about the procedure that is associated with this claim line. |
| 33 | `PX_TAX_AMT` | NUMERIC |  | The tax amount for a procedure based claim line. Used when tax amounts are calculated using expected reimbursement values. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `DRG_ID` | [CLARITY_DRG](CLARITY_DRG.md) | sole_pk | high |

