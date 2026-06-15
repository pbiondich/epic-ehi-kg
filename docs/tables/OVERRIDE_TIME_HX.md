# OVERRIDE_TIME_HX

> The OVERRIDE_TIME_HX table contains information about order override time history.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IP_OVRD_TM_BY_ID` | VARCHAR |  | The unique ID of the user who adjusted the times or schedule. If the times or schedule are adjusted and then the order is verified, it will contain the ID of the user who verified the order. |
| 4 | `IP_OVRD_TM_BY_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `OVRD_UPD_AT_TM` | DATETIME (Local) |  | This is the instant at which the times for the order were set. If the times were adjusted and then the order was verified, the instant the order was verified will be stored. |
| 6 | `OVRD_TIMES` | VARCHAR |  | Stores the override scheduled times for the order if the order has a specified frequency. |
| 7 | `OVRD_INST_NS_TM` | DATETIME (Local) |  | Stores the override schedule time for orders with a non-specified frequency. |
| 8 | `OVRD_REASON_C_NAME` | VARCHAR | org | Stores the override reason for adjusting the medication administration times. |
| 9 | `IP_OVRDTM_SRCDEP_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 10 | `MLSIG_PERIOD_AND_PART` | VARCHAR |  | Stores multiline sig period and part the override data came from |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

