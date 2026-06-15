# RES_ADDL_COMPONENT_LRR

> This item stores additional obstetric fetal measurement data. If more than one value is sent from an ultrasound machine for a given result, we will store the additional ones in this table.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ADDL_READ_COMPONENT_ID` | NUMERIC |  | If additional measurement values are provided for a component, this item will store the ID of the component (LRR). |
| 4 | `ADDL_READ_COMPONENT_ID_NAME` | VARCHAR |  | The name of the component. |
| 5 | `ADDL_READ_VALUE` | VARCHAR |  | If additional measurement values are provided for a component, this item will store the value of the LRR component. |
| 6 | `ADDL_READ_UNITS` | VARCHAR |  | If additional measurement values are provided for a component, this item will store the units of the LRR component. |
| 7 | `ADDL_READ_OB_MEAS_SOURCE_C_NAME` | VARCHAR |  | If additional measurement values are provided for a component, this item will store the source of the reading. |
| 8 | `ADDL_READ_DESCR_C_NAME` | VARCHAR |  | This item flags an OB ultrasound reading with a descriptor. |
| 9 | `ADDL_READ_GA_VAL` | VARCHAR |  | This column contains the gestational age (in days) for the associated result component reading row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

