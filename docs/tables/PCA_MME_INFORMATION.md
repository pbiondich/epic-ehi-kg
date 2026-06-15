# PCA_MME_INFORMATION

> Stores PCA milligram morphine equivalence (MME) information for medication orders.

**Primary key:** `ORDER_ID`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `PCA_MME_FACTOR` | NUMERIC |  | Static item for the calculated morphine equivalent conversion factor of this PCA order. If the order is not for a PCA or it does not have a linked PCA assessment configured, it will be null. The conversion factor is calculated as the equivalent amount of mg of morphine based on a 1 unit dose of the order, using the unit for the linked PCA assessment flowsheet row for total dose. If the medication doesn't contain an opioid as defined in the I LSD 10700:10703 morphine equivalence conversion table, this value will be zero. If there is an error calculating the morphine equivalency, the value will be 999999. |
| 3 | `PCA_TOTAL_DOSE_FLO_MEAS_ID` | VARCHAR |  | Static item for the flowsheet row ID for the total dose row of the order's linked PCA assessments. If the order is not for a PCA or it does not have a linked PCA assessment configured, it will be null. |
| 4 | `PCA_TOTAL_DOSE_FLO_MEAS_ID_DISP_NAME` | VARCHAR |  | The display name given to the flowsheet group/row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

