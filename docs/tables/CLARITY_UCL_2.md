# CLARITY_UCL_2

> Universal Charge Line information. Each row represents one UCL transaction.

**Overflow of:** [CLARITY_UCL](CLARITY_UCL.md)  
**Primary key:** `UCL_ID`  
**Columns:** 16  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `UCL_ID` | VARCHAR | PK | The unique identifier (.1 item) for the charge line record. |
| 2 | `CHARGE_STAGE_C_NAME` | VARCHAR |  | This item stores the current stage for the charge. |
| 3 | `CREATED_IN_RTR_YN` | VARCHAR |  | This item indicates whether the charge was created by the charge router. |
| 4 | `CREATED_FROM_UCL_ID` | VARCHAR |  | The charge from which this charge was created. This means that whenever a charge is generated from another charge, this item will represent the charge it was created from. If a charge is created manually in the editor, this item will not be set since it wasn't created from another charge. |
| 5 | `THIRD_PTY_ELIG_YN` | VARCHAR |  | This item indicates whether the charge is third party eligible. This is used by lab charges. |
| 6 | `PRO_HOSP_ACCT_ID` | NUMERIC |  | The professional billing hospital account tied to the visit for the guarantor account. |
| 7 | `PRO_VIS_NUM` | VARCHAR |  | The current professional billing visit for the guarantor account. |
| 8 | `RESEARCH_ENROLL_ID` | NUMERIC |  | The unique ID of the research study association linked to this charge. |
| 9 | `ORIG_BILL_AREA_ID` | NUMERIC |  | The item stores the original value of provider bill area. |
| 10 | `ORIG_BILL_AREA_ID_BILL_AREA_NAME` | VARCHAR |  | The record name of this bill area, financial subdivision, or financial division. |
| 11 | `DELEGATE_BILL_SOURCE_TX_ID` | NUMERIC |  | The source Tapestry ETR that the charge is linked to. |
| 12 | `DELEGATE_BILL_SOURCE_CLAIM_ID` | NUMERIC |  | The source Tapestry CLM that the charge is linked to. |
| 13 | `SPLIT_RELATED_HAR_TYPE_C_NAME` | VARCHAR | org | Identifies the system calculated related HAR type (I HAR 146) of the HAR that this charge will be split to. |
| 14 | `SPLIT_RELATED_HAR_RULE_ID` | VARCHAR |  | Indicates the rule in the PB Profile that qualified the charge for the related visit account type stored in item 16801. |
| 15 | `SPLIT_RELATED_HAR_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 16 | `SPLIT_RELATED_HAR_SOURCE_C_NAME` | VARCHAR |  | Tracks how the related visit account type stored in UCL item 16801 was set. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [CLARITY_UCL](CLARITY_UCL.md).

