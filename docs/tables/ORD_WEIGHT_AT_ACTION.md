# ORD_WEIGHT_AT_ACTION

> Extracts values documenting the patient's vitals and the order's AUC dose calculation at the time that certain actions were taken on the order.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_WEIGHT` | NUMERIC |  | Stores the patient weight when an action (verify or release) was taken on the linked order. |
| 4 | `PAT_BSA` | NUMERIC |  | Stores the patient's body surface area (BSA) when an action (verify or release) was taken on the linked order. |
| 5 | `AUC_DOSE` | NUMERIC |  | Stores the area under the curve (AUC) dose when an action (verify or release) was taken on the linked order. AUC dosing is used for a specific chemotherapy drug: carboplatin. The curve refers to a concentration-over-time graph in which the concentration of the drug in a patient's blood is measured against the time when the sample was taken. |
| 6 | `ORDER_ACT_C_NAME` | VARCHAR |  | Stores what order action (Verify, Release) the patient weight, patient BSA, or order dose was saved at. |
| 7 | `AUC_DOSE_DESCRIPTION_AT_ACTION` | VARCHAR |  | For an order with an AUC dosing programming point configured, this item stores the dose calculation description when a particular action was taken. |
| 8 | `AUC_GFR_DESCRIPTION_AT_ACTION` | VARCHAR |  | For an order with an AUC dosing programming point configured, this item stores the description of the GFR calculation when a particular action was taken. |
| 9 | `AUC_PARAM_DESCRIPTION_AT_ACT` | VARCHAR |  | For an order with an AUC dosing programming point configured, this item stores the description of the parameters used in the calculation when a particular action was taken. |
| 10 | `ACTION_INSTANT_DTTM` | DATETIME (Attached) |  | This column stores the instant that the data related to the action taken on the order was recorded. |
| 11 | `AUC_DOSE_DISP_QTYUNIT_C_NAME` | VARCHAR | org | This column stores the unit associated with the AUC dose that was calculated when an action was taken on the order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

