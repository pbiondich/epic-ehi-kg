# ESTIMATE_ACCUM_INFO

> Contains accumulation information for each search result in a Cost Calculator estimate.

**Primary key:** `ESTIMATE_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESTIMATE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the estimate record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EST_ACCUM_LINE_NUM` | INTEGER |  | The line number of related group 18000, which stores accmulation information about the estimate. |
| 4 | `ACCUM_GRP_NAME` | VARCHAR |  | The display name for the accumulation group. This name is generated at the original runtime of the estimate, based on the context of the benefit plan. |
| 5 | `ACCUM_GRP_LIMIT` | NUMERIC |  | The maximum amount that can be contributed to the accumulation group. |
| 6 | `ACCUM_GRP_ADDL_AMT` | NUMERIC |  | Additional amount added to the accumulation group from the estimate. |
| 7 | `ACCUM_GRP_REMAIN` | NUMERIC |  | Amount left in the accumulation group after adding the additional amount from the estimate. |
| 8 | `ACCUM_GRP_LEVEL_C_NAME` | VARCHAR |  | The account level that the accumulation contributes to. Can be Inidvidual (patient) or Family (account). |
| 9 | `ACCUM_GRP_TYPE_C_NAME` | VARCHAR |  | The type of accumulation this accumulation group represents. Can be a MOOP, a deductible, or other. |
| 10 | `ACCUM_IS_MONETARY_YN` | VARCHAR |  | Is the accumulation for this accumulation group a monetary amount? |
| 11 | `ACCUM_IS_PER_DAY_YN` | VARCHAR |  | Is the accumulation for this accumulation group limited per day? |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

