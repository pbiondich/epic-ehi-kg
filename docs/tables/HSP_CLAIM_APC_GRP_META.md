# HSP_CLAIM_APC_GRP_META

> Table for Ambulatory Payment Classification (APC) grouping metadata. Holds information such as the instant of grouping, the payment classification method, and, if grouped by Epic, the mapping and locale records used.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | This column stores the unique identifier for the claim print record associated with a single hospital account/bucket. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AMB_GROUPING_DTTM` | DATETIME (UTC) |  | Holds the date & time that this claim was grouped, via Epic or a third-party. |
| 4 | `APC_EPIC_PMT_CLASS_GRP_C_NAME` | VARCHAR | org | This item stores the payment classification used during grouping, such as for Medicare or TRICARE. If grouping by Epic, it will be one of the values in the release range from Payment Classification Category (I PCD 101), excluding value 100. If grouping through an external system, it will hold a value of 100-External System. If there is no value in this item (from pre-existing data), then the default method is set to 1-Medicare APC if APC Data Source (I CLP 390) is set to 1-Epic, or 100-External System if the grouping source is set to 101-External System (APC) or 103-External System (APG). |
| 5 | `APC_EPIC_PCM_ID` | VARCHAR |  | This item stores the payment classification mapping record used if ambulatory payment classification (APC) grouping was done by Epic. |
| 6 | `APC_EPIC_PCM_ID_PCM_NAME` | VARCHAR |  | The name of the payment classification mapping. |
| 7 | `APC_EPIC_PMT_CLASS_RATE_C_NAME` | VARCHAR |  | This item stores the payment classification category used to determine the reimbursement weights and rates for APC codes if APC grouping was done by Epic. For example, if a commercial payer was configured to group by Medicare's logic, but reimburse based on their own set of rates, I CLP 392 would be set to 1-Medicare, and this item would be set to the customer-released category corresponding to this third party. If left blank, the category shown in I CLP 392 is used. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

