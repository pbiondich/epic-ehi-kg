# PRE_AR_CHG_3

> This table is a continuation of the PRE_AR_CHG table. This table contains one row for each line of each TAR record (think of a TAR record as one charge entry screen and each line as an individual procedure). Deleting charge lines will delete rows from this table. This table contains additional information about the procedure. *Note: TAR records in Chronicles are purged periodically depending on your system setting. Be aware that old data in this table may be lost if you truncate the table.

**Overflow of:** [PRE_AR_CHG](PRE_AR_CHG.md)  
**Primary key:** `TAR_ID`, `LINE`  
**Columns:** 24  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TAR_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the charge session record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ADV_PRICING_DESCRIPTION` | VARCHAR |  | Description of the advanced pricing line in ECP used for this charge. |
| 4 | `ADV_PRICING_INDEX_ID` | VARCHAR |  | Component or component group used in advanced pricing. |
| 5 | `ADV_PRICING_INDEX_ID_COMPONENT_INDEX_NAME` | VARCHAR |  | The name of the component index record |
| 6 | `ADV_PRICING_RULE_ID` | VARCHAR |  | Rule used for advanced pricing. |
| 7 | `ADV_PRICING_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 8 | `ADV_PRICING_MECHANISM_C_NAME` | VARCHAR |  | Advanced pricing mechanism used. |
| 9 | `ADV_PRICING_FSC1_ID` | NUMERIC |  | Fee schedule 1 used in advanced pricing. |
| 10 | `ADV_PRICING_FSC1_ID_FEE_SCHEDULE_NAME` | VARCHAR |  | The name of each fee schedule. |
| 11 | `ADV_PRICING_FSC2_ID` | NUMERIC |  | Fee schedule 2 used in advanced pricing. |
| 12 | `ADV_PRICING_FSC2_ID_FEE_SCHEDULE_NAME` | VARCHAR |  | The name of each fee schedule. |
| 13 | `ADV_PRICING_FSC_PERC_1` | NUMERIC |  | Percent of specified fee schedule 1 used in advanced pricing. |
| 14 | `ADV_PRICING_FSC_PERC_2` | NUMERIC |  | Percent of specified fee schedule 2 used in advanced pricing. |
| 15 | `ADV_PRICING_PERC_BASE` | INTEGER |  | Percent of base price used in advanced pricing. |
| 16 | `ADV_PRICING_LPP_ID` | NUMERIC |  | Pricing extension used in advanced pricing. |
| 17 | `ADV_PRICING_LPP_ID_LPP_NAME` | VARCHAR |  | The name of the extension. |
| 18 | `FIN_ASST_TRACKER_ID` | NUMERIC | FK→ | The unique identifier of the financial assistance tracker that discounted this transaction. |
| 19 | `SPLIT_RELATED_HAR_TYPE_C_NAME` | VARCHAR | org | Identifies the system calculated related HAR type (I HAR 146) of the HAR that this charge will be split to. |
| 20 | `DELEGATE_BILL_SOURCE_TX_ID` | NUMERIC |  | The source Tapestry ETR that the charge is linked to. |
| 21 | `SPLIT_RELATED_HAR_RULE_ID` | VARCHAR |  | Indicates the rule in the PB Profile that qualified the charge for the related visit account type stored in item 16801. |
| 22 | `SPLIT_RELATED_HAR_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 23 | `OVRD_SPLIT_RELATED_HAR_TYPE_C_NAME` | VARCHAR |  | Identifies the manually overridden related HAR type (I HAR 146) of the HAR that this charge will be split to. |
| 24 | `DELEGATE_BILL_SOURCE_CLAIM_ID` | NUMERIC |  | The source Tapestry CLM that the charge is linked to. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FIN_ASST_TRACKER_ID` | [FIN_ASST_TRACKER](FIN_ASST_TRACKER.md) | name_stem | high |

