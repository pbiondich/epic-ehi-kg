# PR_EST_FAC_PROC

> Procedure information for the facility fees in the price estimate. Facility fees are generated in Resolute Hospital Billing.

**Primary key:** `ESTIMATE_ID`, `LINE`  
**Columns:** 25  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESTIMATE_ID` | NUMERIC | PK shared | This column stores the unique identifier for the patient estimate record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HB_CONTEXT_LINE` | INTEGER |  | References the context information from related group 200 for the charge line. |
| 4 | `HB_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 5 | `HB_MODIFIERS` | VARCHAR |  | Procedure modifiers associated with service for which estimate is made. |
| 6 | `HB_QUANTITY` | INTEGER |  | Procedure quantity for estimated service. |
| 7 | `HB_CHARGE_AMOUNT` | NUMERIC |  | Charge amount for estimated service. |
| 8 | `HB_ALLOWED_AMOUNT` | NUMERIC |  | Allowed amount for estimated service. |
| 9 | `HB_SP_AMOUNT` | NUMERIC |  | Self-pay amount for the estimated service. |
| 10 | `HB_SYS_SP_AMOUNT` | NUMERIC |  | The system calculated self-pay amount for the estimated service. |
| 11 | `HB_ACTUAL_DISCOUNT_AMT` | NUMERIC |  | Discount amount for estimated service. |
| 12 | `HB_SYSTEM_DISCOUNT_AMT` | NUMERIC |  | The system-calculated discount amount for the estimated service. |
| 13 | `HB_SYS_CHG_AMT` | NUMERIC |  | The system-calculated charge amount for the estimated service. |
| 14 | `HB_SYS_ALLOWED_AMT` | NUMERIC |  | The system-calculated allowed amount for the estimated service. |
| 15 | `HB_ADDL_LINE` | INTEGER |  | This item holds a line number in the PR_EST_ADDL_INFO table, which stores additional information about the charge line. |
| 16 | `HB_SUPPLY_ID` | VARCHAR |  | This column stores the supply code used to price a hospital billing individual procedure line. |
| 17 | `HB_SUPPLY_ID_SUPPLY_NAME` | VARCHAR |  | The name of the inventory item. |
| 18 | `HB_INVENTORY_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 19 | `HB_MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 20 | `HB_MEDICATION_QTY` | NUMERIC |  | This column stores the medication quantity used to price a hospital billing individual procedure line. |
| 21 | `HB_MEDICATION_UNIT_C_NAME` | VARCHAR | org | This column stores the medication unit used to price a hospital billing individual procedure line. |
| 22 | `HB_PROCEDURE_CODE` | VARCHAR |  | The code used for an individual procedure line. |
| 23 | `HB_PROCEDURE_CODE_TYPE_C_NAME` | VARCHAR | org | The code type for a corresponding procedure code on an individual procedure line. |
| 24 | `HB_PROCEDURE_TYPE_C_NAME` | VARCHAR |  | The type of charge this procedure line represents. |
| 25 | `SELF_PAY_CONTRACT_AMT` | NUMERIC |  | Contract amount calculated to apply as part of a self-pay discount. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

