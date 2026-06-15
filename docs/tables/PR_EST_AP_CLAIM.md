# PR_EST_AP_CLAIM

> This table stores accounts payable claim context information for managed care estimates.

**Primary key:** `ESTIMATE_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESTIMATE_ID` | NUMERIC | PK shared | The unique identifier for the patient estimate record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `VENDOR_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 4 | `PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 5 | `POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 6 | `CLAIM_FORMAT_C_NAME` | VARCHAR |  | The claim format for the estimate claim detail. |
| 7 | `HISTORY_TYPE_C_NAME` | VARCHAR |  | The type of historical data used for this estimate claim detail. |
| 8 | `HX_UB_CLASS_C_NAME` | VARCHAR |  | The historical UB claim classification to use for this estimate claim detail. |
| 9 | `POS_TYPE_C_NAME` | VARCHAR | org | The place of service type of the related line. |
| 10 | `MC_ANCHOR_CONTEXT` | INTEGER |  | This is the Anchor context, meaning if there are mulitple lines in the related group that come from the same Anchor procedure this number points to the line that has the Anchor procedure. The Anchor procedure is what is shown to the member in Cost Calculator. |
| 11 | `MC_SEARCH_CONTEXT` | INTEGER |  | Holds a line number that corresponds to a line in RG PES 18180 which has the related search parameters that were in use when the detailed view was selected. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

